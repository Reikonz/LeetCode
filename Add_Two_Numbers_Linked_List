# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        
        # Resolve the first linked list
        cur_node = l1
        while cur_node is not None:
            num1 = num1 + str(cur_node.val)             
            cur_node = cur_node.next
        
        num1 = ''.join(reversed(num1))        
        
        # Resolve the second linked list
        cur_node = l2
        while cur_node is not None:
            num2 = num2 + str(cur_node.val)             
            cur_node = cur_node.next
        
        num2 = ''.join(reversed(num2))        
        
        # Calculate the sum
        result = str(int(num1) + int(num2))        
                
        # Assemble the linked list    
        node_list = []
        node_count = 0
        for digit in result:
            if node_count == 0:
                node = ListNode(digit, None)
            else:
                node = ListNode(digit, node_list[node_count - 1])
            node_list.append(node)
            node_count = node_count + 1
            
        return node_list[len(node_list)-1]
