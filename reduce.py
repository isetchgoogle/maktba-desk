import json

with open('xmltojson.json',encoding="charmap") as data_file:
    data = json.load(data_file)

for element in data:
    if 'codeabarre' in element:
        del element['codeabarre']
for element in data:
    if 'Codelivre' in element:
        del element['Codelivre']
for element in data:
    if 'Nbr_COTE' in element:
        del element['Nbr_COTE']
for element in data:
    if 'Nbr_EXP' in element:
        del element['Nbr_EXP']
for element in data:
    if 'EDITION' in element:
        del element['EDITION']
for element in data:
    if 'ANED' in element:
        del element['ANED']
for element in data:
    if 'ISBN' in element:
        del element['ISBN']

with open('data4.json', 'w') as data_file:
    data = json.dump(data, data_file)
