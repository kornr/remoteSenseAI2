import os
import logging
from wifi_manager import WifiManager
from drone_controller import DroneController
from data_processor import DataProcessor
from utils.power_manager import PowerManager

def main():
    # Configuración del sistema
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger("WiFiDroneSystem")
    logger.info("Iniciando el Sistema Portátil de Cobertura Wi-Fi y Mapeo Geoespacial")

    # Inicializar componentes principales
    try:
        # Gestión de energía
        power_manager = PowerManager()
        power_manager.check_power_status()

        # Configuración de Wi-Fi
        wifi_manager = WifiManager(ssid="Dron-WiFi", password="12345678")
        wifi_manager.start_wifi()
        logger.info("Wi-Fi configurado exitosamente.")

        # Control de drones
        drone_controller = DroneController()
        drone_controller.initialize_drones()

        # Procesamiento de datos
        data_processor = DataProcessor()
    except Exception as e:
        logger.error(f"Error durante la inicialización: {e}")
        return

    # Ciclo principal del sistema
    try:
        while True:
            logger.info("Iniciando operación de drones...")
            
            # Control de drones para recopilación de datos
            drone_data = drone_controller.collect_geospatial_data()
            logger.info("Datos geoespaciales recopilados por los drones.")

            # Procesamiento de datos
            processed_data = data_processor.process_data(drone_data)
            logger.info("Datos procesados exitosamente.")

            # Transmisión de datos y mantenimiento del Wi-Fi
            wifi_manager.broadcast_data(processed_data)
            logger.info("Datos transmitidos vía Wi-Fi.")

            # Verificar estado de energía
            power_manager.check_power_status()

    except KeyboardInterrupt:
        logger.info("Sistema detenido por el usuario.")
    except Exception as e:
        logger.error(f"Error durante la ejecución: {e}")
    finally:
        # Limpieza y apagado
        wifi_manager.stop_wifi()
        drone_controller.shutdown_drones()
        logger.info("Sistema apagado correctamente.")

if __name__ == "__main__":
    main()
