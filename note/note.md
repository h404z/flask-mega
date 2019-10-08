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



#### Jinja

**变量、if、for、注释、继承**的用法

```jinja2
{# base.html #}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% if title %}  {# if语句 #}
        <title>{{ title }} - flask-mega</title>  {# render_template传进来的title变量 #}
    {% else %}
        <title>Oh my - flask-mega</title>
    {% endif %}
</head>
<body>
<div id="container">
    <div>flask-mega: <a href="/index">Home</a></div>
    <hr>
    {% block content %}
    {% endblock %}
</div>
</body>
</html>
```

```jinja2
{# index.html #}
{% extends "base.html" %}
{% block content %}
    <h1>hello, {{ user.username }}!</h1>

    {% for post in posts %}  {# for语句 #}
        <div><p>{{ post.author.username }} says:<b>{{ post.body }}</b></p></div>
    {% endfor %}

{% endblock %}
```

```python
@app.route("/")
@app.route("/index")
def index():
    user = {"username": "NickHo"}

    posts = [
        {
            "author": {"username": "Vicky"},
            "body": "I want to go to Disneyland!"
        },
        {
            "author": {"username": "Hayden"},
            "body": "I'm a little human!"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
```

#### 配置方式

用Config类来管理配置，增加配置的可扩展性（关注点分离原则）

```python
# config.py
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRETE_KEY') or 'you-are-beautiful'
    
# __init__.py
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

# microblog.py
from app import app
```

验证配置生效

```bash
>>> from microblog import app
>>> app.config["SECRET_KEY"]
'you-are-beautiful'
```





