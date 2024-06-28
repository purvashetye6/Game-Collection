import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 5,
    "C": 7,
    "D": 9
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Collection")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")  # Set background color
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12), padding=10, width=20)  # Uniform button size
        self.style.configure('TLabel', font=('Arial', 14), padding=10)
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'), padding=10)

        self.main_frame = ttk.Frame(root, padding=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Welcome to Game Collection", style='Header.TLabel').pack(pady=20)

        ttk.Button(self.main_frame, text="Rock Paper Scissors", command=self.start_rock_paper_scissors).pack(pady=10)
        ttk.Button(self.main_frame, text="Slot Machine", command=self.start_slot_machine).pack(pady=10)
        ttk.Button(self.main_frame, text="Guess the Number", command=self.start_guess_the_number).pack(pady=10)

    def start_rock_paper_scissors(self):
        self.clear_frame()
        self.computer_score = 0
        self.user_score = 0

        ttk.Label(self.main_frame, text="Rock Paper Scissors", style='Header.TLabel').pack(pady=20)

        self.rps_choice = tk.StringVar()
        choices_frame = ttk.Frame(self.main_frame)
        choices_frame.pack(pady=10)

        ttk.Button(choices_frame, text="Rock", command=lambda: self.set_rps_choice("rock"), width=20).pack(anchor="w", padx=10, pady=5)
        ttk.Button(choices_frame, text="Paper", command=lambda: self.set_rps_choice("paper"), width=20).pack(anchor="w", padx=10, pady=5)
        ttk.Button(choices_frame, text="Scissors", command=lambda: self.set_rps_choice("scissors"), width=20).pack(anchor="w", padx=10, pady=5)

        ttk.Button(self.main_frame, text="Play", command=self.play_rock_paper_scissors).pack(pady=10)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_menu).pack(pady=10)

        self.score_label = ttk.Label(self.main_frame,
                                    text=f"User Score: {self.user_score} - Computer Score: {self.computer_score}",
                                    style='TLabel')
        self.score_label.pack(pady=10)

    def set_rps_choice(self, choice):
        self.rps_choice.set(choice)

    def play_rock_paper_scissors(self):
        user_choice = self.rps_choice.get()
        if not user_choice:
            messagebox.showerror("Error", "Please make a choice!")
            return

        computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.score_label.config(text=f"User Score: {self.user_score} - Computer Score: {self.computer_score}")
        messagebox.showinfo("Result", f"You chose {user_choice}, computer chose {computer_choice}. {result}")

        if self.user_score == 3:
            messagebox.showinfo("Congratulations!", "You are the WINNER!")
            self.create_main_menu()
        elif self.computer_score == 3:
            messagebox.showinfo("Sorry", "Computer is the WINNER!")
            self.create_main_menu()

    def start_slot_machine(self):
        self.clear_frame()
        self.balance = 100  # Initial balance for the slot machine
        ttk.Label(self.main_frame, text="Slot Machine", style='Header.TLabel').pack(pady=20)

        self.balance_label = ttk.Label(self.main_frame, text=f"Balance: Rs. {self.balance}", style='TLabel')
        self.balance_label.pack(pady=10)

        ttk.Label(self.main_frame, text="Bet Amount:", style='TLabel').pack(pady=5)
        self.bet_entry = ttk.Entry(self.main_frame, width=30)  # Increased input field size
        self.bet_entry.pack(pady=5)

        ttk.Label(self.main_frame, text="Number of Lines:", style='TLabel').pack(pady=5)
        self.lines_entry = ttk.Entry(self.main_frame, width=30)  # Increased input field size
        self.lines_entry.pack(pady=5)

        ttk.Button(self.main_frame, text="Spin", command=self.spin_slot_machine).pack(pady=10)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_menu).pack(pady=10)

        self.slot_result = tk.StringVar()
        self.slot_result.set("Press 'Spin' to play")
        ttk.Label(self.main_frame, textvariable=self.slot_result, style='TLabel').pack(pady=20)

    def spin_slot_machine(self):
        try:
            bet = int(self.bet_entry.get())
            lines = int(self.lines_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for bet and lines")
            return

        if not (MIN_BET <= bet <= MAX_BET):
            messagebox.showerror("Invalid Bet", f"Bet must be between Rs. {MIN_BET} and Rs. {MAX_BET}")
            return
        if not (1 <= lines <= MAX_LINES):
            messagebox.showerror("Invalid Lines", f"Lines must be between 1 and {MAX_LINES}")
            return

        total_bet = bet * lines
        if total_bet > self.balance:
            messagebox.showerror("Insufficient Balance", f"Your balance is Rs. {self.balance}")
            return

        self.balance -= total_bet

        slots = self.slot_machine(ROWS, COLS, symbol_count)
        self.slot_result.set(self.format_slot_machine(slots))

        win_value, win_line = self.winnings(slots, lines, bet, symbol_value)
        self.balance += win_value

        messagebox.showinfo("Result", f"You won Rs. {win_value} on lines {win_line}")
        self.balance_label.config(text=f"Balance: Rs. {self.balance}")

        if self.balance <= 0:
            messagebox.showinfo("Game Over", "You have run out of balance!")
            self.create_main_menu()

    def winnings(self, columns, lines, bet, values):
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

    def slot_machine(self, rows, cols, symbols):
        all_symbols = []
        for symbol, count in symbols.items():
            all_symbols.extend([symbol] * count)

        columns = []
        for _ in range(cols):
            column = random.sample(all_symbols, rows)
            columns.append(column)
        return columns

    def format_slot_machine(self, columns):
        formatted = ""
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(column) - 1:
                    formatted += column[row] + " | "
                else:
                    formatted += column[row]
            formatted += "\n"
        return formatted

    def start_guess_the_number(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Guess the Number", style='Header.TLabel').pack(pady=20)

        self.number_to_guess = random.randint(0, 10)
        self.no_of_guesses = 0

        self.guess_entry = ttk.Entry(self.main_frame, width=30)  # Increased input field size
        self.guess_entry.pack(pady=10)

        ttk.Button(self.main_frame, text="Guess", command=self.check_guess).pack(pady=10)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_menu).pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.no_of_guesses += 1

            if guess < self.number_to_guess:
                message = "Make a bigger guess."
            elif guess > self.number_to_guess:
                message = "Make a smaller guess."
            else:
                message = f"Congratulations! You guessed it right in {self.no_of_guesses} attempts!"
                messagebox.showinfo("Result", message)
                self.create_main_menu()
                return

            if self.no_of_guesses >= 5:
                message = f"Game over. The number was: {self.number_to_guess}"
                messagebox.showinfo("Result", message)
                self.create_main_menu()
            else:
                messagebox.showinfo("Result", message)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number")

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
