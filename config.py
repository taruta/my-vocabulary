from pathlib import Path


class Config:
    ROOT_PATH = Path(__file__).parent
    SQLITE_DB_PATH = ROOT_PATH / 'database.db'
