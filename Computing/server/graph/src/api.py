
from fastapi import FastAPI,BackgroundTasks
# 自定义模块
from fastapi.middleware.cors import CORSMiddleware
from amhs_sjtu.tc_main import *

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
    id = data.get('id')
    bsk(Tc.start)
    backdata =  {
        "code": 200,
        'message':'Success!'
    }
    return backdata


# 终止服务
@app.post('/over/')
def gameOver(data:dict,bsk:BackgroundTasks):
    id = data.get('id')
    bsk(Tc.over)
    backdata =  {
        "code": 200,
        'message':'Over!'
    }
    return backdata

# 暂停服务
@app.post('/stop/')
def stop(data:dict,bsk:BackgroundTasks):
    id = data.get('id')
    status = data.get('status') | False
    
    bsk(Tc.stop,status)
    backdata =  {
        "code": 200,
        'message':'Stop!',
        'bool':status
    }
    return backdata

# 恢复服务
@app.post('/continue/')
def restart(data:dict,bsk:BackgroundTasks):
    id = data.get('id')
    
    status = data.get('status') | True
    bsk(Tc.setRunBool,status)
    backdata =  {
        "code": 200,
        'message':'Resume!',
        'bool':status
    }
    return backdata
