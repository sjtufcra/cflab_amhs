# #!/bin/bash
# if pip3 show amhs_sjtu >/dev/null 2>&1;then
#     echo "Uninstall amhs_sjtu"
#     pipe uninstall amhs_sjtu -y
# else
#     echo "amhs_sjtu not installed"
# fi
# echo "Install amhs_sjtu"
# pip3 install --user computing/dist/amhs_sjtu-1.0.2.tar.gz
# pip3 install -r requirements.txt
# echo "Install amhs_sjtu success"

#!/bin/bash

if pip3 show amhs_sjtu >/dev/null 2>&1; then
    echo "Uninstall amhs_sjtu"
    pip3 uninstall amhs_sjtu -y
else
    echo "amhs_sjtu not installed"
fi

echo "Install amhs_sjtu"
if [[ ! $PWD =~ ^./computing/dist$ ]]; then
    cd computing/dist || exit 1
fi

highest_version=$(ls -1 amhs_sjtu* | sort -V | tail -n 1 | cut -d '-' -f 2- | sed 's/-py[23].py3-none-any.whl//')
echo "$highest_version"

if [[ -z $highest_version ]]; then
    echo "No amhs_sjtu package found."
    exit 1
fi

install_command="pip3 install --user amhs_sjtu-$highest_version.tar.gz"
cd ..
cd ..
pip3 install -r requirements.txt
echo "Insptall amhs_sjtu success"