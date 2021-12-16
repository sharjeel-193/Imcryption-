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
    
    if request.method == 'POST':
        msg = request.form['message']
        img = request.form['image']

        if(msg == ''):
            flash(f'Message Cannot be Empty', category='danger')
        
        # return render_template('encode.html')
        
    return render_template('encode.html')
        