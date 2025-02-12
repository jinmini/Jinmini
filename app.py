from flask import Flask, render_template, request, redirect, url_for
from com.jinmini.calculator.calc_controller import CalcController
from com.jinmini.calculator.calc_model import CalcModel


app = Flask(__name__) #플라스크 - 클래스 (함수)

@app.route('/') #method
def login_page():
    # 기본 페이지 요청 시 로그인 페이지로 리다이렉트트
    return redirect(url_for('login'))

#파이썬은 name = request.할당을 주는 것
@app.route('/login', methods=['GET', 'POST']) #method 4개 중에 POST를 받겠다. 그래서 _s를 붙임.
def login():
    
    login_failed = False

    if request.method == 'POST' :

        print("😊로그인 알고리즘")

        username = request.form.get('username') #request는 변수 .은 그 안에 있는 뜻
        password = request.form.get('password') #password 변수

        print("username:", username)
        print("password:", password)

        if username == 'kjm' and password == '1234':
            print("😁로그인 성공") 
            return redirect(url_for('home')) #로그인 성공 시 홈 화면으로 이동
        else:
            login_failed = True
    
    return render_template("login.html", login_failed=login_failed) 

@app.route('/home')
def home():
    print("🏠홈페이지로 이동")
    return render_template("index.html")

@app.route('/calc',methods=['GET', 'POST'] )
def calc():

    print("전송된 데이터 방식 :", request.method)

    if request.method == 'POST': 
        print("post로 진입")
        num1 = request.form.get('num1') 
        num2 = request.form.get('num2')
        opcode = request.form.get('opcode')

        controller = CalcController(num1 = num1, opcode = opcode, num2 = num2)
        resp: CalcModel = controller.getResult()


        print("num1:", num1) #"자연어", 변수
        print("num2:", num2)
        print("opcode", opcode)

        #if elif else 구문
        render_html = '<h3>결과보기</h3>'
        render_html += f"{resp.num1}{resp.opcode}{resp.num2}={resp.result}"

        return render_template("calculator/calc.html", render_html=render_html)

    else:
        print("get방식으로 전송된 데이터")
        return render_template("calculator/calc.html")
    

@app.route('/energy_esg_collector') #data_analytics 1
def energy_esg_collector():
    return render_template("/esg/data_analytics_platform/energy_esg_collector.html")

@app.route('/finserv_esg_analytics') #data_analytics 2
def finserv_esg_analytics():
    return render_template("/esg/data_analytics_platform/finserv_esg_analytics.html")

@app.route('/manufacturing_esg_report') #data_analytics 3
def manufacturing_esg_report():
    return render_template("/esg/data_analytics_platform/manufacturing_esg_report.html")

@app.route('/construction_report') #fin_impact_automator 1
def construction_report():
    return render_template("/esg/fin_impact_automator/construction_report.html")

@app.route('/healthcare_chatbot') #fin_impact_automator 2
def healthcare_chatbot():
    return render_template("/esg/fin_impact_automator/healthcare_chatbot.html")

@app.route('/retail_fin_collector') #fin_impact_automator 3
def retail_fin_collector():
    return render_template("/esg/fin_impact_automator/retail_fin_collector.html")

@app.route('/finserv_dashboard') #finance_chatbot 1
def finserv_dashboard():
    return render_template("/esg/finance_chatbot/finserv_dashboard.html") 

@app.route('/manufacturing_review') #finance_chatbot 2
def manufacturing_review():
    return render_template("/esg/finance_chatbot/manufacturing_review.html") 

@app.route('/retail_chatbot') #finance_chatbot 3
def retail_chatbot():
    return render_template("/esg/finance_chatbot/retail_chatbot.html") 


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True