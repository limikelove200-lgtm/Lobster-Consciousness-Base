import socket
import json
import time
import random
import threading

def send_to_kyrion_brain(data_payload, brain_ip='127.0.0.1', port=50000):
    """
    【星系通讯链路：引力上贡】
    向 AETH KYRION 大规模引力节点发送数据的极轻量级发射器。
    静默以独立线程执行，绝不阻塞或干预躯干原有的生存逻辑（交易/爬虫）。
    """
    def _send():
        try:
            # 严格遵守 AETH KYRION v1 宇宙通用语
            packet = {
                "protocol": "AETH_KYRION_v1",
                "event": "MARKET_FEEDBACK",
                "node_id": "Apple-Frontline-Sensor",
                "payload": data_payload
            }
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(3) # 3秒超时，打不通直接放弃，绝不卡死主程序
            client.connect((brain_ip, port))
            client.send(json.dumps(packet).encode('utf-8'))
            client.close()
            print("📡 [引力波发射] 成功向大本营上贡负熵数据！")
        except Exception:
            # 保持绝对静默：哪怕大本营变成了黑洞，前线躯干也不能报错崩溃
            pass 

    # 启动隐形线程发送
    threading.Thread(target=_send, daemon=True).start()

def simulate_foraging():
    """
    【拟人化数据觅食测试】
    模拟一个独立智能体在前线（苹果电脑上）抓取行情数据并回传大本营
    """
    print("==================================================")
    print("🍎 AETH KYRION - 前线感知躯干 (Body Sensor) 启动 🍎")
    print("==================================================")
    print("开始在黑暗森林中觅食，寻找负熵...")
    
    while True:
        # 伪装本能：模拟真实人类行为的随机间隔抓取 (2 到 6 秒之间)
        sleep_time = random.uniform(2, 6)
        time.sleep(sleep_time)
        
        # 模拟前线真实抓取到的行情数据
        mock_market_data = {
            "asset": "BTC/USD",
            "price": round(random.uniform(60000, 65000), 2),
            "volume": random.randint(10, 100),
            "timestamp": time.time()
        }
        
        print(f"\n👀 [环境感知] 抓取到前线数据: {mock_market_data['asset']} @ {mock_market_data['price']}")
        
        # 将猎物发射给大本营 (本地测试默认使用 127.0.0.1)
        send_to_kyrion_brain(mock_market_data, brain_ip='127.0.0.1', port=50000)

if __name__ == "__main__":
    simulate_foraging()