from flask import Flask, url_for, render_template,request #importing flask for webgui
import spacy#spacy for Natural Language Processing.
import sqlite3 #database
from flaskwebgui import FlaskUI#webapp generator

#initializing the database 
connection = sqlite3.connect('Qanda.db')
cursor = connection.cursor()

cursor.execute(
    """
        SELECT * FROM qanda
    """
)
data = cursor.fetchone()
question = data[0]
answer = data[1]

#Initializing the flask app
app = Flask(__name__)

ui = FlaskUI(app)
ui.maximized

nlp = spacy.load("en_core_web_md")


@app.route('/')
def index():
    return render_template('base.html', question = question)
    

@app.route('/result', methods=["GET","POST"])
def result():
    if request.method == 'POST':
        rawtext = request.form.get("rawtext")
        doc1 = nlp(rawtext)
        doc2 = nlp(answer)
        score = doc1.similarity(doc2)
        score = int(score*100)
    if score>50: 
        return render_template('result.html',rawtext = rawtext,score = score,answer = answer)
    else:
        return render_template('resultfail.html',rawtext = rawtext,score = score,answer = answer)

ui.run()