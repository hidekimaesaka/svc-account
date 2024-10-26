from functools import cache

from sqlmodel import create_engine, Session
from sqlalchemy.engine import Engine


@cache
class Database:

    def __init__(self, database_uri: str = None):
        self.engine = self._create_engine(database_uri)
        self.session = self._create_session()

    def _create_engine(self, database_uri: str = None) -> Engine:
        self.conn_str = 'sqlite:///svc_database.db'

        if database_uri or self.conn_str:
            return create_engine(database_uri or self.conn_str)

        raise Exception('No database URI was found or provided')

    def _create_session(self) -> Session:
        if not self.engine:
            raise Exception('There is no engine to create a database session')

        return Session(bind=self.engine)
