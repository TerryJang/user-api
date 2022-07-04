import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import ROOT_PATH

Base = declarative_base()
logger = logging.getLogger('server')


class MysqlConnectionPool:
    config = {}
    engine = None

    def setup(self,  config: dict):
        try:
            if os.environ.get('APPLICATION_ENV') == 'test':
                url = f'sqlite:///{ROOT_PATH}/test.db'
                self.engine = create_engine(url)
            else:
                self.config = config
                mysql_config = self.config["mysql"]
                self.engine = create_engine(f'mysql+mysqldb://{mysql_config["user"]}:{mysql_config["password"]}@{mysql_config["host"]}:{mysql_config["port"]}/{mysql_config["db"]}')
        except Exception as e:
            logging.error(f'[ERROR] {str(e)}')

    def get_connection(self, autocommit=False) -> scoped_session:
        try:
            return scoped_session(sessionmaker(bind=self.engine, autocommit=autocommit))
        except Exception as e:
            logging.error(f'[ERROR] {str(e)}')


mysql_connection_pool = MysqlConnectionPool()
