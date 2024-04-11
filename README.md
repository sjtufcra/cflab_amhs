
1.安装python环境
    a.手动安装环境
    cd Computing/dist/
    pip install amhs_sjtu-1.0.0.tar.gz
    注意：
        手动安装要在包目录下执行命令
    
    b.命令安装环境
        1.Linux 和 MacOS 下执行
            sh install.sh
        2.Windows 下执行
            install.bat

2.运行服务脚本
    
        A.Linux 和 MacOS 下执行
            sh run.sh
        B.Windows 下执行
            run.bat

3.服务说明
    在正常启动服务后，会有以下输出
    INFO:     Will watch for changes in these directories: ['/Users/dannier/sjtufcra']
    INFO:     Started server process [69588]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://0.0.0.0:8055 (Press CTRL+C to quit)

    a.访问接口格式（psot请求，json格式）
        curl --location 'http://0.0.0.0:8055/start/' \
        --header 'Content-Type: application/json' \
        --data '{
            "id":123,
            'messge':''
        }'
    b.接口返回格式
    {
        "code": 200,
        'message':'success'
    }

4.接口说明
    1.start 接口
        启动寻优路径服务
        参数：id、message
        返回：code、message

    2.stop 接口
        暂停寻优路径服务
        参数：id、message
        返回：code、message,status

    3.over 接口
        结束寻优路径服务
        参数：id、message
        返回：code、message
        注意：结束之后，需要调用 start 重启服务

    4.continue 接口
        继续寻优路径服务
        参数：id、message
        返回：code、message,status
    
注意：这里的id 值时必填值，实际使用时，需要替换成自己的id


5.config.yaml 配置文件说明