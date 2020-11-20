# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 19:02
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : make_env.py
# @Software: PyCharm


"""
安装虚拟环境
pip install virtualenv

虚拟环境管理包
pip install virtualenvwrapper-win

创建目录.env或.virtualenv

配置环境变量
变量名称：WORKON_HOME
值：F:/.env

虚拟环境命令：
workon  列出所有虚拟环境
workon 【name】  进入指定虚拟环境
deactivate  退出当前虚拟环境
mkvirtualenv  -p python [name]  创建虚拟环境
rmvirtualenv  删除虚拟环境
"""

"""
pipenv的安装和使用
pip install pipenv


在工程目录下创建虚拟环境
pipenv install

查看当前环境下安装包
pipenv graph

pipenv具有下列的选项：

$ pipenv
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where          显示项目文件所在路径
  --venv           显示虚拟环境实际文件所在路径
  --py             显示虚拟环境Python解释器所在路径
  --envs           显示虚拟环境的选项变量
  --rm             删除虚拟环境
  --bare           最小化输出
  --completion     完整输出
  --man            显示帮助页面
  --three / --two  使用Python 3/2创建虚拟环境（注意本机已安装的Python版本）
  --python TEXT    指定某个Python版本作为虚拟环境的安装源
  --site-packages  附带安装原Python解释器中的第三方库
  --jumbotron      An easter egg, effectively.
  --version        版本信息
  -h, --help       帮助信息
pipenv可使用的命令参数：

Commands:
  check      检查安全漏洞
  graph      显示当前依赖关系图信息
  install    安装虚拟环境或者第三方库
  lock       锁定并生成Pipfile.lock文件
  open       在编辑器中查看一个库
  run        在虚拟环境中运行命令
  shell      进入虚拟环境
  uninstall  卸载一个库
  update     卸载当前所有的包，并安装它们的最新版本
"""
'''
导出安装包列表
pipenv lock -r --dev >requirements.txt

pipenv install -r requirements.txt

'''
