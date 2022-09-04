from tkinter import *

#^ we can add the datatype as a parameter
from quiz_brain import QuizBrain
 

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz:QuizBrain): #! here is where we will create our interface, all of the buttons all the layout ...
        self.quiz = quiz
        self.window = Tk()
        self.window.title("quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text=f"Score: {self.quiz.score}",fg="white",bg=THEME_COLOR)
        self.label.grid(column=1,row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,#x position
            125,#y position
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        #& call it immediately so that we dont see dummy text
        self.getNextQuestion()
        
        true_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=true_image, highlightthickness=0, command=self.correct)
        self.correct.grid(column=0, row=2)
        
        false_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=false_image, highlightthickness=0, command=self.wrong)
        self.wrong.grid(column=1, row=2)
        

        
        
        self.window.mainloop()

    def correct(self):
        ans = self.quiz.check_answer("true")
        self.giveFeedBacks(ans)
        
    def wrong(self):
        ans = self.quiz.check_answer("false")
        self.giveFeedBacks(ans)
        
        
    def giveFeedBacks(self,ans):
        if ans:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
    
        self.window.after(1000,self.getNextQuestion)
    

    def getNextQuestion(self): #! this method will tap into the quiz brain and call next_question method
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            text = self.quiz.next_question()
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text,text=text)
        else:
            self.canvas.itemconfig(self.question_text,text=f"you completed the quiz.\n Your final score was: {self.quiz.score}/{self.quiz.question_number} ")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")