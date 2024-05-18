from all_dict import blocks, indexes, all_cells
from all_levels import list_all_lvl

count_fail = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}


def output(table):
    """Выводит поле на экран."""
    print('    A B C   D E F   G H I')
    k1 = 0
    while k1 <= 6:
        print(f'{k1 + 1}  ', *table[k1][:3], ' ', *table[k1 + 1][:3], ' ', *table[k1 + 2][:3])
        print(f'{k1 + 2}  ', *table[k1][3:6], ' ', *table[k1 + 1][3:6], ' ', *table[k1 + 2][3:6])
        print(f'{k1 + 3}  ', *table[k1][6:], ' ', *table[k1 + 1][6:], ' ', *table[k1 + 2][6:])
        print()
        k1 += 3


def check_character_for_isdigit(character, range):
    """Проверяет является ли значение числом из выбранного диапазона."""

    while not character.isdigit() or int(character) not in range:
        if not character.isdigit():
            character = input('Пожалуйста, введите число.\n')
        elif int(character) not in range:
            character = input(f'Пожалуйста, введите число из диапазона от {range[0]} до {range[-1]}.\n')
    return character


def lvl_choice():
    """Выводит на экран имеющиеся уровни и получает номер выбранного уровня."""
    k = 1
    while k <= len(list_all_lvl):
        print(f'Уровень {k}:')
        output(list_all_lvl[str(k)][1])
        k += 1

    choice = input(f'Выберите уровень из предложенного списка (от 1 до {k-1}). \n')
    range_in_function = [numbers for numbers in range(1, k)]
    choice = check_character_for_isdigit(choice, range_in_function)
    return choice


choice_lvl = lvl_choice()
game_field = list_all_lvl[choice_lvl][1]


def get_block(cell_in_function):
    """Возвращает индекс блока, в котором находится ячейка."""
    for key_in_function, value_in_function in blocks.items():
        if cell_in_function in value_in_function:
            return key_in_function


def get_index(cell_in_function):
    """Возвращает индекс ячейки в блоке."""
    for key_in_function, value_in_function in indexes.items():
        if cell_in_function in value_in_function:
            return key_in_function


def get_cell():
    """Запрашивает у пользователя ячейку, проверяет её на корректность, а затем возвращает."""
    cell_in_function = input('Введите ячейку поля, в которую Вы хотите разместить значение. \n')
    while (len(cell_in_function) == 0 or cell_in_function not in all_cells or
           (game_field[get_block(cell_in_function)][get_index(cell_in_function)] != '*')):
        if len(cell_in_function) == 0:
            cell_in_function = input('Пожалуйста, введите ячейку поля, в которую Вы хотите разместить значение. \n')
        elif cell_in_function not in all_cells:
            cell_in_function = input('Такой ячейки нет. Повторите попытку. \n')
        elif game_field[get_block(cell_in_function)][get_index(cell_in_function)] != '*':
            cell_in_function = input('Эта ячейка уже заполнена. Повторите попытку. \n')
    return cell_in_function


def get_number(cell_in_function):
    """Запрашивает у пользователя цифру, проверяет её на корректность, а затем возвращает."""
    number = input(f'Введите значение, которое нужно разместить в ячейке {cell_in_function}. \n')
    range_in_function = [numbers for numbers in range(1, 10)]
    number = check_character_for_isdigit(number, range_in_function)

    return number


def replace_character():
    """Меняет значение ячейки в поле."""
    cell_in_function = get_cell()
    number = get_number(cell_in_function)
    block_in_function = get_block(cell_in_function)
    index_in_function = get_index(cell_in_function)
    game_field[block_in_function][index_in_function] = number
    return cell_in_function, block_in_function


def check_fail(cell_in_function):
    """Проверяет цифру в ячейке на соответствие с верным значением, и если оно неверно,
     возвращает увеличенное количество ошибок. В противном случае возвращает имеющееся количество ошибок."""
    block_in_function = get_block(cell_in_function)
    index_in_function = get_index(cell_in_function)
    if (game_field[block_in_function][index_in_function] !=
            list_all_lvl[choice_lvl][0][block_in_function][index_in_function]):
        print(f'''Вы ошиблись, значение введено неверно. 
Количество ошибок в блоке №{block + 1}: {count_fail[block_in_function] + 1} из 5.''')
        game_field[block_in_function][index_in_function] = '*'
        return count_fail[block_in_function] + 1
    else:
        print('Значение введено верно! \nИгра продолжается.')
        return count_fail[block_in_function]


while True:
    output(game_field)
    cell, block = replace_character()
    count_fail[block] = check_fail(cell)
    for key, value in count_fail.items():
        if value == 5:
            print(f'Вы превысили количество возможных ошибок в блоке №{int(key) + 1}. Игра окончена.')
            exit()
    if game_field == list_all_lvl[choice_lvl][0]:
        print('Вы победили! Поле заполнено. Игра окончена.')
        break
