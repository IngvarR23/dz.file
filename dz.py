cook_book = {}
dish_list = []
with open('file_1', 'rt', encoding = 'utf8') as file:
  for l in file:     
      dish_name = l.strip()   
      ingredients_list = []
      dish = {dish_name: ingredients_list}      
      dish_count = file.readline() 
      for i in range(int(dish_count)):           
        dish_1 = file.readline().strip().split(' | ') 
        ingredients_list.append({'ingredient_name': dish_1[0],
                            'quantity': int(dish_1[1]),
                            'measure': dish_1[2]})
        dish_list.append(dish)                
      blank_line = file.readline()
      cook_book.update(dish)              
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    if dish in cook_book:
      for l in cook_book[dish]:
        person_1 = int(l['quantity']) * person_count
        dict_list = {l['ingredient_name']: {'measure': l['measure'], 'quantity': person_1}}
        shop_list.update(dict_list)
    return shop_list


dict_files = {}
list_files = ['1.txt', '2.txt', '3.txt']

for file in list_files:
    with open(file, 'r', encoding='utf8') as f:
        dict_files[file] = len(f.readlines())

sorted_dict = sorted(dict_files.items(), key=lambda item: item[1])

with open(sorted_dict[0][0], 'r', encoding='utf8') as content:
    text = content.read()
    with open('result.txt', 'w', encoding='utf8') as f:
        f.write(sorted_dict[0][0])
        f.write('\n')
        f.write(str(sorted_dict[0][1]))
        f.write('\n')
        f.write(text)
        f.write('\n')

for name, count in sorted_dict[1:]:
    with open(name, 'r', encoding='utf8') as content:
        text = content.read()
        with open('result.txt', 'a', encoding='utf8') as f:
            f.write(name)
            f.write('\n')
            f.write(str(count))
            f.write('\n')
            f.write(text)
            f.write('\n')