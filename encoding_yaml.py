import yaml

with open("sample_yaml") as data:
    yaml_data = data.read()


yaml_dict = yaml.load(yaml_data, Loader=yaml.FullLoader)
print(type(yaml_dict))
print(yaml_dict)
yaml_dict["interface"]["name"] = "GigabitEthenert1"

with open("sample_yaml", "w") as data:
    data.write(yaml.dump(yaml_dict, default_flow_style=False))