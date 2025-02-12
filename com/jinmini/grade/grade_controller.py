from com.jinmini.grade.grade_model import GradeModel
from com.jinmini.grade.grade_service import GradeService

class GradeController:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.korean = float(kwargs.get("korean"))
        self.english = float(kwargs.get("english"))
        self.math = float(kwargs.get("math"))
        self.society = float(kwargs.get("society"))
        self.science = float(kwargs.get("science"))

    def getResult(self) -> GradeModel:
        service = GradeService()
        grade = GradeModel()
        grade.name = self.name
        grade.korean = self.korean
        grade.english = self.english
        grade.math = self.math
        grade.society = self.society
        grade.science = self.science
        return service.execute(grade)