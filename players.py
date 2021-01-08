from turtle import Turtle
STARTING_POSITIONS = [(-380, -40), (-380, -20), (-380, 0), (-380, 20)]
STARTING_POSITIONS_cpu = [(380, -40), (380, -20), (380, 0), (380, 20)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Player:

    def __init__(self):
        self.segments = []
        self.segments_cpu = []
        self.create_player()
        self.create_cpu()

    def create_player(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def create_cpu(self):
        for position in STARTING_POSITIONS_cpu:
            self.add_segment_cpu(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def add_segment_cpu(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments_cpu.append(new_segment)

    def move(self):
        for segment in self.segments:
            segment.setheading(DOWN)

    def up(self):
        for segment in self.segments:
            segment.setheading(UP)
            segment.forward(70)

    def down(self):
        for segment in self.segments:
            segment.setheading(DOWN)
            segment.forward(70)

    def cpu_down(self):
        for segment in self.segments_cpu:
            segment.setheading(DOWN)
        for segment in self.segments_cpu:
            segment.forward(10)

    def cpu_up(self):
        for segment in self.segments_cpu:
            segment.setheading(UP)
        for segment in self.segments_cpu:
            segment.forward(10)
