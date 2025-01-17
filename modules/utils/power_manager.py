import psutil
import logging
import time
import threading
from datetime import datetime

class PowerManager:
    """Clase encargada de gestionar el estado de la energía del sistema."""

    def __init__(self, battery_threshold=20, log_file="power_log.txt"):
        """
        Inicializa la gestión de energía.

        Parameters:
        - battery_threshold: El umbral de batería (en porcentaje) para advertir sobre baja energía.
        - log_file: El archivo donde se guardarán los registros de energía.
        """
        self.battery_threshold = battery_threshold
        self.log_file = log_file
        self.logger = logging.getLogger("PowerManager")
        self._setup_logging()
        self._stop_thread = False  # Variable para detener el hilo de verificación

    def _setup_logging(self):
        """Configura el sistema de logs para el PowerManager."""
        # Configuración de logging para registrar el estado de la energía
        log_format = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(filename=self.log_file, level=logging.INFO, format=log_format)
        self.logger.info("Iniciando gestión de energía.")

    def check_power_status(self):
        """
        Verifica el estado de la batería o del suministro de energía.

        Si la batería está por debajo del umbral, envía una advertencia.
        """
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            power_plugged = battery.power_plugged

            # Registra el estado actual de la batería
            self.logger.info(f"Estado de la batería: {percent}% - {'Conectado a corriente' if power_plugged else 'No conectado a corriente'}")
            print(f"Estado de la batería: {percent}% - {'Conectado a corriente' if power_plugged else 'No conectado a corriente'}")

            # Si la batería está por debajo del umbral, enviar una advertencia
            if percent < self.battery_threshold:
                self.logger.warning(f"¡Advertencia! La batería está por debajo del umbral crítico de {self.battery_threshold}% ({percent}%)")
                print(f"¡Advertencia! La batería está por debajo del umbral crítico de {self.battery_threshold}% ({percent}%)")

            # Si la batería se está agotando y no está conectada a la corriente
            if not power_plugged and percent < 10:
                self.logger.error("¡Error! La batería está críticamente baja y no está conectada a corriente.")
                print("¡Error! La batería está críticamente baja y no está conectada a corriente.")
                self.shutdown_system()

        else:
            self.logger.error("No se pudo obtener el estado de la batería.")
            print("No se pudo obtener el estado de la batería.")

    def shutdown_system(self):
        """Apaga el sistema de manera segura si la batería está críticamente baja."""
        self.logger.info("Iniciando apagado seguro del sistema debido a batería baja.")
        print("Iniciando apagado seguro del sistema debido a batería baja.")
        
        # Implementar la lógica para apagar los sistemas que lo requieran.
        # Por ejemplo, detener drones, desconectar Wi-Fi, guardar datos importantes.
        # Aquí puedes agregar tu lógica de apagado personalizado.
        time.sleep(3)  # Simulación de tiempo de apagado.
        self.logger.info("Sistema apagado correctamente.")
        print("Sistema apagado correctamente.")
        self._stop_thread = True  # Detener el hilo después del apagado

    def log_power_status(self):
        """
        Realiza un seguimiento periódico del estado de la batería y lo registra en un archivo de log.
        """
        self.logger.info("Iniciando seguimiento del estado de la energía.")
        while not self._stop_thread:
            self.check_power_status()
            time.sleep(60)  # Verifica cada 60 segundos el estado de la energía

    def start_power_check(self):
        """
        Inicia la verificación periódica del estado de la batería en un hilo.
        """
        power_check_thread = threading.Thread(target=self.log_power_status)
        power_check_thread.daemon = True  # El hilo se detendrá cuando el programa termine
        power_check_thread.start()

# Ejemplo de uso:
if __name__ == "__main__":
    power_manager = PowerManager()
    power_manager.start_power_check()  # Inicia la verificación periódica en un hilo separado

    # Simulación de ejecución continua (esto podría reemplazarse con otras operaciones del sistema)
    try:
        while True:
            time.sleep(1)  # El programa se mantiene ejecutándose
    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario.")
