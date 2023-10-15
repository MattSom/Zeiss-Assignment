#
# Mate Somoracz, Zeiss Assignment, October 2023
#

import pytest

from ..helpers import read_data_until_end_line, read_in_chunks_with_skip


class TestReadDataUntilEndLine:
    def test_empty_lines(self):
        lines = []

        assert read_data_until_end_line(lines) == []

    def test_no_end_line_provided(self):
        lines = ["Line 1", "Line 2", "Line 3"]

        assert read_data_until_end_line(lines) == ["Line 1", "Line 2", "Line 3"]

    def test_with_empty_lines_are_skipped(self):
        lines = ["Line 1", "", "Line 2", "Line 3", ""]

        assert read_data_until_end_line(lines) == ["Line 1", "Line 2", "Line 3"]

    def test_with_end_line(self):
        lines = ["Line 1", "", "Line 2", "end line", "", "Line 3", "Line 4"]

        assert read_data_until_end_line(lines, end_line_text="end line") == [
            "Line 1",
            "Line 2",
        ]


class TestReadInChunksWithSkip:
    def test_basic_functionality(self):
        string = "1234567890"
        chunk_size = 2
        skip_size = 1

        result = list(read_in_chunks_with_skip(string, chunk_size, skip_size))

        assert result == ["12", "45", "78", "0"]

    def test_chunk_larger_than_string(self):
        string = "123"
        chunk_size = 4
        skip_size = 1

        result = list(read_in_chunks_with_skip(string, chunk_size, skip_size))
        assert result == ["123"]

    def test_skip_size_larger_than_string(self):
        string = "abcdefgh"
        chunk_size = 2
        skip_size = 10

        result = list(read_in_chunks_with_skip(string, chunk_size, skip_size))

        assert result == ["ab"]

    def test_chunk_is_empty(self):
        string = "abcdefgh"
        chunk_size = 0
        skip_size = 1

        result = list(read_in_chunks_with_skip(string, chunk_size, skip_size))

        assert result == ["", "", "", "", "", "", "", ""]

    def test_empty_string(self):
        string = ""
        chunk_size = 2
        skip_size = 1

        result = list(read_in_chunks_with_skip(string, chunk_size, skip_size))

        assert result == []

    def test_raises_AttributeError_for_zero_chunk_and_zero_skip(self):
        string = "abcdefgh"
        chunk_size = 0
        skip_size = 0

        with pytest.raises(
            AttributeError, match="Can not read empty chunks with zero skips."
        ):
            list(read_in_chunks_with_skip(string, chunk_size, skip_size))
