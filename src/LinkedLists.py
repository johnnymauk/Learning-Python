#
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#
#
# class Node:
#
#     def __init__(self, data, next_node=None):
#         self.data = data
#         self.next_node = next_node
#
#
# class Device:
#     def __init__(self, name, ip):
#         self.name = name
#         self.ip = ip
#
#     def print_info(self):
#         print("Name: " + self.name + "\tIP: " + self.ip)
#
#
#
#
#
# internet = LinkedList()
#
# user_input = None
# new_device = Device(input("Enter device name or done to quit: "), input("Enter ip address: "))
# internet.head = Node(new_device)
# current_node = internet.head
# while user_input != "done":
#     user_input = input("Enter device name or done to quit: ")
#     if user_input != "done":
#         new_device = Device(user_input, input("Enter ip address: "))
#         current_node.next_node = Node(new_device)
#         current_node = current_node.next_node
#
#
# # node_1 = Node("WOW")
# # node_2 = Node("Modem")
# # node_3 = Node("pfSense")
# # node_4 = Node("Switch")
# # node_5 = Node("Computer")
# #
# # network.head = node_1
# # node_1.next_node = node_2
# # node_2.next_node = node_3
# # node_3.next_node = node_4
# # node_4.next_node = node_5
