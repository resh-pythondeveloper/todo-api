from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from app.configs.settings import settings

DATABASE_URL=settings.DATABASE_URL
engine=create_engine(DATABASE_URL)
Base=declarative_base()
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)