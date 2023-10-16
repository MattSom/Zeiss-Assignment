#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from app.services.helpers import read_data_until_end_line
from app.services.create_storage import create_stack_storage_from_lines
from app.services.extract_command import (
    extract_move_command_lines,
    extract_move_command_parameters,
)


class Task:
    def __init__(self, file):
        self.file = file

        with open(file, "r") as file:
            file_lines = file.readlines()

            self.move_command_parameters = [
                extract_move_command_parameters(move_command)
                for move_command in extract_move_command_lines(file_lines)
            ]

            self.storage_data_lines = read_data_until_end_line(
                file_lines, end_line_text="bottom"
            )
            self.storage_data_lines.reverse()

            storage = create_stack_storage_from_lines(self.storage_data_lines)

            print("Task initialized, storage state is:")
            print(storage)
            print(storage.stack_tops(), "\n")

    def run_simulation(self, lifter):
        storage = create_stack_storage_from_lines(self.storage_data_lines)

        for params in self.move_command_parameters:
            lifter.move(
                stack_storage=storage,
                source_stack=params["from"],
                target_stack=params["to"],
                number_of_boxes=params["number_of_boxes"],
            )

        print(f"Storage state using {lifter.__class__.__name__}:")
        print(storage)
        print(storage.stack_tops(), "\n")
