import os
import time
from flask import Flask, request, redirect, jsonify
import whisper
import threading

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'m4a', 'mp3', 'wav'}
WHISPER_MODEL_NAME = 'small'  # tiny, base, small, medium
WHISPER_DEVICE = 'cpu'  # cpu, cuda

print('loading whisper model', WHISPER_MODEL_NAME, WHISPER_DEVICE)
whisper_model = whisper.load_model(WHISPER_MODEL_NAME, device=WHISPER_DEVICE)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app = Flask(__name__, static_url_path='/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

lock = threading.Lock()

def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return redirect('/index.html')

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    time_sta = time.perf_counter()
    print('start transcribe ' + str(time_sta))  # カッコが閉じていない
    file = request.files['file']
    if file and is_allowed_file(file.filename):
        filename = str(int(time.time())) + '.' + file.filename.rsplit('.', 1)[1].lower()
        print(filename)
        saved_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(saved_filename)
        file.save(saved_filename)
        lock.acquire()
        try:
            result = whisper_model.transcribe(saved_filename, fp16=False, language='ja')
            elapsed_time = time.perf_counter() - time_sta  # タイポ修正
            print('time=' + str(elapsed_time))
            print(result)
            return jsonify(result), 200
        except Exception as e:
            print('Error:', str(e))
            return jsonify({'error': 'Transcription error'}), 500
        finally:
            lock.release()
    else:
        print('Invalid file format')
        return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(host='localhost', port=9000)
