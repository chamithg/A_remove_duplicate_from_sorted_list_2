# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        runner = dummy_head

        print(runner.next)

        if not head or not head.next:
            return dummy_head.next

      

        while runner.next.next:
            print(runner.val)
            if runner.next.val == runner.next.next.val:
                temp = runner.next
                if not temp.next.next:
                    runner.next = None
                    return dummy_head.next
                else:
                    while temp.val == temp.next.val:
                        temp.next = temp.next.next
                        if not temp.next:
                            runner.next = None
                            return dummy_head.next

                    runner.next = temp.next
            else:
                runner= runner.next

        return dummy_head.next