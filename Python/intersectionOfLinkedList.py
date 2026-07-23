# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        tempA=headA
        tempB=headB
        nodeA=set()
        while tempA is not None:
            nodeA.add(tempA)
            tempA=tempA.next
        while tempB is not  None:
            if tempB in nodeA:
                return tempB
            else:
                tempB=tempB.next
