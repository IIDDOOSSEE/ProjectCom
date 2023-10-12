while True :
    try :
        a = int(input("num 1 :"))
        b = int(input("num 2 :"))
        if a == 0 and b == 0 :
            break
        if a < 0 or b < 0 :
            raise Exception("gu bok hai sai tua lek i sus !!")
        print(a/b)
        
    except Exception as cuo :
        print(cuo)
    else : 
        print("TUM TOR ")
print("E N D I N G ")