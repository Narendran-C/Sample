try:
    a = int(input())
    b = int(input())
    c = input()
    #print(c/a)
    print(d)
except TypeError as e:
    print('Type Error', e)
except ValueError as e:
    print('Value Error', e)
except Exception:
    print('Something Wrong')