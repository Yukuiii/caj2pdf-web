
from flask import Flask, request, send_file
from caj2pdf.cajparser import CAJParser
import os
from convert import convert_caj_to_pdf as convert
import uuid
import time
app = Flask(__name__)


@app.route('/api/convert', methods=['POST'])
def convert_caj_to_pdf():
    file = request.files['file']
    base_dir = os.path.dirname(os.path.abspath(__file__))
    upload_dir = os.path.join(base_dir, 'upload')
    output_dir = os.path.join(base_dir, 'output')
    if not os.path.exists(upload_dir):
         os.makedirs(upload_dir)
    if not os.path.exists(output_dir):
         os.makedirs(output_dir)
    file_path = os.path.join(upload_dir, file.filename) 
    unique_id = f"{uuid.uuid4()}-{int(time.time())}"
    output_path = os.path.join(output_dir, f"{unique_id}.pdf")
    file.save(file_path)
    caj = CAJParser(file_path)
    caj.convert(output_path)
    return {
        "status": "success",
        "message": "文件转换完成",
        "file_path": output_path
    }, 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)


