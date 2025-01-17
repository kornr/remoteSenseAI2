from modules.utils.logger import Logger

# Crear una instancia del logger
logger = Logger(log_dir="logs", log_level=logging.DEBUG)

# Obtener el logger configurado
log = logger.get_logger()

# Usar el logger en diferentes partes del código
log.info("Sistema iniciado.")
log.warning("Advertencia: El Wi-Fi podría estar inestable.")
log.error("Error: No se pudo conectar con el servidor.")
log.debug("Depuración: Datos del drone recibidos.")
log.critical("Error crítico: Sistema fuera de servicio.")
try:
    1 / 0
except ZeroDivisionError as e:
    log.exception("Se produjo una excepción al dividir por cero.")
