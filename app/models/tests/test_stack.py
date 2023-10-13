#
# Mate Somoracz, Zeiss Assignment, October 2023
#

import pytest

from .. import Box, Stack


class TestStack:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.stack = Stack(number=1)

        self.box_A = Box(label="A")
        self.box_B = Box(label="B")

        self.stack.add_box(self.box_A)
        self.stack.add_box(self.box_B)

    @pytest.mark.parametrize("number", ["1", 0.1, True, [], {}, ()])
    def test_raises_TypeError_for_non_integer_number_arg(self, number):
        with pytest.raises(
            TypeError, match="The argument `number` must be of an integer."
        ):
            Stack(number=number)

    def test_add_box_appends_box(self):
        assert self.stack.boxes == [self.box_A, self.box_B]

    def test_get_top_box_returns_last_box(self):
        assert self.stack.get_top_box() == self.stack.boxes[-1]

    def test_get_top_box_returns_None_for_empty_stack(self):
        self.stack.boxes = []

        assert self.stack.get_top_box() is None
