#
# Mate Somoracz, Zeiss Assignment, October 2023
#

import pytest
import string

from app.models import Box


class TestBox:
    @pytest.mark.parametrize(
        "label",
        [123, "123", "TooLong", True, [], ()],
    )
    def test_raises_ValueError_for_invalid_label(self, label):
        with pytest.raises(
            ValueError,
            match="Box label must be a single capital letter of the English alphabet.",
        ):
            Box(label=label)

    @pytest.mark.parametrize(
        "label",
        list(string.ascii_uppercase),
    )
    def test_passes_for_single_english_alphabetical_label(self, label):
        Box(label)
