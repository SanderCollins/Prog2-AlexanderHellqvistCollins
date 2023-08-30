dic = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}
print(dic["Sverige"])               # "Stockholm"
print(dic["Norge"])                 # "Oslo"          # "Helsingfors"              

dic.update({"Danmark": "köpenhamn"})
dic.pop("Finland")
print(dic["Danmark"]) 
print(dic["Finland"])     