#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from ..create_storage import create_stack_storage_from_lines


class TestCreateStackStorageFromLines:
    def test_successfully_parses_lines_into_storage_object(self):
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
        ]

        storage = create_stack_storage_from_lines(lines)

        assert storage.stack_tops() == "SRSJBTQRT"
