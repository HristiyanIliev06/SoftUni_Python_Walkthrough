from project.peaks.base_peak import BasePeak

class SummitPeak(BasePeak):
    def __init__(self, name, elevation):
        super().__init__(name, elevation)
        
    def get_recommended_gear():
        list = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
        return list
    
    def calculate_difficulty_level(self):
        if self.elevation>2500:
            return "Extreme"
        elif 1500<=self.elevation<=2500:
            return "Advanced"
        