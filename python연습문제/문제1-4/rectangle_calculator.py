# 초기화:
width = 0
height = 0
area = 0
around = 0
# 입력:
width = float(input("가로 길이를 입력하세요: "))
height = float(input("세로 길이를 입력하세요: "))
# 계산:
area = width * height
around = 2 * (width + height)
# 출력:
print("직사각형의 넓이: {}".format(area))
print("직사각형의 둘레: {}".format(around))