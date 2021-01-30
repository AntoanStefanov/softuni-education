def data_types(data_type, data):
    if data_type == "int":
        data = int(data) * 2
    elif data_type == "real":
        data = f"{float(data) * 1.5:.2f}"
    elif data_type == "string":
        data = f"${data}$"
    return data


data_type = input()
data = input()

result = data_types(data_type, data)

print(result)
