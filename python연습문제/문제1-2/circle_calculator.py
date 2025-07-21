r = 0
area = 0
around = 0
pi = 3.14159
r = int(input("원의 반지름을 입력하세요: "))
area = r * r * pi
around = 2 * r * pi
print("반지름이 {}인 원의 넓이: {}".format(r, round(area, 2)))
print("반지름이 {}인 원의 넓이: {}".format(r, round(around, 2)))
