#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from .storage import Storage


class StackStorage(Storage):
    def __init__(self, limit=0, stacks=[]):
        self.limit = limit
        self._stacks = []
        self.stacks = stacks

    @property
    def stacks(self):
        return self._stacks

    @stacks.setter
    def stacks(self, stacks):
        expected_numbers = list(range(1, len(stacks) + 1))
        actual_numbers = sorted([stack.number for stack in stacks])

        if expected_numbers != actual_numbers:
            raise ValueError(
                "Stacks must be numbered consecutively starting from 1 without any gaps."
            )

        self._stacks = stacks

    def __repr__(self):
        storage_repr = ""
        for stack in self.stacks:
            storage_repr += f"{stack}\n"
        return storage_repr

    def add_container(self, stack):
        if len(self.stacks) >= self.limit:
            raise ValueError(f"Maximum number ({self.limit}) of stacks reached.")

        if not stack.number == len(self.stacks) + 1:
            raise ValueError(
                f"Stack number ({stack.number }) must be consecutive without gaps (stack size: {len(self.stacks)})."
            )

        self.stacks.append(stack)

    def stack_tops(self):
        stack_tops = [
            stack.boxes[-1].label if stack.boxes else "_" for stack in self.stacks
        ]

        return "".join(stack_tops)
