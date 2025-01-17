from modules.utils.file_manager import FileManager

# Crear instancia del gestor de archivos
file_manager = FileManager()

# Guardar un archivo JSON
data = {"latitude": 40.7128, "longitude": -74.0060}
file_manager.save_json(data, "location_data.json")

# Cargar el archivo JSON
loaded_data = file_manager.load_json("location_data.json")
print(loaded_data)

# Guardar un archivo CSV
csv_data = [
    {"latitude": 40.7128, "longitude": -74.0060},
    {"latitude": 34.0522, "longitude": -118.2437},
]
file_manager.save_csv(csv_data, "locations.csv", fieldnames=["latitude", "longitude"])

# Cargar el archivo CSV
csv_loaded_data = file_manager.load_csv("locations.csv")
print(csv_loaded_data)

# Hacer un backup del archivo
file_manager.backup_file("location_data.json")

# Listar archivos en el directorio
files = file_manager.list_files(extension=".json")
print(files)

# Eliminar un archivo
file_manager.delete_file("locations.csv")
Resumen:

    Gestión de archivos: El módulo permite guardar, cargar, respaldar y eliminar archivos en formatos JSON y CSV.
    Respaldo: Realiza copias de seguridad de los archivos, añadiendo un sufijo con la fecha y hora actuales.
    Listar archivos: Permite listar todos los archivos o solo aquellos con una extensión específica.
