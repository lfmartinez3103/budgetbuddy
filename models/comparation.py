from enum import Enum

class BudgetLevel(Enum):
    CHEAP = 1
    MID = 2
    FINE = 3


class ClassifyNeeds():
    def __init__(self,
                 budget_level: BudgetLevel,
                 num_persons: int,
                 destination: str,
                 include_transport: bool = False,
                ):
        self.budget_level = budget_level
        self.num_persons = num_persons
        self.destination = destination
        self.include_transport = include_transport