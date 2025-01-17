import pytest
from modules.test_wifi_manager import WifiManager

@pytest.fixture
def drone_comm_manager():
    """Fixture para inicializar DroneCommManager."""
    return DroneCommManager()

def test_drone_comm_manager_initialization(drone_comm_manager):
    # Prueba la inicialización de DroneCommManager
    assert drone_comm_manager is not None
    assert isinstance(drone_comm_manager, DroneCommManager)

def test_send_data(drone_comm_manager):
    # Simula el envío de datos
    data = "Test Data"
    result = drone_comm_manager.send_data(data)
    assert result == "Data sent: Test Data"

def test_receive_data(drone_comm_manager):
    # Simula la recepción de datos
    drone_comm_manager.receive_data("Test Response")
    assert drone_comm_manager.received_data == "Test Response"

def test_connection_status(drone_comm_manager):
    # Verifica el estado de la conexión
    drone_comm_manager.connect()
    assert drone_comm_manager.is_connected() is True
    drone_comm_manager.disconnect()
    assert drone_comm_manager.is_connected() is False

if __name__ == "__main__":
    pytest.test_main()
