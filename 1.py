from turtle import Turtle, Screen

font1 = ('Arial', 24, 'bold')
font2 = ('Arial', 50, 'bold')

marker = Turtle(visible=False)
marker.penup()


screen = Screen()
screen.title("Алексей - это тебе")
screen.bgcolor("#233d4d")
screen.setup(700, 700)

marker = Turtle(visible=False)
marker.penup()
marker.color('#fe7f2d')
marker.goto(-50, 305)
marker.write("Леха", font=font1)

marker.goto(-300, 0)
marker.color('#fcca46')
marker.write("Хорошего вечера", font=font2)

screen.onkey(screen.bye, "Escape")

screen.listen()

screen.mainloop()