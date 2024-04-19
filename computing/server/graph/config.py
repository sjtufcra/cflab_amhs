httpServer = dict(uname ='0.0.0.0',
    paths = "src.api:app",
    ports = 8055,
    log = 'info',
    reloade =True)

# config_file_path= '/Users/dannier/sjtufcra/cflab_amhs/config.yaml'  #debugger
config_file_path= 'config.yaml'
mapPath = 'data/OHTC_MAP_202404191001.json'
positionPath = 'data/OHTC_POSITION_202404191001.json'
orderPath = 'data/TRANSFER_TABLE_202404191002.json'

# 日志目录
log_path = './log'
log_name = 'server.log'
log_level = 'INFO'