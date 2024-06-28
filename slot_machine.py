import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A" : 3,
    "B" : 5,
    "C" : 7,
    "D" : 9
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def winnings(columns, lines, bet, values):
    winnings = 0
    win_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        
        else:
            winnings += values[symbol] * bet
            win_line.append(line + 1)

    return winnings, win_line


def slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(COLS):
        column = []
        symbol_copy = all_symbols[:]
        for _ in range (ROWS):
            value = random.choice(symbol_copy)
            symbol_copy.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()
    
        

def deposit():
    while True:
        amount = input("Enter the amount that you want to deposit: Rs. ")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        else:
            print("Enter a number.")

    return amount

def lines_to_bet_on():
    while True:
        lines = input("How many lines to bet on (1 -" + str(MAX_LINES) + ")? ")

        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= 3:
                break
            else:
                print("Enter valid no. of lines to bet on.")

        else:
            print("Enter a number.")

    return lines

def bet_on_each_line():
    while True:
        amount = input("How much you want to bet on each line: Rs. ")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must between Rs. {MIN_BET} - Rs. {MAX_BET}")

        else:
            print("Enter a number.")
    
    return amount

def spin(balance):
    lines = lines_to_bet_on()

    while True:
        bet = bet_on_each_line()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You cannot bet since your balance is Rs. {balance}")
        else:
            break
        
    print(f"You are betting Rs. {bet} on {lines} lines. Total bet is equal to Rs. {total_bet}.")

    slots = slot_machine(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    win_value, win_line = winnings(slots, lines, bet, symbol_value)
    print(f"You won Rs. {win_value}")
    print(f"You won on line: ", *win_line)

    return win_value - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is Rs. {balance}")
        play = input("Hit entre to play (q to quit)")
        if play == "q":
            break
        else:
            balance += spin(balance)

main()