"""
Challenge 1: Backtracking (The "State Cleanup" Test)

Problem: The Power Set with Constraints
Write a function `generateSubsets(int[] nums, int target)` that finds all unique subsets of an array that sum up to a specific target.

    The Constraint: You cannot use the same element twice, and your result must not contain duplicate subsets.

    The Mastery Test: You must use a single List or Array to track your "current path." You must add an element, recurse, and then explicitly remove that element (the cleanup) before the next iteration.

    Why this is hard: If you don't clean up the state correctly, your subsequent recursive branches will inherit "garbage" from previous attempts.
"""


"""
Finds all unique subsets that sum to the target.
:param nums: List[int] - The input numbers (may contain duplicates)
:param target: int - The target sum
:return: List[List[int]] - All unique combinations
"""
def find_subsets(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()  # Sort to handle duplicates and enable early termination
    results = []
    current_path = []  # Single list — mutated and cleaned up as we go

    def backtrack(start: int, remaining: int):
        # Base case: found a valid subset
        if remaining == 0:
            results.append(list(current_path))  # Snapshot, not a reference
            return

        for i in range(start, len(nums)):
            # Skip duplicates at the same recursion level
            if i > start and nums[i] == nums[i - 1]:
                continue

            # Early termination: array is sorted, so no point continuing
            if nums[i] > remaining:
                break

            current_path.append(nums[i])   # ADD
            backtrack(i + 1, remaining - nums[i])  # RECURSE
            current_path.pop()             # REMOVE (state cleanup)

    backtrack(0, target)
    return results

# --- TEST CASES ---
def run_tests():
    test_cases = [
        {"nums": [1, 2, 3, 7], "target": 10, "expected": [[1, 2, 7]]},
        {"nums": [10, 1, 2, 7, 6, 1, 5], "target": 8, "expected": [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]},
        {"nums": [2, 4, 6], "target": 5, "expected": []},
        {"nums": [1, 2, 3], "target": 0, "expected": [[]]}
    ]

    for i, test in enumerate(test_cases, 1):
        actual = find_subsets(test["nums"], test["target"])
        # Sorting results to ensure comparison works regardless of order
        actual_sorted = sorted([sorted(x) for x in actual])
        expected_sorted = sorted([sorted(x) for x in test["expected"]])

        status = "PASS" if actual_sorted == expected_sorted else "FAIL"
        print(f"Test {i}: {status}")
        print(f"   Expected: {test['expected']}")
        print(f"   Actual:   {actual}\n")


if __name__ == "__main__":
    run_tests()