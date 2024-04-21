class Class:
    students = []
    grades = []
    __students_count = 22
    average = 0
    
    def __init__(self, name):
        self.name = name
        
    def add_student(self, name:str, grade:float):
        if self.__students_count>0:
            self.students.append(name)
            self.grades.append(grade)
            self.__students_count-=1
        
    def get_average_grade(self):
        self.average = sum(self.grades)/len(self.grades)
        return  self.average
    
    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {(sum(self.grades)/len(self.grades)):.2f}" 
    
a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
