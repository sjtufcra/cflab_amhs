###开启服务接口
curl --location 'http://0.0.0.0:8055/start/' \
--header 'Content-Type: application/json' \
--data '{
    "id":123,
    "message":""

}'

###关闭服务接口
curl --location 'http://0.0.0.0:8055/over/' \
--header 'Content-Type: application/json' \
--data '{
    "id":123,
    "message":""

}'

###暂停服务接口
curl --location '/stop/' \
--header 'Content-Type: application/json' \
--data '{
    "id":123,
    "status":flase,
    "message":""

}'

###继续服务接口
curl --location '/continue/' \
--header 'Content-Type: application/json' \
--data '{
    "id":123,
    "status":true,
    "message":""

}'