from flask import Flask, render_template, request, redirect, url_for
from com.jinmini.auth.login_controller import LoginController
from com.jinmini.auth.login_model import LoginModel
from com.jinmini.calculator.calc_controller import CalcController
from com.jinmini.calculator.calc_model import CalcModel
from com.jinmini.grade.grade_controller import GradeController
from com.jinmini.grade.grade_model import GradeModel

app = Flask(__name__) 

@app.route('/') 
def login_page():
    
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST']) 
def login():
    
    if request.method == 'POST' :

        print("😊로그인 알고리즘")

        username = request.form.get('username') 
        password = request.form.get('password') 

        print("username:", username)
        print("password:", password)
       
        controller = LoginController(username, password)
        resp: LoginModel = controller.getResult()

        return redirect(url_for(resp.result))
    
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

        print("num1:", num1) 
        print("num2:", num2)
        print("opcode", opcode)

        render_html = '<h3>결과보기</h3>'
        render_html += f"{resp.num1}{resp.opcode}{resp.num2}={resp.result}"

        return render_template("calculator/calc.html", render_html=render_html)

    else:
        print("get방식으로 전송된 데이터")
        return render_template("calculator/calc.html")
    
@app.route('/grade',methods=['GET', 'POST'] )
def grade():

    print("전송된 데이터 방식 :", request.method)

    if request.method == 'POST': 
        print("post로 진입")

        name = request.form.get('name') 
        korean = request.form.get('korean')
        english = request.form.get('english')
        math = request.form.get('math')
        society = request.form.get('society')
        science = request.form.get('science')
    
        controller = GradeController(name=name, korean=korean, english=english, math=math, society=society, science=science)
        resp: GradeModel = controller.getResult()

        print("name:", name) 
        print("korean:", korean)
        print("english", english)
        print("math", math)
        print("society", society)
        print("science", science)

        render_html = '<h3>결과보기</h3>'
        render_html += f"{resp.name}님의 성적은{resp.result}입니다"

        return render_template("grade/grade.html", render_html=render_html)

    else:
        print("get방식으로 전송된 데이터")
        return render_template("grade/grade.html")

@app.route('/energy_esg_collector') 
def energy_esg_collector():
    return render_template("/esg/data_analytics_platform/energy_esg_collector.html")

@app.route('/finserv_esg_analytics') 
def finserv_esg_analytics():
    return render_template("/esg/data_analytics_platform/finserv_esg_analytics.html")

@app.route('/manufacturing_esg_report') 
def manufacturing_esg_report():
    return render_template("/esg/data_analytics_platform/manufacturing_esg_report.html")

@app.route('/construction_report') 
def construction_report():
    return render_template("/esg/fin_impact_automator/construction_report.html")

@app.route('/healthcare_chatbot') 
def healthcare_chatbot():
    return render_template("/esg/fin_impact_automator/healthcare_chatbot.html")

@app.route('/retail_fin_collector') 
def retail_fin_collector():
    return render_template("/esg/fin_impact_automator/retail_fin_collector.html")

@app.route('/finserv_dashboard') 
def finserv_dashboard():
    return render_template("/esg/finance_chatbot/finserv_dashboard.html") 

@app.route('/manufacturing_review') 
def manufacturing_review():
    return render_template("/esg/finance_chatbot/manufacturing_review.html") 

@app.route('/retail_chatbot') 
def retail_chatbot():
    return render_template("/esg/finance_chatbot/retail_chatbot.html") 

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True