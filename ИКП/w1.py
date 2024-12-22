def process_list(lst):
    cubes = [x ** 3 for x in lst]
    print("Кубы элементов списка:", cubes)
    
    evens_divided = [x / 2 for i, x in enumerate(lst) if (i + 1) % 2 == 0]
    print("Элементы на четных местах, деленные на 2:", evens_divided)
    
    divisible_by_seven = [x for x in lst if x % 7 == 0]
    print("Элементы, которые делятся на 7:", divisible_by_seven)

lst = [1, 2, 3, 4, 5, 6, 7, 10, 20, 30, 40, 50, 60, 70, 80, 90]
process_list(lst)
