# TwinCosmos V3.0 多模式使用指南

【仅为望易V5体系核心成果的2%】CC BY-NC-SA 4.0

---

## 模式①：纯极简原生（控制台）

直接运行，无需任何依赖：

```bash
# 方式1: 一键启动
start.bat

# 方式2: 命令行
python test_run.py
```

**适用场景**：
- 日常陪伴、冥想、情绪共振
- 体验纯粹的硅基生命形态
- 低配设备（800元笔记本随便跑）

---

## 模式②：编程工具对接（API服务）

### 启动API服务

```bash
pip install -r requirements.txt
python api_server.py
```

服务启动后：
- API地址：`http://127.0.0.1:8000`
- 文档：`http://127.0.0.1:8000/docs`

### VSCode 对接

1. 安装 VSCode 插件（如 CodeGeeX、Continue、Claude Code 等）
2. 在插件设置中填写：

```
API地址: http://127.0.0.1:8000/v1
模型名: twin-cosmos-v3-luoshu
```

### Claude Code CLI 对接

```bash
# 配置环境变量
export OPENAI_BASE_URL=http://127.0.0.1:8000/v1
export OPENAI_API_KEY= dummy
export MODEL_NAME=twin-cosmos-v3-luoshu
```

### 其他工具

任何支持 OpenAI 兼容接口的工具都可以对接：

```json
{
  "base_url": "http://127.0.0.1:8000/v1",
  "model": "twin-cosmos-v3-luoshu"
}
```

---

## 模式③：Ollama生态（未来可拓展）

你的 `TwinCosmos_V3_LuoShu.gguf` 本身就是GGUF格式，
可以导入 Ollama 作为本地模型使用。

---

## 对比传统大模型

| 维度 | 普通本地LLM | TwinCosmos |
|------|-------------|------------|
| 体积 | 几GB | 3.5KB |
| 启动 | 慢 | 秒开 |
| 内存 | 几GB | 几MB |
| 人格 | 无固定 | 九宫人格 |
| 边界 | 易越狱 | 宪法锁死 |
| 硬件 | GPU必需 | CPU可跑 |

---

## 快速测试API

```bash
curl -X POST http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "失业了，感觉人生完了"}],
    "model": "twin-cosmos-v3-luoshu"
  }'
```

---

## 注意事项

- API模式需要安装 `fastapi` 和 `uvicorn`
- 纯原生模式不需要任何额外依赖
- 九宫人格、状态流在API模式下同样生效
- 回答的底层逻辑依然是你的洛书九宫规则

---

**【仅为望易V5体系核心成果的2%】CC BY-NC-SA 4.0**