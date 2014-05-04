import re

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float

Base = declarative_base()

class Cable(Base):
    __tablename__ = "cable"
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    refid = Column(String)
    classification = Column(String)
    origin = Column(String)
    destination = Column(Text)
    header = Column(Text)
    content = Column(Text)
    
    def subject(self):
        content = re.sub(r"\n", " ", self.content)
        m = re.search(r"SUBJECT:(.*?)\s\s\s\s", content)
        if m:
            return m.group(1).strip()
        else:
            return None

class Term(Base):
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True)
    term = Column(String)
    df = Column(Integer)
    tf = Column(Integer)

class DocumentVector(Base):
    __tablename__ = "document_vectors"

    id = Column(Integer, primary_key=True)
    cable_id = Column(Integer)
    term_id = Column(Integer)
    value = Column(Float)
