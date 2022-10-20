from flask import Flask,redirect,url_for,render_template,request
from werkzeug.utils import secure_filename


app=Flask(__name__)

# @app.route("/")
# def index():
#     return "Hola mundo"

# @app.route("/cosita/<string:name>")
# def main(name):
#     return f"Hola {name} espero estes bien"

# @app.route('/redirects')
# @app.route('/redirects/<string:name>')
# def redirects(name=None):
#     print(name)
#     if name==None:
#         return redirect(url_for('index'))
#     else:
#         return redirect(url_for('main',name=name))

@app.route('/')
def upload():
    return render_template('index.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    if request.method=='POST':
        f=request.files['file']
        f.save(secure_filename(f.filename))
        return 'cargado correctamente'

if __name__=='__main__':
    app.run(debug=True)