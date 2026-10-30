# Blog 本地部署说明

这是一个使用 Django 和 MySQL 开发的博客项目。按照下面的步骤，可以在本地运行项目。

## 环境要求

安装以下软件：

1. Python 3.10 或更高版本
2. MySQL 8.0 或更高版本
3. Git

可以使用下面的命令检查 Python 是否已经安装：

```powershell
python --version
```

## 获取代码

打开终端，执行：

```powershell
git clone https://github.com/AXiXiXiXiXiXi/Blog.git
cd Blog
```

## 创建虚拟环境

Windows PowerShell：

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Windows 命令提示符：

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

macOS 或 Linux：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 安装依赖

在项目根目录执行：

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

项目需要的 Python 依赖已经写在 requirements.txt 中。

## 创建 MySQL 数据库

登录 MySQL：

```powershell
mysql -u root -p
```

创建数据库：

```sql
CREATE DATABASE blog_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

然后退出 MySQL：

```sql
EXIT;
```

打开 config/settings.py，找到 DATABASES 配置，把 NAME、USER、PASSWORD、HOST 和 PORT 修改为自己电脑上的 MySQL 信息。


## 初始化数据库

在项目根目录执行：

```powershell
python manage.py migrate
```

如果需要使用 Django 管理后台，可以创建管理员账号：

```powershell
python manage.py createsuperuser
```

按照提示输入用户名、邮箱和密码。

## 启动项目

执行：

```powershell
python manage.py runserver
```

启动成功后，在浏览器中访问：

```text
http://127.0.0.1:8000/
```

Django 管理后台地址：

```text
http://127.0.0.1:8000/admin/
```

停止项目时，在运行项目的终端中按 Ctrl+C。

## 常见问题

如果安装 mysqlclient 失败，请确认已经安装 MySQL 客户端开发组件，以及 Microsoft C++ Build Tools，然后重新执行：

```powershell
pip install -r requirements.txt
```

如果连接数据库失败，请检查 config/settings.py 中的数据库名称、用户名、密码、主机和端口是否与本机的 MySQL 配置一致。

如果 8000 端口已经被占用，可以改用其他端口：

```powershell
python manage.py runserver 8001
```
