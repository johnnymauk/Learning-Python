from SortingAlgorithms.SAInterface import SAInterface


class Radix(SAInterface):

    @staticmethod
    def get_name():
        return 'Radix Sort'

    @staticmethod
    def sort(array):
        max_digits = Radix.find_max_digits(array)
        digit = 1

    @staticmethod
    def find_max_digits(array):
        base = 1
        index = 0
        while index < len(array):
            if array[index] / base > 1:
                base *= 10
                index -= 1
            index += 1
        return int(base/10)

    @staticmethod
    def buckets(array, base):
        buckets = [[],[],[],[],[],[],[],[],[],[]]

        for num in range(len(array)):
            buckets[array%(base*10)] = num

        # for bucket in range(len(buckets)):



