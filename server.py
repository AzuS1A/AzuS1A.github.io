from flask import Flask, send_from_directory

app = Flask(__name__)

# 把 /files 这个 URL 前缀映射到本地目录 ./files
@app.route('/files/<path:filename>')
def files(filename):
    return send_from_directory('files', filename)

# 根路径直接访问 index.html
@app.route('/')
def home():
    return send_from_directory('files', 'indexO.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)