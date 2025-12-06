def max_drone_capacity(weights, k):
    # Convert values like "10theta" → 10
    clean_weights = []
    for w in weights:
        if isinstance(w, (int, float)):
            clean_weights.append(w)
        else:
            # Strip all non-numeric characters
            filtered = "".join(ch for ch in str(w) if ch.isdigit())
            if filtered != "":
                clean_weights.append(int(filtered))

    # Need at least 2 weights
    if len(clean_weights) < 2:
        return -1

    # Sort the numeric weights
    clean_weights.sort()

    left = 0
    right = len(clean_weights) - 1
    max_weight = -1

    # Two-pointer search for best pair under k
    while left < right:
        total = clean_weights[left] + clean_weights[right]

        if total <= k:
            max_weight = max(max_weight, total)
            left += 1
        else:
            right -= 1

    return max_weight
"""Given a list of drone weights (which may include non-numeric characters)
    and a maximum weight limit k, return the maximum combined weight of two drones
    that does not exceed k. If no such pair exists, return -1."""

#EXAPLE USAGE:
weights = [10, "20kg", 15, "5lbs", "30units"]
k = 35
print(max_drone_capacity(weights, k))  # Output: 35