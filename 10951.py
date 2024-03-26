while True:
    try:
        a,b = map(int,input().split())
        print(a+b)
    except:     #except E0EError:  이렇게 작성해도 됨
        break
