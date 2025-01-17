import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from .test_drones_comm_manager import DroneCommManager


@pytest.fixture
def test_drones_comm_manager():
    """Fixture para inicializar un DroneCommManager para pruebas."""
    return DroneCommManager(drone_id="drone_test", port=8080)

def test_initialization(drone_comm_manager):
    """Prueba que DroneCommManager se inicializa correctamente."""
    assert drone_comm_manager.drone_id == "drone_test"
    assert drone_comm_manager.port == 8080
    assert isinstance(drone_comm_manager.peers, list)

def test_connect_to_nearby_drones(drone_comm_manager):
    """Prueba la conexión con drones cercanos."""
    nearby_drones = ["drone_1", "drone_2"]
    drone_comm_manager.connect_to_nearby_drones(nearby_drones)
    assert set(drone_comm_manager.peers) == set(nearby_drones)

def test_disconnect_from_all_peers(drone_comm_manager):
    """Prueba la desconexión de todos los drones cercanos."""
    nearby_drones = ["drone_1", "drone_2"]
    drone_comm_manager.connect_to_nearby_drones(nearby_drones)
    drone_comm_manager.disconnect_from_all_peers()
    assert not drone_comm_manager.peers

def test_peer_monitoring(drone_comm_manager, caplog):
    """Prueba el monitoreo de conexiones con los drones cercanos."""
    nearby_drones = ["drone_1"]
    drone_comm_manager.connect_to_nearby_drones(nearby_drones)

    with caplog.at_level("INFO"):
        drone_comm_manager.monitor_connections()
        assert any(
            "Monitoreando conexión con" in record.message for record in caplog.records
        )
