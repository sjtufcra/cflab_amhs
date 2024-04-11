
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

config = read_yaml_config(config_file_path)

def read_yaml_config(file_path):
    """
    读取指定路径的YAML配置文件，并将其内容解析为字典返回。

    参数:
        file_path (str): YAML配置文件的路径。

    返回:
        dict: 解析后的配置数据。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        config_data = yaml.safe_load(file)
    return config_data

# 示例：读取当前目录下的 "config.yaml"
config_file_path = "config.yaml"
config = read_yaml_config(config_file_path)


# 示例化
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
