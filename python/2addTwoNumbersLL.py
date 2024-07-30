# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            #get values
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            #calculate sum
            total = x + y + carry
            carry = total // 10
            digit = total % 10

            #create new node
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next  


# Helper function to convert a linked list to a list of values
def linked_list_to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

# Test the solution
solution = Solution()

# Test case: 342 + 465 = 807
l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])

result = solution.addTwoNumbers(l1,l2)
print(linked_list_to_list(result))      
