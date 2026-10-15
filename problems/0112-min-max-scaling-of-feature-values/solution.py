def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    n = len(x)
    max_value = max(x)
    min_value = min(x)
    for i in range(0, n):
        x[i] = (x[i] - min_value) / (max_value - min_value)
    
    return x