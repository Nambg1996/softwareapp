from flask import Flask, send_from_directory
from flask import Flask, jsonify, render_template
import socket
app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/ip_address')
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return jsonify(ip_address=ip_address)

if __name__ == '__main__':
    app.run(host='127.0.0.2', port=3000)