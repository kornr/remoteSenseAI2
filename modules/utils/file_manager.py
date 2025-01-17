import os
import json
import csv
import logging

logger = logging.getLogger("FileManager")

class FileManager:
    """Clase encargada de gestionar la carga, guardado y organización de archivos."""

    def __init__(self, data_dir="data"):
        """Inicializa el gestor de archivos con el directorio de datos por defecto."""
        self.data_dir = data_dir

        # Crear directorios de datos si no existen
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            logger.info(f"Directorio {self.data_dir} creado.")
    
    def save_json(self, data, filename):
        """
        Guardar datos en un archivo JSON.

        Parameters:
        - data: Los datos que se quieren guardar.
        - filename: Nombre del archivo donde guardar los datos.
        """
        try:
            filepath = os.path.join(self.data_dir, filename)
            with open(filepath, "w") as f:
                json.dump(data, f, indent=4)
            logger.info(f"Datos guardados exitosamente en {filepath}.")
        except Exception as e:
            logger.error(f"Error al guardar los datos en {filename}: {e}")
    
    def load_json(self, filename):
        """
        Cargar datos desde un archivo JSON.

        Parameters:
        - filename: Nombre del archivo desde el cual cargar los datos.

        Returns:
        - Los datos cargados desde el archivo JSON.
        """
        try:
            filepath = os.path.join(self.data_dir, filename)
            with open(filepath, "r") as f:
                data = json.load(f)
            logger.info(f"Datos cargados exitosamente desde {filepath}.")
            return data
        except Exception as e:
            logger.error(f"Error al cargar los datos desde {filename}: {e}")
            return None

    def save_csv(self, data, filename, fieldnames):
        """
        Guardar datos en un archivo CSV.

        Parameters:
        - data: Los datos a guardar en formato de lista de diccionarios.
        - filename: Nombre del archivo CSV.
        - fieldnames: Lista con los nombres de las columnas para el CSV.
        """
        try:
            filepath = os.path.join(self.data_dir, filename)
            with open(filepath, mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            logger.info(f"Datos guardados exitosamente en {filepath}.")
        except Exception as e:
            logger.error(f"Error al guardar los datos en {filename}: {e}")
    
    def load_csv(self, filename):
        """
        Cargar datos desde un archivo CSV.

        Parameters:
        - filename: Nombre del archivo CSV.

        Returns:
        - Lista de diccionarios con los datos del archivo CSV.
        """
        try:
            filepath = os.path.join(self.data_dir, filename)
            with open(filepath, mode='r') as f:
                reader = csv.DictReader(f)
                data = [row for row in reader]
            logger.info(f"Datos cargados exitosamente desde {filepath}.")
            return data
        except Exception as e:
            logger.error(f"Error al cargar los datos desde {filename}: {e}")
            return None

    def backup_file(self, filename):
        """
        Realizar un backup de un archivo (JSON o CSV) copiándolo con un sufijo de fecha y hora.

        Parameters:
        - filename: El nombre del archivo a respaldar.
        """
        try:
            filepath = os.path.join(self.data_dir, filename)
            if not os.path.exists(filepath):
                logger.warning(f"El archivo {filename} no existe para respaldar.")
                return

            backup_filename = f"{filename.split('.')[0]}_backup_{self.get_current_timestamp()}.{filename.split('.')[1]}"
            backup_filepath = os.path.join(self.data_dir, backup_filename)
            os.rename(filepath, backup_filepath)  # Renombrar el archivo original como backup
            logger.info(f"Archivo respaldado exitosamente como {backup_filename}.")
        except Exception as e:
            logger.error(f"Error al hacer backup del archivo {filename}: {e}")

    def get_current_timestamp(self):
        """Obtener la fecha y hora actual como una cadena de texto."""
        from datetime import datetime
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def list_files(self, extension=None):
        """
        Listar archivos en el directorio de datos.

        Parameters:
        - extension: Filtro para listar solo archivos con una extensión específica.

        Returns:
        - Una lista de archivos que coinciden con la extensión dada.
        """
        try:
            files = os.listdir(self.data_dir)
            if extension:
                files = [file for file in files if file.endswith(extension)]
            logger.info(f"Archivos listados: {files}.")
            return files
        except Exception as e:
            logger.error(f"Error al listar los archivos: {e}")
            return []

    def delete_file(self, filename):
        """
        Eliminar un archivo del sistema.

        Parameters:
        - filename: El nombre del archivo que se desea eliminar.
        """
        try:
            filepath = os.path.join(self.data_dir, filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                logger.info(f"Archivo {filename} eliminado exitosamente.")
            else:
                logger.warning(f"El archivo {filename} no existe.")
        except Exception as e:
            logger.error(f"Error al eliminar el archivo {filename}: {e}")
