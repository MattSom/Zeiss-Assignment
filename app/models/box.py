#
# Mate Somoracz, Zeiss Assignment, October 2023
#


class Box:
    def __init__(self, label):
        if len(str(label)) == 1 and label.isalpha():
            self.label = label.upper()
        else:
            raise ValueError(
                "Box label must be a single capital letter of the English alphabet."
            )

    def __repr__(self) -> str:
        return f"|{self.label}|"
