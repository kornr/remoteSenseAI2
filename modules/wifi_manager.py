import time
import subprocess
import pywifi
from pywifi import PyWiFi, const, Profile

class WifiManager:
    def __init__(self, interface_name='wlan0', ssid='Drone_Network', password='password123'):
        self.interface_name = interface_name  # Interfaz de red Wi-Fi (por ejemplo, 'wlan0')
        self.ssid = ssid                      # Nombre del SSID (punto de acceso)
        self.password = password              # Contraseña de la red Wi-Fi
        self.wifi = PyWiFi()                   # Instancia de PyWiFi
        self.interface = self.wifi.interfaces()[0]  # Obtener la primera interfaz Wi-Fi
        self.profile = self._create_wifi_profile()  # Perfil para el punto de acceso

    def _create_wifi_profile(self):
        """Crear el perfil del punto de acceso Wi-Fi"""
        profile = Profile()
        profile.ssid = self.ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = self.password
        return profile

    def start_ap(self):
        """Iniciar el punto de acceso Wi-Fi"""
        print(f"Iniciando punto de acceso Wi-Fi '{self.ssid}'...")
        self.interface.remove_all_network_profiles()  # Limpiar perfiles antiguos
        self.interface.add_network_profile(self.profile)  # Añadir el perfil de la red
        self._start_network()  # Ejecutar el punto de acceso (implementación específica dependiendo del sistema)

    def stop_ap(self):
        """Detener el punto de acceso Wi-Fi"""
        print(f"Deteniendo el punto de acceso '{self.ssid}'...")
        self.interface.remove_all_network_profiles()  # Limpiar los perfiles
        # Aquí se implementaría la detención del punto de acceso en sistemas reales (ej. NetworkManager en Linux)

    def check_connectivity(self):
        """Verificar la conectividad a la red Wi-Fi"""
        print(f"Verificando conectividad a '{self.ssid}'...")
        if self.interface.status() == const.IFACE_CONNECTED:
            print(f"Conectado exitosamente a '{self.ssid}'")
            return True
        else:
            print(f"No se pudo conectar a '{self.ssid}'")
            return False

    def scan_networks(self):
        """Escanear redes disponibles"""
        print("Escaneando redes Wi-Fi...")
        self.interface.scan()
        time.sleep(2)  # Esperar para que se completen las búsquedas de redes
        networks = self.interface.scan_results()
        print("Redes encontradas:")
        for network in networks:
            print(f"SSID: {network.ssid} | Señal: {network.signal}")
        return networks

    def connect_to_network(self, ssid, password):
        """Conectar a una red Wi-Fi"""
        print(f"Intentando conectar a {ssid}...")
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        self.interface.remove_all_network_profiles()
        self.interface.add_network_profile(profile)
        self.interface.connect(self.interface.network_profiles()[0])
        time.sleep(5)  # Esperar a que se establezca la conexión
        return self.check_connectivity()

    def auto_reconnect(self):
        """Intentar reconectar a la red Wi-Fi automáticamente"""
        retries = 3
        while retries > 0:
            if self.check_connectivity():
                return True
            print(f"Reintentando conexión ({retries} intentos restantes)...")
            time.sleep(3)
            retries -= 1
        print("No se pudo establecer la conexión después de múltiples intentos.")
        return False

    def _start_network(self):
        """Comando para iniciar el punto de acceso, sistema específico"""
        try:
            # Configuración básica para hostapd
            subprocess.run(['sudo', 'hostapd', '-B', '/etc/hostapd/hostapd.conf'], check=True)
            print(f"Punto de acceso '{self.ssid}' iniciado correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al iniciar el punto de acceso: {e}")

if __name__ == '__main__':
    wifi_manager = WifiManager()
    
    # Iniciar punto de acceso
    wifi_manager.start_ap()

    # Verificar conectividad
    time.sleep(2)  # Esperar a que el AP esté listo
    wifi_manager.check_connectivity()

    # Escanear redes disponibles
    wifi_manager.scan_networks()

    # Intentar reconectar si la conexión falla
    wifi_manager.auto_reconnect()

    # Detener el punto de acceso
    wifi_manager.stop_ap()
