from Tools import Stopwatch, RandomArray
import SortingAlgorithms as SA

algorithm_list = [SA.Insertion, SA.Radix, SA.Quick]
processing_time = []
tests = 10


for algorithm in algorithm_list:
    for test in range(tests):
        processing_time.append(Stopwatch.start(algorithm, RandomArray.SMALL, 23))
    print(
        algorithm.get_name() + "\n" +
        "Min: {:,} ns".format(min(processing_time)) +
        "\tMax: {:,} ns".format(max(processing_time)) +
        "\tAvg: {:,.0f} ns".format(sum(processing_time)/tests)
    )
    processing_time.clear()
