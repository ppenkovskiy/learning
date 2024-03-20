# remove duplicates from sorted List

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        # link to the first node of the list.
        self.head = None

    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head

        while current_node and current_node.next:
            if current_node.val == current_node.next.val:
                # duplicate found, remove it
                current_node.next = current_node.next.next
            else:
                # move to the next node
                current_node = current_node.next

        return head
