#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
#1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]
#2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
#3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]

deposit = float(input())
deposit_time = int(input())
yearly_interest = float(input()) / 100

sum = deposit + deposit_time * ((deposit * yearly_interest) / 12)

print(sum)
