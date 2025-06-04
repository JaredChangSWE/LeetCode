def sliding_window_flexible_shortest(input):
    window = []
    anwser = 0
    left = 0
    for right in range(len(input)):
        window.append(input[right])
        while valid(window):
            anwser = min(anwser, window)      # window is guaranteed to be valid here
            window.remove(input[left])
            left += 1
    return anwser
