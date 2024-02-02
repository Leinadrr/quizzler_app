from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, pady=20, padx=20)
        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, width=270, text="Placeholder",
                                                     font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=35)

        self.label = Label(fg="White", bg=THEME_COLOR, text="Score: 0", font=("Arial", 10, "bold"))
        self.label.grid(row=0, column=1, sticky=N)

        self.image1 = PhotoImage(file="images/true.png")
        self.image2 = PhotoImage(file="images/false.png")
        self.button1 = Button(image=self.image1, borderwidth=0, highlightthickness=0, command=self.check_true)
        self.button1.grid(row=2, column=0)
        self.button2 = Button(image=self.image2, borderwidth=0, highlightthickness=0, command=self.check_false)
        self.button2.grid(row=2, column=1)

        self.get_net_question()

        self.window.mainloop()

    def get_net_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Sorry, there are no more question for "
                                                            "today.\nCome tomorrow")
            self.button1.config(state="disabled")
            self.button2.configure(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))
        # self.get_net_question()

    def check_false(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            print("pepe")
            self.canvas.configure(bg="green")
            self.window.after(1000, self.get_net_question)
            self.update_score()

        else:
            self.canvas.configure(bg="red")
            self.window.after(1000, self.get_net_question)
            self.update_score()

    def update_score(self):
        self.label.configure(text=f"Score: {self.quiz.score}")

