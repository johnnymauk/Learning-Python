import time
from Tools.RandomArray import RandomArray


class Stopwatch:
    @staticmethod
    def start(sorting_algorithm, random_array_specs, set_seed=time.time()):
        array = RandomArray.generate(random_array_specs.value, set_seed)
        start_time = time.perf_counter_ns()
        sorting_algorithm.sort(array)
        end_time = time.perf_counter_ns()
        print(sorting_algorithm.get_name() +
              ':\t'+random_array_specs.name+'\t:\t' +
              '{:,} ns'.format(end_time - start_time))
        return end_time - start_time

    @staticmethod
    def start_all(sorting_algorithm, set_seed=time.time()):
        times = []
        for name, member in RandomArray.__members__.items():
            times.append(Stopwatch.start(sorting_algorithm, member, set_seed))
        return times
