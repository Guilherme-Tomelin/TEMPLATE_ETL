import logging

from src.configs.db_settings import DatabaseConnector


from typing import List, Type, Dict
from sqlalchemy import inspect, MetaData, Table, select, and_
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.exc import SQLAlchemyError


class DatabaseHandler:
    def __init__(self, target="dev"):
        self.db_connector = DatabaseConnector(target=target)
        self.engine = self.db_connector.get_engine()
        self.Session = sessionmaker(bind=self.engine)

    # def fetch_columns_by_values(
    #     self,
    #     table: str,
    #     key_column: str,
    #     values_to_fetch: list[str],
    #     columns_to_fetch: list[str],
    # ) -> list[dict]:
    #     """
    #     Tipo: Manual \n
    #     Busca registros da tabela 'table' onde a coluna 'key_column' contém valores presentes em 'values_to_fetch', retornando apenas as colunas listadas em 'columns_to_fetch'.
    #     """
    #     if "." not in table:
    #         raise ValueError(
    #             "Parâmetro 'table' deve estar no formato 'schema.nome_tabela'."
    #         )
    #     schema, table_name = table.split(".")

    #     metadata = MetaData()
    #     tabela_ref = Table(
    #         table_name, metadata, autoload_with=self.engine, schema=schema
    #     )

    #     selected_columns = [
    #         tabela_ref.c[column_name] for column_name in columns_to_fetch
    #     ]

    #     filter = tabela_ref.c[key_column].in_(values_to_fetch)
    #     stmt = select(*selected_columns).where(filter)

    #     with self.Session() as session:
    #         result = session.execute(stmt).fetchall()
    #         return [dict(row._mapping) for row in result]

    # def fetch_columns_with_filters(
    #     self, 
    #     table: str, 
    #     columns: list[str], 
    #     **filters
    # ) -> list[dict]:
    #     """
    #     Tipo: Manual \n+
    #     Busca registros na tabela 'table' retornando colunas 'columns' que atendem aos filtros, '**filters', passados como parâmetros kwargs.
    #     """
    #     try:
    #         if "." not in table:
    #             raise ValueError(
    #                 "Parâmetro 'table' deve estar no formato 'schema.nome_tabela'."
    #             )

    #         schema, table_name = table.split(".")

    #         metadata = MetaData()
    #         tabela_ref = Table(
    #             table_name, metadata, autoload_with=self.engine, schema=schema
    #         )

    #         selected_cols = [tabela_ref.c[col] for col in columns]
    #         conditions = [tabela_ref.c[col] == val for col, val in filters.items()]

    #         stmt = select(*selected_cols).where(and_(*conditions))

    #         with self.Session() as session:
    #             result = session.execute(stmt).fetchall()
    #             return [dict(row._mapping) for row in result]
            

    #     except Exception as e:
    #         raise Exception(f"❌ Erro ao buscar dados em {table}: {e}")

    # def insert_instances(self, instances: list) -> None:
    #     try:
    #         with self.Session() as session:
    #             session.add_all(instances)
    #             session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         raise Exception(f"❌ Erro ao inserir instâncias: {e}")
    
    # def fetch_by_status(self, status: str, model: Type[DeclarativeBase]) -> List[Dict]:
    #     """
    #     Tipo: Model \n
    #     Retorna todos os registros da tabela 'model' onde a coluna 'status' é igual ao valor fornecido.
    #     """
    #     with self.Session() as session:
    #         stmt = select(model).where(model.status == status)
    #         results = session.execute(stmt).scalars().all()

    #         registros = [
    #             {col.name: getattr(obj, col.name) for col in model.__table__.columns}
    #             for obj in results
    #         ]
    #         return registros
        
    # def add_status (
    #         self, 
    #         tarefa_id: str|int, 
    #         status: str, 
    #         status_detalhado: str, 
    #         ) -> None:
        
    #     if isinstance(tarefa_id,str):
    #         tarefa_id = int(tarefa_id)

    #     with self.Session() as session:
    #         new_status = Status(
    #             tarefa_id = tarefa_id,
    #             status = status,
    #             sistema = "ETL_NM_Extract_Tasks",
    #             status_detalhado = status_detalhado 
    #         )

    #         session.add(new_status)
    #         session.commit()