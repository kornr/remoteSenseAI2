import logging
import numpy as np
import json

logger = logging.getLogger("DataProcessor")

class DataProcessor:
    """Clase encargada del procesamiento de datos geoespaciales y de mapeo."""

    def __init__(self):
        """Inicializa el procesador de datos."""
        self.data = None
        self.processed_data = None

    def process_data(self, raw_data):
        """
        Procesar los datos geoespaciales de los drones.

        Parameters:
        - raw_data: Datos en bruto obtenidos de los drones (por ejemplo, coordenadas, imágenes, etc.)

        Returns:
        - processed_data: Datos procesados y listos para ser transmitidos
        """
        self.data = raw_data
        logger.info("Comenzando el procesamiento de datos geoespaciales.")

        # Paso 1: Filtrar y normalizar los datos si es necesario
        self.filtered_data = self.filter_data(self.data)
        self.normalized_data = self.normalize_data(self.filtered_data)

        # Paso 2: Agregar o convertir datos en un formato adecuado
        self.processed_data = self.aggregate_data(self.normalized_data)

        logger.info("Procesamiento de datos completado.")
        return self.processed_data

    def filter_data(self, data):
        """
        Filtrar los datos para eliminar valores erróneos o atípicos.

        Parameters:
        - data: Datos geoespaciales en bruto

        Returns:
        - filtered_data: Datos filtrados
        """
        logger.info("Filtrando los datos.")
        filtered_data = []
        for entry in data:
            if self.is_valid(entry):
                filtered_data.append(entry)
        return filtered_data

    def is_valid(self, entry):
        """Verifica si los datos son válidos (por ejemplo, comprobación de rangos o coherencia)."""
        lat, lon = entry['latitude'], entry['longitude']
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            return True
        return False

    def normalize_data(self, data):
        """
        Normalizar los datos para que estén en un rango común.

        Parameters:
        - data: Datos filtrados de los drones

        Returns:
        - normalized_data: Datos normalizados
        """
        logger.info("Normalizando los datos.")
        normalized_data = []
        latitudes = [entry['latitude'] for entry in data]
        longitudes = [entry['longitude'] for entry in data]

        lat_min, lat_max = min(latitudes), max(latitudes)
        lon_min, lon_max = min(longitudes), max(longitudes)

        for entry in data:
            normalized_entry = entry.copy()
            normalized_entry['latitude'] = (entry['latitude'] - lat_min) / (lat_max - lat_min)
            normalized_entry['longitude'] = (entry['longitude'] - lon_min) / (lon_max - lon_min)
            normalized_data.append(normalized_entry)

        return normalized_data

    def aggregate_data(self, data):
        """
        Agregar los datos procesados (puede ser una agregación geoespacial o por métricas).

        Parameters:
        - data: Datos normalizados y filtrados

        Returns:
        - aggregated_data: Datos agregados para enviar o almacenar
        """
        logger.info("Agregando los datos.")
        avg_lat = np.mean([entry['latitude'] for entry in data])
        avg_lon = np.mean([entry['longitude'] for entry in data])

        aggregated_data = {
            "average_latitude": avg_lat,
            "average_longitude": avg_lon,
            "total_entries": len(data),
            "raw_data": data
        }
        
        return aggregated_data

    def format_for_transmission(self, data):
        """
        Formatear los datos para su transmisión a través de la red (en este caso, en formato JSON).

        Parameters:
        - data: Datos procesados y agregados

        Returns:
        - formatted_data: Datos listos para ser enviados
        """
        logger.info("Formateando los datos para su transmisión.")
        return json.dumps(data)

    def save_processed_data(self, data, filename="processed_data.json"):
        """
        Guardar los datos procesados en un archivo.

        Parameters:
        - data: Datos procesados
        - filename: Nombre del archivo para guardar los datos
        """
        logger.info(f"Guardando los datos procesados en {filename}.")
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_processed_data(self, filename="processed_data.json"):
        """
        Cargar datos procesados desde un archivo.

        Parameters:
        - filename: Nombre del archivo desde el cual cargar los datos
        """
        logger.info(f"Cargando los datos procesados desde {filename}.")
        with open(filename, "r") as f:
            data = json.load(f)
        return data
