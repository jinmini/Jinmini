from com.jinmini.calculator.calc_model import CalcModel


class CalcService:
    def __init__(self):
        pass

    def execute(self, calc: CalcModel)-> CalcModel: #?
        num1 = calc.num1
        num2 = calc.num2
        opcode = calc.opcode

        if opcode == "+" :
            result=int(num1) + int(num2)
        elif opcode == "-" :
            result=int(num1) - int(num2)
        elif opcode == "*" :
            result=int(num1) * int(num2)
        elif opcode == "/" :
            result=int(num1) / int(num2)
        else : 
            result= "계산 오류"

        calc.result = result

        return calc