# offline config
httpServer = dict(uname ='0.0.0.0',
    paths = "src.api:app",
    ports = 8055,
    log = 'info',
    reloade =True)

config_file_path= '/Users/dannier/sjtufcra/cflab_amhs/config.yaml'  #debugger

# config_file_path= 'config.yaml' #online

# set run mode
runmode = 'runing_mode'

server = 'httpServer'  #online
local = 'localServer' #local


# log config
log_path = './log'
log_name = 'server.log'
log_level = 'INFO'