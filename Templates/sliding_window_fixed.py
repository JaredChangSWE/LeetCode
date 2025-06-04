def checkInclusion(input: list[int], window_size: int) -> bool:
    
    left = 0
    window = []

    for right in range(len(input)):
        right_element = input[right]
        window.append(right_element)
        
        if optimal(window):
            return True
        
        left_element = input[left]
        window.remove(left_element)
        left += 1

    return False