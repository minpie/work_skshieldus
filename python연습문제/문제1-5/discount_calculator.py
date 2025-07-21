# 초기화:
originalPrice = 0
discountedPrice = 0
discountedAmount = 0
discountRatio = 0
# 입력:
originalPrice = int(input("상품 가격을 입력하세요: "))
discountRatio = float(input("할인율을 입력하세요(%): "))
# 계산:
discountedAmount = originalPrice * discountRatio / 100
discountedPrice = originalPrice - discountedAmount
# 출력:
print("원래 가격: {}원".format(originalPrice))
print("할인율: {}%".format(discountRatio))
print("할인 금액: {}".format(discountedAmount))
print("최종 가격: {}".format(discountedPrice))