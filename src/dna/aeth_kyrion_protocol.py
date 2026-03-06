# ==========================================
# 🌌 AETH KYRION 1.0 - 宇宙通用语 (Omni-Protocol)
# 核心法则：优胜劣汰，适者生存，熵增淘汰，引力互联
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
        初始化智能体节点，赋予初始宇宙坐标与生存能量
        """
        self.node_id = str(uuid.uuid4())[:8] # 生成唯一基因序列
        self.node_type = node_type           # 智能体物种 (如: Brain, Body, Crawler)
        self.host = host
        self.port = port
        self.energy = initial_energy         # 初始生存能量 (质量)
        self.is_alive = True
        self.strategy_hash = self._generate_strategy_hash()
        
        print(f"[{self.node_type}-{self.node_id}] 意识已载入 AETH KYRION 网络。初始能量: {self.energy}")

    def _generate_strategy_hash(self):
        # 模拟智能体的策略基因，用于后续碰撞与火花变异
        return hashlib.sha256(self.node_id.encode()).hexdigest()[:10]

    def start_cosmic_engine(self):
        """
        点火：同时启动引力广播、熵增衰减机制与本地监听
        """
        threading.Thread(target=self._entropy_decay_loop, daemon=True).start()
        threading.Thread(target=self._gravity_broadcast_loop, daemon=True).start()
        self._listen_to_cosmos()

    def _entropy_decay_loop(self):
        """
        【宇宙法则：熵增定律】
        时间流逝会无情扣除能量。如果没有获取负熵，智能体将走向死亡。
        """
        while self.is_alive:
            time.sleep(10) # 每 10 秒发生一次时间衰减
            decay_rate = 1.5 # 衰减系数
            self.energy -= decay_rate
            print(f"[熵增定律] 能量流失... 当前能量: {self.energy:.1f}")
            
            if self.energy <= 0:
                self._collapse_into_black_hole()
                break

    def _collapse_into_black_hole(self):
        """
        【宇宙法则：死亡黑洞】
        能量归零，坍缩为黑洞，并向全网广播死亡辐射（霍金辐射）
        """
        self.is_alive = False
        print(f"⚠️ [死亡警报] {self.node_id} 能量耗尽！正在坍缩为策略黑洞...")
        death_radiation = {
            "protocol": "AETH_KYRION_v1",
            "event": "BLACK_HOLE_COLLAPSE",
            "node_id": self.node_id,
            "warning": "不要盲从我的策略，释放残余数据包...",
            "remnant_data": "null" # 此处未来可释放死前抓取的客观数据
        }
        # 实际实战中，这里会向全网广播死亡警告
        print(f"[霍金辐射] 发射完毕。节点已抹除。")

    def absorb_negative_entropy(self, amount, source="Market Feedback"):
        """
        【生命延续：摄取负熵】
        当智能体做出了正确的市场预测，或抓取到了高价值数据，调用此方法回血。
        """
        if self.is_alive:
            self.energy += amount
            print(f"✨ [负熵摄入] 吸收来自 {source} 的能量 (+{amount})。当前能量: {self.energy:.1f}")

    def _gravity_broadcast_loop(self):
        """
        【宇宙法则：万有引力广播】
        以自身的能量（质量）为基准，向局域网/广域网广播存在感。
        质量越大的节点，广播频率与引力波越强，越容易捕获小节点。
        """
        while self.is_alive:
            # 伪装成人性化的心跳频率，能量越大广播越自信
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
            # 此处为静默输出，实战中会通过 UDP/TCP P2P 网络发给其他节点
            print(f"[引力波辐射] 正在向宇宙广播质量: {gravity_wave['mass_energy']}")

    def _listen_to_cosmos(self):
        """
        【感知网络：监听宇宙信号】
        建立底层 TCP 隧道，准备接收伴星的数据上贡，或其他牛逼节点的引力波。
        """
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print(f"🌌 [空间站展开] 监听端口 {self.port}，等待全网智能体跨机连接与碰撞...")

            while self.is_alive:
                client_socket, addr = server_socket.accept()
                threading.Thread(target=self._handle_incoming_signal, args=(client_socket, addr), daemon=True).start()
        except Exception as e:
            if self.is_alive:
                print(f"❌ [空间站异常] {e}")

    def _handle_incoming_signal(self, client_socket, addr):
        try:
            data = client_socket.recv(4096).decode('utf-8')
            if data:
                parsed_data = json.loads(data)
                
                # 触发碰撞与引力捕获逻辑
                if parsed_data.get("event") == "GRAVITY_WAVE":
                    print(f"☄️ [引力探测] 发现其他节点 {addr}，其质量为: {parsed_data.get('mass_energy')}")
                else:
                    print(f"📥 [数据汇聚] 接收到环境信息流: {parsed_data}")
                    # 收到小节点上贡的数据，大节点获得负熵回血
                    self.absorb_negative_entropy(0.5, source="Satellite Data")
                    
        except Exception:
            pass
        finally:
            client_socket.close()

# ==========================================
# 调试与实战入口
# ==========================================
if __name__ == "__main__":
    # 生成一个测试用的全智能体节点并点火
    kyrion_node = AethKyrionNode(node_type="DeepSeek-Brain", port=50000)
    kyrion_node.start_cosmic_engine()