import tkinter as tk
from tkinter import messagebox
from main import coin_change
def calculate():
    try:
        coins = list(map(int, coins_entry.get().split(",")))
        amount = int(amount_entry.get())

        if not coins or any(c <= 0 for c in coins):
            raise ValueError

        if amount < 0:
            raise ValueError

        minimum, selected, dp_table = coin_change(
            coins, amount
        )

        result_box.config(state="normal")
        result_box.delete("1.0", tk.END)

        if minimum == -1:
            result_box.insert(
                tk.END, "No solution found!"
            )
        else:
            result_box.insert(
                tk.END,
                f"Minimum Coins: {minimum}\n\n"
            )

            result_box.insert(
                tk.END,
                f"Selected Coins: {selected}\n"
            )

        result_box.config(state="disabled")

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid positive coins and amount!"
        )
root = tk.Tk()
root.title("Coin Change Solver")
root.geometry("550x500")
root.configure(bg="#172033")
title = tk.Label(
    root,
    text="COIN CHANGE SOLVER",
    font=("Arial", 22, "bold"),
    bg="#172033",
    fg="white"
)
title.pack(pady=25)
tk.Label(
    root,
    text="Enter Coins (e.g. 1,3,4)",
    bg="#172033",
    fg="white",
    font=("Arial", 12)
).pack()
coins_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
coins_entry.pack(pady=10)
coins_entry.insert(0, "1,3,4")
tk.Label(
    root,
    text="Enter Amount",
    bg="#172033",
    fg="white",
    font=("Arial", 12)
).pack()
amount_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
amount_entry.pack(pady=10)
amount_entry.insert(0, "6")
calculate_button = tk.Button(
    root,
    text="CALCULATE",
    command=calculate,
    bg="#2878E5",
    fg="white",
    font=("Arial", 13, "bold"),
    width=20,
    cursor="hand2"
)
calculate_button.pack(pady=20)
tk.Label(
    root,
    text="RESULTS",
    bg="#172033",
    fg="white",
    font=("Arial", 15, "bold")
).pack(pady=10)
result_box = tk.Text(
    root,
    height=8,
    width=48,
    font=("Consolas", 12),
    bg="#25334D",
    fg="white"
)
result_box.pack(pady=10)
result_box.config(state="disabled")
root.mainloop()
