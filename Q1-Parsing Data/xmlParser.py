from operator import mod
from unittest import result
import xml.etree.ElementTree as ET
tree = ET.parse('file 03.xml')
root = tree.getroot()

header = ""
commondata = ""

# Finding the data that will be common for each row
for child in root.iter("*"):
    if child.tag == "{http://isac.hp.com/schema/isac}cid":
        header += "cid\t"
        commondata += f"{child.text}\t"
    if child.tag == "{http://isac.hp.com/schema/ckm}pers_give_nm":
        header += "pres_give_nm\t"
        commondata += f"{child.text}\t"
    if child.tag == "{http://isac.hp.com/schema/ckm}pers_last_nm":
        header += "pres_last_nm\t"
        commondata += f"{child.text}\t"
    if child.tag == "{http://isac.hp.com/schema/ckm}email_add_nm":
        header += "email_add_nm\t"
        commondata += f"{child.text}\t"
    if child.tag == "{http://isac.hp.com/schema/ckm}addr_country_cd":
        header += "addr_country_cd\t"
        commondata += f"{child.text}\t"
    if child.tag == "{http://isac.hp.com/schema/ckm}home_address_valid":
        header += "home_address_valid\t"
        commondata += f"{child.text}\t"

products = []
product_registrations = list(
    root.iter("{http://isac.hp.com/schema/isac}product_registrations"))[0]

# Creating separate row by iterating over each product
for product in product_registrations:
    currentProduct = {}
    for attribute in product:
        for subAttribute in attribute:
            if subAttribute.tag == "{http://isac.hp.com/schema/ckm}product_model_group":
                for model_data in subAttribute:
                    currentProduct[model_data.tag.split(
                        "}")[-1]] = model_data.text
            if subAttribute.tag == "{http://isac.hp.com/schema/ckm}prod_serial_id":
                currentProduct["prod_serial_id"] = subAttribute.text
            if subAttribute.tag == "{http://isac.hp.com/schema/ckm}service_id_cd":
                currentProduct["service_id_cd"] = subAttribute.text
            if subAttribute.tag == "{http://isac.hp.com/schema/ckm}invoice_amount":
                currentProduct["invoice_amount"] = subAttribute.text
    products.append(currentProduct)


header += "\t".join(products[0].keys())

result = [header]

# Combining Common data with each product
for product in products:
    product_row = "\t".join(product.values())
    result.append(commondata+product_row)

# Writing the output file
with open("output\\file3.txt", "w") as f:
    f.write("\n".join(result))
