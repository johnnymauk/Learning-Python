import basics


def print_time(name, pt, t):
    print(
        '{:<20s}\tMin: {:>20,} ns\tMax: {:>20,} ns\tAvg: {:>20,.0f} ns'.format(
            sa.get_name(),
            min(processing_time),
            max(processing_time),
            sum(processing_time) / tests
        )
    )


processing_time = []
tests = 10


sa: basics.SortingAlgorithm
for sa in basics.SA.list():
    for test in range(tests):
        processing_time.append(basics.Stopwatch.start(sa, basics.RandomArray.MASSIVE, 23))
    print_time(sa.get_name(), processing_time, tests)
    processing_time.clear()


