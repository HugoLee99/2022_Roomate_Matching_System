from flask import Flask,render_template
app = Flask(__name__)

@app.route("/home")
def index():
    return render_template('home.html')


@app.route("/questionnaire.html")
def questions():
    return render_template('questionnaire.html')

if __name__ == "__main__":
    app.run(threaded=True)

