#!/bin/bash
if pip3 show amhs_sjtu >/dev/null 2>&1;then
    echo "Uninstall amhs_sjtu"
    pipe uninstall amhs_sjtu -y
else
    echo "amhs_sjtu not installed"
fi
echo "Install amhs_sjtu"
pip3 install --user computing/dist/amhs_sjtu-1.0.0.tar.gz
pip3 install -r requirements.txt
echo "Install amhs_sjtu success"