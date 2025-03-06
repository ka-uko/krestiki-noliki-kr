import tkinter as tk
from tkinter import messagebox, simpledialog

window = tk.Tk()
window.title('Крестики-нолики')
window.geometry('280x400')
window.configure(bg='lightgrey')  # общий фон окна

current_player = "X"
player_symbol = "X"
opponent_symbol = "O"
buttons = []

player_wins = 0
opponent_wins = 0

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True

    return False

def check_draw():
    for row in buttons:
        for button in row:
            if button['text'] == '':
                return False
    return True

def on_click(row, col):
    global current_player, player_wins, opponent_wins

    if buttons[row][col]['text'] != '':
        return
    buttons[row][col]['text'] = current_player
    buttons[row][col]['fg'] = 'blue' if current_player == 'X' else 'DarkViolet'  # цвет текста X и O

    #счетчик
    if check_winner():
        if current_player == player_symbol:
            player_wins += 1
        else:
            opponent_wins += 1

        update_score()

        if player_wins == 3:
            messagebox.showinfo('Игра окончена!', 'Игрок выиграл!')
            reset_all()
        elif opponent_wins == 3:
            messagebox.showinfo('Игра окончена!', 'Оппонент выиграл!')
            reset_all()
        else:
            messagebox.showinfo('Игра окончена!', f'Игрок {current_player} победил!')
            reset_game()
    elif check_draw():
        messagebox.showinfo('Игра окончена!', 'Ничья!')
        reset_game()
    else:
        current_player = opponent_symbol if current_player == player_symbol else player_symbol

def reset_game():
    global current_player
    current_player = player_symbol
    for row in buttons:
        for button in row:
            button['text'] = ''

def reset_all():
    global player_wins, opponent_wins
    player_wins = 0
    opponent_wins = 0
    update_score()
    reset_game()

def update_score():
    score_label.config(text=f"Игрок: {player_wins} | Оппонент: {opponent_wins}")

def choose_symbol():
    global player_symbol, opponent_symbol, current_player
    player_symbol = simpledialog.askstring("Выбор символа", "Выберите свой символ: X или O")
    if player_symbol not in ["X", "O"]:
        player_symbol = "X"
    opponent_symbol = "O" if player_symbol == "X" else "X"
    current_player = player_symbol

choose_symbol()

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text='', font=('Arial', 20), width=5, height=2, bg='grey',
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j,padx=1, pady=1)
        row.append(btn)
    buttons.append(row)

reset_button = tk.Button(window, text='Сброс', font=('Arial', 14), bg='dark green', fg='white',
                         command=reset_all)
reset_button.grid(row=3, column=0, columnspan=3)

score_label = tk.Label(window, text="Игрок: 0 | Оппонент: 0", font=('Arial', 14), bg='lightgrey')
score_label.grid(row=4, column=0, columnspan=3)

window.mainloop()