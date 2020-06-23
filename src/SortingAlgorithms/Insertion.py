import SortingAlgorithms.SAInterface as SAInterface


class Insertion(SAInterface):

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

Insertion.sort([1,2,3,5,6,8])
