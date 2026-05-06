# 用户管理模块接口自动化测试项目

## 一、项目简介

本项目是基于 Python + Pytest + Requests + PyMySQL 搭建的接口自动化测试项目，主要围绕用户管理模块进行接口测试实践。

项目覆盖用户信息查询、Token 鉴权、接口响应断言、接口返回数据与 MySQL 数据库数据一致性校验、多条件查询、数据驱动测试、日志记录、HTML 测试报告和 Allure 可视化测试报告等内容。

项目采用分层结构设计，将请求封装、数据库操作、配置管理、日志记录、公共前置条件和测试用例进行拆分，提高代码复用性和维护性。

## 二、技术栈

- Python
- Pytest
- Requests
- PyMySQL
- MySQL
- pytest-html
- Allure
- Git / GitHub

## 三、项目结构

```text
api-auto-test-project/
│
├── common/                        # 公共工具封装
│   ├── request_util.py             # 请求封装
│   ├── db_util.py                  # 数据库操作封装
│   └── log_util.py                 # 日志封装
│
├── config/                        # 配置文件
│   └── config.py                   # 接口地址、数据库配置
│
├── logs/                          # 日志文件目录
│
├── testcases/                     # 测试用例目录
│   ├── test_api_mysql_user_by_util.py
│   ├── test_user_auth_check.py
│   ├── test_user_auth_mysql_check.py
│   ├── test_user_city_role_check.py
│   ├── test_user_data_driven.py
│   └── test_user_info_by_mysql.py
│
├── conftest.py                    # Pytest 公共前置 fixture
├── pytest.ini                     # Pytest 配置文件
├── report.html                    # pytest-html 测试报告
├── requirements.txt               # 项目依赖
└── README.md                      # 项目说明文档

四、已实现功能
使用 Requests 封装 GET、POST 请求方法，统一管理接口请求逻辑。
使用 Pytest 编写接口自动化测试用例，覆盖用户查询、Token 鉴权、多条件查询等场景。
使用 conftest.py 管理公共前置条件，例如 token 和 Authorization 请求头。
使用 config.py 统一管理接口基础地址和数据库连接信息，减少硬编码。
使用 PyMySQL 连接 MySQL，对接口返回数据和数据库数据进行一致性校验。
使用 logging 封装日志模块，记录请求信息、响应结果、SQL 和查询结果。
使用 pytest.mark.parametrize 实现数据驱动测试，支持同一接口多组数据执行。
支持生成 pytest-html 报告和 Allure 可视化测试报告。
五、运行方式

安装依赖：

pip install -r requirements.txt

执行全部测试用例：

python -m pytest testcases -s

生成 pytest-html 报告：

python -m pytest testcases -s --html=report.html --self-contained-html

生成 Allure 原始结果：

python -m pytest testcases -s --alluredir=allure-results

打开 Allure 报告：

allure serve allure-results
六、测试报告

项目支持两种测试报告：

1. pytest-html 报告

执行后会在项目根目录生成：

report.html

可直接在浏览器中打开查看测试结果。

2. Allure 报告

执行后会生成：

allure-results/

通过 allure serve allure-results 可以打开可视化报告，查看用例总数、通过率、执行耗时和失败详情。

当前项目测试执行结果：

8 passed
七、项目亮点
项目采用分层结构，测试用例、请求封装、数据库封装、配置文件和日志模块职责清晰。
通过 config.py 统一管理接口地址和数据库配置，避免在测试用例中硬编码。
使用 Pytest fixture 管理公共前置条件，减少重复代码。
结合 MySQL 做接口返回数据与数据库数据一致性校验，更贴近真实测试场景。
使用日志记录接口请求、响应和 SQL 查询过程，方便失败后定位问题。
使用 Pytest 参数化实现数据驱动测试，提高测试用例扩展性。
同时支持 pytest-html 和 Allure 报告，方便测试结果展示和问题分析。
八、项目总结

本项目主要用于接口自动化测试学习和实践，重点展示了接口请求封装、Pytest 自动化测试用例设计、数据库校验、配置管理、日志记录、数据驱动测试、测试报告生成和 Git 版本管理等能力。

通过该项目，可以模拟真实接口自动化测试中的常见流程，包括发送接口请求、提取响应数据、查询数据库、进行断言校验、记录日志和生成测试报告。