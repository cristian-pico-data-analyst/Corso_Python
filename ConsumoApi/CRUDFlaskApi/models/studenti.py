from sqlalchemy import Column, Integer, String, CHAR, Date
from sqlalchemy.orm import sessionmaker

base = sessionmaker()

class Studenti(base):
    __tablename__ = 'Studenti' # I dati li ho presi dal database StudentiDb

    StudenteId = Column(Integer, primary_key=True, index=True)
    Nome = Column(String(50), nullable=False)
    Cognome = Column(String(50), nullable=False)
    DataNascita = Column(Date)
    Email = Column(String(150), unique=True)
    Telefono = Column(String(50))
    CodiceFiscale = Column(CHAR(16), unique=True)