n = int(input())
arr = map(int, input().split())

skorlar = list(arr)
skorlar.sort(reverse=True)

for i in range(n-1):
    if skorlar[i] > skorlar[i+1]:
        print(skorlar[i+1])
        print(i+1)
        break