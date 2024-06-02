import pywebio
import pandas as pd
import matplotlib.pyplot as plt

from ask_ai import ask_ai_for_pd, ask_ai_for_graph
import data_access.read_db

from config.get_config import config_data
from manuel_mode import pandas_html

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    pywebio.output.put_markdown("# Data Copilot")
    pywebio.output.put_markdown("## 自然语言数据库查询")

    dict_data, merged_dict_data = data_access.read_db.get_data_from_db()
    list_data = list(dict_data.values())
    merged_list_data = list(merged_dict_data.values())
    pywebio.output.put_table([list(dict_data.keys())])

    actions = [
        {'label': '所有数据', 'value': 'show'},
        {'label': '智能查询', 'value': 'query'},
        {'label': '智能绘图', 'value': 'graph'},
    ]
    # 显示按钮并获取用户点击的结果
    selected_action = pywebio.input.actions('选项', actions)

    if selected_action == 'show':
        html = pandas_html.get_html(pd.concat(dict_data.values(), axis=1))
        pywebio.output.clear()
        pywebio.output.put_text("刷新以输入新的查询")
        pywebio.output.put_html('<div style="position: absolute; left: 0; right: 0;"> ' + html + "</div>")

    if selected_action == 'graph' or selected_action == 'query':
        # 获取用户输入
        question = pywebio.input.input("请输入你的问题")
        pywebio.output.put_text(question)

        while 1:
            if selected_action == 'graph' or selected_action == 'graph_again':
                try:
                    ask_ai_for_graph.ask_graph(list_data + merged_list_data, question)
                except Exception as e:
                    print(e)

                # 定义两个按钮的操作
                actions = [
                    {'label': '重新查询', 'value': 'graph_again'},
                    {'label': '高级模式', 'value': 'query'}
                ]
                # 显示按钮并获取用户点击的结果
                selected_action = pywebio.input.actions('刷新以输入新的查询', actions)

            if selected_action == 'query':
                try:
                    ask_ai_for_pd.ask_pd(list_data + merged_list_data, question)
                except Exception as e:
                    print(e)
                break

            elif selected_action == 'graph_again':
                continue
            else:
                break


if __name__ == "__main__":
    pywebio.start_server(main,
                         port=config_data['server_port'],
                         debug=True)
