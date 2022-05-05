import json
from unittest import result


with open("file 01.json", "r") as f:
    data = json.load(f)

result = []

# Creating the header row
header = ""
for key in data[0]:
    if type(data[0][key]) == list:
        for internalKey in data[0][key][0]:
            header += f"{key}.{internalKey}\t"
    else:
        header += f"{key}\t"
result.append(header)

# Iteratively creating a row for each product
for obj in data:
    commonData = ""
    rowData = []
    for key in obj:
        if type(obj[key]) == list:
            for internalData in obj[key]:
                currentRowdata = ""
                for internalKey in internalData:
                    currentRowdata += f"{internalData[internalKey] if len(internalData[internalKey]) else 'null'}\t"
                rowData.append(currentRowdata)
        else:
            commonData += f"{obj[key] if len(obj[key]) else 'null'}\t"
    for row in rowData:
        result.append(f"{commonData}{row}")

# writing the output text file
with open("output\\file1.txt", "w") as f:
    f.write("\n".join(result))
