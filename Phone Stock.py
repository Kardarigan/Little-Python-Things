storage = {
    "mobile_1" : {
        "is_smart" : True,
        "brand" : "apple",
        "storage" : 128,
        "color" : "black",
        "wanted" : True
        },
    "mobile_2" : {
        "is_smart" : True,
        "brand" : "apple",
        "storage" : 128,
        "color" : "blue",
        "wanted" : True
        },
    "mobile_3" : {
        "is_smart" : True,
        "brand" : "apple",
        "storage" : 32,
        "color" : "gold",
        "wanted" : True
        },
    "mobile_4" : {
        "is_smart" : True,
        "brand" : "samsung",
        "storage" : 128,
        "color" : "black",
        "wanted" : True
        },
    "mobile_5" : {
        "is_smart" : True,
        "brand" : "samsung",
        "storage" : 64,
        "color" : "blue",
        "wanted" : True
        },
    "mobile_6" : {
        "is_smart" : True,
        "brand" : "samsung",
        "storage" : 32,
        "color" : "titaniom",
        "wanted" : True
        },
    "mobile_7" : {
        "is_smart" : True,
        "brand" : "apple",
        "storage" : 128,
        "color" : "black",
        "wanted" : True
        },
    "mobile_8" : {
        "is_smart" : True,
        "brand" : "apple",
        "storage" : 128,
        "color" : "blue",
        "wanted" : True
        },
    "mobile_9" : {
        "is_smart" : True,
        "brand" : "tesla",
        "storage" : 512,
        "color" : "black",
        "wanted" : True
        },
    "mobile_10" : {
        "is_smart" : True,
        "brand" : "xiami",
        "storage" : 128,
        "color" : "gold",
        "wanted" : True
        },
    "mobile_11" : {
        "is_smart" : True,
        "brand" : "xiami",
        "storage" : 64,
        "color" : "blue",
        "wanted" : True
        },
    "mobile_12" : {
        "is_smart" : True,
        "brand" : "samsung",
        "storage" : 256,
        "color" : "gold",
        "wanted" : True
        }
}

while True :

    print("\n========== mobile storage ==========")
    
    print("enter these information in order =>  is_smart , brand , storage , color")
    info = []
    q = input()
    if q == "True" :
        q1 = True
    else:
        q1 = False
    w = input()
    e = input()
    r = input()   


    for i in storage :
        info.append(i)

    if q  != " ":
        for i in storage :
            if storage[i]["is_smart"] != q1 :
                if i in info :
                    info.remove(i)

        for j in storage :
            if storage[j]["brand"] != w :
                if j in info :
                    info.remove(j)

    if e != " ":
        for k in storage :
            if storage[k]["storage"] < int(e) :
                if k in info :
                    info.remove(k)
    if r != " ":
        for o in storage :
            if storage[o]["color"] != r :
                if o in info :
                    info.remove(o)
    
    for u  in info :
        print(storage[u])












    while False :



        for i in storage.values  :
            if i[0] == q1 :
                if i[1] == w :
                    if i[2] >= int(e) :
                        if i[3] == r  :
                            info.append(i)
                        
                print(info)




