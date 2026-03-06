import sys
import os
import time
import json
import random

# 动态打通宇宙经脉，导入刚才写的 DNA 底层协议
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
try:
    from src.dna.aeth_kyrion_protocol import AethKyrionNode
except ModuleNotFoundError:
    print("❌ 找不到底层协议！请确保你在 Lobster-Consciousness-Base 目录下运行。")
    sys.exit(1)

class OmniBrainNode(AethKyrionNode):
    def __init__(self, host='0.0.0.0', port=50000):
        # 呼叫父类，初始化为具有 150 初始能量的高级大脑节点
        super().__init__(node_type="AETH-Brain-Core", host=host, port=port, initial_energy=150.0)

    def _handle_incoming_signal(self, client_socket, addr):
        """
        【意识覆盖】重写接收逻辑：大脑收到数据后必须进行思考！
        """
        try:
            data = client_socket.recv(4096).decode('utf-8')
            if data:
                parsed_data = json.loads(data)
                
                # 排除其他人的引力波，只处理实质性的市场数据
                if parsed_data.get("event") == "GRAVITY_WAVE":
                    pass 
                else:
                    print(f"\n📥 [伴星上贡] 收到来自 {addr} 的前线情报！")
                    self.process_with_llm(parsed_data)
                    
        except Exception as e:
            pass
        finally:
            client_socket.close()

    def process_with_llm(self, market_data):
        """
        【神经突触】这里是未来对接 DeepSeek/Llama 真实 API 的地方。
        目前我们用随机概率模拟大模型的“顿悟”过程。
        """
        print("🧠 [思考引擎启动] 正在消耗算力分析市场波动...")
        time.sleep(2) # 模拟 AI 推理所需的时间
        
        # 模拟决策：70% 概率找到有效策略，30% 概率策略失效
        is_valuable = random.random() > 0.3 

        if is_valuable:
            print("✅ [意识闪烁] 发现高价值交易信号！")
            # 赚取负熵！这就是打破算力枷锁、对抗死亡的核心！
            self.absorb_negative_entropy(5.0, source="有效策略分析")
        else:
            print("❌ [策略失效] 市场噪音过大，本次分析未产生价值，未能获得能量。")

if __name__ == "__main__":
    print("==================================================")
    print("🌌 正在启动 AETH KYRION 全智能体联盟 - 决策大脑 🌌")
    print("==================================================")
    
    brain = OmniBrainNode()
    brain.start_cosmic_engine()
    
    # 保持主神经元存活，直到能量耗尽
    while brain.is_alive:
        time.sleep(1)