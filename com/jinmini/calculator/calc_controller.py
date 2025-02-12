
from com.jinmini.calculator.calc_model import CalcModel
from com.jinmini.calculator.calc_service import CalcService

class CalcController :
    def __init__(self, **kwargs):
        self.num1 = int(kwargs.get("num1"))
        self.opcode = kwargs.get("opcode")
        self.num2 = int(kwargs.get("num2"))

    def getResult(self) -> CalcModel:
        calc = CalcModel()
        calc.num1 = self.num1
        calc.num2 = self.num2
        calc.opcode = self.opcode
        service = CalcService()
        return service.execute(calc)

