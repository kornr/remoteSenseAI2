Ejemplo de Uso:

    Iniciar drones con red P2P:


from modules.drone_comm_manager import DroneCommManager
from modules.drone_locator import DroneLocator

# Simulamos que tenemos 3 drones
drones = []
for drone_id in range(3):
    drone_locator = DroneLocator(drone_id)
    drone_comm_manager = DroneCommManager(drone_id)
    drones.append({"locator": drone_locator, "comm_manager": drone_comm_manager})

# Conectar drones cercanos
for drone in drones:
    nearby_drones = drone["locator"].detect_nearby_drones([d["locator"] for d in drones if d != drone])
    drone["comm_manager"].connect_to_nearby_drones([d.get_position() for d in nearby_drones])

# Los drones empiezan a comunicarse entre ellos
drones[0]["comm_manager"].send_data("Datos de mapeo geoespacial")

Resumen:

Con estos módulos, los drones pueden formar una red P2P para transmitir y recibir datos entre ellos, 
incluso si pierden la conexión con una estación central. Estos módulos pueden ser ampliados o modificados 
dependiendo de los requisitos específicos del proyecto y la infraestructura de red.
