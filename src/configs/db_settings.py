import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


class DatabaseConnector:

    def __init__(self):
        self.driver = "postgresql+psycopg2"
        self.server = os.getenv("PROD_HOST")
        self.username = os.getenv("PROD_USER")
        self.password = os.getenv("PROD_PASSWORD")
        self.database = os.getenv("PROD_DB")
        self.port = os.getenv("PROD_PORT")
        self.engine = None
        self.connect()

    def connect(self):
        try:
            self.engine = create_engine(
                f"{self.driver}://{self.username}:{self.password}@{self.server}:{self.port}/{self.database}",
                connect_args={"client_encoding": "utf8"},
            )
        except Exception as e:
            logging.error(f"❌ Erro ao conectar ao banco de dados: {e}")
            self.engine = None

    def get_engine(self):
        return self.engine

    def db_close(self):
        if self.engine:
            self.engine.dispose()
            logging.info("Conexão com o banco de dados fechada.")
