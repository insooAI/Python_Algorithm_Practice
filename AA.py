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
