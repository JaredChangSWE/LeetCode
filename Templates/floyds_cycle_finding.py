def hasCycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False
    
    slow = fast = head

    while True :
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    return True