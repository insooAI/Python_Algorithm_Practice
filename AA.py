**대표값 구하기**  
- 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램  
- 평균과 가장 가까운 점수가 여러 개일 경우, 평균과 먼저 점수가 높은 학생의 번호를 출력  
- 만약 높은 점수를 가진 학생이 여러 명일 경우, 평균과 그 중 학생번호가 빠른 학생의 번호를 출력


import sys
# sys.stdin = open('input.txt','rt')

number = int(input())
score = list(map(int, input().split()))  

mean = sum(score) / number
mean = int(mean+0.5)


r_score = []
index = []
epsilon_ls = []

epsilon = 100

for i in range(number):
    if abs(score[i] - mean) <= epsilon:
        epsilon = abs(score[i] - mean)
        epsilon_ls.append(epsilon)
        r_score.append(score[i])
        index.append(i)

s = r_score[-1]

for x in r_score:
    if (x== max(r_score)) & (epsilon_ls[r_score.index(x)] == min(epsilon_ls)) :
        print(mean, index[r_score.index(x)]+1)
        break

else:
    print(mean, index[r_score.index(s)]+1)
