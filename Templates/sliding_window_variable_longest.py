def sliding_window_flexible_longest(input):
    anwser = 0
    window = []

    left = 0

    for right in range(len(input)):
        window.append(input[right])
        while invalid(window):        # update left until window is valid again
            window.remove(input[left])
            left += 1
        anwser = max(anwser, optimal(window))        # window is guaranteed to be valid here

    return anwser
