from sqlalchemy.orm import sessionmaker
from configuracion import engine, Club, Jugador

Session = sessionmaker(bind=engine)
session = Session()

with open("data/datos_clubs.txt", "r", encoding="utf-8") as archivo_clubs:
    for e in archivo_clubs:
        nombre, deporte, fundacion = e.strip().split(";")
        club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
        session.add(club)

session.commit()
print("Clubes guardados correctamente.")



with open("data/datos_jugadores.txt", "r", encoding="utf-8") as archivo_jugadores:
    for e in archivo_jugadores:
        nombre_club, posicion, dorsal, nombres = e.strip().split(";")
        club = session.query(Club).filter_by(nombre=nombre_club).one()
        jugador = Jugador(nombres=nombres, posicion=posicion, dorsal=int(dorsal), equipo=club)
        session.add(jugador)

session.commit()
print("Jugadores guardados correctamente.")
