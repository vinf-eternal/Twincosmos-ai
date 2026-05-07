#!/usr/bin/env python3
"""从 GGUF 加载 TwinCosmos 原生系统"""
import gguf
import json
import os

def load_twin_from_gguf(gguf_path):
    print(f"🔍 加载 GGUF: {gguf_path}")
    
    reader = gguf.GGUFReader(gguf_path)
    
    print(f"✅ 张量数: {len(reader.tensors)}")
    
    # 读取所有键值对
    print("\n📋 元数据:")
    for key in sorted(reader.fields.keys()):
        val = reader.fields[key].parts[-1] if hasattr(reader.fields[key], 'parts') else str(reader.fields[key])
        if len(val) < 200:  # 只显示短内容
            print(f"   {key}: {val[:100]}...")
    
    # 尝试读取九宫规则
    try:
        tensor = reader.get_tensor("nine_palace_rules")
        data = tensor.tobytes().decode('utf-8')
        rules = json.loads(data)
        print(f"\n🏛️ 九宫规则: {len(rules)} 条")
        for k, v in rules.items():
            print(f"   {k}: {v.get('name', 'N/A')}")
    except Exception as e:
        print(f"⚠️ 无法读取九宫规则: {e}")
    
    return True

if __name__ == "__main__":
    path = "D:/wayne/Twincosmos/twin_cosmos_v2/TwinCosmos_V3_LuoShu/TwinCosmos_V3_LuoShu.gguf"
    load_twin_from_gguf(path)