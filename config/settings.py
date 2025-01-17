# config/settings.py

class Settings:
    """Clase para manejar la configuración del sistema."""

    # Configuración de Wi-Fi
    WIFI_SSID = "Dron-WiFi"               # Nombre de la red Wi-Fi
    WIFI_PASSWORD = "12345678"            # Contraseña de la red Wi-Fi
    WIFI_TIMEOUT = 30                     # Tiempo en segundos para esperar la conexión Wi-Fi

    # Configuración de los drones
    DRONE_MAX_ALTITUDE = 500              # Altitud máxima que los drones pueden alcanzar (en metros)
    DRONE_MIN_ALTITUDE = 10               # Altitud mínima en la que los drones operan (en metros)
    DRONE_BATTERY_WARNING_THRESHOLD = 20  # Umbral de batería para advertencia (en %)
    DRONE_CONNECTION_RETRY_LIMIT = 5      # Número de intentos de reconexión en caso de error de comunicación

    # Configuración de energía
    POWER_LOW_THRESHOLD = 15             # Umbral de energía baja (en %)
    POWER_WARNING_MESSAGE = "¡Advertencia! Energía baja. Conecte a una fuente de alimentación."

    # Configuración de transmisión de datos
    DATA_BROADCAST_INTERVAL = 10         # Intervalo de tiempo (en segundos) entre las transmisiones de datos de los drones
    DATA_FORMAT = "JSON"                 # Formato de los datos transmitidos (puede ser JSON, XML, etc.)
    
    # Configuración de logs
    LOG_LEVEL = "INFO"                   # Nivel de log (INFO, DEBUG, ERROR, etc.)
    LOG_FILE = "logs/system_log.txt"     # Ruta donde se almacenan los logs del sistema
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # Formato del log

    # Otras configuraciones generales
    SYSTEM_NAME = "Wi-Fi Drone System"    # Nombre del sistema
    MAX_RETRIES = 3                      # Número máximo de intentos para operaciones críticas como la conexión Wi-Fi

    @classmethod
    def get_wifi_config(cls):
        """Retorna la configuración Wi-Fi."""
        return {
            "ssid": cls.WIFI_SSID,
            "password": cls.WIFI_PASSWORD,
            "timeout": cls.WIFI_TIMEOUT
        }

    @classmethod
    def get_drone_config(cls):
        """Retorna la configuración de los drones."""
        return {
            "max_altitude": cls.DRONE_MAX_ALTITUDE,
            "min_altitude": cls.DRONE_MIN_ALTITUDE,
            "battery_warning_threshold": cls.DRONE_BATTERY_WARNING_THRESHOLD,
            "connection_retry_limit": cls.DRONE_CONNECTION_RETRY_LIMIT
        }

    @classmethod
    def get_power_config(cls):
        """Retorna la configuración de energía."""
        return {
            "low_threshold": cls.POWER_LOW_THRESHOLD,
            "warning_message": cls.POWER_WARNING_MESSAGE
        }

    @classmethod
    def get_data_config(cls):
        """Retorna la configuración de datos."""
        return {
            "broadcast_interval": cls.DATA_BROADCAST_INTERVAL,
            "data_format": cls.DATA_FORMAT
        }

    @classmethod
    def get_log_config(cls):
        """Retorna la configuración de los logs."""
        return {
            "log_level": cls.LOG_LEVEL,
            "log_file": cls.LOG_FILE,
            "log_format": cls.LOG_FORMAT
        }

    @classmethod
    def get_system_config(cls):
        """Retorna configuración general del sistema."""
        return {
            "system_name": cls.SYSTEM_NAME,
            "max_retries": cls.MAX_RETRIES
        }

# Acceso a la configuración y visualización
config = Settings()

wifi_settings = config.get_wifi_config()
drone_settings = config.get_drone_config()
power_settings = config.get_power_config()
data_settings = config.get_data_config()
log_settings = config.get_log_config()
system_settings = config.get_system_config()

# Imprimir configuración
print("Wi-Fi Configuration:", wifi_settings)
print("Drone Configuration:", drone_settings)
print("Power Configuration:", power_settings)
print("Data Configuration:", data_settings)
print("Log Configuration:", log_settings)
print("System Configuration:", system_settings)
