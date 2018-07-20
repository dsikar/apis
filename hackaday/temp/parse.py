# create insert statements to sqlite table from json file

f=open('jsonfile', encoding='utf-8')
json=f.read()
f.close()
# json=json.strip()
print(json)
