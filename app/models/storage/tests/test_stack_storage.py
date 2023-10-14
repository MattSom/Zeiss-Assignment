#
# Mate Somoracz, Zeiss Assignment, October 2023
#

import pytest

from app.models import Stack

from ..stack_storage import StackStorage


class TestStackStorage:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.storage = StackStorage(limit=10)

    def test_setting_valid_stacks_passes(self):
        valid_stacks = [Stack(number=1), Stack(number=2), Stack(number=3)]
        self.storage.stacks = valid_stacks

    @pytest.mark.parametrize(
        "invalid_stacks",
        [
            [Stack(number=1), Stack(number=3), Stack(number=4)],
            [Stack(number=2), Stack(number=3), Stack(number=4)],
        ],
    )
    def test_setting_invalid_stacks_raises_ValueError(self, invalid_stacks):
        with pytest.raises(
            ValueError,
            match="Stacks must be numbered consecutively starting from 1 without any gaps.",
        ):
            self.storage.stacks = invalid_stacks

    def test_add_container_appends_stack(self):
        stack = Stack(number=1)
        self.storage.add_container(stack)
        assert self.storage.stacks == [stack]

    def test_add_container_raises_ValueError_for_appending_stack_beyond_storage_limit(
        self,
    ):
        self.storage.stacks = [
            Stack(number=i) for i in range(1, self.storage.limit + 1)
        ]

        with pytest.raises(
            ValueError,
            match=f"Maximum number \\({self.storage.limit}\\) of stacks reached.",
        ):
            self.storage.add_container(Stack(number=self.storage.limit + 1))

    def test_add_container_passes_for_stack_with_consecutive_number(self):
        stack_number = 1
        self.storage.stacks = [Stack(number=stack_number)]

        self.storage.add_container(Stack(number=stack_number + 1))

    def test_add_container_raises_ValueError_if_new_stack_number_is_consecutive(self):
        stack_number = 1
        self.storage.stacks = [Stack(number=stack_number)]

        new_stack = Stack(number=stack_number + 2)

        with pytest.raises(
            ValueError,
            match=f"Stack number \\({new_stack.number}\\) must be consecutive without gaps \\(stack size: {len(self.storage.stacks)}\\).",
        ):
            self.storage.add_container(new_stack)
