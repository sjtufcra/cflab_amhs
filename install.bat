-- Active: 1712560317566@@127.0.0.1@3306
@REM pip install -r requirements.txt
pip3 uninstall amhs_sjtu -y
pip3 install computing/dist/amhs_sjtu-1.0.0.tar.gz
pip3 install -r requirements.txt
echo "install success"
