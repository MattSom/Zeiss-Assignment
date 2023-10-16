#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from .lifter import Lifter


class HeavyLifterV1(Lifter):
    def move(self, stack_storage, source_stack, target_stack, number_of_boxes):
        for _ in range(number_of_boxes):
            box_to_move = stack_storage.stacks[source_stack - 1].boxes.pop()
            stack_storage.stacks[target_stack - 1].boxes.append(box_to_move)
