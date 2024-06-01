import pywebio
import pandas as pd
import matplotlib.pyplot as plt

from ask_ai import ask_ai_for_pd, ask_ai_for_graph
import data_access.read_db

from config.get_config import config_data

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

    # 获取用户输入
    question = pywebio.input.input("请输入你的问题")
    pywebio.output.put_text(question)

    while 1:
        try:
            ask_ai_for_graph.ask_graph(list_data + merged_list_data, question)
        except Exception as e:
            print(e)
            break

        # 定义两个按钮的操作
        actions = [
            {'label': '重新查询', 'value': 'c'},
            {'label': '高级模式', 'value': 'g'}
        ]
        # 显示按钮并获取用户点击的结果
        selected_action = pywebio.input.actions('刷新以输入新的查询', actions)

        if selected_action == 'g':
            try:
                ask_ai_for_pd.ask_pd(list_data + merged_list_data, question)
            except Exception as e:
                print(e)
            break

        elif selected_action == 'c':
            continue
        else:
            break


if __name__ == "__main__":
    pywebio.start_server(main,
                         port=config_data['server_port'],
                         debug=True)
