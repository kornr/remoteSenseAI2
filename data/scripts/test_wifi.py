# test_wifi.py
import pytest
from modules.wifi_manager import WifiManager

@pytest.fixture
def wifi_manager():
    """Fixture para inicializar WifiManager con valores por defecto."""
    return WifiManager()

def test_initialization(wifi_manager):
    """Verifica que el objeto WifiManager se inicialice correctamente."""
    assert wifi_manager is not None
    assert isinstance(wifi_manager, WifiManager)
    assert wifi_manager.ssid is None
    assert wifi_manager.password is None
    assert wifi_manager.is_connected is False

def test_connect_to_network(wifi_manager):
    """Prueba la conexión a una red Wi-Fi."""
    ssid = "MyNetwork"
    password = "password123"
    
    result = wifi_manager.connect(ssid, password)
    assert result is True
    assert wifi_manager.is_connected is True
    assert wifi_manager.ssid == ssid

def test_disconnect_from_network(wifi_manager):
    """Prueba la desconexión de la red Wi-Fi."""
    wifi_manager.connect("MyNetwork", "password123")
    wifi_manager.disconnect()
    assert wifi_manager.is_connected is False
    assert wifi_manager.ssid is None

def test_invalid_connection(wifi_manager):
    """Simula un intento de conexión con credenciales incorrectas."""
    ssid = "WrongNetwork"
    password = "wrongpassword"
    
    result = wifi_manager.connect(ssid, password)
    assert result is False
    assert wifi_manager.is_connected is False

def test_reconnect_to_same_network(wifi_manager):
    """Prueba reconectarse a la misma red después de desconectarse."""
    ssid = "MyNetwork"
    password = "password123"
    
    wifi_manager.connect(ssid, password)
    wifi_manager.disconnect()
    result = wifi_manager.connect(ssid, password)
    
    assert result is True
    assert wifi_manager.is_connected is True
    assert wifi_manager.ssid == ssid

