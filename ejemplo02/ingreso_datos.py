from sqlalchemy.orm import sessionmaker
from genera_tablas import engine, Club, Jugador

# Creamos una conexion con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Leemos y guardamos los clubes desde el archivo
with open("data/datos_clubs.txt", "r", encoding="utf-8") as archivo_clubs:
    for linea in archivo_clubs:
        # Se separan los datos del club y se crea un objeto Club
        nombre, deporte, fundacion = linea.strip().split(";")
        club = Club(nombre=nombre, deporte=deporte, fundacion=int(fundacion))
        session.add(club)

session.commit()
print("Clubes guardados correctamente.")

# Leemos y guardamos los jugadores desde el archivo
with open("data/datos_jugadores.txt", "r", encoding="utf-8") as archivo_jugadores:
    for linea in archivo_jugadores:
        # Se obtienen datos del jugador y se busca el club correspondiente
        nombre_club, posicion, dorsal, nombre = linea.strip().split(";")
        club = session.query(Club).filter_by(nombre=nombre_club).one()
        # Se crea el jugador y se asocia al club
        jugador = Jugador(nombre=nombre, posicion=posicion, dorsal=int(dorsal), equipo=club)
        session.add(jugador)

session.commit()
print("Jugadores guardados correctamente.")
