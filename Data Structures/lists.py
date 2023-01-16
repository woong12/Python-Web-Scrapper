days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# Lists

print(days_of_week[2])
print(days_of_week)

# list에 value을 추가할 수가 있다
days_of_week.append("Sat")
print(days_of_week)
days_of_week.append("Sun")
print(days_of_week)

# list에 특정 value을 없엘 수가 있다
days_of_week.remove("Sun")
print(days_of_week)

# list의 value들을 앞뒤 순서 바꿔버린다
days_of_week.reverse()
print(days_of_week)

# list의 특정value가 몇개 있는지 알려준다
print(days_of_week.count("Mon"))

# list에있는 모든 value들을 없엔다
days_of_week.clear()
print(days_of_week)
