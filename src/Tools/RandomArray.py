from random import seed
from random import randint
from enum import Enum
import time


class RandomArray(Enum):
    # specs: [number_elements, range_min, range_max]
    TINY = [10, 0, 100]
    SMALL = [100, 0, 1000]
    MEDIUM = [1000, 0, 10000]
    # LARGE = [10000, 0, 100000]

    @staticmethod
    def generate(specs, seed_val=time.time()):
        seed(seed_val)
        array = []
        for index in range(0, specs[0]):
            array.append(randint(specs[1], specs[2]))
        return array

# print(RandomArray.generate([10, 0, 100] ))
