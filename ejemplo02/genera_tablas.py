from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Base = declarative_base()

class Club(Base):
    __tablename__ = 'club'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    deporte = Column(String)
    fundacion = Column(Integer)
    jugadores = relationship("Jugador", back_populates="equipo")
    
    def __repr__(self):
        return "Club: nombre=%s deporte=%s fundación=%d" % (
            self.nombre, self.deporte, self.fundacion)

class Jugador(Base):
    __tablename__ = 'jugador'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    posicion = Column(String)
    dorsal = Column(Integer)
    club_id = Column(Integer, ForeignKey('club.id'))
    equipo = relationship("Club", back_populates="jugadores")
    
    def __repr__(self):
        return "Jugador: %s - posicion %f - dorsal:%d" % (
                self.nombre, self.posicion, self.dorsal)

Base.metadata.create_all(engine)
