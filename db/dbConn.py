from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from MySQLdb import *
import gl

"""Python SQLAlchemy+MySQLdb"""
#The engine to connect mysql
engine = create_engine('mysql://%s:%s@%s/%s?charset=%s'%(gl.db_config['user'],
                                                         gl.db_config['passwd'],
                                                         gl.db_config['host'],
                                                         gl.db_config['db'],
                                                         gl.db_config['charset']), echo=False)
#bm=BaseModel
bm = declarative_base()

def init_db():
    bm.metadata.create_all(engine)
    
def drop_db():
    bm.metadata.drop_all(engine)

#table_image Model
class Image(bm):
    __tablename__="image"
    
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    system = Column(String(10))
    size = Column(Integer(10))
    version = Column(String(20))
    description = Column(String(20))
    status = Column(Integer(10))

#initial database
init_db()

#sqlalchemy-session
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

#table to dbmeta
metadata = MetaData(engine)
img_table = Table('image',metadata,autoload=True)
