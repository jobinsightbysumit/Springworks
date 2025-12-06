def complete_levels(n):
    level = 1
    completed = 0

    while n >= level:
        n -= level       # use required battery packs
        completed += 1   # level completed
        level += 1       # next level needs more packs

    return completed
# Example usage:
n = 10  
print(complete_levels(n))  # Output: 4