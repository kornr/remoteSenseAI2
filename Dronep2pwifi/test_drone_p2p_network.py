import time
import logging
import socket
from threading import Thread

logger = logging.getLogger("DroneP2PNetwork")

class DroneP2PNetwork:
    """Clase para gestionar la red P2P entre drones."""

    def __init__(self, drone_id, port=5000):
        """Inicializa el sistema de red P2P entre drones."""
        self.drone_id = drone_id
        self.port = port
        self.connections = {}  # Diccionario que guarda conexiones activas (drone_id -> socket)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("0.0.0.0", self.port))
        self.socket.settimeout(5)
        self.peers = []  # Lista de IDs de drones cercanos (vecinos)

    def add_peer(self, peer_ip):
        """Agregar un peer (drone cercano) a la red."""
        if peer_ip not in self.peers:
            self.peers.append(peer_ip)

    def remove_peer(self, peer_ip):
        """Eliminar un peer de la red."""
        if peer_ip in self.peers:
            self.peers.remove(peer_ip)

    def send_data(self, data, target_ip):
        """Enviar datos a un drone específico."""
        try:
            self.socket.sendto(data.encode(), (target_ip, self.port))
            logger.info(f"Datos enviados a {target_ip}")
        except Exception as e:
            logger.error(f"Error al enviar datos a {target_ip}: {e}")

    def listen_for_messages(self):
        """Escuchar mensajes entrantes de otros drones."""
        while True:
            try:
                message, address = self.socket.recvfrom(1024)
                logger.info(f"Mensaje recibido de {address}: {message.decode()}")
                self.handle_received_message(message.decode(), address)
            except socket.timeout:
                continue
            except Exception as e:
                logger.error(f"Error al recibir mensaje: {e}")

    def handle_received_message(self, message, address):
        """Manejar el mensaje recibido de un peer."""
        # Se pueden agregar condiciones según el tipo de mensaje recibido
        if message == "Ping":
            self.send_data("Pong", address[0])
        # Otros tipos de mensajes pueden ser manejados aquí

    def start_listening(self):
        """Inicia el hilo para escuchar los mensajes entrantes."""
        listening_thread = Thread(target=self.listen_for_messages)
        listening_thread.daemon = True
        listening_thread.start()

    def broadcast_data(self, data):
        """Difundir datos a todos los peers."""
        for peer_ip in self.peers:
            self.send_data(data, peer_ip)

    def connect_to_peer(self, peer_ip):
        """Establecer una conexión con un peer."""
        self.add_peer(peer_ip)
        logger.info(f"Conectado con el drone {peer_ip}")
        self.broadcast_data(f"Drone {self.drone_id} está en línea.")

    def disconnect_from_peer(self, peer_ip):
        """Desconectar a un peer de la red."""
        self.remove_peer(peer_ip)
        self.broadcast_data(f"Drone {self.drone_id} se desconectó.")
        logger.info(f"Desconectado de {peer_ip}")

    def reconnect_peer(self, peer_ip):
        """Intentar reconectar a un drone si la conexión se pierde."""
        logger.warning(f"Reconectando con {peer_ip}...")
        self.connect_to_peer(peer_ip)
        time.sleep(5)  # Espera antes de intentar nuevamente

    def maintain_connections(self):
        """Asegurarse de que todas las conexiones sean estables."""
        for peer_ip in self.peers:
            try:
                # Intentar enviar un 'ping' a cada peer para verificar su conexión
                self.send_data("Ping", peer_ip)
            except Exception as e:
                logger.error(f"Error al mantener conexión con {peer_ip}: {e}")
                self.reconnect_peer(peer_ip)
