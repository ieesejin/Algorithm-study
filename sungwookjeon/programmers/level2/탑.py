def solution(heights):
    answer = []
    heights.reverse()
    location = list(range(1, len(heights) + 1))
    location.reverse()
    for i in range(len(heights) - 1):
        for j in range(i + 1, len(heights)):
            if heights[i] < heights[j]:
                answer.append(location[j])
                break
            if j == len(heights) - 1:
                answer.append(0)
        if i == len(heights) - 2:
            answer.append(0)
    answer.reverse()
    return answer
