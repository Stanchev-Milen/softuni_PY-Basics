#1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
#2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
#3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

number_pages = int(input())
pace = int(input()) #pages per hour
max_days = int(input())

hours_per_day = number_pages / (max_days * pace)

print(int(hours_per_day))