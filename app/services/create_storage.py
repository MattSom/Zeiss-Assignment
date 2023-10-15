#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from app.models import Box, Stack, StackStorage
from .helpers import read_in_chunks_with_skip


def create_stack_storage_from_lines(lines):
    lines.reverse()

    stack_numbers = list(map(int, lines[0].split()))
    box_data_lines = lines[1:]

    box_data = [
        [
            chunk[1] if chunk != "   " else None
            for chunk in read_in_chunks_with_skip(line, chunk_size=3, skip_size=1)
        ]
        for line in box_data_lines
    ]

    storage = StackStorage(limit=len(stack_numbers))

    for i, number in enumerate(stack_numbers):
        stack = Stack(number=number)

        for box_labels in box_data:
            if box_label := box_labels[i]:
                stack.add_box(Box(label=box_label))

        storage.add_container(stack)

    return storage
