import logging

from src.helpers.decorators import timer_this


@timer_this
def extract() -> list[dict]:
    logging.info("📥 Iniciando Extração...")

    data = extract_01()

    return data

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

def extract_01() -> list[dict]:
    data = [
        {"id": 1, "name": "João", "age": 27},
        {"id": 2, "name": "Bruno", "age": 95},
        {"id": 3, "name": "Gabriel", "age": 27},
        {"id": 4, "name": "John", "age": 26},
    ]
    return data

