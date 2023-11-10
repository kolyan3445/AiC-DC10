import tkinter as tk
from tkinter.messagebox import showwarning, showinfo

font = 'Arial 15'

game_window = tk.Tk()
game_window.title("Крестики-нолики")
game_window.geometry("460x475+500+400")
game_window.resizable(False, False)

button_list = ['1 1', '1 2', '1 3', '2 1',
               '2 2', '2 3', '3 1', '3 2', '3 3']
button_in_use = {'1 1': '', '1 2': '', '1 3': '',
                 '2 1': '', '2 2': '', '2 3': '',
                 '3 1': '', '3 2': '', '3 3': ''}
button_y_coordinate = -150
x = -1
button_x_coordinates = [5, 155, 305]

turn_counter = 0
game_matrix = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def bot_player():
    for mark in ['O', '☓']:
        for i in range(3):
            vertical_check = [game_matrix[i][0], game_matrix[i][1], game_matrix[i][2]]
            horizontal_check = [game_matrix[0][i], game_matrix[1][i], game_matrix[2][i]]
            main_diagonal_check = [game_matrix[0][0], game_matrix[1][1], game_matrix[2][2]]
            sub_diagonal_check = [game_matrix[2][0], game_matrix[1][1], game_matrix[0][2]]

            if vertical_check.count(mark) == 2 and vertical_check.count('-') == 1:
                return [i, vertical_check.index('-')]

            if horizontal_check.count(mark) == 2 and horizontal_check.count('-') == 1:
                return [horizontal_check.index('-'), i]

            if main_diagonal_check.count(mark) == 2 and main_diagonal_check.count('-') == 1:
                return [main_diagonal_check.index('-'), main_diagonal_check.index('-')]
            if sub_diagonal_check.count(mark) == 2 and sub_diagonal_check.count('-') == 1:
                if sub_diagonal_check.index('-') == 0:
                    return [2, 0]
                if sub_diagonal_check.index('-') == 1:
                    return [1, 1]
                if sub_diagonal_check.index('-') == 2:
                    return [0, 2]

    if game_matrix[1][1] == '-':
        return [1, 1]
    else:
        for int_i in range(3):
            for int_j in range(3):
                if game_matrix[int_j][int_i] == '-':
                    return [int_j, int_i]


def game_state(mark):
    global game_matrix
    global turn_counter
    if game_end_check(mark)[0]:
        showinfo('', game_end_check(mark)[1])
        game_matrix = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

        for button_num in range(len(button_list)):
            button_in_use[button_list[button_num]].config(text='')
            turn_counter = 0
        return True
    else:
        return False


def game_end_check(mark):
    for i in range(3):
        if (game_matrix[i][0] == game_matrix[i][1] == game_matrix[i][2] != '-') or (
                game_matrix[0][i] == game_matrix[1][i] == game_matrix[2][i] != '-'):
            return [True, 'Победа ' + mark]
        elif (game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2] != '-') or (
                game_matrix[2][0] == game_matrix[1][1] == game_matrix[0][2] != '-'):
            return [True, 'Победа ' + mark]
    if turn_counter == 9:
        return [True, 'Ничья']
    return [False, 'Игра продолжается']


def whose_turn(button):
    key_coord = list(button_in_use.keys())[list(button_in_use.values()).index(button)]
    coord_list = key_coord.split(' ')

    global game_matrix
    global turn_counter

    if game_matrix[int(coord_list[0]) - 1][int(coord_list[1]) - 1] == '-':
        turn_counter += 1
        button["text"], mark = '☓', 'крестов'
        game_matrix[int(coord_list[0]) - 1][int(coord_list[1]) - 1] = button["text"]

        if not game_state(mark):
            turn_counter += 1
            button_bot = bot_player()
            button_in_use[str(button_bot[0] + 1) + ' ' + str(button_bot[1] + 1)]["text"], mark = 'O', 'ноликов'
            game_matrix[button_bot[0]][button_bot[1]] = \
                button_in_use[str(button_bot[0] + 1) + ' ' + str(button_bot[1] + 1)]["text"]

        game_state(mark)


for btn_num in range(len(button_list)):
    x += 1
    if btn_num % 3 == 0:
        button_y_coordinate += 155
        x = 0
    button_in_use[button_list[btn_num]] = tk.Button(game_window)
    button_in_use[button_list[btn_num]].config(height=5, width=10, font=font,
                                               command=lambda m=button_in_use[button_list[btn_num]]: whose_turn(m))
    button_in_use[button_list[btn_num]].place(x=button_x_coordinates[x], y=button_y_coordinate)
game_window.mainloop()