import copy
    l = [
            [1,2,3],
            "text",
            {
                "Feld1": [1,2,3,4],
                "Feld2": "Wort"
            },
            3,
            4,
            5]

        l2 = l[:]
        l2[0] = "HUHU"

        print(l)
        print(l2)
