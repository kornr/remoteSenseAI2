# Dronep2pwifi/test_drone_comm_manager.py

import pytest
from modules.drone_comm_manager import DroneCommManager

@pytest.fixture
def comm_manager():
    """Fixture para inicializar DroneCommManager."""
    return DroneCommManager()

def test_drone_comm_manager_initialization(comm_manager):
    # Prueba la inicialización de DroneCommManager
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
