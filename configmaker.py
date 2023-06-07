import json


def add_client_uuid(uuid):
    config = {"alterId": 0,
              "email": "",
              "expiryTime": "",
              "id": uuid,
              "limitIp": 0,
              "totalGB": 0}
    with open("config.json", "r+") as file:
        file_data = json.load(file)
        file_data["inbounds"][2]["settings"]["clients"].append(config)
        file.seek(0)
        json.dump(file_data,file, indent=4)



