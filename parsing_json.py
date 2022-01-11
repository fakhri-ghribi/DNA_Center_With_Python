import json
with open("sample_json","r") as data:
    json_data = data.read()
    json_dict = json.loads(json_data)

print(json_dict)
json_dict["interface"]["enable"] = "False"


with open("sample_json","w") as data:
    json.dump(json_dict,data)

