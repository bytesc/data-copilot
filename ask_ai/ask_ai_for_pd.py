import concurrent

import pandas as pd
import pywebio

from llm_access.LLM import llm
from manuel_mode import pandas_html

from config.get_config import config_data
from ask_ai import ask_api


def ask_pd(data, question):
    tries = 0
    while 1:
        pywebio.output.popup("高级模式启动中", [
            pywebio.output.put_text(question),
            pywebio.output.put_loading(),
        ])
        clean_data_pd_list = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(ask_api.ask, data,
                                       question, llm, False) for _ in range(config_data['ai']['concurrent'])]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                print(result, "\n--------------------------------")
                if not isinstance(result, pd.DataFrame):
                    result = None
                if result is not None:
                    clean_data_pd_list.append(result)

        if len(clean_data_pd_list) != 0:
            clean_data_pd = clean_data_pd_list[0]
            tb_data = [clean_data_pd.columns.to_list()] + clean_data_pd.values.tolist()
            print(tb_data)
            pywebio.output.popup("高级模式启动成功", [
                pywebio.output.put_text(question),
                pywebio.output.put_table(tb_data),
            ])
            pywebio.output.put_table(tb_data),
            html = pandas_html.get_html(clean_data_pd)
            pywebio.output.clear()
            pywebio.output.put_text("高级模式 刷新以输入新的查询")
            pywebio.output.put_html('<div style="position: absolute; left: 0; right: 0;"> ' + html + "</div>")
            break
        else:
            if tries < 3:
                tries += 1
                print(tries, "##############")
                continue
            else:
                pywebio.output.popup("失败", [
                    pywebio.output.put_text("查询失败"),
                ])
                break
