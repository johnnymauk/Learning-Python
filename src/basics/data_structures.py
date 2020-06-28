class LinkedList:

    """
    Linked List Implementation:
    1.
    """

    def __init__(self):
        self.__head: LinkedList.__Node = None

    class __Node:

        def __init__(self, data=None, next_node=None):
            self.data = data
            self.next_node = next_node

    @staticmethod
    def create_node(data, next_node: __Node = None):
        return LinkedList.__Node(data, next_node)

    def get_head(self):
        return self.__head
