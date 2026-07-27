class Solution(object):
    def sortList(self, head):
        if not head:
            return head

        swapped = True
        while swapped:
            swapped = False
            curr = head

            while curr and curr.next:
                if curr.val > curr.next.val:
                    curr.val, curr.next.val = curr.next.val, curr.val
                    swapped = True
                curr = curr.next

        return head
      
