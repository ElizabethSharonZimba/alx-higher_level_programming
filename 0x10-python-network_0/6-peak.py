def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers using binary search.

    Args:
        list_of_integers (list): List of integers to find peak from.

    Returns:
        int or None: Peak of list_of_integers or None if list is empty.
    """

    size = len(list_of_integers)

    # Check if the list is empty
    if size == 0:
        return None

    left = 0
    right = size - 1

    while left < right:
        mid = (left + right) // 2

        # Compare mid element with its neighbors
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    # At this point, left == right == peak index
    return list_of_integers[left]

