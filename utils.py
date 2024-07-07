async def filter_chapters(lst, start=None, end=None):
    """
    Filter the chapters in the list from a specified start item to an end item.

    Args:
        lst (list): The list containing the items.
        start (int): The chapter number to start from. If not specified, starts from the first item.
        end (int): The chapter number to stop at. If not specified, continues to the end of the list.

    Returns:
        list: A list of filtered items.
    """
    if not lst:
        raise ValueError("The list is empty")

    if start is not None:
        if not isinstance(start, int) or start < 1 or start > len(lst):
            raise ValueError(
                "Invalid start value. It must be a valid chapter number within the list range."
            )
        start_index = start - 1
    else:
        start_index = 0

    if end is not None:
        if not isinstance(end, int) or end < 1 or end > len(lst):
            raise ValueError(
                "Invalid end value. It must be a valid chapter number within the list range."
            )
        if end < start:
            raise ValueError(
                "The end value must be greater than or equal to the start value."
            )
        end_index = end
    else:
        end_index = len(lst)

    filtered_items = []
    for item in lst[start_index:end_index]:

        filtered_items.append(item)
    return filtered_items
