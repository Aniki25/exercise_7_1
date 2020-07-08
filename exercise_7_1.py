# создаем пустой словарь
# создаем пустой список
# открываем текстовый файл
from collections import Counter


cook_book = {}
list_dish = []
dish_number = -1

with open('recipes.txt', encoding='utf8') as f:
    for line in f:
        list_dish.append(line.strip())
        ingredients_q = int(f.readline().strip())
        dish_number += 1
        temp_dict = {}
        ingredients_list = []

        for index in range(ingredients_q):
            ingredients = f.readline().strip().split(' | ')
            temp_dict = {'ingredient_name': ingredients[0], 'quantity': int(ingredients[1]), 'measure': ingredients[2]}
            ingredients_list.append(temp_dict)
            cook_book[list_dish[dish_number]] = ingredients_list

        f.readline()

print(cook_book)
print()


def get_shop_list_by_dishes(dishes, person_count):
    dishes_list = []
    for element in dishes:
        dishes_list.append(element.capitalize())

    for element in dishes_list:
        if element in cook_book:
            pass
        else:
            dishes.remove(element)

    shop_dic = {}
    count = 1
    Counter(dishes)
    for dish in dishes:
        for index in cook_book[dish]:
            count = Counter(dishes)[dish]
            shop_dic[index['ingredient_name']] = {'quantity': index['quantity'] * count * person_count,
                                                       'measure': index['measure']}
    print(shop_dic)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)

