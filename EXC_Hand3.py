try:
    a = int(input())
    b = int(input())
except ValueError as e:
    print('Value Error', e)
except Exception:
    print('Something Wrong')
finally:
    print('Done')