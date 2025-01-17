import pytest
from modules.test_wifi_manager import DroneCommManager

@pytest.fixture
def drone_comm_manager():
    """Fixture para inicializar DroneCommManager."""
    return DroneCommManager()

def test_drone_comm_manager_initialization():
    # Prueba la inicialización de DroneCommManager
    comm_manager = DroneCommManager()
    assert comm_manager is not None
    assert isinstance(comm_manager, DroneCommManager)

def test_send_data(comm_manager):
    # Simula el envío de datos
    data = "Test Data"
    result = comm_manager.send_data(data)
    assert result == "Data sent: Test Data"

def test_receive_data(comm_manager):
    # Simula la recepción de datos
    comm_manager.receive_data("Test Response")
    assert comm_manager.received_data == "Test Response"

def test_connection_status(comm_manager):
    # Verifica el estado de la conexión
    comm_manager.connect()
    assert comm_manager.is_connected() is True
    comm_manager.disconnect()
    assert comm_manager.is_connected() is False

if __name__ == "__main__":
    try:
    except ModuleNotFoundError as e:
        print(f"Error al importar: {e}")
    else:
        pytest.test_main()
