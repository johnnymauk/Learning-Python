import enum


class SortingAlgorithm(object):

    @staticmethod
    def sort(array):
        """Sorting algorithm implementation"""
        raise NotImplementedError

    @staticmethod
    def get_name():
        """Get algorithm name"""
        raise NotImplementedError


class Insertion(SortingAlgorithm):

    @staticmethod
    def get_name():
        return 'Insertion Sort'

    @staticmethod
    def sort(array):
        for outer in range(1, len(array)):
            if array[outer] < array[outer-1]:
                for inner in range(0, outer):
                    if array[outer] <= array[inner]:
                        array.insert(inner, array.pop(outer))
                        break
        return array


class Quick(SortingAlgorithm):

    @staticmethod
    def get_name():
        return 'Quick Sort'

    @staticmethod
    def sort(array):
        left = []
        right = []
        if len(array) > 1:
            for index in range(len(array) - 1):
                if array[index] < array[-1]:
                    left.append(array[index])
                else:
                    right.append(array[index])
            left = Quick.sort(left)
            left.extend(array[-1:])
            left.extend(Quick.sort(right))
            return left
        else:
            return array


class Radix(SortingAlgorithm):

    @staticmethod
    def get_name():
        return 'Radix Sort'

    @staticmethod
    def sort(array):
        max_base = Radix.__find_max_digits(array)
        base = 10
        while base < max_base:
            test = Radix.__buckets(array, base)
            array = test
            base *= 10
        return array

    @staticmethod
    def __find_max_digits(array):
        base = 1
        index = 0
        while index < len(array):
            if array[index] / base > 1:
                base *= 10
                index -= 1
            index += 1
        return base

    @staticmethod
    def __buckets(array, base):
        buckets = [[], [], [], [], [], [], [], [], [], []]

        # print(array)
        for num in range(len(array)):
            # print(str(num) + " + " + str(base) + " + " + str(array[num]) + " + " + str((int(array[num]/base)) % 10) )
            buckets[int(array[num]/base) % 10].append(array[num])

        while len(buckets) > 1:
            buckets[0].extend(buckets.pop(1))
        buckets.extend(buckets.pop(0))
        return buckets


class SA(enum.Enum):
    INSERTION = Insertion
    QUICK = Quick
    RADIX = Radix

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls.__members__.values()))
