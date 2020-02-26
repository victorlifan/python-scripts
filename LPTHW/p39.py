from collections import OrderedDict
shengs = {
"Jiangsu" : "Su",
"Zhejiang" : "Zhe",
"Anhui" : "Wan",
"Guangdong" : "Yue"
}

chengs = {
"Su" : "Nanjing",
"Zhe" : "Hangzhou",
"Wan" : "Hefei",
"Yue" : "Guangzhou"
}

shengs ["Sichuan"] = "Chuan"
shengs ["Liaoning"] = "Liao"
chengs ["Chuan"] = "Chengdu"
chengs ["Liao"] = "Shenyang"

x = OrderedDict(shengs)
print(x)
print("Abbreviation of Anhui is", shengs["Anhui"])
print("Capitial of Anhui is", chengs[shengs["Anhui"]])

print("Capitial of Sichuan is", chengs[shengs["Sichuan"]])
print("Abbreviation Zhe's Capitial is", chengs["Zhe"])

for sheng, abbrev in list(shengs.items()):
    print(sheng,"has canpital", chengs[abbrev])
for abbrev, cheng in list(chengs.items()):
    print(abbrev ,"has city", cheng)

print(shengs.get("sadasd", "doesn't exit"))
