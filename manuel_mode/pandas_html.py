import pygwalker as pyg


def get_html(df):
    try:
        html_str = pyg.to_html(df, dark='light')
    except Exception as e:
        print("df err", e)
        html_str = ""

    return html_str
