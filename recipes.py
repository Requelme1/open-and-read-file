from pprint import pprint

with open("recipes.txt", "rt", encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        cook_book_name = line.strip()
        quantity_ingredients = int(file.readline())
        quantitys = []
        for _ in range(quantity_ingredients):
            rec = file.readline().strip()
            name, quantity, measure = rec.split(' | ')
            quantitys.append({'ingredient_name': name,
                              'quantity': quantity,
                              'measure': measure
                              })

        file.readline()
        cook_book[cook_book_name] = quantitys
    pprint(cook_book, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    cooking_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                if ingr['ingredient_name'] not in cooking_list:
                    value = {'quantity': int(ingr['quantity']) * person_count, 'measure': ingr['measure']}
                    cooking_list[ingr['ingredient_name']] = value
                else:
                    cooking_list[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count

    return cooking_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
