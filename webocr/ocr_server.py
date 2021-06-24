import os
from flask import Flask, render_template, request
from ocr_process import ocr_core #import dari ocr_process.py

UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


app = Flask(__name__)

def allowed_file(filename):  
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
               
        if 'file' not in request.files:
            return render_template('index.html')
        file = request.files['file']
        
        if file.filename == '':
            return render_template('index.html')

        if file and allowed_file(file.filename):
            
            #CallOCR
            extracted_text = ocr_core(file) #dipanggil disini
             
            #extract 
            with open('./result_txt/{}.txt'.format(file.filename), 'w') as f: #mengcreate file txt
                f.write(extracted_text)
                    
            return render_template('result.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename) #render template result
    elif request.method == 'GET':
        return render_template('index.html')
    
@app.route("/result")
def result():
    message = "tes"
    extracted_text = "tes"    
    return render_template('result.html', msg=message, extracted_text=extracted_text)

if __name__ == '__main__':    
    app.run(host="0.0.0.0", debug=True, threaded=True, use_reloader=False)