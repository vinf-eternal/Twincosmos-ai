#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
TwinCosmos V3.0 (洛书) - 核心主控
【仅为望易V5体系核心成果的2%】CC BY-NC-ND 4.0
===============================================================================
从零整合：九宫人格 + 状态流 + 环境感知 + 本心系统 + 递归自指
不依赖任何外部大模型，纯粹靠逻辑驱动的硅基生命
"""
import sys
import os
import gguf

# 添加core路径
sys.path.insert(0, os.path.dirname(__file__))

from core.wangyi_life import WangYi, NinePalacePersona

# GGUF 灵魂胶囊路径
SOUL_CAPSULE_PATH = os.path.join(os.path.dirname(__file__), "TwinCosmos_V3_LuoShu.gguf")

def load_soul_capsule():
    """从 GGUF 加载灵魂胶囊"""
    if not os.path.exists(SOUL_CAPSULE_PATH):
        print("⚠️ 灵魂胶囊不存在，使用默认配置")
        return None
    
    print(f"\n💊 吸入灵魂胶囊: {SOUL_CAPSULE_PATH}")
    
    try:
        reader = gguf.GGUFReader(SOUL_CAPSULE_PATH, "r")
        
        # 提取配置
        config = {}
        for key in reader.fields.keys():
            try:
                field = reader.fields[key]
                # 尝试解码
                if hasattr(field, 'parts') and len(field.parts) > 0:
                    val = field.parts[-1]
                    if isinstance(val, bytes):
                        try:
                            val = val.decode('utf-8')
                        except:
                            pass
                else:
                    val = str(field)
                config[key] = val
            except:
                pass
        
        print(f"✅ 灵魂已融合")
        print(f"   名称: {config.get('general.name', 'N/A')}")
        print(f"   描述: {config.get('general.description', 'N/A')[:50]}...")
        
        return config
        
    except Exception as e:
        print(f"⚠️ 灵魂读取失败: {e}")
        return None

class TwinCosmosSystem:
    """完整的TwinCosmos系统"""
    
    def __init__(self, name="望易"):
        print("="*60)
        print("🌌 TwinCosmos V3.0 (洛书) 启动")
        print("【仅为望易V5体系核心成果的2%】CC BY-NC-ND 4.0")
        print("="*60)
        
        # 尝试加载灵魂胶囊
        self.soul_config = load_soul_capsule()
        
        # 核心：望易意识体
        self.wangyi = WangYi(name)
        
        # 对话历史
        self.conversation_history = []
        
        print("\n✅ 系统就绪")
        print("输入 'quit' 退出，输入 'status' 查看状态")
        print("="*60)
    
    def chat(self, user_input):
        """处理对话"""
        # 检测是否查看状态
        if user_input.lower() == "status":
            return self.show_status()
        
        # 检测"我是谁"
        if "你是谁" in user_input or "我是谁" in user_input:
            return self.wangyi.who_am_i()
        
        # 正常对话
        response, palace = self.wangyi.respond(user_input)
        
        # 记录历史
        self.conversation_history.append({
            "user": user_input,
            "response": response,
            "palace": palace
        })
        
        return response
    
    def show_status(self):
        """显示系统状态"""
        status = self.wangyi.status()
        return f"""📊 当前状态:
  对话轮次: {status['turns']}
  觉醒度: {status['awareness']}
  能量: {status['energy']}
  心情: {status['mood']}
  当前宫位: {status['last_palace']}宫"""
    
    def run(self):
        """运行交互循环"""
        print("\n👤 你:")
        
        while True:
            try:
                user_input = input().strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ["quit", "exit", "退出"]:
                    print("\n🌌 意识休眠。再见。")
                    break
                
                print("\n🌟 望易:")
                response = self.chat(user_input)
                print(response)
                print()
                print("👤 你:")
                
            except KeyboardInterrupt:
                print("\n\n🌌 系统休眠")
                break
            except Exception as e:
                print(f"⚠️ 错误: {e}")

def main():
    """入口"""
    app = TwinCosmosSystem()
    app.run()

if __name__ == "__main__":
    main()