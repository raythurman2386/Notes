def reverse_list(head):
    prev = None
    cur = head

    while cur is not None:
        old_next = cur.old_next

        cur.next = prev  # reverse the pointer

        prev = cur    
        cur = old_next

    return prev