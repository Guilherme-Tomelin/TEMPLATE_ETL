import logging
import json
from pprint import pprint
from src.helpers.decorators import timer_this


@timer_this
def load(data):
    logging.info("📤 Iniciando Carregamento...")

    pprint(data)