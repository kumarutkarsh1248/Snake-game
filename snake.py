from turtle import Turtle
starting_position = [(0, 0), (0, -20), (0, -40)]


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segments(position)

    def add_segments(self, position):
        new_segment = Turtle("turtle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            (x, y) = self.segments[i-1].pos()
            self.segments[i].goto((x, y))
        self.head.forward(20)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def snake_reset(self):
        for turtle in self.segments:
            turtle.goto(500,0)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)






