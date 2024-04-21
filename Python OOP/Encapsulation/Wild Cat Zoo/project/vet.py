from project.worker import Worker

class Vet(Worker):
    def __init__(self, n, a, s) -> None:
        super().__init__(n, a, s)
        
    def __repr__(self):
        return super().__repr__()