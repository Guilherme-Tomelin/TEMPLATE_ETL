import logging

from src.configs import LOGGER_CONFIG
from src.configs import LoggerConfig

LoggerConfig(**LOGGER_CONFIG)
from src.etl import extract, transform, load
from src.helpers.decorators import timer_this



@timer_this
def main():
    logging.warning("▶️  Iniciando o ETL...")

    data = extract()
    if data:
        data = transform(data)
        load(data)
    else:
        logging.warning("Nenhum novo dado para ser tratado")



if __name__ == "__main__":
    main()