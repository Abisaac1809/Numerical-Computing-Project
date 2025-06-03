from __future__ import annotations

class Node:
    def __init__(self, data:any=None):
        self.__data:any = data
        self.__next = None
        self.__prev = None

    def get_data(self) -> any:
        return self.__data

    def get_next(self) -> Node:
        return self.__next

    def get_prev(self) -> Node:
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def set_next(self, next_node):
        self.__next = next_node

    def set_prev(self, prev_node):
        self.__prev = prev_node
