# ساخت صفحه بازی
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# دریافت ورودی بازیکنان
def player_input(player):
    while True:
        try:
            move = int(input(f'Player {player}, enter your move (1-9): ')) - 1
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print('This spot is already taken.')
        except (ValueError, IndexError):
            print('Invalid input. Please enter a number between 1-9.')

# بررسی شرایط برد
def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# اجرای بازی
def game():
    current_player = 'X'
    for _ in range(9):
        print_board()
        player_input(current_player)
        if check_win(current_player):
            print(f'Player {current_player} wins!')
            print_board()
            return
        current_player = 'O' if current_player == 'X' else 'X'
    print('The game is a tie!')
    print_board()

game()