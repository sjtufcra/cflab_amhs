
import yaml
import os 
from fastapi import FastAPI,BackgroundTasks

# 自定义模块
from fastapi.middleware.cors import CORSMiddleware
from amhs_sjtu.tc_main import *
from config import *

# 参数表
def read_yaml_config(file_path):
    path = os.path.abspath(file_path)
    with open(path, 'r', encoding='utf-8') as file:
        config_data = yaml.safe_load(file)
    return config_data

# 实例化
config = read_yaml_config(config_file_path)
app = FastAPI()
Tc = Amhs(config)
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
    arg = data.get('status')
    status = arg if arg is None else False
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
    arg = data.get('status')
    status = arg if arg is None else True
    bsk(Tc.setRunBool,status)
    backdata =  {
        "code": 200,
        'message':'Resume!',
        'bool':status
    }
    return backdata
