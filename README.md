# data-copilot


✨ **基于 langchain 和大语言模型 (LLM) 的自然语言数据库查询系统 (RAG)**

通过自然语言提问，使用大语言模型智能解析数据库结构，对数据进行智能多表结构化查询和统计计算，根据查询结果智能绘制多种图表。 Pywebio 交互式前端网页，不必须 openai api，100%纯 Python 代码。 

[个人网站：www.bytesc.top](http://www.bytesc.top) 

🔔 如有项目相关问题，欢迎在本项目提出`issue`，我一般会在 24 小时内回复。

## 功能简介

- 1, 使用自然语言提问
- 2, 实现多表结构化查询和统计计算
- 3, 实现智能绘制多种类型的图表和交互式图表制作
- 4, 智能解析数据库结构，使用不同的 mysql 数据库无需额外配置
- 4, 支持多线程并发查询
- 5, 能够处理大语言模型表现不稳定等异常情况
- 6, 支持本地离线部署 (需 GPU) `huggingface` 格式模型 (例如`qwen-7b`) 
- 7, 支持 `openai` 格式和 dashscope `qwen` 的 api 接口

## 展示

提问界面

![](./readme_img/img1.png)
![](./readme_img/img2.png)

根据查到的数据，智能选择图表类型绘图，支持多表结构化查询。在这个例子中，智能连接了员工表和工资表，进行结构化查询。智能选择了柱状图绘图。

![](./readme_img/db.png)
![](./readme_img/img4.png)

如果对智能绘图结果不满意，高级模式，根据智能查询到的数据，手动交互式绘图

![](./readme_img/img7.png)

支持智能智能统计计算。在这个例子中，智能统计了在各国销量的百分比，智能选择了饼图绘图。

![](./readme_img/db1.png)
![](./readme_img/img10.png)
![](./readme_img/img12.png)

高级模式，交互式绘图

![](./readme_img/img15.png)
![](./readme_img/img16.png)

同样支持平均值，求和，最大值，最小值等统计计算

![](./readme_img/img20.png)
![](./readme_img/img22.png)
![](./readme_img/img23.png)
![](./readme_img/img24.png)
![](./readme_img/img31.png)
![](./readme_img/img33.png)

## 如何使用

### 安装依赖

python 版本 3.9

```bash
pip install -r requirement.txt
```

### 填写配置信息

`./config/config.yaml` 是配置信息文件。

#### 数据库配置
连接即可，模型会自动读取数据库结构，无需额外配置
```yml
mysql: mysql+pymysql://root:123456@127.0.0.1/data_copilot
# mysql: mysql+pymysql://用户名:密码@地址:端口/数据库名
```

#### 大语言模型配置
如果使用 dashscope `qwen` api （推荐）
```yml
llm:
  model: qwen1.5-110b-chat # 模型名称
  url: ""  # 使用 dashscope `qwen` api 时此项无需填写

# qwen1.5-72b-chat   qwen1.5-110b-chat
# qwen-turbo  qwen-plus   qwen-max   qwen-long
```
同时在 `llm_access/LLM.py` 中
```python
# llm = llm_access.openai_access.llm
llm = llm_access.qwen_access.llm
```

如果使用 openai api （此处填写的是 glm 的 openai 兼容 api）

```yml
llm:
  model: glm-4 # 模型名称
  url: "https://open.bigmodel.cn/api/paas/v4/"   # endpoint_url 请求地址

# qwen1.5-72b-chat   qwen1.5-110b-chat
# qwen-turbo  qwen-plus   qwen-max   qwen-long
```
同时在 `llm_access/LLM.py` 中
```python
llm = llm_access.openai_access.llm
# llm = llm_access.qwen_access.llm
```

如果需要本地离线部署，相关代码在 `./llm_access/qwen_access.py`

#### 获取 apikey

如果从[阿里云 dashscope ](https://dashscope.console.aliyun.com/)获取 `qwen` 大语言模型的 api-key


保存 `api-key` 到 `llm_access/api_key_qwen.txt`

如果使用 `openai` 格式 api 的 api-key

保存 `api-key` 到 `llm_access/api_key_openai.txt`

### 运行

main.py 是项目入口，运行此文件即可启动服务器

```bash
python main.py
```

默认情况下，浏览器输入 [ http://192.168.71.51:8087/ ]( http://192.168.71.51:8087/ )即可

## 基本技术原理

未完待续......


# 开源许可证

此翻译版本仅供参考，以 LICENSE 文件中的英文版本为准

MIT 开源许可证：

版权所有 (c) 2023 bytesc

特此授权，免费向任何获得本软件及相关文档文件（以下简称“软件”）副本的人提供使用、复制、修改、合并、出版、发行、再许可和/或销售软件的权利，但须遵守以下条件：

上述版权声明和本许可声明应包含在所有副本或实质性部分中。

本软件按“原样”提供，不作任何明示或暗示的保证，包括但不限于适销性、特定用途适用性和非侵权性。在任何情况下，作者或版权持有人均不对因使用本软件而产生的任何索赔、损害或其他责任负责，无论是在合同、侵权或其他方面。
