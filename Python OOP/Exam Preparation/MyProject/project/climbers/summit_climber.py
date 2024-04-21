from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak

class SummitClimber(BaseClimber):
    STRENGTH = 150
    MINIMUM_STRENGTH_TO_CLIMB = 75
    def __init__(self, name: str) -> None:
        super().__init__(name, strength = self.MINIMUM_STRENGTH_TO_CLIMB)
        
    def can_climb(self):
        if self._strength>=self.MINIMUM_STRENGTH_TO_CLIMB:
            return True
        
        return False
    
    def climb(self, peak: BasePeak):
        if peak.calculate_difficulty_level()=='Extreme':
            self._strength-=(30*1.3)
        else:
            self._strength-=(30*2.5)
            
        self.conquered_peaks.append(peak.name)