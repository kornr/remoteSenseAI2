import random
import time
import logging

logger = logging.getLogger("DroneLocator")


class DroneLocator:
    """Clase que simula la localización de los drones en un área dada."""

    def __init__(self, drone_id):
        """Inicializa la localización del drone."""
        self.drone_id = drone_id
        self.position = (random.uniform(-100, 100), random.uniform(-100, 100))  # Coordenadas aleatorias en 2D
        self.last_update_time = time.time()

    def get_position(self):
        """Obtener la posición actual del drone."""
        return self.position

    def update_position(self):
        """Simula el movimiento del drone y actualiza su posición."""
        self.position = (random.uniform(-100, 100), random.uniform(-100, 100))
        self.last_update_time = time.time()
        logger.info(f"Drone {self.drone_id} nueva posición: {self.position}")

    def detect_nearby_drones(self, all_drones, range_radius=50):
        """Detecta drones cercanos dentro de un rango determinado."""
        nearby_drones = []
        for drone in all_drones:
            distance = self.calculate_distance(self.position, drone.get_position())
            if distance < range_radius:
                nearby_drones.append(drone)
        return nearby_drones

    @staticmethod
    def calculate_distance(pos1, pos2):
        """Calcula la distancia euclidiana entre dos posiciones."""
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2) ** 0.5
