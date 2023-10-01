from flask import Flask, render_template
from mongo import MongoConnection


app =Flask(__name__)

db_client = MongoConnection().client
db = db_client.get_database('TFINALTD')
col = db.get_collection('peliPuss')

@app.route('/')
def index():
    peliculas_data=col.find({})
    return render_template('inicio.html', peliPuss=peliculas_data)

if __name__ == '__main__':
    app.run(debug=True)