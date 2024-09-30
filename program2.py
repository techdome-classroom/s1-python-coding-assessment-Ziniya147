def decode_message(secret: str, pattern: str) -> bool:
    # Initialize a DP table with dimensions (len(secret) + 1) x (len(pattern) + 1)
    dp = [[False] * (len(pattern) + 1) for _ in range(len(secret) + 1)]
    
    # Empty pattern matches empty secret
    dp[0][0] = True

    # Handle patterns that start with '*'
    for j in range(1, len(pattern) + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
    for i in range(1, len(secret) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] == secret[i - 1] or pattern[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    return dp[len(secret)][len(pattern)]



