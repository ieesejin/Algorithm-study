def solution(participant, completion):
    answer = ''
    same_name = 1
        
    for name in participant:
        name.lower()
    for name in completion:
        name.lower()
 
    for i in participant:
        if i not in completion:
            answer = i
        elif (participant.count(i) >= 1) and (participant.count(i) > completion.count(i)):
            answer = i
        else:
            continue
            
    return answer
