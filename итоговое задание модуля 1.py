f = open('cities.txt', 'r', encoding = 'utf-8')
cities_list = [line.strip().lower() for line in f]
f.close()

answers = []

imput_count = int()

f = open('answers.txt', 'w')
for ans in answers:
    f.write(ans + '\n')
f.close()

import random

def pc_move(last = None):
    global answers
    if last is None:
        pc = random.choice(cities_list)
    else:
        last_gamer_symbol = last[-1] if last[-1] not in ['ь', 'ъ', 'ы'] else last[-2]
        citi_filtr = [citi for citi in cities_list if citi.startswith(last_gamer_symbol)]
        
        available_cities = [citi for citi in citi_filtr if citi not in answers]
        
        if available_cities:
            pc = random.choice(available_cities)
        else:
            print('Компьтер не может дать найти город на такую букву, игрок победил')
            exit()
            return
    answers.append(pc)
    print(f'Компьютер выбрал город: {pc.capitalize()}')


pc_move()

for citi in cities_list:
    gamer = input('Введите город: ').lower().strip()
    
    last_ans = answers[-1]
    
    if not gamer:
        continue
        
    if not gamer in cities_list or gamer in answers or gamer[0] != (last_ans[-1] if last_ans[-1] not in ['ь', 'ъ', 'ы'] else last_ans[-2]):
        imput_count += 1   
        print(f'Неверное значение. Осталось попыток {5 - imput_count}')
        if imput_count >= 5:
            print('5 неверных ответов, игра окончена')
            break
    else:
        imput_count = 0
        answers.append(gamer)
        pc_move(gamer)

        
        

    