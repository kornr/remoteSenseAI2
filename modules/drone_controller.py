import socket
import threading
import time

class DroneController:
    def __init__(self, drone_ip, drone_port=8888):
        self.drone_ip = drone_ip       # IP del drone
        self.drone_port = drone_port   # Puerto de comunicación
        self.socket = None             # Socket de comunicación
        self.is_connected = False      # Estado de la conexión

    def connect(self):
        """Establecer conexión con el drone"""
        print(f"Conectando al drone en {self.drone_ip}:{self.drone_port}...")
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.drone_ip, self.drone_port))
            self.is_connected = True
            print("Conexión exitosa.")
        except Exception as e:
            print(f"Error al conectar con el drone: {e}")
            self.is_connected = False

    def send_command(self, command):
        """Enviar un comando al drone"""
        if not self.is_connected:
            print("No hay conexión establecida con el drone.")
            return
        
        try:
            self.socket.sendall(command.encode('utf-8'))
            print(f"Comando '{command}' enviado al drone.")
        except Exception as e:
            print(f"Error al enviar el comando: {e}")

    def receive_data(self):
        """Recibir datos del drone (por ejemplo, estado de la batería, ubicación)"""
        if not self.is_connected:
            print("No hay conexión establecida con el drone.")
            return
        
        try:
            data = self.socket.recv(1024).decode('utf-8')
            print(f"Datos recibidos del drone: {data}")
            return data
        except Exception as e:
            print(f"Error al recibir datos: {e}")
            return None

    def monitor_drone(self):
        """Monitorear el estado del drone en un hilo separado"""
        while self.is_connected:
            data = self.receive_data()
            if data:
                print(f"Estado del drone: {data}")
            time.sleep(2)  # Esperar 2 segundos antes de la siguiente lectura

    def disconnect(self):
        """Cerrar la conexión con el drone"""
        if self.socket:
            self.socket.close()
            self.is_connected = False
            print("Conexión cerrada.")

if __name__ == '__main__':
    drone_ip = "192.168.1.100"  # Ejemplo de IP del drone (ajustar según la red)
    controller = DroneController(drone_ip)

    # Conectar al drone
    controller.connect()

    # Iniciar monitoreo del drone
    if controller.is_connected:
        monitoring_thread = threading.Thread(target=controller.monitor_drone)
        monitoring_thread.start()

    # Enviar comandos (ejemplo)
    controller.send_command("MOVER IZQUIERDA")
    time.sleep(5)
    controller.send_command("MOVER DERECHA")

    # Desconectar
    controller.disconnect()

