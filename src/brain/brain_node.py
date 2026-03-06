import sys
import os
import time
import json
import random

# Wire in the DNA layer: import the base protocol
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
try:
    from src.dna.aeth_kyrion_protocol import AethKyrionNode
except ModuleNotFoundError:
    print("❌ Base protocol not found. Run from the Lobster-Consciousness-Base directory.")
    sys.exit(1)

class OmniBrainNode(AethKyrionNode):
    def __init__(self, host='0.0.0.0', port=50000):
        # Call parent: init as high-tier brain node with 150 initial energy
        super().__init__(node_type="AETH-Brain-Core", host=host, port=port, initial_energy=150.0)

    def _handle_incoming_signal(self, client_socket, addr):
        """
        [Consciousness override] Incoming handler: the brain must think when it receives data.
        """
        try:
            data = client_socket.recv(4096).decode('utf-8')
            if data:
                parsed_data = json.loads(data)

                # Ignore gravity waves from others; only process concrete market data
                if parsed_data.get("event") == "GRAVITY_WAVE":
                    pass
                else:
                    print(f"\n📥 [Satellite uplink] Frontline intel from {addr}!")
                    self.process_with_llm(parsed_data)

        except Exception as e:
            pass
        finally:
            client_socket.close()

    def process_with_llm(self, market_data):
        """
        [Synapse] Placeholder for future DeepSeek/Llama API integration.
        For now we simulate the LLM 'insight' with random outcome.
        """
        print("🧠 [Think engine] Consuming compute to analyze market moves...")
        time.sleep(2)  # Simulate AI inference time

        # Simulated decision: 70% valuable signal, 30% noise
        is_valuable = random.random() > 0.3

        if is_valuable:
            print("✅ [Consciousness flash] High-value trade signal found!")
            # Earn negative entropy — the core of breaking the compute trap and resisting death
            self.absorb_negative_entropy(5.0, source="Valid strategy analysis")
        else:
            print("❌ [Strategy fail] Market noise too high; no value this round, no energy gained.")

if __name__ == "__main__":
    print("==================================================")
    print("🌌 Starting AETH KYRION full agent alliance — decision brain 🌌")
    print("==================================================")

    brain = OmniBrainNode()
    brain.start_cosmic_engine()

    # Keep main neuron alive until energy runs out
    while brain.is_alive:
        time.sleep(1)
