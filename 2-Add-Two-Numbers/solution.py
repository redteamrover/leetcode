"""LeetCode Problem 2 - Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
"""

from typing import Optional, TypeVar

from pytest import fixture


T = TypeVar("T")


class ListNode:

    def __init__(self, value: T, next_node: Optional['ListNode'] = None) -> None:
        self.value = value
        self.next = next_node


def get_number_from_list(head: Optional[ListNode]) -> int:
    # This is the number we will eventually return.
    number = 0

    # Since the number is given to us in reverse order, we need to keep track
    # of the number of digits we have processed in order to increment the value
    # of the number by the proper amount.
    place_value = 0

    # Define our iterator.
    current = head

    while current:
        # The value of the current digit we are on is the value of the digit
        # multiplied by ten times the place value we are on.
        i = current.value * (10**place_value)

        # Increment the number by the current value.
        number += i

        # Increment the place value every time we process a number.
        place_value += 1

        # Move on to the next node in the list.
        current = current.next
    
    # Finally, return the number.
    return number


def make_list_from_number(n: int) -> ListNode:
    """Make Linked List From Number

    This function accepts an integral argument from which a linked list is
    made. This linked list is a reversed representation of the number, with the
    head of the linked list containing a reference to the number's last digit.
    """
    head = None

    while True:
        # The first thing we need to check for is whether the head of the
        # linked list is null. If we instead opted for checking whether n is
        # equal to zero first, we would return from the function with a null
        # head node, thereby triggering a segmentation fault, or whatever it is
        # that Python does.
        if head is None:
            x = n % 10
            head = ListNode(x)
            current = head
            n = n // 10
            continue
        
        # If n equals zero, we have already finished adding all of its digits
        # to the linked list, so we can simply break out of the loop here.
        if not n:
            break
        
        # Reversing a number's digits is as easy as getting the remainder when
        # dividing by ten, and using that as the next value in the list.
        x = n % 10

        # Once we've done that, we simply divide the number by ten until we
        # collected all of the digits in reverse order. Note that we use floor
        # division (meaning the end result is truncated) in order to prevent
        # integral type coercion to floating point.
        n = n // 10

        # We add the current digit to the list by creating a list node as the
        # next node of the currently referenced list node.
        current.next = ListNode(x)

        # Once the next node has been initialized and appended, we increment
        # our list node iterator to reference the last node in the list.
        current = current.next

    # The linked list contains the digits in reversed order, so now all we need
    # to do is return the head of the list.
    return head


def make_list_from_array(digits: ListNode) -> ListNode:
    """Make Linked List From Array

    This function is a utility function to allow for testing LeetCode test
    cases via the same interface.

    Note that this function expects the digits array to contain the reversed
    digits of a number, as is the case on the test cases online.
    """
    head = None
    current = None

    for digit in digits:
        if head is None:
            head = ListNode(digit)
            current = head
            continue
        
        current.next = ListNode(digit)
        current = current.next
    
    return head


def add_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    a = get_number_from_list(l1)
    b = get_number_from_list(l2)
    return make_list_from_number(a + b)


@fixture
def list_342() -> ListNode:
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    return head


def test_get_number_from_list(list_342: ListNode) -> None:
    assert get_number_from_list(list_342) == 342


def test_make_list_from_number() -> None:
    assert get_number_from_list(make_list_from_number(342)) == 342


def test_make_list_from_array() -> None:
    assert get_number_from_list(make_list_from_array([2, 4, 3])) == 342
