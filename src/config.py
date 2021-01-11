import yaml

with open('data/config.cfg','r',encoding='utf-8')as f:
    config = yaml.safe_load(f)