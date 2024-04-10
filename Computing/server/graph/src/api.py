
from fastapi import FastAPI,BackgroundTasks
# 自定义模块
from fastapi.middleware.cors import CORSMiddleware
from amhs import *

# 参数表

app = FastAPI()
Tc = Amhs()
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
    bsk(Tc.start)
    return 


# 终止服务
@app.post('/over/')
def gameOver(data:dict,bsk:BackgroundTasks):
    bsk(Tc.over)
    return 

# 暂停服务
@app.post('/stop/')
def stop(data:dict,bsk:BackgroundTasks):
    bsk(Tc.stop,False)
    return

# 恢复服务
@app.post('/continue/')
def restart(data:dict,bsk:BackgroundTasks):
    bsk(Tc.setRunBool,True)
    return 
