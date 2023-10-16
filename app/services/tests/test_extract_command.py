#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from ..extract_command import (
    extract_move_command_lines,
    extract_move_command_parameters,
)


class TestExtractMoveCommandLines:
    def test_extract_commands(self):
        lines = [
            "|S|                 |T| |Q|        ",
            "|L|             |B| |M| |P|     |T|",
            "|F|     |S|     |Z| |N| |S|     |R|",
            "|Z| |R| |N|     |R| |D| |F|     |V|",
            "|D| |Z| |H| |J| |W| |G| |W|     |G|",
            "|B| |M| |C| |F| |H| |Z| |N| |R| |L|",
            "|R| |B| |L| |C| |G| |J| |L| |Z| |C|",
            "|H| |T| |Z| |S| |P| |V| |G| |M| |M|",
            " 1   2   3   4   5   6   7   8   9 ",
            "               bottom              ",
            "move 7 from 6 to 7",
            "This is not a command",
            "move 3 from 2 to 4",
            "move 6 from 4 to 3",
            "Another line without a command",
            "                           ",
            "move 1 from 5 to 1",
        ]

        assert extract_move_command_lines(lines) == [
            "move 7 from 6 to 7",
            "move 3 from 2 to 4",
            "move 6 from 4 to 3",
            "move 1 from 5 to 1",
        ]


class TestExtractMoveCommandParameters:
    def test_valid_command(self):
        command = "move 7 from 6 to 7"

        assert extract_move_command_parameters(command) == {
            "number_of_boxes": 7,
            "from": 6,
            "to": 7,
        }
