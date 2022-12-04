from flask import Flask,request,render_template
from flask_cors import CORS
import pymysql

conn = pymysql.connect(host='localhost',port=3306,user='root',password='Mcqmyxh2$',database='matching',charset='utf8')
app = Flask(__name__)

CORS(app)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/questionnaire",methods = ["GET","POST"])
def questions():
    if request.method == "GET":
        return render_template('questionnaire1.0.html')
    elif request.method =='POST':
        data = request.form
        print('--->upload form data: ',data)
        gender = data.get('gender')
        zuoxi = data.get('zuoxi')
        shejiao = data.get('shejiao')
        add_name_db(gender, zuoxi, shejiao)
        return "gender：%s zuoxi：%s shejiao：%s" % (gender,zuoxi,shejiao)

def add_name_db(gender, zuoxi, shejiao):
    with conn.cursor() as c:
        sql = "insert into matching(gender,zuoxi,shejiao) values (%s,%s,%s)"
        c.execute(sql, args=(gender, zuoxi, shejiao))
        conn.commit()


if __name__ == '__main__':
    app.run(debug=True)