import copy

l = [
        [1,2,3], 
        "Text", 
        { 
            "Feld1": [1,2,3,4], 
            "Feld2": "Wort" }, 
        3, 
        4, 
        5]

l2 = copy.deepcopy(l)
l2[0] = "HUHU"

print(l)
print(l2)

l2[2]["Feld1"][0] = "HUHU"
print(l)
print(l2)