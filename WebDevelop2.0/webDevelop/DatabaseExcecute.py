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
        return render_template('questionnaire.html')
    elif request.method =='POST':
        data = request.form
        print('--->upload form data: ',data)
        name=data.get('name')
        gender = data.get('gender')
        getup=data.get('getup')
        sleep=data.get('sleep')
        zuoxi = data.get('zuoxi')
        xizao = data.get('xizao')
        yifu=data.get('yifu')
        shouji=data.get('shouji')
        ciji=data.get('ciji')
        weisheng=data.get('weisheng')
        wupin=data.get('wupin')
        dianfei=data.get('dianfei')
        kongtiao=data.get('kongtiao')
        add_name_db(name, gender, getup, sleep, zuoxi, xizao, yifu, shouji, ciji, weisheng, wupin, dianfei, kongtiao)

        v1 = data.get('v1')
        v2 = data.get('v2')
        v3 = data.get('v3')
        v4 = data.get('v4')
        v5 = data.get('v5')
        v6 = data.get('v6')
        v7 = data.get('v7')
        v8 = data.get('v8')
        v9= data.get('v9')
        v10 =data.get('v10')
        v11= data.get('v11')
        add_data_db(name,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11)

        return "Thanks for joining!"

def add_name_db(name,gender,getup,sleep,zuoxi,xizao,yifu,shouji,ciji,weisheng,wupin,dianfei,kongtiao):
    with conn.cursor() as c:
        sql = "insert into matching1(name,gender,getup,sleep,zuoxi,xizao,yifu,shouji,ciji,weisheng,wupin,dianfei,kongtiao) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql, args=(name,gender,getup,sleep,zuoxi,xizao,yifu,shouji,ciji,weisheng,wupin,dianfei,kongtiao,))
        conn.commit()

def add_data_db(name,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11):
    with conn.cursor() as c:
        sql = "insert into matching2(name,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql, args=(name,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11))
        conn.commit()

if __name__ == '__main__':
    app.run(debug=True)