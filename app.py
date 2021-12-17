from  flask import Flask, render_template, request, flash
from PIL import Image

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = "super secret key"

@app.route('/')
def index_page():
    return render_template('home.html')

@app.route('/encode', methods=['GET','POST'])
def encode_page():
    msg = ''
    img = ''
    if request.method == 'POST':
        # print({'Request': request.form})
        msg = request.form['message']
        img = request.files['image']

        # print(msg, img)
        imgShow = Image.open(img)
        imgShow.convert('L').show()

        return render_template('encode.html', enc_img='https://yt3.ggpht.com/ytc/AKedOLQhCqLTkEGQeSzNuaSndU18yVP8hqtaW-zJ4-ylRlw=s900-c-k-c0x00ffffff-no-rj')
    else:   
        return render_template('encode.html')
        