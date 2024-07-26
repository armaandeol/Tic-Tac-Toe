positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_board():
    print(f'''
    Welcome to Tic Tac Toe!

      {positions[0][0]}  ┃  {positions[0][1]}  ┃  {positions[0][2]}
    ──────────────────
      {positions[1][0]}  ┃  {positions[1][1]}  ┃  {positions[1][2]}
    ──────────────────
      {positions[2][0]}  ┃  {positions[2][1]}  ┃  {positions[2][2]}

      ''')


def check_winner():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if positions[i][0] == positions[i][1] == positions[i][2]:
            return True
        if positions[0][i] == positions[1][i] == positions[2][i]:
            return True
    if positions[0][0] == positions[1][1] == positions[2][2]:
        return True
    if positions[0][2] == positions[1][1] == positions[2][0]:
        return True
    return False


def game(player, choice):
    for i in range(3):
        if choice in positions[i]:
            location = positions[i].index(choice)
            positions[i][location] = "✖" if player == 1 else "🔘"
            print_board()
            return check_winner()
    return False


game_on = True
taken = []
period = 1

print_board()

while game_on:
    for i in range(1, 3):
        if period > 9:
            print("It's a tie!")
            game_on = False
            break

        valid_move = False
        while not valid_move:
            try:
                choice = int(input(f"Player {i}, type in a number to play: "))
                if choice not in range(1, 10):
                    print("Invalid input. Please choose a number between 1 and 9.")
                    continue
                if choice in taken:
                    print("Position already taken. Try another one.")
                    continue
                valid_move = True
            except ValueError:
                print("Invalid input. Please enter a number.")

        taken.append(choice)
        if game(i, choice):
            print(f"Player {i} wins!")
            game_on = False
            break
        period += 1