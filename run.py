#
# Mate Somoracz, Zeiss Assignment, October 2023
#

from app.task import Task
from app.models import HeavyLifterV1, HeavyLifterV2


task = Task("instruction_set_01.txt")

task.run_simulation(HeavyLifterV1())
task.run_simulation(HeavyLifterV2())
