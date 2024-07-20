from sqlalchemy import create_engine

from config import PATH_TO_DB_FILE

engine = create_engine(fr"sqlite:///{PATH_TO_DB_FILE.absolute()}", echo=False)
