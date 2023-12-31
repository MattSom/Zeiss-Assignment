#
# Mate Somoracz, Zeiss Assignment, October 2023
#


class Stack:
    def __init__(self, number, boxes=None):
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("The argument `number` must be of an integer.")

        self.number = number
        self.boxes = boxes

        if boxes is None:
            self.boxes = []

    def __repr__(self):
        box_repr = " ".join(f"{box}" for box in self.boxes)
        return f"<Stack {self.number} {box_repr}>"

    def add_box(self, box):
        self.boxes.append(box)

    def add_boxes(self, boxes):
        self.boxes.extend(boxes)

    def get_top_box(self):
        return self.boxes[-1] if self.boxes else None
