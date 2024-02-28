import csv
from csv import writer
from flask import Flask
from flask import render_template,request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("TSweb.html")
    #python -m flask run


@app.route("/", methods=["GET","POST"])
@app.route("/save", methods=["GET","POST"])
def save():
    if request.method == "POST":
        name = request.form['fname']
        album = request.form['tsAlbums']
        info = [name, album]

    
        with open('TS.csv', 'a', newline = '') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(info)
            f_object.close()
        
            return("success")


if __name__ == "__main__": 
    app.debug = True
    app.run()  

