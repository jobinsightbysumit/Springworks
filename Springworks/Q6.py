def max_ads(timestamps, k):
    # Convert values like "10theta" → 10
    clean = []
    for t in timestamps:
        if isinstance(t, (int, float)):
            clean.append(t)
        else:
            # remove non-digit characters
            digits = "".join(ch for ch in str(t) if ch.isdigit())
            if digits:
                clean.append(int(digits))

    # Sort timestamps (problem states sorted, but ensure safety)
    clean.sort()

    # No timestamps? No ads.
    if not clean:
        return 0

    count = 1        # always place an ad at the first timestamp
    last_ad = clean[0]

    # Greedy selection of next ads
    for t in clean[1:]:
        if t - last_ad >= k:
            count += 1
            last_ad = t

    return count

# Example usage:
timestamps = [0, "10theta", 20, "25alpha", 30, 40]
k = 10      
print(max_ads(timestamps, k))  # Output: 5  
"""Given a list of timestamps (which may include non-numeric characters)
    and a minimum interval k, return the maximum number of ads that can be placed
    such that no two ads are less than k time units apart."""           
"""Given a list of timestamps (which may include non-numeric characters)
    and a minimum interval k, return the maximum number of ads that can be placed
    such that no two ads are less than k time units apart."""

