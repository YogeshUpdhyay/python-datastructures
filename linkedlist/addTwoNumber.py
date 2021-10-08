from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num1 = 0
    count = 0
    while l1 is not None:
        num1 = num1 + (10**count)*l1.val
        count += 1
        l1 = l1.next
    
    num2 = 0
    count = 0
    while l2 is not None:
        num2 = num2 + (10**count)*l2.val
        count += 1
        l2 = l2.next
    
    ans = num1 + num2
    
    ansNode = ListNode()
    curNode = ansNode
    
    while ans > 0:
        curNode.val = ans%10
        ans = ans // 10
        curNode.next = ListNode() if ans > 0 else None
        curNode = curNode.next
        
    return ansNode

print(addTwoNumbers(ListNode(2,ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))