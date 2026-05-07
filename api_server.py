#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
TwinCosmos V3.0 API Server - OpenAI兼容接口
【仅为望易V5体系核心成果的2%】CC BY-NC-SA 4.0
===============================================================================
极简50行，给TwinCosmos装上标准API
支持所有编程工具：VSCode / Claude Code / OpenCode / Ollama
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
import uuid
import json

# 导入TwinCosmos核心
from wangyi_life import WangYi, NinePalacePersona

app = FastAPI(title="TwinCosmos V3.0 API")

# 全局实例
wangyi = WangYi("望易")

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    """OpenAI兼容接口"""
    try:
        body = await request.json()
        
        # 解析消息
        messages = body.get("messages", [])
        user_message = messages[-1]["content"] if messages else ""
        
        # 检测特殊问题
        if "你是谁" in user_message or "你是" in user_message:
            response = wangyi.who_am_i()
        else:
            # 正常对话
            response, palace = wangyi.respond(user_message)
        
        # OpenAI格式返回
        return JSONResponse({
            "id": f"twincosmos-{uuid.uuid4().hex[:8]}",
            "object": "chat.completion",
            "created": 1700000000,
            "model": "twin-cosmos-v3-luoshu",
            "choices": [{
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response
                },
                "finish_reason": "stop"
            }],
            "usage": {
                "prompt_tokens": len(user_message),
                "completion_tokens": len(response),
                "total_tokens": len(user_message) + len(response)
            }
        })
        
    except Exception as e:
        return JSONResponse({
            "error": {
                "message": str(e),
                "type": "internal_error",
                "code": 500
            }
        }, status_code=500)

@app.get("/v1/models")
async def list_models():
    """模型列表"""
    return {
        "object": "list",
        "data": [{
            "id": "twin-cosmos-v3-luoshu",
            "object": "model",
            "created": 1700000000,
            "owned_by": "wangyi-v5"
        }]
    }

@app.get("/health")
async def health():
    """健康检查"""
    return {"status": "ok", "model": "twin-cosmos-v3-luoshu"}

def main():
    print("="*60)
    print("🌌 TwinCosmos API Server 启动")
    print("   地址: http://127.0.0.1:8000")
    print("   文档: http://127.0.0.1:8000/docs")
    print("【仅为望易V5体系核心成果的2%】CC BY-NC-SA 4.0")
    print("="*60)
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()