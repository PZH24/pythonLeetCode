"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode(0)
    curr = dummy_head
    carry = 0
    while l1 is not None or l2 is not None:
        x = l1.val
        y = l2.val
        sum_num = carry + x + y
        carry = sum_num / 10
        curr.next = ListNode(sum_num % 10)
        curr = curr.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    if carry > 0:
        curr.next = ListNode(carry)
    return dummy_head.next


def addTwoNumbers2( l1: ListNode, l2: ListNode) -> ListNode:  # 这是返回的数据结构
    if l1 is None and l2 is None:
        return ListNode(0)
    elif l1 is None or l2 is None:
        return l1 if l1 is not None else l2
    else:
        l3 = ListNode(0)
        if (l1.val + l2.val) < 10:
            l3 = ListNode(l1.val + l2.val)
            l3.next = addTwoNumbers2(l1.next, l2.next)
        else:
            l3 = ListNode(l1.val + l2.val - 10)
            l3.next = addTwoNumbers2(l1.next, addTwoNumbers(l2.next, ListNode(1)))
        return l3


if __name__ == "__main__":
    print(addTwoNumbers2( ListNode(243), ListNode(564)))
