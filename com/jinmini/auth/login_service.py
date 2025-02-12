
from com.jinmini.auth.login_model import LoginModel


class LoginService:
    def __init__(self):
        pass

    def execute(self, login:LoginModel) -> LoginModel:
        username = login.username
        password = login.password
        if username == "kjm" and password == "1234":
            result = "home"
        else:
            result = "login_page"
        login.result = result
        return login