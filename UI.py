import random
import pandas as pd
import tkinter as tk

try:
    from tkmacosx import Button
except ImportError:
    from tkmacosx import Button

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'


class Flashy_UI:
    def __init__(self, file_path):
        self.data = pd.read_csv(filepath_or_buffer=file_path)
        self.file = file_path
        # Screen

        self.window = tk.Tk()
        self.window.title(string='Flashy')
        self.window.config(bg=BACKGROUND_COLOR,
                           padx=50,
                           pady=50,
                           )
        # Canvas

        self.canvas = tk.Canvas(master=self.window,
                                width=800,
                                height=526,
                                highlightthickness=0,
                                bg=BACKGROUND_COLOR
                                )
        # Image in Canvas

        self.card_front_img = tk.PhotoImage(file='images/card_front.png')
        self.card_back_img = tk.PhotoImage(file='images/card_back.png')
        self.image = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.canvas.grid(column=0,
                         row=0,
                         columnspan=2)

        # Language name in Canvas

        self.language = self.canvas.create_text(400, 100, text="Title", font=(FONT_NAME, 45, 'italic'))

        # Word in Canvas

        self.word = self.canvas.create_text(400, 263, text='Word', font=(FONT_NAME, 70, 'bold'))
        # Buttons

        right_image = tk.PhotoImage(file='images/right.png')
        wrong_image = tk.PhotoImage(file='images/wrong.png')
        self.wrong_button = tk.Button(master=self.window,
                                      image=wrong_image,
                                      highlightthickness=0,
                                      highlightbackground=BACKGROUND_COLOR,
                                      command=self.wrong_answer
                                      )
        self.wrong_button.grid(column=0,
                               row=1,
                               )
        self.right_button = tk.Button(master=self.window,
                                      image=right_image,
                                      highlightthickness=0,
                                      highlightbackground=BACKGROUND_COLOR,
                                      command=self.right_answer
                                      )
        self.right_button.grid(column=1,
                               row=1,
                               )
        self.answer()
        self.window.mainloop()

    def set_language(self, language: str):
        self.canvas.itemconfig(self.language, text=language.title())

    def set_word(self, word: str):
        self.canvas.itemconfig(self.word, text=word.title())

    def next_word(self):
        word = self.data.sample()
        lan_list = word.columns
        first_lan = random.choice(lan_list)
        second_lan = [lan for lan in lan_list if lan != first_lan]
        second_lan = second_lan[0]
        first_word = word[first_lan].values[0]
        second_word = word[second_lan].values[0]
        return [first_lan, first_word, second_lan, second_word]

    def answer(self):
        self.current_card = self.next_word()
        self.set_language(self.current_card[0])
        self.set_word(self.current_card[1])
        self.swap_card_func = self.window.after(3000, self.swap_card, self.current_card[2], self.current_card[3])

    def swap_card(self, language: str, word: str):
        self.canvas.itemconfig(self.image, image=self.card_back_img)
        self.set_word(word=word)
        self.set_language(language)

    def right_answer(self):
        self.window.after_cancel(self.swap_card_func)
        self.answer()
        self.canvas.itemconfig(self.image, image=self.card_front_img)

        self.update_data()

    def wrong_answer(self):
        self.window.after_cancel(self.swap_card_func)
        self.answer()
        self.canvas.itemconfig(self.image, image=self.card_front_img)

    def update_data(self):
        index = self.data.index[self.data[self.current_card[0]] == self.current_card[1]]
        data = self.data.drop(index=index, axis=0)
        self.data.to_csv('Words.csv', index=False)
