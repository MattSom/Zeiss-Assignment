#
# Mate Somoracz, Zeiss Assignment, October 2023
#

import re


def extract_move_command_lines(lines):
    return [line.strip() for line in lines if line.startswith("move")]


def extract_move_command_parameters(command):
    pattern = r"move (\d+) from (\d+) to (\d+)"

    match = re.match(pattern, command)

    if match:
        return {
            "number_of_boxes": int(match.group(1)),
            "from": int(match.group(2)),
            "to": int(match.group(3)),
        }
