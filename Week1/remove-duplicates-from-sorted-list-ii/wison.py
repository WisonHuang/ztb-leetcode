class Solution:

    # @param head, a ListNode

    # @return a ListNode

    def deleteDuplicates(self, head):
        result=ListNode(0)
        r=result
        pre=head
        if not pre:
            return None
        cur=head.next
        if not cur:
            return head
        while cur:
            if pre.val!=cur.val:
                result.next=pre
                pre=pre.next
                cur=cur.next
                result=result.next
            else:
                while cur and pre.val==cur.val:
                    cur=cur.next
                if cur:
                    pre=cur
                    cur=cur.next
        if  not pre.next:
            result.next=pre
            result=result.next
        result.next=None
        return r.next
