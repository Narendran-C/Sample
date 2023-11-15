def converting(value):
    return float(value) * 1260 / 22


x = input(f"Enter the Radian Value : ")
print(f"Degree : ", round(converting(x), 3))
