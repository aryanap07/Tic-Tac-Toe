import tkinter as tk
from tkinter import messagebox


WINNING_COMBINATIONS: list[list[int]] = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

current_player: str = "X"
winner: bool = False


def reset() -> None:
    global current_player, winner

    current_player = "X"
    winner = False

    label.config(
        text=f"Player {current_player}'s Turn",
        fg="black",
    )

    for button in buttons:
        button.config(
            text="",
            bg="white",
            state="normal",
        )


def winning_animation(combo: list[int]) -> None:
    def toggle_color(count: int = 0) -> None:
        if count >= 6:
            return

        color: str = "lightblue" if count % 2 == 0 else "white"

        for index in combo:
            buttons[index].config(bg=color)

        root.after(300, toggle_color, count + 1)

    toggle_color()


def check_winner() -> None:
    global winner

    for combo in WINNING_COMBINATIONS:
        first, second, third = combo

        if (
            buttons[first]["text"]
            == buttons[second]["text"]
            == buttons[third]["text"]
            != ""
        ):
            winner = True

            winning_animation(combo)

            messagebox.showinfo(
                "Tic-Tac-Toe",
                f"Hurray! Player {buttons[first]['text']} Wins!",
            )

            root.after(1000, reset)
            return

    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo(
            "Tic-Tac-Toe",
            "Oh! It's a Tie!",
        )

        root.after(500, reset)


def button_click(index: int) -> None:
    if buttons[index]["text"] == "" and not winner:
        buttons[index].config(
            text=current_player,
            bg="lightgrey",
        )

        check_winner()

        if not winner:
            toggle_player()


def toggle_player() -> None:
    global current_player

    current_player = "X" if current_player == "O" else "O"

    label.config(
        text=f"Player {current_player}'s Turn",
    )


def main() -> None:
    global root, label, buttons

    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    root.configure(bg="#f5f5f5")

    label = tk.Label(
        root,
        text="Player X's Turn",
        font=("Arial", 18, "bold"),
        bg="#f5f5f5",
        fg="black",
    )
    label.grid(
        row=0,
        column=0,
        columnspan=3,
        pady=10,
    )

    buttons = [
        tk.Button(
            root,
            text="",
            font=("Arial", 20, "bold"),
            width=8,
            height=3,
            bg="white",
            command=lambda i=i: button_click(i),
        )
        for i in range(9)
    ]

    for index, button in enumerate(buttons):
        button.grid(
            row=(index // 3) + 1,
            column=index % 3,
            padx=5,
            pady=5,
        )

    restart_button = tk.Button(
        root,
        text="Restart",
        font=("Arial", 16, "bold"),
        bg="gray",
        fg="white",
        command=reset,
    )
    restart_button.grid(
        row=4,
        column=0,
        columnspan=3,
        pady=10,
    )

    reset()
    root.mainloop()


if __name__ == "__main__":
    main()
