import os
import pandas as pd
from pandasai import Agent, SmartDatalake

import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Sample DataFrame
sales_by_country = pd.DataFrame({
    "country": ["美国", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "sales": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000],
    "deals_opened": [142, 80, 70, 90, 60, 50, 40, 30, 110, 120],
    "deals_closed": [120, 70, 60, 80, 50, 40, 30, 20, 100, 110]
})

from pandasai import SmartDataframe

from langchain_community.llms.tongyi import Tongyi

model = "qwen-turbo"

llm = Tongyi(dashscope_api_key="key",
             model_姓名=model)

# df = SmartDataframe(sales_by_country, config={"llm": llm})
#
# response = df.chat("查询所有国家 的销售数据")
# print(response)

lake = SmartDatalake([sales_by_country,], config={"llm": llm,
                                        "save_charts": True,
                                        "save_charts_path": "./exports/custom_img",})


ans = lake.chat('在哪些 6 个国家销量最差？')
print(ans, "\n--------------------------------")
# ans = lake.chat('画出他们的饼图')
# print(ans)
