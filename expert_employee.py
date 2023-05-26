class Employee:
    def __init__(self,name,productivity,skills,experience):
        self.name=name
        self.productivity=productivity
        self.skills=skills
        self.experience=experience


class expert:

    def __init__(self):
        self.criteria={
            'productivity':80,
            'skills':80,
            'experience':5
        }

       
    def evaluator(self,employee):
        score=0
        if employee.productivity > self.criteria['productivity']:
            score+=130
        if employee.skills > self.criteria['skills']:
            score+=120
        
        if employee.experience > self.criteria['experience']:
            score+=50

        if score==300:
            print("Employee fits best for our company")
        else:
            print("take interview and evaluate")
        
        return score


emp=Employee('sakshi',100,90,8)
exp=expert()
exp.evaluator(emp)