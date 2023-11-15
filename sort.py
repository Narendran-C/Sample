def order_list(numbers, order):
    if order == "asc":
        return sorted(numbers)
    elif order == "desc":
        return sorted(numbers, reverse=True)
    elif order == "none":
        return numbers
    else:
        raise ValueError("Invalid value for the 'order' parameter. Use 'asc', 'desc', or 'none'.")


numbers_list = [4, 1, 5, 9, 2, 6, 5, 3, 5]
ascending_result = order_list(numbers_list, "asc")
descending_result = order_list(numbers_list, "desc")
unaltered_result = order_list(numbers_list, "none")

print("Original List:", numbers_list)
print("Ascending Order:", ascending_result)
print("Descending Order:", descending_result)
print("Unaltered List:", unaltered_result)
