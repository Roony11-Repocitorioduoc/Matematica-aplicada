import random

# Definimos una clase para los ataques
class Ataque:
    def __init__(self, nombre, tipo, danio, coste_energia=0):
        self.nombre = nombre
        self.tipo = tipo
        self.danio = danio
        self.coste_energia = coste_energia

    def calcular_danio(self, atacante, defensor):
        # La fórmula de daño puede ser más compleja, pero para fines de simplicidad,
        # vamos a utilizar la diferencia entre el ataque y la defensa, y consideramos
        # ventajas de tipo.
        base_danio = atacante.ataque + self.danio - defensor.defensa
        if base_danio < 0:
            base_danio = 0
        
        # Consideramos las ventajas de tipo
        if self.tipo == "fuego" and defensor.tipo == "planta":
            base_danio *= 2
        elif self.tipo == "agua" and defensor.tipo == "fuego":
            base_danio *= 2
        elif self.tipo == "planta" and defensor.tipo == "agua":
            base_danio *= 2
        
        return base_danio

# Definimos una clase para los Pokémon
class Pokemon:
    def __init__(self, nombre, tipo, salud, ataque, defensa, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.ataques = []

    def recibir_ataque(self, danio):
        self.salud -= danio
        if self.salud < 0:
            self.salud = 0

    def esta_vivo(self):
        return self.salud > 0

    def mostrar_info(self):
        print(f"{self.nombre} | Salud: {self.salud} | Ataque: {self.ataque} | Defensa: {self.defensa} | Velocidad: {self.velocidad}")

    def agregar_ataque(self, ataque):
        self.ataques.append(ataque)

# Creamos algunos ataques
hoja_aguda = Ataque("Hoja Aguda", "planta", 45)
somnifero = Ataque("Somnifero", "planta", 50)

ataque_rapido = Ataque("Ataque rápido", "electrico", 30)
impactrueno = Ataque("Impactrueno", "electrico", 40)

# Creamos algunos Pokémon
pikachu = Pokemon("Pikachu", "electrico", 100, 40, 35, 50)
bulbasaur = Pokemon("Bulbasaur", "planta", 100, 100, 100, 100)

# Agregamos los ataques a los Pokémon
pikachu.agregar_ataque(ataque_rapido)
pikachu.agregar_ataque(impactrueno)

bulbasaur.agregar_ataque(hoja_aguda)
bulbasaur.agregar_ataque(somnifero)

# Función para que el jugador realice su turno
def turno_jugador(jugador, oponente):
    print("\nEs tu turno!")
    print("Selecciona un ataque:")
    for i, ataque in enumerate(jugador.ataques, 1):
        print(f"{i}. {ataque.nombre} (daño: {ataque.danio})")
    
    ataque_idx = int(input("Elige el número de tu ataque: ")) - 1
    ataque = jugador.ataques[ataque_idx]

    danio = ataque.calcular_danio(jugador, oponente)
    print(f"¡{jugador.nombre} usó {ataque.nombre}! El daño infligido fue: {danio}")
    oponente.recibir_ataque(danio)

# Función para que el oponente realice su turno
def turno_oponente(jugador, oponente):
    print(f"\nEs el turno de {oponente.nombre}!")
    ataque = random.choice(oponente.ataques)
    
    danio = ataque.calcular_danio(oponente, jugador)
    print(f"{oponente.nombre} usó {ataque.nombre}! El daño infligido fue: {danio}")
    jugador.recibir_ataque(danio)

# Función para la batalla
def batalla(jugador, oponente):
    while jugador.esta_vivo() and oponente.esta_vivo():
        jugador.mostrar_info()
        oponente.mostrar_info()

        turno_jugador(jugador, oponente)
        if not oponente.esta_vivo():
            print(f"{oponente.nombre} ha sido derrotado. ¡Ganaste!")
            break

        turno_oponente(jugador, oponente)
        if not jugador.esta_vivo():
            print(f"{jugador.nombre} ha sido derrotado. ¡Perdiste!")
            break

# Comienza el juego
print("¡Bienvenido al juego de Pokémon!")
print("Tú serás Pikachu y lucharás contra Bulbasaur.\n")

batalla(pikachu, bulbasaur)
