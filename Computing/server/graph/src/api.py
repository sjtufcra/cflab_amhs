
from fastapi import FastAPI,BackgroundTasks
# 自定义模块
from fastapi.middleware.cors import CORSMiddleware
# from src.tc_main import *
# 参数表
app = FastAPI()
   
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 开始服务
@app.post('/start/')
def restart(data:dict,bsk:BackgroundTasks):
    start()
    return 


# 终止服务
@app.post('/end/')
def gameOver(data:dict,bsk:BackgroundTasks):
    return 

# 暂停服务
@app.post('/stop/')
def stop(data:dict,bsk:BackgroundTasks):

    return

# 恢复服务
@app.post('/continue/')
def restart(data:dict,bsk:BackgroundTasks):
    return 
