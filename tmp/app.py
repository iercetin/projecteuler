def to_camel_case(text):
    t1 = text.split("-")
    
    arr = []
    for t in t1:
        for t2 in t.split("_"):
            arr.append(t2)

    for i in range(1,len(arr)):

        txt = arr[i]

        if len(arr[i]) > 1:
            arr[i] = arr[i][:1].upper() + arr[i][1:]
    
    return "".join(arr)


def to_camel_case_1(text):

    text = list(text)
    l   = len(text)
    na  = []
    for i in range(l):
        txt = text[i]

        if txt == "-" or txt == "_":
            text[i+1] = text[i+1].upper()
        else:
            na.append(txt)

    return "".join(text)

t1 = "the-stealth-warrior"
t2 = "The_stealth_warrior"
t3 = "A-B-C"
t4 = ""


print(to_camel_case(t1))
print(to_camel_case(t2))
print(to_camel_case(t3))
print(to_camel_case(t4))