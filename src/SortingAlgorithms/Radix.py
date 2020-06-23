from SortingAlgorithms.SAInterface import SAInterface


class Radix(SAInterface):

    @staticmethod
    def get_name():
        return 'Radix Sort'

    @staticmethod
    def sort(array):
        max_base = Radix.find_max_digits(array)
        base = 10
        while base < max_base:
            # print('Base: ' + str(base))
            test = Radix.buckets(array, base)
            array = test
            base *= 10
        return array

    @staticmethod
    def find_max_digits(array):
        base = 1
        index = 0
        while index < len(array):
            if array[index] / base > 1:
                base *= 10
                index -= 1
            index += 1
        return base

    @staticmethod
    def buckets(array, base):
        buckets = [[], [], [], [], [], [], [], [], [], []]

        # print(array)
        for num in range(len(array)):
            # print(str(num) + " + " + str(base) + " + " + str(array[num]) + " + " + str((int(array[num]/base)) % 10) )
            buckets[int(array[num]/base) % 10].append(array[num])

        while len(buckets) > 1:
            buckets[0].extend(buckets.pop(1))
        buckets.extend(buckets.pop(0))
        return buckets


# Radix.sort([1, 23, 45, 123, 95, 11, 13, 54, 89, 109])
