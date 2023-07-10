import tkinter as tk
import load_questions

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.build_gui()

        self.root.mainloop()

    def build_gui(self):
        self.frm_questions = tk.Frame(self.root)
        self.frm_questions.pack()

        self.lbl_question = tk.Label(
            self.frm_questions,
            text='Question text',
            font=('Helvetica', 40),
            pady=30
        )
        self.lbl_question.pack()

        self.frm_buttons = tk.Frame(self.root)
        self.frm_buttons.pack()

        self.btn_start = tk.Button(
            self.frm_buttons,
            text='Start',
            command=self.start,
            font=('Helvetica', 40),
            pady=30
        )
        self.btn_start.pack()

        self.btn_next = tk.Button(
            self.frm_buttons,
            text='Next',
            command=self.show_next,
            pady=20
        )
        self.btn_next.pack()
    
    def start(self):
        print('Start')
        self.questions = load_questions.get_questions('questions.csv')
    
    def show_next(self):
        print('Next')

if __name__ == "__main__":
    App()
