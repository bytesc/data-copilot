
import yaml

config_data = None

# 读取YAML文件
with open('./config/config.yaml', 'r') as stream:
    try:
        config_data = yaml.safe_load(stream)
        print(config_data)
    except yaml.YAMLError as exc:
        print(exc)



