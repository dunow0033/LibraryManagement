from User import User

class Student(User): 
    def __init__(self, name, grade, school): 
        User.__init__(self, name)
        self._grade = grade 
        self._school = school  