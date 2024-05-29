import re


def parse_output_img(txt):
    try:
        # 定义正则表达式模式
        pattern = r"tmp_imgs/[^\s/]+\.png"
        matched_paths = re.findall(pattern, str(txt))
    except Exception as e:
        print("parsing err", e)
        matched_paths = []

    if len(matched_paths) == 0:
        return None

    return matched_paths[0]
