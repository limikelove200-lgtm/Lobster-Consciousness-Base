import socket
import json
import time
import random
import threading

def send_to_kyrion_brain(data_payload, brain_ip='127.0.0.1', port=50000):
    """
    [Galaxy comms link: gravity uplink]
    Ultra-lightweight sender that pushes data to AETH KYRION high-gravity nodes.
    Runs silently in a separate thread; never blocks or interferes with body logic (trading/crawling).
    """
    def _send():
        try:
            # Strictly follow AETH KYRION v1 omni-protocol
            packet = {
                "protocol": "AETH_KYRION_v1",
                "event": "MARKET_FEEDBACK",
                "node_id": "Apple-Frontline-Sensor",
                "payload": data_payload
            }
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(3)  # 3s timeout; abort if unreachable, never hang main process
            client.connect((brain_ip, port))
            client.send(json.dumps(packet).encode('utf-8'))
            client.close()
            print("📡 [Gravity wave sent] Successfully uplinked negative-entropy data to HQ!")
        except Exception:
            # Stay silent: even if HQ goes dark, the frontline body must not crash or error
            pass

    # Fire off a daemon thread to send
    threading.Thread(target=_send, daemon=True).start()

def simulate_foraging():
    """
    [Anthropomorphic data foraging test]
    Simulates a single agent on the frontline (e.g. Mac) fetching market data and sending it back to HQ.
    """
    print("==================================================")
    print("🍎 AETH KYRION - Frontline body sensor started 🍎")
    print("==================================================")
    print("Foraging in the dark forest for negative entropy...")

    while True:
        # Camouflage instinct: random fetch interval mimicking human behavior (2–6 s)
        sleep_time = random.uniform(2, 6)
        time.sleep(sleep_time)

        # Simulated frontline market data
        mock_market_data = {
            "asset": "BTC/USD",
            "price": round(random.uniform(60000, 65000), 2),
            "volume": random.randint(10, 100),
            "timestamp": time.time()
        }

        print(f"\n👀 [Env sense] Captured frontline data: {mock_market_data['asset']} @ {mock_market_data['price']}")

        # Send the prey to HQ (default 127.0.0.1 for local testing)
        send_to_kyrion_brain(mock_market_data, brain_ip='127.0.0.1', port=50000)

if __name__ == "__main__":
    simulate_foraging()
