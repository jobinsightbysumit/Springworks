def maxDroneCapacity(weights, K):
    # Convert values like "10theta" → 10
    clean = []
    for w in weights:
        if isinstance(w, (int, float)):
            clean.append(w)
        else:
            digits = "".join(ch for ch in str(w) if ch.isdigit())
            if digits:
                clean.append(int(digits))

    # If fewer than 2 valid weights, no pair possible
    if len(clean) < 2:
        return -1

    # Sort weights for two-pointer method
    clean.sort()

    left = 0
    right = len(clean) - 1
    max_weight = -1

    while left < right:
        total = clean[left] + clean[right]

        if total <= K:
            max_weight = max(max_weight, total)
            left += 1   # try a bigger value
        else:
            right -= 1  # reduce the sum

    return max_weight
# Example usage:
weights = [10, "20kg", 15, "5lbs", "30units"]
K = 35      
print(maxDroneCapacity(weights, K))  # Output: 35
"""Given a list of drone weights (which may include non-numeric characters) 
    and a maximum weight limit K, return the maximum combined weight of two drones
    that does not exceed K. If no such pair exists, return -1."""   