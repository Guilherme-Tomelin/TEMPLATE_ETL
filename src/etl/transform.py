import logging
from src.helpers.decorators import timer_this


@timer_this
def transform(data):
    logging.info("🛠️  Iniciando Transformação...")
    
    data = rename_column(data, "id", "user_id")

    return data

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def rename_column(data: list[dict], old_name: str, new_name: str) -> list[dict]:
    try:
        for row in data:
            if old_name in row:
                row[new_name] = row.pop(old_name)
        return data
    except Exception as e:
        logging.error(f"❌ Erro ao modificar o nome da coluna: {e}")


