records = []
scores = []
people = []
firstMin = 0
time = 0

for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score]) #Değerleri ikili olarak kaydediyorum.

for i in range(len(records)):
    scores.append(records[i][1]) #Sadece skor değerlerini bir listeye kaydediyorum.

scores.sort() #Skor değerlerini büyükten küçüğe sıralıyorum.

for i in range(len(scores)-1): 
    if scores[i] < scores[i+1]: #En küçük değerden sonra gelen ilk büyük değeri yani ikinci küçük değeri buluyorum.
        firstMin = scores[i+1] 
        break #Döngünün daha fazla çalışmasını istemiyorum çünkü istediğimi buldum

for i in scores:
    if i == firstMin: #En küçük ikinci değer kaç kere tekrar ediyor diye kontrol ediyor.
        time += 1

if time > 1:
    for i in range(len(records)):
        if records[i][1] == firstMin:
            people.append(records[i][0]) 

people.sort()

if time == 1:
    for i in range(len(records)):
        if records[i][1] == firstMin:
            print(records[i][0])
elif time !=1:
    for i in range(len(people)):
        print(people[i]) 