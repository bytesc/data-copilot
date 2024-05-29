import PIL.Image
import pandas as pd
from pandasai import Agent, SmartDatalake
import matplotlib.pyplot as plt

import data_access.read_db
from llm_access.qwen_access import llm
from output_parsing import parse_img
from input_process import input_process

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.ioff()

import pywebio


def main():
    while 1:
        dict_data = data_access.read_db.get_data_from_db()
        list_data = list(dict_data.values())

        # from langchain_community.llms.tongyi import Tongyi
        # model = "qwen-turbo"
        # llm = Tongyi(dashscope_api_key="key",
        #              model_name=model)

        lake = SmartDatalake(list_data, config={"llm": llm,
                                                "save_charts": True,
                                                "save_charts_path": "./tmp_imgs/",
                                                "open_charts": False,
                                                "enable_cache": False,
                                                "max_retries": 5})

        # 获取用户输入
        question = pywebio.input.input("请输入你的问题")
        # ans = lake.chat('在哪 2 个国家销量最少？ ，同时画出它们的饼图')   # 同时给出pandas
        # ans = lake.chat('查询Liam 的工资')

        pywebio.output.popup("加载中", [
            pywebio.output.put_loading(),
        ])

        processed_question = input_process.process_question(question)
        print(processed_question)

        ans = lake.chat(processed_question)
        print(ans, "\n--------------------------------")

        img_path = parse_img.parse_output_img(ans)
        # print("img_path:", img_path)
        graph_img = PIL.Image.open(img_path)

        pywebio.output.popup("结果", [
            pywebio.output.put_text(ans),
            pywebio.output.put_image(graph_img)
        ])

        # 定义两个按钮的操作
        actions = [
            {'label': '满意', 'value': 'y'},
            {'label': '不满意', 'value': 'n'}
        ]
        # 显示按钮并获取用户点击的结果
        selected_action = pywebio.input.actions('是否对结果满意', actions)
        # 根据用户的选择输出不同的信息
        if selected_action == 'n':
            pywebio.output.popup("高级模式加载中", [
                pywebio.output.put_loading(),
            ])
            lake = SmartDatalake(list_data, config={"llm": llm,
                                                    "save_charts": True,
                                                    "save_charts_path": "./tmp_imgs/",
                                                    "open_charts": False,
                                                    "enable_cache": False,
                                                    "max_retries": 5})
            df_ans = lake.chat(question + "return pandas dataframe only")
            print(df_ans, "\n--------------------------------")
            from manuel_mode import pandas_html
            html = pandas_html.get_html(df_ans)
            pywebio.output.popup("继续", [
                pywebio.output.put_text("高级模式已启动")
            ])
            pywebio.output.put_html(html)


if __name__ == "__main__":
    pywebio.start_server(main,
                         port=8087)
