class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def addTwoNumbers(l1, l2):
        answer = ListNode()
        answer.next = Solution.add_dem3(l1, l2, answer)
        return answer.next


    @staticmethod
    def add_dem3(a, b, answer):
        ans_head = answer
        while a is not None and b is not None:
            ans = a.val + b.val

            if ans > 9:
                carry = int(ans / 10)
                ans = ans % 10
                if a.next is None:
                    a.next = ListNode(carry)
                else:
                    a.next.val += 1
            answer.next = ListNode(ans)
            answer = answer.next
            if a.next is None:
                if b.next is None:
                    break
                a = ListNode()
                b = b.next
            elif b.next is None:
                if a.next is None:
                    break
                b = ListNode()
                a = a.next
            else:
                a = a.next
                b = b.next
        return ans_head.next





list1 = ListNode(2, ListNode(4, ListNode(3)))
list2 = ListNode(5, ListNode(6, ListNode(4, ListNode(1))))

sol = Solution.addTwoNumbers(l1=list1, l2=list2)
print (sol)

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        answer.next = Solution.add_dem3(l1, l2, answer)
        return answer.next

    @staticmethod
    def add_dem3(a, b, answer):
        ans_head = answer
        while a is not None and b is not None:
            ans = a.val + b.val

            if ans > 9:
                carry = int(ans / 10)
                ans = ans % 10
                if a.next is None:
                    a.next = ListNode(carry)
                else:
                    a.next.val += 1
            answer.next = ListNode(ans)
            answer = answer.next
            if a.next is None:
                if b.next is None:
                    break
                a = ListNode()
                b = b.next
            elif b.next is None:
                if a.next is None:
                    break
                b = ListNode()
                a = a.next
            else:
                a = a.next
                b = b.next
        return ans_head.next


'''