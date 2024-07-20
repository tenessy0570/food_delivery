import logging
from pathlib import Path

format_ = "[%(name)s][%(levelname)s][%(asctime)s] on line %(lineno)d - %(filename)s.%(funcName)s - %(message)s"
logging.basicConfig(format=format_, level=logging.INFO)

logger = logging.getLogger("app")

ROOT_PATH = Path(__file__).parent
PATH_TO_DB_FILE = ROOT_PATH.absolute() / "db" / "db.db"
