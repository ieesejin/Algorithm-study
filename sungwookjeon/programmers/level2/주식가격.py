def solution(prices):
    answer = []
    # while True:
    #     count = 0
    #     for i in range(index + 1, len(prices)):
    #         if prices[index] <= prices[i]:
    #             count += 1
    #     answer.append(count)
    #     index += 1
    #     if index == len(prices):
    #         return answer
    for i in range(len(prices) - 1):
        count = 0
        for j in range(i + 1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
    answer.append(0)
    return answer
