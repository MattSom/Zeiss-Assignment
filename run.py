#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from app.services.helpers import read_data_until_end_line
from app.services.create_storage import create_stack_storage_from_lines


filename = "instruction_set_01.txt"
with open(filename, "r") as file:
    file_lines = file.readlines()

    storage_data_lines = read_data_until_end_line(file_lines, end_line_text="bottom")
    storage = create_stack_storage_from_lines(storage_data_lines)

    print(storage)
    print(storage.stack_tops())
