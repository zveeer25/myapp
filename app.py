from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo

app = Flask("myapp")
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/flaskdb"
mongo = PyMongo(app)
namemain_collection = mongo.db.namemains


@app.route("/read")
def read_data():
    namemain = (namemain_collection.find().skip(namemain_collection.count() - 5))
    lastname = (namemain_collection.find().skip(namemain_collection.count() - 1))
    return render_template('index.html', namemain=namemain, lastname=lastname)


@app.route("/")
def form():

    return render_template('form.html')


@app.route("/data", methods=['GET'])
def show_data():
    if request.method == 'GET':
        name = request.args.get("x")
        if name != "":
            namemain = namemain_collection.insert_one(
                {"name": name,})
            return redirect('/read')
        else:
            return ("Kindly fill the form")




app.run(debug=False)
