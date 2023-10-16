#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from app.services.helpers import pop_last_n_elements

from .lifter import Lifter


class HeavyLifterV2(Lifter):
    def move(self, stack_storage, source_stack, target_stack, number_of_boxes):
        boxes_to_move = pop_last_n_elements(
            stack_storage.stacks[source_stack - 1].boxes, number_of_boxes
        )
        stack_storage.stacks[target_stack - 1].boxes.extend(boxes_to_move)
