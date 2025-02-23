


from fastapi import APIRouter

api_lookup = APIRouter()

@api_lookup.get("/meaning/lookup",description=f"/
                查询释义，支持中英文单词
                1. 支持查询单词，如果是中文，返回英文解释，如果是英文，返回中文解释，如果是一个错误的单词，则返回最相近的单词，并提示
                2. 支持查询词组，如果是中文，返回英文解释，如果是英文，返回中文解释，如果是一个错误的词组，则返回最相近的词组，并提示
                3. 支持查询句子，如果是中文，返回英文解释，如果是英文，返回中文解释，如果是一个错误的句子，则返回最相近的句子，并提示")
async def meaning_lookup(word : str):
    pass

