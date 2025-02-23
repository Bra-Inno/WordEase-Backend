
from openai import OpenAI
from fastapi import APIRouter, HTTPException, Depends
from app.utils.user import get_current_user
from app import app_config, logger
from app import llm_client


api_ai = APIRouter()
llm_config=app_config.llm_config
system_prompt=llm_config["system_prompt"]
model=llm_config["model"]

@api_ai.post("/ai/llm", description="大语言模型对话")
def call_llm(user_message):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    response = llm_client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content