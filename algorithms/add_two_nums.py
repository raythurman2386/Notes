import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1, l2):
        def to_int(node):
            return node.val + 10 * to_int(node.next) if node else 0
        def to_list(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = to_list(n / 10)
            return node
        return to_list(math.floor(to_int(l1) + to_int(l2)))



sol = Solution()
list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)
list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)
result = sol.add_two_numbers(list1, list2)
while result is not None:
    print(result.val)
    result = result.next
list3 = ListNode(5)
list4 = ListNode(5)
result = sol.add_two_numbers(list3, list4)
while result is not None:
    print(result.val)
    result = result.next
list5 = ListNode(1)
list5.next = ListNode(8)
list6 = ListNode(0)
result = sol.add_two_numbers(list5, list6)
while result is not None:
    print(result.val)
    result = result.next
