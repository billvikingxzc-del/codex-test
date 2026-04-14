import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("简易计算器")
        self.root.resizable(False, False)

        self.expression = tk.StringVar(value="")

        self._build_ui()

    def _build_ui(self) -> None:
        entry = tk.Entry(
            self.root,
            textvariable=self.expression,
            justify="right",
            font=("Segoe UI", 20),
            bd=8,
            relief=tk.RIDGE,
            width=16,
        )
        entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky="nsew")

        buttons = [
            ("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2),
        ]

        for text, row, col in buttons:
            cmd = (lambda t=text: self.on_button_click(t))
            tk.Button(
                self.root,
                text=text,
                command=cmd,
                font=("Segoe UI", 16),
                width=4,
                height=2,
            ).grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

        tk.Button(
            self.root,
            text="退出",
            command=self.root.quit,
            font=("Segoe UI", 16),
            width=4,
            height=2,
        ).grid(row=5, column=3, padx=4, pady=4, sticky="nsew")

        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)

        self.root.bind("<Return>", lambda _event: self.calculate())
        self.root.bind("<BackSpace>", lambda _event: self.backspace())

    def on_button_click(self, char: str) -> None:
        if char == "C":
            self.expression.set("")
        elif char == "⌫":
            self.backspace()
        elif char == "=":
            self.calculate()
        else:
            self.expression.set(self.expression.get() + char)

    def backspace(self) -> None:
        current = self.expression.get()
        self.expression.set(current[:-1])

    def calculate(self) -> None:
        expr = self.expression.get().strip()
        if not expr:
            return

        try:
            result = eval(expr, {"__builtins__": {}}, {})
            self.expression.set(str(result))
        except Exception:
            messagebox.showerror("错误", "表达式无效，请重新输入。")


if __name__ == "__main__":
    app_root = tk.Tk()
    CalculatorApp(app_root)
    app_root.mainloop()
