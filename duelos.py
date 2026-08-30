import random
import time
import os

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.energia = 100
        self.nivel = 1
        self.experiencia = 0
        self.ataques_especiales = {
            "Ataque Crítico": {"daño": 25, "costo": 20, "probabilidad": 0.8},
            "Golpe Demoledor": {"daño": 35, "costo": 30, "probabilidad": 0.6},
            "Defensa Reforzada": {"daño": 5, "costo": 15, "probabilidad": 1.0},
            "Ataque Tormenta": {"daño": 40, "costo": 35, "probabilidad": 0.5}
        }
        self.defensa = 5

    def ataque_normal(self):
        daño = random.randint(8, 15)
        return daño

    def ataque_especial(self, tipo_ataque):
        ataque = self.ataques_especiales.get(tipo_ataque)
        if not ataque:
            return None, "Ataque no válido"
        
        if self.energia < ataque["costo"]:
            return None, "Energía insuficiente"
        
        if random.random() > ataque["probabilidad"]:
            self.energia -= ataque["costo"]
            return 0, "¡Ataque falló!"
        
        self.energia -= ataque["costo"]
        daño_real = ataque["daño"] + random.randint(-5, 10)
        return max(0, daño_real), f"¡{tipo_ataque} exitoso!"

    def recibir_daño(self, daño):
        daño_reducido = max(1, daño - self.defensa)
        self.vida -= daño_reducido
        return daño_reducido

    def recuperar_energia(self):
        recuperado = random.randint(10, 20)
        self.energia = min(100, self.energia + recuperado)
        return recuperado

    def subir_nivel(self):
        self.nivel += 1
        self.vida += 10
        self.energia += 10
        self.defensa += 2

    def esta_vivo(self):
        return self.vida > 0

    def mostrar_estado(self):
        barra_vida = "█" * (self.vida // 5) + "░" * (20 - self.vida // 5)
        barra_energia = "█" * (self.energia // 5) + "░" * (20 - self.energia // 5)
        print(f"\n{self.nombre} - Nivel {self.nivel}")
        print(f"Vida:    [{barra_vida}] {self.vida}/100")
        print(f"Energía: [{barra_energia}] {self.energia}/100")
        print(f"Experiencia: {self.experiencia}/100")

class Duel:
    def __init__(self, nombre_j1, nombre_j2):
        self.jugador1 = Jugador(nombre_j1)
        self.jugador2 = Jugador(nombre_j2)
        self.turno = 1
        self.ronda = 1

    def mostrar_tablero(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print("=" * 60)
        print(f"              ⚔️  DUELO DE CAMPEONES ⚔️")
        print(f"                    RONDA {self.ronda}")
        print("=" * 60)
        
        self.jugador1.mostrar_estado()
        print()
        self.jugador2.mostrar_estado()
        print("=" * 60)

    def mostrar_opciones(self, jugador):
        print(f"\n🎮 Turno de {jugador.nombre}")
        print("\nOpciones de ataque:")
        print("1. Ataque Normal (8-15 daño)")
        print("2. Ataque Crítico (25 daño, 80% precisión, costo 20 energía)")
        print("3. Golpe Demoledor (35 daño, 60% precisión, costo 30 energía)")
        print("4. Defensa Reforzada (5 daño + defensa, costo 15 energía)")
        print("5. Ataque Tormenta (40 daño, 50% precisión, costo 35 energía)")
        print("6. Recuperar energía")
        print("7. Ver estadísticas")

    def ejecutar_turno(self, jugador_actual, jugador_rival):
        self.mostrar_tablero()
        self.mostrar_opciones(jugador_actual)
        
        while True:
            try:
                opcion = input(f"\n{jugador_actual.nombre}, ¿qué haces? (1-7): ")
                
                if opcion == "1":
                    daño = jugador_actual.ataque_normal()
                    daño_recibido = jugador_rival.recibir_daño(daño)
                    print(f"\n💥 {jugador_actual.nombre} realiza un ataque normal!")
                    print(f"✨ Daño causado: {daño_recibido}")
                    break
                
                elif opcion == "2":
                    daño, mensaje = jugador_actual.ataque_especial("Ataque Crítico")
                    if daño is not None:
                        daño_recibido = jugador_rival.recibir_daño(daño)
                        print(f"\n⚡ {mensaje}")
                        print(f"✨ Daño causado: {daño_recibido}")
                    else:
                        print(f"\n❌ {mensaje}")
                        continue
                    break
                
                elif opcion == "3":
                    daño, mensaje = jugador_actual.ataque_especial("Golpe Demoledor")
                    if daño is not None:
                        daño_recibido = jugador_rival.recibir_daño(daño)
                        print(f"\n💥 {mensaje}")
                        print(f"✨ Daño causado: {daño_recibido}")
                    else:
                        print(f"\n❌ {mensaje}")
                        continue
                    break
                
                elif opcion == "4":
                    daño, mensaje = jugador_actual.ataque_especial("Defensa Reforzada")
                    if daño is not None:
                        print(f"\n🛡️  {mensaje}")
                        jugador_actual.defensa += 5
                        print(f"Defensa aumentada a {jugador_actual.defensa}")
                    else:
                        print(f"\n❌ {mensaje}")
                        continue
                    break
                
                elif opcion == "5":
                    daño, mensaje = jugador_actual.ataque_especial("Ataque Tormenta")
                    if da��o is not None:
                        daño_recibido = jugador_rival.recibir_daño(daño)
                        print(f"\n🌪️  {mensaje}")
                        print(f"✨ Daño causado: {daño_recibido}")
                    else:
                        print(f"\n❌ {mensaje}")
                        continue
                    break
                
                elif opcion == "6":
                    recuperado = jugador_actual.recuperar_energia()
                    print(f"\n💚 {jugador_actual.nombre} recupera {recuperado} de energía")
                    break
                
                elif opcion == "7":
                    print(f"\n📊 Estadísticas de {jugador_actual.nombre}:")
                    print(f"Vida: {jugador_actual.vida}")
                    print(f"Energía: {jugador_actual.energia}")
                    print(f"Nivel: {jugador_actual.nivel}")
                    print(f"Defensa: {jugador_actual.defensa}")
                    continue
                
                else:
                    print("❌ Opción no válida")
                    continue
                    
            except ValueError:
                print("❌ Por favor, ingresa un número válido")

        time.sleep(2)

    def jugar(self):
        print("\n" + "=" * 60)
        print(f"🎮 ¡Bienvenido al DUELO DE CAMPEONES!")
        print(f"{self.jugador1.nombre} vs {self.jugador2.nombre}")
        print("=" * 60 + "\n")
        time.sleep(2)

        while self.jugador1.esta_vivo() and self.jugador2.esta_vivo():
            self.ejecutar_turno(self.jugador1, self.jugador2)
            
            if not self.jugador2.esta_vivo():
                break
            
            self.ejecutar_turno(self.jugador2, self.jugador1)
            
            if not self.jugador1.esta_vivo():
                break
            
            self.ronda += 1

        self.mostrar_tablero()
        self.mostrar_ganador()

    def mostrar_ganador(self):
        print("\n" + "=" * 60)
        if self.jugador1.esta_vivo():
            ganador = self.jugador1
            perdedor = self.jugador2
        else:
            ganador = self.jugador2
            perdedor = self.jugador1
        
        print(f"🏆 ¡¡{ganador.nombre.upper()} ES EL CAMPEÓN!!")
        print("=" * 60)
        print(f"\n📊 Estadísticas Finales:")
        print(f"\n🥇 {ganador.nombre}:")
        print(f"   Vida restante: {ganador.vida}")
        print(f"   Experiencia ganada: +50")
        ganador.experiencia += 50
        
        print(f"\n🥈 {perdedor.nombre}:")
        print(f"   Vida final: {perdedor.vida}")
        print(f"   Experiencia ganada: +20")
        perdedor.experiencia += 20
        
        if ganador.experiencia >= 100:
            ganador.subir_nivel()
            print(f"\n⭐ ¡{ganador.nombre} SUBIÓ DE NIVEL! Ahora es nivel {ganador.nivel}")
        
        print("\n" + "=" * 60)

def main():
    print("\n" + "=" * 60)
    print("   ⚔️  BIENVENIDO AL SISTEMA DE DUELOS ⚔️")
    print("=" * 60 + "\n")
    
    nombre_j1 = input("Nombre del jugador 1: ").strip() or "Jugador 1"
    nombre_j2 = input("Nombre del jugador 2: ").strip() or "Jugador 2"
    
    duel = Duel(nombre_j1, nombre_j2)
    duel.jugar()
    
    while True:
        jugar_again = input("\n¿Deseas jugar otro duelo? (s/n): ").lower()
        if jugar_again == 's':
            main()
        else:
            print("\n¡Gracias por jugar! ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
