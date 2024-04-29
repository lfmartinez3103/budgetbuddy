class HotelUser:
    def __init__(self, budget, num_persons, rating):
        self.budget = budget
        self.num_persons = num_persons
        self.rating = rating


def clasificar_necesidades_usuario_hotel(budget: str, num_persons: int, rating: int) -> HotelUser:
    global clasificacion_presupuesto
    global clasificacion_personas
    global calificacion
    clasificacion_presupuesto = ""
    clasificacion_personas = ""
    calificacion = ""

    if budget == "$": clasificacion_presupuesto = "cheap"
    elif budget == "$$": clasificacion_presupuesto = "mid"
    elif budget == "$$$": clasificacion_presupuesto = "fine"
    
    if num_persons == 1: clasificacion_personas = "Individual"
    elif num_persons == 2: clasificacion_personas = "Pareja"
    elif 3 <= num_persons <= 5: clasificacion_personas = "Grupo pequeño"
    else: clasificacion_personas = "Grupo grande"

    if rating == 5: calificacion = "excellent"
    elif rating == 4: calificacion == "Very Good"
    elif rating == 3: calificacion == "average"
    elif rating == 2: calificacion == "poor"
    elif rating == 1: calificacion == "terrible"

    result = HotelUser(clasificacion_presupuesto, clasificacion_personas, calificacion)
    return result

budget = input("Ingrese cual es su presupuesto ($, $$, $$$): ")
num_persons = int(input("Ingrese la cantidad de personas: "))
rating = int(input("Ingrese la calificacion deseada: "))

necesidades = clasificar_necesidades_usuario_hotel(budget, num_persons, rating)
print("Ordenado")
print(f"Presupuesto: {necesidades.budget}")
print(f"Cantidad personas: {necesidades.num_persons}")
print(f"Estrellitas deseadas: {necesidades.rating}")