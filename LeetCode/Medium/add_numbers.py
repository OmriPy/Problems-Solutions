class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def size(l: ListNode) -> int:
    size_l = 0
    while l != None:
        size_l += 1
        l = l.next
    return size_l

def fix_list_node(l: ListNode, n: int) -> ListNode:
    pos_l = l
    while pos_l.next != None:
        pos_l = pos_l.next
    for _ in range(n):
        pos_l.next = ListNode(0)
        pos_l = pos_l.next
    return l


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    size_l1 = size(l1)
    size_l2 = size(l2)
    if size_l1 < size_l2:
        l1 = fix_list_node(l1, size_l2 - size_l1)
    elif size_l1 > size_l2:
        l2 = fix_list_node(l2, size_l1 - size_l2)

    ret = None
    add = 0
    while l1 != None and l2 != None:
        val = l1.val + l2.val + add
        remainder = val % 10
        add = val // 10

        if ret == None:
            ret = ListNode(remainder)
            pos_ret = ret
        else:
            pos_ret.next = ListNode(remainder)
            pos_ret = pos_ret.next

        l1 = l1.next
        l2 = l2.next
    if add > 0:
        pos_ret.next = ListNode(add)
        pos_ret = pos_ret.next
    return ret


def print_list_node(l: ListNode):
    while l != None:
        print(l.val, end='')
        l = l.next
    print()


def build_list(num: tuple) -> ListNode:
    node = None
    pos_node = None
    for n in num:
        if node == None:
            node = ListNode(n)
            pos_node = node
        else:
            pos_node.next = ListNode(n)
            pos_node = pos_node.next
    return node