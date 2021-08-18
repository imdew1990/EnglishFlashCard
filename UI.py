import tkinter as tk
try:
    from tkmacosx import Button
except ImportError:
    from tkmacosx import Button
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'


class Flashy_UI:
    def __init__(self):
        # Screen
        self.window = tk.Tk()
        self.window.title(string='Flashy')
        self.window.config(bg=BACKGROUND_COLOR,
                           padx=50,
                           pady=50,
                           )
        # Canvas
        card_back = tk.PhotoImage(file='images/card_back.png')
        card_front = tk.PhotoImage(file='images/card_front.png')

        self.canvas = tk.Canvas(master=self.window,
                                width=800,
                                height=526,
                                highlightthickness=0,
                                bg=BACKGROUND_COLOR
                                )
        self.canvas.create_image(400, 263, image=card_back)
        self.canvas.create_image(400, 263, image=card_front)
        self.canvas.grid(column=0,
                         row=0,
                         columnspan=2)

        # Buttons
        right_image = tk.PhotoImage(file='images/right.png')
        wrong_image = tk.PhotoImage(file='images/wrong.png')
        self.wrong_button = tk.Button(master=self.window,
                                      image=wrong_image,
                                      highlightthickness=0,
                                      )
        self.right_button = tk.Button(master=self.window,
                                      image=right_image,
                                      highlightthickness=0,
                                     )
        self.right_button.grid(column=0,
                               row=2,
                               )
        self.window.mainloop()
