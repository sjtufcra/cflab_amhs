
import yaml
import os 
from fastapi import FastAPI,BackgroundTasks

from fastapi.middleware.cors import CORSMiddleware
from amhs.tc_main import *
from config import *
from loguru import logger as log

def read_yaml_config(file_path):
    path = os.path.abspath(file_path)
    with open(path, 'r', encoding='utf-8') as file:
        config_data = yaml.safe_load(file)
    return config_data

config = read_yaml_config(config_file_path)
# log add
log.remove()
log.add(log_name,level=log_level)
app = FastAPI()
Tc = Amhs(config.get('httpServer'))
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/start/')
def restart(data:dict,bsk:BackgroundTasks):
    id = data.get('id')
    bsk.add_task(Tc.start)
    backdata =  {
        "code": 200,
        'message':'Success!'
    }
    return backdata


@app.post('/over/')
def gameOver(data:dict,bsk:BackgroundTasks):
    id = data.get('id')
    bsk.add_task(Tc.over)
    backdata =  {
        "code": 200,
        'message':'Over!'
    }
    return backdata

@app.post('/stop/')
def stop(data:dict,bsk:BackgroundTasks):
    id = data.get('id')
    arg = data.get('status')
    status = arg if arg is None else False
    bsk.add_task(Tc.setRunBool,status)
    backdata =  {
        "code": 200,
        'message':'Stop!',
        'bool':status
    }
    return backdata

@app.post('/continue/')
def restart(data:dict,bsk:BackgroundTasks):
    id = data.get('id')
    arg = data.get('status')
    status = arg if arg is None else True
    bsk.add_task(Tc.setRunBool,status)
    backdata =  {
        "code": 200,
        'message':'Resume!',
        'bool':status
    }
    return backdata

@app.get('/')
def read_root():
    return {'Hello': 'World'}