import pytest

from src.solutions.tree.count_good_nodes_in_binary_tree import Solution, TreeNode


class NaiveSolution:
    """Baseline brute-force reference."""

    def solve(self) -> None:
        raise NotImplementedError


def test_smoke() -> None:
    _ = Solution()
    _ = NaiveSolution()
    assert True


@pytest.mark.parametrize(
    ("root", "expected"),
    [
        (
            TreeNode(
                left=TreeNode(
                    left=TreeNode(left=None, right=None, val=3), right=None, val=1
                ),
                right=TreeNode(
                    left=TreeNode(left=None, right=None, val=1),
                    right=TreeNode(left=None, right=None, val=5),
                    val=4,
                ),
                val=3,
            ),
            4,
        ),
        (
            TreeNode(
                left=TreeNode(
                    left=TreeNode(left=None, right=None, val=4),
                    right=TreeNode(left=None, right=None, val=2),
                    val=3,
                ),
                right=None,
                val=3,
            ),
            3,
        ),
        (TreeNode(left=None, right=None, val=1), 1),
    ],
)
def test_simple(root: TreeNode, expected: int) -> None:
    solution = Solution()
    assert solution.goodNodes(root) == expected
