#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from abc import ABC, abstractmethod


class Lifter(ABC):
    @abstractmethod
    def move(self, storage, source_container, target_container, number_of_items):
        pass
