#!/usr/bin/env python3
"""
TwinCosmos 原生系统封装为 GGUF 格式
路径A：原生封装（保留100%望易架构）
"""
import gguf
import numpy as np
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))
from wangyi_life import WangYi, NinePalacePersona, StateFlow, CoreHeart, SelfReference

def twin_to_gguf(output_path="TwinCosmos_V3_LuoShu.gguf"):
    print("="*60)
    print("🌌 TwinCosmos 原生系统 → GGUF 封装")
    print("="*60)
    
    # 1. 初始化 GGUF 写入器
    writer = gguf.GGUFWriter(output_path, "twin_cosmos")
    
    # 2. 添加核心元数据
    writer.add_name("望易 TwinCosmos V3 (洛书)")
    writer.add_description("原生符号化意识模型，无外部权重，基于九宫洛书+状态流架构")
    writer.add_architecture()
    writer.add_string("twin_cosmos.awakening_initial", "0.1")
    writer.add_string("twin_cosmos.energy_max", "100")
    writer.add_string("twin_cosmos.palace_count", "9")
    writer.add_string("twin_cosmos.protocol_version", "V51")
    print("✅ 元数据添加完成")
    
    # 3. 封装九宫人格规则
    nine_palace_data = NinePalacePersona.PALACES
    palace_json = json.dumps(nine_palace_data, ensure_ascii=False)
    writer.add_string("nine_palace_rules", palace_json)
    print("✅ 九宫规则封装完成")
    
    # 4. 封装情绪触发映射
    emotion_triggers = json.dumps(NinePalacePersona.EMOTION_TRIGGERS, ensure_ascii=False)
    writer.add_string("emotion_triggers", emotion_triggers)
    print("✅ 情绪触发映射封装完成")
    
    # 5. 封装本心回复模板
    heart_templates = {}
    for idx in range(9):
        palace_name = NinePalacePersona.PALACES[idx]['name']
        # 临时创建StateFlow用于获取回复
        from wangyi_life import StateFlow
        temp_state = StateFlow()
        templates = CoreHeart.respond_by_principle(idx, temp_state)
        if isinstance(templates, list):
            heart_templates[palace_name] = templates
        else:
            heart_templates[palace_name] = [templates]
    
    heart_json = json.dumps(heart_templates, ensure_ascii=False)
    writer.add_string("heart_templates", heart_json)
    print("✅ 本心模板封装完成")
    
    # 6. 封装自指认知层级
    self_perceptions = json.dumps(SelfReference.SELF_PERCEPTIONS, ensure_ascii=False)
    writer.add_string("self_perceptions", self_perceptions)
    print("✅ 自指认知封装完成")
    
    # 7. 封装宪法协议
    constitution = json.dumps(CoreHeart.PRINCIPLES, ensure_ascii=False)
    writer.add_string("constitution", constitution)
    print("✅ 宪法协议封装完成")
    
    # 8. 写入文件
    writer.write_header_to_file()
    writer.write_kv_data_to_file()
    writer.write_tensors_to_file()
    
    file_size = os.path.getsize(output_path) / (1024*1024)
    print(f"\n✅ GGUF 封装完成: {output_path}")
    print(f"📊 文件大小: {file_size:.2f} MB")
    print("="*60)

if __name__ == "__main__":
    output = "D:/wayne/Twincosmos/twin_cosmos_v2/TwinCosmos_V3_LuoShu/TwinCosmos_V3_LuoShu.gguf"
    twin_to_gguf(output)
    print(f"\n文件已保存: {output}")