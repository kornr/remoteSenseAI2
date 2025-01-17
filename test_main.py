import sys
import os
import logging
import time
from modules.test_wifi_manager import WifiManager
from modules.drone_comm_manager import DroneCommManager
from modules.data_processor import DataProcessor
from modules.power_manager import PowerManager

def test_main():
    # Configuración del sistema
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger("WiFiDroneSystem")
    logger.info("Iniciando el Sistema Portátil de Cobertura Wi-Fi y Mapeo Geoespacial")

    # Tiempo de inicio total
    start_time = time.time()

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
        drone_controller = DroneCommManager()
        drone_controller.initialize_drones()
        logger.info("Drones inicializados correctamente.")

        # Procesamiento de datos
        data_processor = DataProcessor()
        logger.info("Módulo de procesamiento de datos cargado.")

    except Exception as e:
        logger.error(f"Error durante la inicialización: {e}")
        return

    # Ciclo principal del sistema
    try:
        while True:
            logger.info("Iniciando operación de drones...")

            # Verificar estado de energía antes de continuar
            power_check_start = time.time()
            power_manager.check_power_status()
            power_check_end = time.time()
            logger.info(f"Tiempo de verificación de energía: {power_check_end - power_check_start:.2f} segundos")

            # Control de drones para recopilación de datos
            try:
                data_collection_start = time.time()
                drone_data = drone_controller.collect_geospatial_data()
                data_collection_end = time.time()
                logger.info(f"Datos geoespaciales recopilados por los drones. Tiempo: {data_collection_end - data_collection_start:.2f} segundos.")
            except Exception as e:
                logger.error(f"Error al recopilar datos geoespaciales: {e}")
                continue  # Continuar con la siguiente iteración del ciclo

            # Procesamiento de datos
            try:
                data_processing_start = time.time()
                processed_data = data_processor.process_data(drone_data)
                data_processing_end = time.time()
                logger.info(f"Datos procesados exitosamente. Tiempo de procesamiento: {data_processing_end - data_processing_start:.2f} segundos.")
            except Exception as e:
                logger.error(f"Error al procesar los datos: {e}")
                continue  # Continuar con la siguiente iteración del ciclo

            # Transmisión de datos y mantenimiento del Wi-Fi
            try:
                wifi_broadcast_start = time.time()
                wifi_manager.broadcast_data(processed_data)
                wifi_broadcast_end = time.time()
                logger.info(f"Datos transmitidos vía Wi-Fi. Tiempo de transmisión: {wifi_broadcast_end - wifi_broadcast_start:.2f} segundos.")
            except Exception as e:
                logger.error(f"Error al transmitir datos vía Wi-Fi: {e}")

    except KeyboardInterrupt:
        logger.info("Sistema detenido por el usuario.")
    except Exception as e:
        logger.error(f"Error durante la ejecución: {e}")
    finally:
        # Limpieza y apagado
        try:
            wifi_stop_start = time.time()
            wifi_manager.stop_wifi()
            wifi_stop_end = time.time()
            logger.info(f"Wi-Fi detenido correctamente. Tiempo de detención: {wifi_stop_end - wifi_stop_start:.2f} segundos.")
        except Exception as e:
            logger.error(f"Error al detener Wi-Fi: {e}")

        try:
            drone_shutdown_start = time.time()
            drone_controller.shutdown_drones()
            drone_shutdown_end = time.time()
            logger.info(f"Drones apagados correctamente. Tiempo de apagado: {drone_shutdown_end - drone_shutdown_start:.2f} segundos.")
        except Exception as e:
            logger.error(f"Error al apagar los drones: {e}")

        # Tiempo total de ejecución
        end_time = time.time()
        logger.info(f"Tiempo total de ejecución: {end_time - start_time:.2f} segundos.")
        
        logger.info("Sistema apagado correctamente.")

if __name__ == "__main__":
    test_main()
