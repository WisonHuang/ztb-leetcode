class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        p1=head
        step_first=n+1
        while step_first >0 and p1: #防止p1已经越界
            p1=p1.next
            step_first-=1
        if p1 is None and step_first>0:#针对越界的处理
            return head.next
        p2=head
        while p1:
            p1=p1.next
            p2=p2.next
        p2.next=p2.next.next
        return head
