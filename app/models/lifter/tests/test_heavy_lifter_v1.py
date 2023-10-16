#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from app.models import StackStorage, Stack, Box

from .. import HeavyLifterV1


class TestHeavyLifterV1:
    def test_moves_boxes_one_after_another(self):
        storage = StackStorage(
            limit=4,
            stacks=[
                Stack(number=1, boxes=[Box(label="P"), Box(label="A"), Box(label="K")]),
                Stack(number=2, boxes=[Box(label="U"), Box(label="Q")]),
                Stack(number=3, boxes=[Box(label="B")]),
                Stack(number=4, boxes=[Box(label="T"), Box(label="F")]),
            ],
        )

        lifter = HeavyLifterV1()

        lifter.move(
            stack_storage=storage, source_stack=1, target_stack=3, number_of_boxes=2
        )

        assert storage.stack_tops() == "PQAF"
