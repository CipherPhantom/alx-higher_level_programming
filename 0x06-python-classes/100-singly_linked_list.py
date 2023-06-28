#!/usr/bin/python3
class Node:

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not value or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        NewNode = Node(value)
        if not self.__head:
            self.__head = NewNode
            return

        current = self.__head
        prev = None
        while current:
            if current.data > NewNode.data:
                NewNode.next_node = current
                if prev:
                    prev.next_node = NewNode
                else:
                    self.__head = NewNode
                break
            prev = current
            current = current.next_node

        if not current:
            prev.next_node = NewNode

    def print_all(self):
        nodes = ""
        current = self.__head
        while current:
            nodes += str(current.data)
            nodes += "\n" if current.next_node else ""
            current = current.next_node

        return nodes

    def __str__(self):
        return self.print_all()