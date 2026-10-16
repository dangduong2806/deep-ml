def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    if len(values) == 0:
        return []
    
    dct = {}
    for i, v in enumerate(order):
        dct[v] = i
    
    ordinal_category = []
    for v in values:
        if dct.get(v) is not None:
            ordinal_category.append(dct.get(v))
        else:
            ordinal_category.append(-1)
    
    return ordinal_category
    