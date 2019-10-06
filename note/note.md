#### 虚拟环境

```bash
$ pip3 install virtualenv
```

创建独立的虚拟环境

``` bash
$ virtualenv --no-site-packages venv  # venv是运行环境的名称
```

激活虚拟环境

```bash
# windows
venv/Scripts/activate.bat  # 在pycharm的项目根目录下打开terminal就会自动激活

# linux/macOS
待补充
```

生成依赖文件

```bash
$ pip freeze > requirements.txt
```

