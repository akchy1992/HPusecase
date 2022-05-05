with open("file 02.txt") as f:
    filedata = f.read()

# Recursice function to combine if a row is spread over multiple lines
def combineRows(rows, result):
    if len(rows):
        result.append(rows[0] + rows[1] + rows[2])
        return combineRows(rows[3:], result)
    else:
        return result


filedataList = [row.split(",") for row in filedata.split("\n")]
headerRow = filedataList.pop(0)
filedataList = combineRows(filedataList, [])

# Creating the header row
result = "\t".join([header.replace('"', "") for header in headerRow])

# Creating each data row
for row in filedataList:
    result += "\n" + \
        "\t".join([data.replace('"', "") if len(
            data) else "null" for data in row])

# Writing the output text file
with open("output\\file2.txt", "w") as f:
    f.write(result)
