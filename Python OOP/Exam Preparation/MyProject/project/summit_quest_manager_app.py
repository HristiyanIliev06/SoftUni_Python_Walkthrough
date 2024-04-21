from typing import List

from project.climbers.base_climber import BaseClimber
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber

from project.peaks.base_peak import BasePeak
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak

class SummitQuestManagerApp:
    VALID_CLIMBER_TYPES = ['ArcticClimber', 'SummitClimber']
    VALID_PEAK_TYPES = ['ArcticPeak', 'SummitPeak']
    
    def __init__(self):
        self.climbers = []
        self.peaks = []
        
    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."
        
        if climber_name in self.climbers:
            return f"{climber_name} has been already registered."
        
        self.climbers.append(climber_name)
        return f"{climber_name} is successfully registered as a {climber_type}."
    
    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type  not in self.VALID_PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."
        
        self.peaks.append(peak_name)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."
    
    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]): 
        