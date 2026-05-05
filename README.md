# 用户管理模块接口自动化测试项目

## 一、项目简介

本项目是一个基于 Python + Pytest + Requests + PyMySQL 的用户管理模块接口自动化测试项目，主要用于练习和展示接口自动化测试的基本流程。

项目实现了接口请求封装、公共前置条件管理、测试用例编写、数据库校验、HTML 测试报告生成等内容，适合作为接口自动化测试学习和简历项目展示。

## 二、技术栈

- Python
- Pytest
- Requests
- PyMySQL
- MySQL
- HTMLTestReport / pytest-html
- Git / GitHub

## 三、项目结构

```text
api_test_project/
├── common/
│   ├── --init--.py
│   └── db_util.py           # 封装数据库查询方法
│   ├── request_util.py      # 封装接口请求方法
├── testcases/
│   ├── __init__.py
│   └── test_api_mysql_user_by_util.py     # 接口 + 数据库校验测试用例
│   └── test_user_auth_check.py            # 用户鉴权相关接口测试用例
│   └── test_user_auth_mysql_check.py      # 校验token / header是否携带成功
│   └──test_user_city_role_check.py        # 按 city + role 条件查询并进行数据库校验
│   └── test_user_info_by_mysql.py         # 用户信息接口 + 数据库校验测试用例
├── conftest.py              # pytest 公共前置条件，如 token、headers
├── report.html              # 自动化测试报告
├── requirements.txt         # 项目依赖包
└── README.md                # 项目说明文档

四、项目功能

本项目主要实现了以下功能：

使用 requests 发送 GET、POST 等接口请求
使用 pytest 编写接口自动化测试用例
使用 conftest.py 管理公共前置条件
实现登录接口 token 提取
将 token 拼接到 Authorization 请求头中
使用 fixture 复用 headers，避免重复编写鉴权代码
使用 PyMySQL 连接 MySQL 数据库
根据接口返回结果查询数据库
对接口返回数据和数据库数据进行一致性校验
生成 HTML 自动化测试报告


五、核心设计说明
1. 请求封装

项目中将接口请求方法封装在 common/request_util.py 中，例如：

send_get()
send_post()

这样可以减少测试用例中的重复代码，后续如果需要统一添加 headers、token、日志、异常处理，也可以在封装方法中统一维护。

2. 数据库封装

项目中将数据库连接和查询方法封装在 common/db_util.py 中。

测试用例中不需要重复编写数据库连接代码，只需要调用封装好的查询方法即可完成数据库校验。

3. pytest fixture 管理公共前置条件

项目使用 conftest.py 管理公共前置条件，例如：

登录接口获取 token
拼接 Authorization 请求头
返回通用 headers

测试用例中可以直接使用 fixture，不需要每个用例都重复登录和拼接 headers。

## 六、测试场景示例

### 场景一：接口 + 数据库校验测试

测试目标：验证接口返回数据是否与数据库中的数据一致。

测试流程：

1. 调用用户信息查询接口
2. 获取接口返回的用户信息，例如 username、city、role、status 等字段
3. 根据接口返回的用户 id 或 username 查询 MySQL 数据库
4. 对比接口返回数据和数据库数据是否一致

主要校验内容：

- 接口状态码是否为 200
- 接口返回字段是否正确
- 数据库是否能查询到对应用户
- 接口返回的用户信息是否和数据库一致

---

### 场景二：用户鉴权相关接口测试

测试目标：验证需要登录鉴权的接口是否能够正常访问。

测试流程：

1. 调用登录接口
2. 从登录接口响应中提取 token
3. 拼接请求头：Authorization: Bearer token
4. 使用携带 token 的 headers 请求用户相关接口
5. 校验接口是否正常返回数据

主要校验内容：

- 登录接口是否成功返回 token
- token 是否能正确提取
- headers 是否正确携带 Authorization
- 携带 token 后接口是否能正常访问

---

### 场景三：校验 token / headers 是否正确携带

测试目标：验证测试用例中是否正确传递 token 和 headers。

测试流程：

1. 通过 fixture 获取公共 headers
2. 在 headers 中拼接 Authorization 字段
3. 发送需要鉴权的接口请求
4. 校验接口是否成功接收到 token 信息

主要校验内容：

- headers 中是否包含 Authorization 字段
- Authorization 格式是否正确
- token 是否正确拼接到 Bearer 后面
- 接口是否识别到当前登录状态

---

### 场景四：带 token 请求 + MySQL 数据一致性校验

测试目标：验证登录鉴权后的接口返回数据是否与数据库保持一致。

测试流程：

1. 登录接口获取 token
2. 使用 token 请求用户信息接口
3. 从接口响应中提取用户 id、username 等字段
4. 根据接口返回字段查询 MySQL 数据库
5. 对比接口数据和数据库数据是否一致

主要校验内容：

- token 鉴权是否成功
- 接口返回用户信息是否正确
- 数据库是否存在对应用户
- 接口返回数据是否与 MySQL 查询结果一致

---

### 场景五：按 city + role 条件查询并进行数据库校验

测试目标：验证接口按 city 和 role 条件查询用户时，返回结果是否符合数据库数据。

测试流程：

1. 构造查询参数 city 和 role
2. 调用用户查询接口
3. 获取接口返回的用户列表
4. 查询 MySQL 数据库中相同 city 和 role 条件下的用户数据
5. 对比接口返回结果和数据库查询结果

主要校验内容：

- 接口是否正确接收 city、role 参数
- 返回用户的 city 是否符合预期
- 返回用户的 role 是否符合预期
- 接口返回数据是否与数据库查询结果一致
七、运行方式
1. 安装依赖
pip install -r requirements.txt
2. 执行测试用例
pytest testcases -s
3. 生成 HTML 测试报告
pytest testcases -s --html=report.html --self-contained-html

执行完成后，可以在项目根目录查看 report.html 测试报告。

八、项目亮点
使用 pytest 组织自动化测试用例
使用 requests 完成接口请求
使用 fixture 管理登录 token 和公共 headers
对请求方法进行二次封装，提升代码复用性
对数据库操作进行封装，支持接口返回数据与数据库数据校验
支持生成 HTML 测试报告
项目结构清晰，符合接口自动化测试项目的基本规范
九、项目收获

通过本项目，我熟悉了接口自动化测试的基本流程，包括接口请求发送、响应断言、token 鉴权、fixture 使用、数据库校验和测试报告生成。

同时也理解了自动化测试项目中常见的分层思想，例如：

请求方法封装
数据库操作封装
测试用例分层
公共前置条件管理
测试报告输出

本项目可以作为用户管理模块接口自动化测试岗位的基础项目，也为后续继续学习 Allure 报告、日志封装、配置文件管理、数据驱动测试等内容打下基础。