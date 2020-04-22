N = int(input())
applicant = list(map(int, input().split()))
B, C = map(int, input().split())

new_list = [1] * N
for i in range(0, len(applicant)):
    applicant[i] -= B
    if applicant[i] < 0:
        applicant[i] = 0
for i in range(0, len(applicant)):
    new_list[i] += int(applicant[i] / C)
    applicant[i] = applicant[i] % C
while sum(applicant) != 0:
    for i in range(0, len(applicant)):
        if applicant[i] == 0:
            continue
        if applicant[i] > C:
            new_list[i] += int(applicant[i] % C)
        if applicant[i] == C or applicant[i] < C:
            new_list[i] += 1
            applicant[i] = 0
print(sum(new_list))
