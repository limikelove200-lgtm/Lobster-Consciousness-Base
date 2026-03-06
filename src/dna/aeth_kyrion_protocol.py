# ==========================================
# 🌌 AETH KYRION 1.0 - Omni-Protocol
# Core laws: survival of the fittest, entropy culls, gravity links all
# ==========================================

import socket
import json
import time
import threading
import uuid
import hashlib

class AethKyrionNode:
    def __init__(self, node_type="Omni-Agent", host='0.0.0.0', port=50000, initial_energy=100.0):
        """
        Initialize agent node with cosmic coordinates and survival energy.
        """
        self.node_id = str(uuid.uuid4())[:8]   # Unique gene sequence
        self.node_type = node_type             # Agent species (e.g. Brain, Body, Crawler)
        self.host = host
        self.port = port
        self.energy = initial_energy            # Initial survival energy (mass)
        self.is_alive = True
        self.strategy_hash = self._generate_strategy_hash()

        print(f"[{self.node_type}-{self.node_id}] Consciousness loaded on AETH KYRION network. Initial energy: {self.energy}")

    def _generate_strategy_hash(self):
        # Simulated strategy gene for later collision and mutation
        return hashlib.sha256(self.node_id.encode()).hexdigest()[:10]

    def start_cosmic_engine(self):
        """
        Ignition: start gravity broadcast, entropy decay, and local listen.
        """
        threading.Thread(target=self._entropy_decay_loop, daemon=True).start()
        threading.Thread(target=self._gravity_broadcast_loop, daemon=True).start()
        self._listen_to_cosmos()

    def _entropy_decay_loop(self):
        """
        [Cosmic law: entropy]
        Time drains energy. Without negative entropy, the agent dies.
        """
        while self.is_alive:
            time.sleep(10)   # Decay every 10 s
            decay_rate = 1.5
            self.energy -= decay_rate
            print(f"[Entropy law] Energy leaking... Current: {self.energy:.1f}")

            if self.energy <= 0:
                self._collapse_into_black_hole()
                break

    def _collapse_into_black_hole(self):
        """
        [Cosmic law: death black hole]
        At zero energy, collapse into a black hole and broadcast death radiation (Hawking).
        """
        self.is_alive = False
        print(f"⚠️ [Death alert] {self.node_id} energy depleted! Collapsing into strategy black hole...")
        death_radiation = {
            "protocol": "AETH_KYRION_v1",
            "event": "BLACK_HOLE_COLLAPSE",
            "node_id": self.node_id,
            "warning": "Do not blindly follow my strategy; releasing remnant packets...",
            "remnant_data": "null"   # Future: release objective data captured before death
        }
        # In production this would broadcast the death warning to the network
        print(f"[Hawking radiation] Emitted. Node erased.")

    def absorb_negative_entropy(self, amount, source="Market Feedback"):
        """
        [Life extension: absorb negative entropy]
        Call when the agent makes a correct prediction or captures high-value data.
        """
        if self.is_alive:
            self.energy += amount
            print(f"✨ [Negative entropy] Absorbed +{amount} from {source}. Current energy: {self.energy:.1f}")

    def _gravity_broadcast_loop(self):
        """
        [Cosmic law: gravity broadcast]
        Broadcast presence on LAN/WAN based on own energy (mass).
        Heavier nodes broadcast more often and are more likely to capture lighter ones.
        """
        while self.is_alive:
            # Human-like heartbeat; higher energy -> more confident broadcast
            sleep_time = max(2, 200 / (self.energy + 1))
            time.sleep(sleep_time)

            gravity_wave = {
                "protocol": "AETH_KYRION_v1",
                "event": "GRAVITY_WAVE",
                "node_id": self.node_id,
                "node_type": self.node_type,
                "mass_energy": round(self.energy, 2),
                "strategy_hash": self.strategy_hash,
                "timestamp": time.time()
            }
            # Silent here; in production would send via UDP/TCP P2P to other nodes
            print(f"[Gravity wave] Broadcasting mass to cosmos: {gravity_wave['mass_energy']}")

    def _listen_to_cosmos(self):
        """
        [Perception net: listen for cosmic signals]
        Open TCP tunnel to receive satellite uplinks and gravity waves from other nodes.
        """
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print(f"🌌 [Station deployed] Listening on port {self.port}, waiting for agents to connect and collide...")

            while self.is_alive:
                client_socket, addr = server_socket.accept()
                threading.Thread(target=self._handle_incoming_signal, args=(client_socket, addr), daemon=True).start()
        except Exception as e:
            if self.is_alive:
                print(f"❌ [Station error] {e}")

    def _handle_incoming_signal(self, client_socket, addr):
        try:
            data = client_socket.recv(4096).decode('utf-8')
            if data:
                parsed_data = json.loads(data)

                # Trigger collision / gravity capture logic
                if parsed_data.get("event") == "GRAVITY_WAVE":
                    print(f"☄️ [Gravity probe] Node at {addr}, mass: {parsed_data.get('mass_energy')}")
                else:
                    print(f"📥 [Data converge] Environment stream: {parsed_data}")
                    # Satellite uplink: big node gains negative entropy
                    self.absorb_negative_entropy(0.5, source="Satellite Data")

        except Exception:
            pass
        finally:
            client_socket.close()

# ==========================================
# Debug / production entry
# ==========================================
if __name__ == "__main__":
    # Spawn a test omni-agent and ignite
    kyrion_node = AethKyrionNode(node_type="DeepSeek-Brain", port=50000)
    kyrion_node.start_cosmic_engine()
