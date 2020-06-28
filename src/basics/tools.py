from random import seed
from random import randint
from enum import Enum
import time


class RandomArray(Enum):
    # specs: [number_elements, range_min, range_max]
    SMALL = [10, 0, 100]
    MEDIUM = [100, 0, 1000]
    LARGE = [1000, 0, 10000]
    MASSIVE = [100000, 0, 1000000]

    @staticmethod
    def generate(specs, seed_val=time.time()):
        seed(seed_val)
        array = []
        for index in range(0, specs[0]):
            array.append(randint(specs[1], specs[2]))
        return array


class Stopwatch:
    @staticmethod
    def start(sorting_algorithm, random_array_specs, set_seed=time.time()):
        array = RandomArray.generate(random_array_specs.value, set_seed)
        start_time = time.perf_counter_ns()
        sorting_algorithm.sort(array)
        end_time = time.perf_counter_ns()
        time_elapsed = end_time - start_time
        return time_elapsed

    @staticmethod
    def start_all(sorting_algorithm, set_seed=time.time()):
        times = []
        for name, member in RandomArray.__members__.items():
            times.append(Stopwatch.start(sorting_algorithm, member, set_seed))
        return times
