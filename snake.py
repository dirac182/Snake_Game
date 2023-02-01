from turtle import *

START_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):

        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self,position):

        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snakes.append(snake)

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def extend(self):
        # add new segment to snake
        self.add_segment(self.snakes[-1].position())

    def move(self):

        for seg_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg_num - 1].xcor()
            new_y = self.snakes[seg_num - 1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):

        if self.head.heading() == RIGHT:
            return

        self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() == LEFT:
            return

        self.head.setheading(RIGHT)

    def up(self):

        if self.head.heading() == DOWN:
            return

        self.head.setheading(UP)

    def down(self):

        if self.head.heading() == UP:
            return

        self.head.setheading(DOWN)