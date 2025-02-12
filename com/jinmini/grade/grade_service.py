
from com.jinmini.grade.grade_model import GradeModel

class GradeService:
    
    def __init__(self):
        pass

    def execute(self, grade:GradeModel) -> GradeModel:
        name = grade.name
        korean = float(grade.korean)
        english = float(grade.english)
        math = float(grade.math)
        society = float(grade.society)
        science = float(grade.science)

        scores = [korean, english, math, society, science]
        total = sum(scores)
        avg = total/5

        if avg >= 90:
            result = ' A '
        elif avg >= 80:
            result = ' B '
        elif avg >= 70:
            result = ' C '
        elif avg >= 60:
            result = ' D '
        else:
            result = ' F '

        grade.result = result
        grade.name = name

        return grade


      
        
    


    
