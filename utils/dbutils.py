from sqlalchemy import create_engine

from utils.config import DBConfig

db_engine = create_engine(
    DBConfig().get_connection_str(),
    connect_args={"options": f"-c search_path={DBConfig.DBSCHEMA}"},
    echo=True,
)