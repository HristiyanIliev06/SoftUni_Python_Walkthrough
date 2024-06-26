class Programmer:
    def __init__(self, nm:str, l:str, ss:int):
        self.name =nm
        self.language = l
        self.skills = ss
        
    def watch_course(self, course_name:str, language:str, skills_earned:int)->str:
        if self.language==language:
            self.skills+=skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"
               
    def change_language(self,  new_language:str, skills_needed:int)->str:
        if self.skills >= skills_needed and self.language!=new_language:
            previous_language = self.language
            self.language=new_language
            return f"{self.name} switched from {previous_language} to {new_language}"
        elif self.skills>=skills_needed and self.language==new_language:
            return f"{self.name} already knows {self.language}"
        elif self.skills < skills_needed:
            return f"{self.name} needs {skills_needed-self.skills} more skills" 
            