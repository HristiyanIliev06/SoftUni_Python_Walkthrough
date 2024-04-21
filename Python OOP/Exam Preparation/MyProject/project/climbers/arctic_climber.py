from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak

class ArcticClimber(BaseClimber):
    STRENGTH = 200
    MINIMUM_STRENGTH_TO_CLIMB = 100
    def __init__(self, name: str) -> None:
        super().__init__(name, strength = self.STRENGTH)
        
    def can_climb(self):
        if self._strength>=self.MINIMUM_STRENGTH_TO_CLIMB:
            return True
        
        return False
    
    def climb(self, peak: BasePeak):
        if peak.calculate_difficulty_level()=='Extreme':
            self._strength-=(20*2)
        else:
            self._strength-=(20*1.5)
            
        self.conquered_peaks.append(peak.name)
        
    