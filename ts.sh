#!/bin/bash

# 检查是否在 computing/dist 目录下，如果不是，切换到该目录
if [[ ! $PWD =~ ^./computing/dist$ ]]; then
    cd computing/dist || exit 1
fi

# 找到最高版本号
highest_version=$(ls -1 amhs_sjtu* | sort -V | tail -n 1 | cut -d '-' -f 2- | sed 's/-py[23].py3-none-any.whl//')
echo "$highest_version"
# 检查最高版本号是否为空
if [[ -z $highest_version ]]; then
    echo "No amhs_sjtu package found."
    exit 1
fi

# 安装最高版本
install_command="pip3 install --user amhs_sjtu-$highest_version.tar.gz"
echo "Installing $install_command"
$install_command

# 检查安装是否成功
if [[ $? -eq 0 ]]; then
    echo "Installation successful."
else
    echo "Installation failed."
fi