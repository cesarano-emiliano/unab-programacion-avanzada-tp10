"""
Ejercicio 2: Patrón de Comportamiento - Strategy
"""
from abc import ABC, abstractmethod
from typing import List

class DrillStrategy(ABC):
    """Interfaz común para estrategias de entrenamiento."""
    @abstractmethod
    def execute_drill(self, players: List[str]) -> None:
        pass


class BacksAttackStrategy(DrillStrategy):
    """Entrenamiento táctico enfocado en velocidad y juego desplegado."""
    def execute_drill(self, players: List[str]) -> None:
        print(f"-> Ejecutando jugada desplegada con {', '.join(players)}: Pases rápidos hacia la punta.")


class ForwardsScrumStrategy(DrillStrategy):
    """Entrenamiento enfocado en contacto, obtención y empuje."""
    def execute_drill(self, players: List[str]) -> None:
        print(f"-> Ejecutando práctica de Scrum y limpieza de Ruck con {', '.join(players)}: Enfoque estático.")


class RugbySessionContext:
    """El Contexto mantiene una referencia a la estrategia activa y delega su ejecución."""
    def __init__(self, strategy: DrillStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DrillStrategy):
        """Permite cambiar dinámicamente la táctica en tiempo de ejecución."""
        self._strategy = strategy

    def run_training(self, squad: List[str]):
        self._strategy.execute_drill(squad)


# --- Ejemplo Concreto de Uso ---
if __name__ == "__main__":
    print("\n=== TEST PATRÓN STRATEGY ===")
    
    jugadores = ["Juan", "Lucas", "Mateo", "Tomás"]
    
    # Definimos las estrategias disponibles
    entrenamiento_backs = BacksAttackStrategy()
    entrenamiento_forwards = ForwardsScrumStrategy()
    
    # Inicializamos el entrenamiento con la estrategia de backs
    sesion_entrenamiento = RugbySessionContext(entrenamiento_backs)
    print("Bloque 1 de la sesión:")
    sesion_entrenamiento.run_training(jugadores)
    
    # Cambiamos la estrategia dinámicamente según la necesidad de la práctica
    sesion_entrenamiento.set_strategy(entrenamiento_forwards)
    print("\nBloque 2 de la sesión (Cambio de estrategia dinámico):")
    sesion_entrenamiento.run_training(jugadores)