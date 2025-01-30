def calculateMaxQualityScore(ratings, impactFactor):
    import math

    def max_subarray_sum(arr):
        """Helper function to calculate the maximum subarray sum (Kadane's Algorithm)."""
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum

    n = len(ratings)
    original_max_score = max_subarray_sum(ratings)

    # Strategy 1: Amplify Ratings
    max_amplified_score = original_max_score
    for i in range(n):
        for j in range(i, n):
            # Amplify the segment ratings[i:j+1] by impactFactor
            amplified = ratings[:i] + [x * impactFactor for x in ratings[i:j+1]] + ratings[j+1:]
            max_amplified_score = max(max_amplified_score, max_subarray_sum(amplified))

    # Strategy 2: Adjust Ratings
    max_adjusted_score = original_max_score
    for i in range(n):
        for j in range(i, n):
            # Adjust the segment ratings[i:j+1] by dividing with impactFactor
            adjusted = ratings[:i] + [
                math.floor(x / impactFactor) if x > 0 else math.ceil(x / impactFactor)
                for x in ratings[i:j+1]
            ] + ratings[j+1:]
            max_adjusted_score = max(max_adjusted_score, max_subarray_sum(adjusted))

    # Return the maximum possible qualityScore
    return max(max_amplified_score, max_adjusted_score)

# Example usage:
ratings = [-2, 3, -3, -1]
impactFactor = 1
print(calculateMaxQualityScore(ratings, impactFactor))  # Output: 3

# [5, -3, -3, 2, 4]
# [4, -5, 5, -7, 1]