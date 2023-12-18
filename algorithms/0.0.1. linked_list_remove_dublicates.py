# Remove Duplicates from Sorted List

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        # Link to the first node of the list.
        self.head = None

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head

        while current_node and current_node.next:
            if current_node.val == current_node.next.val:
                # Duplicate found, remove it
                current_node.next = current_node.next.next
            else:
                # Move to the next node
                current_node = current_node.next

        return head
