from sqlalchemy.orm import sessionmaker
from genera_tablas import engine, Club, Jugador

Session = sessionmaker(bind=engine)
session = Session()

with open("data/datos_clubs.txt", "r", encoding="utf-8") as archivo_clubs:
    for linea in archivo_clubs:
        nombre, deporte, fundacion = linea.strip().split(";")
        club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
        session.add(club)

session.commit()
print("Clubes guardados correctamente.")

with open("data/datos_jugadores.txt", "r", encoding="utf-8") as archivo_jugadores:
    for linea in archivo_jugadores:
        nombre_club, posicion, dorsal, nombre = linea.strip().split(";")
        club = session.query(Club).filter_by(nombre=nombre_club).one()
        jugador = Jugador(nombre=nombre, posicion=posicion, dorsal=int(dorsal), equipo=club)
        session.add(jugador)

session.commit()
print("Jugadores guardados correctamente.")
