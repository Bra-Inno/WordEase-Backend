# web 服务器
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import os

from app import logger,app_config
from app.api.user import api_user
from app.api.ai import api_ai


#from wordease.api.user import api_user
mysql_config = app_config.mysql_config

logo_tmpl=r"""
----------------------------------------
            wordease已经运行
----------------------------------------
"""
def check_env():
    pass
app = FastAPI(
    title="WordEase API",
    description="一款随时陪伴的语言学习软件",
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

register_tortoise(
        app,
        config=mysql_config,
        generate_schemas=True,  # 开发环境可以生成表结构，生产环境建议关闭
        add_exception_handlers=True,  # 显示错误信息
    )


@app.get("/")
async def root():
    return {"message": "欢迎来到WordEase,一款随时陪伴的语言学习软件"}
    # 初始化 Tortoise ORM
    
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 允许所有来源
        allow_credentials=True,
        allow_methods=["*"],  # 允许所有方法
        allow_headers=["*"],  # 允许所有头
    )

app.include_router(api_user, prefix="/user", tags=["用户相关接口"])
app.include_router(api_ai, prefix="/ai", tags=["AI相关接口"])


if __name__ == '__main__':
    check_env()
    logger.info(logo_tmpl)
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
    