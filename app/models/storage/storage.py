#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add_container(self, container):
        pass
