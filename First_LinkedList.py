#!/usr/bin/python
# -*- coding: UTF-8 -*-



class MyLinkedList:

    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self):
        self.node = self.Node(None, None)

    def get(self, index: int) -> int:
        _index = 0
        if index == _index:
            if self.node:
                return -1 if self.node.val is None else self.node.val
            else:
                return -1

        check = self.node
        while check.next:
            _index += 1
            if _index == index:
                return check.next.val
            else:
                check = check.next
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        if self.node.next:
            t = self.node.val
            n = self.Node(t, self.node.next)
            self.node.val = val
            self.node.next = n
        elif self.node.val is not None:
            n = self.Node(self.node.val, None)
            self.node.val = val
            self.node.next = n
        else:
            self.node.val = val

    def addAtTail(self, val: int) -> None:
        if self.node.val is None:
            self.node.val = val
            return
        n = self.Node(val, None)
        check = self.node
        while check.next:
            check = check.next
        check.next = n

    def addAtIndex(self, index: int, val: int) -> None:
        if self.node:
            if self.node.val is not None:
                _index = 0
            else:
                _index = -1
        else:
            _index = -1

        if index == 0:
            return self.addAtHead(val)

        check = self.node
        while check.next:
            _index += 1
            if _index == index:
                n = self.Node(val, check.next)
                check.next = n
                break
            check = check.next
        else:
            if index == _index + 1:
                return self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        _index = 0
        if index == 0:
            if self.node.next:
                self.node = self.node.next
            else:
                self.node = None
            return

        check = self.node
        while check.next:
            _index += 1
            if _index == index:
                check.next = check.next.next
                break
            check = check.next

    def show(self) -> None:
        lst = []
        if self.node.val is not None:
            lst.append(self.node.val)
        while self.node.next:
            self.node = self.node.next
            lst.append(self.node.val)

        print(lst)



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


if __name__ == '__main__':

    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    c = obj.get(1)
    print(c)
    obj.deleteAtIndex(1)
    # obj.show()
    c = obj.get(1)
    print(c)
    c = obj.get(3)
    print(c)
    obj.deleteAtIndex(3)
    obj.deleteAtIndex(0)
    c = obj.get(0)
    print(c)
    obj.deleteAtIndex(0)
    c = obj.get(0)
    print(c)
    # obj.show()
    # obj.addAtTail(7)
    # obj.show()
    # obj.addAtTail(8)
    # obj.addAtTail(9)
    obj.show()
    # obj.addAtTail(2)
    # obj.show()
    # obj.addAtIndex(1, 3)
    # obj.show()


