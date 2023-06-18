from sqlalchemy import create_engine

from config import Config
from models import Base

if __name__ == '__main__':
    engine = create_engine(f"sqlite:///{Config.SQLITE_DB_PATH}", echo=True)
    Base.metadata.create_all(engine)
