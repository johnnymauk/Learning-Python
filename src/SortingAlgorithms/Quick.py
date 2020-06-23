import SortingAlgorithms.SAInterface as SAInterface


class Quick(SAInterface):

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
            # print(array)
            # print(left)
            # print(right)

            return left
        else:
            return array
