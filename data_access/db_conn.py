from sqlalchemy import create_engine
from config.get_config import config_data
engine = create_engine(config_data['mysql'])

