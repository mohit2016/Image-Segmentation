from flask import Flask,flash,request,redirect,url_for, render_template
from werkzeug.utils import secure_filename
import os
import dominant_color







app = Flask(__name__,static_url_path='/static')



@app.route('/')
def tmrf():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        n = request.form['number']
        
        f.save("static/"+secure_filename(f.filename))
        # print(f.filename)
        
        dominant_color.extract_image(f.filename,int(n))

        extracted_name = "static/extracted_images/extracted_" +str(n) + f.filename
        original_name = "static/" + f.filename
        print(extracted_name)
        result_dic={
            'image':[original_name,extracted_name],
            'title':["Original Image","Edited Image"]
        }

    return render_template('home.html', results = result_dic) 


if __name__ =="__main__":
    app.run(debug=True)
