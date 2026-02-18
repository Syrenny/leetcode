from typing import Iterable, Optional

import pytest

from src.solutions.linked_list.merge_two_sorted_lists import ListNode, Solution


def build_list(values: Iterable[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    tail: Optional[ListNode] = None

    for v in values:
        node = ListNode(val=v)
        if head is None:
            head = node
            tail = node
        else:
            assert tail is not None
            tail.next = node
            tail = node

    return head


def to_pylist(head: Optional[ListNode], *, limit: int = 10_000) -> list[int]:
    out: list[int] = []
    steps = 0
    cur = head
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
        steps += 1
        assert steps <= limit, "List is too long; possible cycle."
    return out


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("list1", "list2", "expected"),
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([2, 2], [1, 2], [1, 2, 2, 2]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
    ],
)
def test_merge_two_lists(
    list1: list[int], list2: list[int], expected: list[int]
) -> None:
    solution = Solution()
    result = solution.mergeTwoLists(build_list(list1), build_list(list2))
    assert to_pylist(result) == expected
