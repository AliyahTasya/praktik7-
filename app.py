from flask import Flask, jsonify, request  # type: ignore
import time

app = Flask(__name__)

@app.route('/process', methods=['GET'])
def process_data():
    time.sleep(1)  # simulasi pemrosesan berat
    return jsonify({"message": "Data processed successfully!"})

if __name__ == '__main__':
    from waitress import serve  # type: ignore
    serve(app, host='0.0.0.0', port=8000)
