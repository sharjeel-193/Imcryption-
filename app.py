from  flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from PIL import Image
from werkzeug.utils import secure_filename
import os
import utils

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = "super secret key"

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     


@app.route('/')
def index_page():
    return render_template('home.html')

@app.route('/encode', methods=['GET','POST'])
def encode_page():
    msg = ''
    img = ''
    if request.method == 'POST':
        msg = request.form['message']
        img = request.files['image']

        if img.filename=='' or msg=='':
            flash('Message and Image is Must', category='danger')
            return redirect(request.url)

        if img and allowed_file(img.filename):
            file_arr = img.filename.split('.')
            # print(file_arr)
            file_name = secure_filename(file_arr[0]+'.png')
            newImg = utils.encodeMsgintoImg(img, msg)
            newImg.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            return render_template('encode.html', newFile=file_name)
            # return render_template('encode.html')
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif', category='danger')
            return redirect(request.url)
        
    else:   
        return render_template('encode.html')

@app.route('/decode', methods=['GET','POST'])
def decode_page():
    img = ''
    if request.method =='POST':
        img = request.files['encImg']
        if(img.filename == ''):
            flash('Message and Image is Must', category='danger')
            return redirect(request.url)
        if img and allowed_file(img.filename):
            msg = utils.decodeMsgFromImg(img)
            print(msg)
            return render_template('decode.html', hidMsg=msg)
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif', category='danger')
            return redirect(request.url)
    else:
        return render_template('decode.html')


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # print(app.root_path)
    full_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    # print(full_path)
    return send_from_directory(full_path, filename)


if __name__ == "__main__":
    app.run()