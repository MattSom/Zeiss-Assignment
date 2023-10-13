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
        box_repr = " ".join(f"{box}" for box in self.boxes[::-1])
        return f"{self.number} {box_repr}"

    def add_box(self, box):
        self.boxes.append(box)

    def get_top_box(self):
        if self.boxes:
            return self.boxes[-1]
        else:
            return None
