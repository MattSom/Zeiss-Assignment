#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from .storage import Storage


class StackStorage(Storage):
    def __init__(self, limit=0, stacks=[]):
        self.limit = limit
        self.stacks = stacks

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
