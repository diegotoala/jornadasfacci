
from flask import Flask,request,render_template,make_response
from flask_pymongo import MongoClient,PyMongo
import pdfkit

app = Flask(__name__)

mongodb_uri = "mongodb://facci:Uleam16@ds139278.mlab.com:39278/jornadasfacci"
client = MongoClient(mongodb_uri)
db = client.jornadasfacci


@app.route('/registrados')
def registrados():
    registrado = db.registrados.find_one({"correo":"diego.xibian@gmail.com"},{"nombre":1,"apellido":1,"_id":0,"rol":1})
    return str(registrado)

@app.route('/')
def hello():
    return "Hola"

@app.route('/certificado/<mail>')
def certificado(mail):
    rendered = render_template('certificado.html',mail=mail)
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf)
    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition']='inline; filename = jornadasfaccicertificado.pdf'

    return response


if __name__ == "__main__":
    app.run(debug=True)
