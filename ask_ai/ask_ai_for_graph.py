import concurrent

import PIL
import pywebio

from llm_access.LLM import llm
from output_parsing import parse_img

from config.get_config import config_data
from ask_ai import ask_api


def ask_graph(data, question):
    tries = 1
    while 1:
        pywebio.output.popup("数据查询中", [
            pywebio.output.put_text(question),
            pywebio.output.put_text("数据查询"),
            pywebio.output.put_loading(),
        ])

        result_list = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(ask_api.ask, data,
                                       question, llm, True) for _ in range(tries*config_data['ai']['concurrent'])]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                img_path = parse_img.parse_output_img(result)
                if img_path is not None:
                    result_list.append(img_path)

        if len(result_list) != 0:
            # print("img_path:", img_path)
            graph_img = PIL.Image.open(result_list[0])

            pywebio.output.popup("画图完成", [
                pywebio.output.put_text("画图成功"),
                # pywebio.output.put_text(img_ans),
                pywebio.output.put_image(graph_img)
            ])
            for path in result_list:
                graph_img = PIL.Image.open(path)
                pywebio.output.put_image(graph_img)
            break
        else:
            if tries <= config_data['ai']['tries']:
                tries += 1
                print(tries, "##############")
                continue
            pywebio.output.popup("失败", [
                pywebio.output.put_text("画图失败"),
                # pywebio.output.put_text(img_ans),
            ])
            break
