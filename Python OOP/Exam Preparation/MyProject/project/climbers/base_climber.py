from project.peaks.base_peak import BasePeak
from abc import ABC, abstractmethod

class BaseClimber(ABC):
    STRENGTH_INCREASE = 15
    def __init__(self, name: str, strength: float) -> None:
        self._name = name
        self._strength = strength
        self.conquered_peaks = []
        self.is_prepared = True
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, v:str):
        if v.strip()=="":
            raise ValueError("Climber name cannot be null or empty!")
        self._name = v 
        
    @property
    def strength(self):
        return self._strength
    
    @strength.setter
    def strength(self, v:str):
        if v<=0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self._strength = v 
    
    @abstractmethod    
    def can_climb(self)->bool:
        pass
    
    @abstractmethod
    def climb(self, peak: BasePeak):
        pass
    
    def rest(self):
        self._strength+=BaseClimber.STRENGTH_INCREASE
        
    def __str__(self):
        return f"{self.__class__.__name__}: /// Climber name: {self._name} * Left strength: {float(self._strength)} * Conquered peaks: {', '.join(cp for cp in sorted(self.conquered_peaks))} ///"
        
        
        