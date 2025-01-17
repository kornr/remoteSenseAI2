import logging
import os

class Logger:
    """Clase encargada de configurar y gestionar los logs del sistema."""

    def __init__(self, log_dir="logs", log_level=logging.INFO):
        """
        Inicializa el Logger configurando el directorio y el nivel de log.

        Parameters:
        - log_dir: El directorio donde se guardarán los archivos de log.
        - log_level: El nivel de severidad de los logs (por defecto INFO).
        """
        self.log_dir = log_dir
        self.log_level = log_level
        self.logger = logging.getLogger("WiFiDroneSystem")

        # Crear directorio de logs si no existe
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            print(f"Directorio de logs creado en: {self.log_dir}")

        # Configuración de los manejadores de logs
        self._setup_logging()

    def _setup_logging(self):
        """
        Configura los manejadores de logging (consola y archivo).
        """
        # Formato del log
        log_format = "%(asctime)s - %(levelname)s - %(message)s"
        formatter = logging.Formatter(log_format)

        # Manejador para mostrar logs en la consola
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(self.log_level)
        self.logger.addHandler(console_handler)

        # Manejador para guardar logs en archivo
        log_filename = os.path.join(self.log_dir, "system.log")
        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(self.log_level)
        self.logger.addHandler(file_handler)

        # Configurar el nivel de log global
        self.logger.setLevel(self.log_level)

        print(f"Logging configurado con nivel {self.log_level} y archivos en {self.log_dir}")

    def get_logger(self):
        """Devuelve el logger configurado para su uso en otras partes del sistema."""
        return self.logger

    def log_info(self, message):
        """Registrar un mensaje informativo."""
        self.logger.info(message)

    def log_warning(self, message):
        """Registrar un mensaje de advertencia."""
        self.logger.warning(message)

    def log_error(self, message):
        """Registrar un mensaje de error."""
        self.logger.error(message)

    def log_debug(self, message):
        """Registrar un mensaje de depuración."""
        self.logger.debug(message)

    def log_critical(self, message):
        """Registrar un mensaje crítico."""
        self.logger.critical(message)

    def log_exception(self, exception):
        """Registrar una excepción con su traza."""
        self.logger.exception(f"Excepción ocurrida: {exception}")

