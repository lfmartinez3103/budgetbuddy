import models.comparation

def classify_needs(budget_level: str, num_persons: int, destination: str, include_transport: bool) -> models.comparation.ClassifyNeeds | ValueError:
    if budget_level == "$": budget_level = models.comparation.BudgetLevel.CHEAP
    elif budget_level == "$$": budget_level = models.comparation.BudgetLevel.MID
    elif budget_level == "$$$": budget_level = models.comparation.BudgetLevel.FINE
    else: raise ValueError("Invalid budget level")

    if num_persons < 1: raise ValueError("Invalid number of persons")
    elif num_persons > 6: raise ValueError("Number of persons too high")

    if not destination: raise ValueError("Invalid destination")

    return models.comparation.ClassifyNeeds(budget_level, num_persons, destination, include_transport)