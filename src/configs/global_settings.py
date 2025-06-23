import logging
from pathlib import Path


# ════════════════════════════════[CORE]════════════════════════════════


DEV_MODE = True


# ════════════════════════════════[PATHS]════════════════════════════════


_LOGS_PATH = Path("caminho/para/salvar/logs").resolve()



# ════════════════════════════════[ LOG CONFIG ]════════════════════════════════
"""
LOGGER_CONFIG - Definindo Configurações de Logging
Níveis: DEBUG < INFO < WARNING < ERROR < CRITICAL

[log_level]      -->  Nível de log para o arquivo (se log_file não for None). Ex: logging.INFO, logging.ERROR, etc.
[console_level]  -->  Nível de log exibido no console.
[log_format]     -->  Formato das mensagens de log.
[datefmt]        -->  Formato da data/hora no log.
[log_file]       -->  Se None, loga apenas no console; se for um caminho (ou qualquer valor), loga em arquivo logs/app.log.
"""

LOGGER_CONFIG = {
    "log_level": logging.INFO,
    "console_level": logging.DEBUG,
    "log_format": "[%(asctime)s] - %(levelname)s - %(message)s",
    "datefmt": "%d/%m/%Y - %H:%M:%S",
    "log_file": None,  # Ou _LOGS_PATH
}
