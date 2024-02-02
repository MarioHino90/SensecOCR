from typing import Dict, List
from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db_string = "postgresql://postgres:gr8Times!@3.217.57.231:5432/postgres"

db = create_engine(db_string)

base = declarative_base()


class DocumentMeta(base):
    __tablename__ = "metadata"
    id = Column(
        Integer, primary_key=True
    )  # probably still want automatic incrementing IDs
    path = Column(String)
    datecreated = Column(Date)
    author = Column(String)
    organization = Column(String)
    classification = Column(String)
    # etc ...


def create_tables() -> None:
    session = sessionmaker(db)
    session = session()
    base.metadata.create_all(db)


def write_documents(doc):
    session = sessionmaker(db)
    session = session()
    #for doc in docs:
    document = DocumentMeta(
        path=doc["path"],
        datecreated=doc["datecreated"],
        author=doc["author"],
        organization=doc["organization"],
        classification=doc["classification"]
        # etc ...
    )
    session.add(document)
    session.commit()
