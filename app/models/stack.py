#
# Mate Somoracz, Zeiss Assignment, October 2023
#


class Stack:
    def __init__(self, number):
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("The argument `number` must be of an integer.")

        self.boxes = []
        self.number = number

    def __repr__(self):
        box_repr = " ".join(f"{box}" for box in self.boxes)
        return f"{self.number} {box_repr}"

    def add_box(self, box):
        self.boxes.append(box)

    def add_boxes(self, boxes):
        self.boxes.extend(boxes)

    def get_top_box(self):
        return self.boxes[-1] if self.boxes else None
