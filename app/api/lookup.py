


from fastapi import APIRouter
from app import llm_client,app_config
llm_config=app_config.llm_config

api_lookup = APIRouter()
meaning_lookup_prompt=f"""你是一个翻译大师，我会给你提供一些单词，词组，句子，你需要给我提供它们的释义，如果你觉得我提供的单词，词组，句子不对，你就可以告诉我：主人，你查找的不存在，你可能在查找XXX，XXX为最接近的
回答要简约，就只回答释义，不做其他解释，如果是中文的则翻译为英文，如果是英文的，则翻译为中文
"""

@api_lookup.get("/meaning/lookup",
                description=f"""\
                查询释义，支持中英文单词\
                1. 支持查询单词，如果是中文，返回英文解释，如果是英文，返回中文解释，如果是一个错误的单词，则返回最相近的单词，并提示\
                2. 支持查询词组，如果是中文，返回英文解释，如果是英文，返回中文解释，如果是一个错误的词组，则返回最相近的词组，并提示\
                3. 支持查询句子，如果是中文，返回英文解释，如果是英文，返回中文解释，如果是一个错误的句子，则返回最相近的句子，并提示""")
async def meaning_lookup(info : str):
    messages = [
        {"role": "system", "content": meaning_lookup_prompt},
        {"role": "user", "content": info}
    ]

    response = llm_client.chat.completions.create(
        model=llm_config["model"],
        messages=messages
    )
    return response.choices[0].message.content

