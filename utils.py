from itertools import combinations


def filter_above(number_in_text, target_number):
    """If a number is greater than target_number we don't even have to see it because we don't have any negative"""
    return [n for n in number_in_text if n <= target_number]


def find_k_sum_backtrack(nums, target, k):
    """
    Returns all unique k-tuples from nums that sum to target.
    Uses sorting and backtracking to prune branches early.
    """
    results = []

    def backtrack(start, k_remain, target_remain, path):
        # Base case: found k numbers that sum exactly
        if k_remain == 0 and target_remain == 0:
            results.append(tuple(path))
            return
        # If no more picks or target impossible, prune
        if k_remain == 0 or target_remain < 0:
            return

        for i in range(start, len(nums)):
            # skip duplicates at the same depth
            if i > start and nums[i] == nums[i-1]:
                continue
            # prune if the smallest possible sum is already too big
            if nums[i] * k_remain > target_remain:
                break
            # prune if the largest possible sum is still too small
            if nums[-1] * k_remain < target_remain:
                break

            # choose nums[i]
            backtrack(i+1, k_remain-1, target_remain - nums[i], path + [nums[i]])

    backtrack(0, k, target, [])
    return results


def find_k_sum_combinations(nums, target, k):
    """
    Returns all k-tuples from nums that sum to target.
    Suitable when len(nums) and k are both fairly smalll.
    """
    return [
        tuple(comb)
        for comb in combinations(nums, k)
        if sum(comb) == target
    ]

