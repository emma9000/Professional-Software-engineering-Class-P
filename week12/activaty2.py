from flask import Flask, request,url_for

app = Flask(__name__)

@app.route("/index")
def load_image():
    return '<a href="/upload">Click here to upload an image</a>'

import os
@app.route("/upload",methods=['GET','POST'])
def upload_image():
    if request.method == 'POST':
        # 获取上传的文件对象
        f = request.files['file']
        
        # 保存到 static/uploads 文件夹
        file_path = "/static/uploads/" + f.filename
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        f.save(file_path)

        # 生成网页上可访问的 URL
        image_url = url_for('static', filename=f'uploads/{f.filename}')
        return f'''
        <p>File uploaded successfully!</p>
        <img src="{image_url}" width="300">
        <br><a href="/upload">Upload another</a>
        '''
    return '''
    <form method="POST" enctype="multipart/form-data"> 
        <input type="file" name="file">
        <input type="submit">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
