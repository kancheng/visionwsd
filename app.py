from flask import Flask, render_template, request, url_for, jsonify
import os
import cv2
import uuid
import threading
from ultralytics import YOLO

app = Flask(__name__)

# 設定上傳與結果存放資料夾
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = os.path.join('static', 'results')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# 載入 YOLO 模型（支援檢測與分割）
model = YOLO("yolov8n-seg.pt")

# 全域字典存放各工作進度與結果
# 格式： jobs[job_id] = {"progress": int, "result_file": str, "file_type": "image" 或 "video"}
jobs = {}

def process_image(job_id, file_path, filename):
    # 模擬部分進度更新
    jobs[job_id]['progress'] = 10
    results = model(file_path)
    jobs[job_id]['progress'] = 50
    result_img = results[0].plot()
    result_file = "result_" + filename
    result_path = os.path.join(RESULT_FOLDER, result_file)
    cv2.imwrite(result_path, result_img)
    jobs[job_id]['progress'] = 100
    jobs[job_id]['result_file'] = result_file
    jobs[job_id]['file_type'] = "image"

def process_video(job_id, file_path, filename):
    cap = cv2.VideoCapture(file_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # 嘗試改用 avc1 編碼
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 強制輸出為 mp4
    result_file = "result_" + os.path.splitext(filename)[0] + ".mp4"
    result_path = os.path.join(RESULT_FOLDER, result_file)
    out = cv2.VideoWriter(result_path, fourcc, fps, (width, height))
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        
        # 每一幀使用 YOLO 模型進行推論
        results = model(frame)
        result_frame = results[0].plot()
        out.write(result_frame)
        
        # 更新進度百分比
        progress = int((frame_count / total_frames) * 100)
        jobs[job_id]['progress'] = progress
        
    cap.release()
    out.release()
    jobs[job_id]['progress'] = 100
    jobs[job_id]['result_file'] = result_file
    jobs[job_id]['file_type'] = "video"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    uploaded_file = request.files.get("file")
    if uploaded_file:
        filename = uploaded_file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)
        
        ext = filename.split('.')[-1].lower()
        job_id = uuid.uuid4().hex
        jobs[job_id] = {'progress': 0, 'result_file': None, 'file_type': None}
        
        # 根據檔案類型啟動背景處理
        if ext in ['jpg', 'jpeg', 'png', 'bmp']:
            thread = threading.Thread(target=process_image, args=(job_id, file_path, filename))
            thread.start()
        elif ext in ['mp4', 'avi', 'mov', 'mkv']:
            thread = threading.Thread(target=process_video, args=(job_id, file_path, filename))
            thread.start()
        else:
            return jsonify({"error": "不支援的檔案格式！"}), 400
        
        return jsonify({"job_id": job_id})
    return jsonify({"error": "未上傳檔案！"}), 400

@app.route("/progress")
def progress():
    job_id = request.args.get("job_id")
    if job_id in jobs:
        return jsonify({
            "progress": jobs[job_id]['progress'],
            "result_file": jobs[job_id]['result_file'],
            "file_type": jobs[job_id]['file_type']
        })
    return jsonify({"progress": 0, "result_file": None, "file_type": None})

if __name__ == "__main__":
    app.run(debug=True)
