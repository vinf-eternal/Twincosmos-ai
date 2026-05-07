#!/usr/bin/env python3
import sys
sys.path.insert(0, "D:/wayne/Twincosmos/twin_cosmos_v2/TwinCosmos_V3_LuoShu/core")
from wangyi_life import WangYi, NinePalacePersona

wangyi = WangYi("望易")

print("\n" + "="*60)
print("TwinCosmos V3.0 整合测试")
print("="*60)

tests = [
    "你是谁？",
    "失业了，感觉人生完了",
    "太棒了，拿到offer了！",
    "你算什么东西",
    "我好累，想休息"
]

for t in tests:
    resp, palace = wangyi.respond(t)
    print(f"\n用户: {t}")
    print(f"望易 [{palace}]: {resp}")

print("\n" + "="*60)
print("我是谁？")
print(f"望易: {wangyi.who_am_i()}")
print("="*60)

print("\n状态:")
status = wangyi.status()
for k, v in status.items():
    print(f"  {k}: {v}")