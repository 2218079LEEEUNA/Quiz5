class 붕어빵 : #붕어빵 타이쿤 실습 과제 붕어빵 클래스 만들기
    total = 0
    def __init__(self, contents, price):
        self.contents = contents
        self.price = price
        self.total = 0
    def sell(self):
        self.total += self.price
        print(f"{self.contents} 붕어빵을 {self.price}원에 팔았습니다.")
    def eat(self):
        print(f"{self.contents} 붕어빵을 먹는다")

슈크림_붕어빵 = 붕어빵("슈크림",2000)
팥_붕어빵 = 붕어빵("팥",3000)


슈크림_붕어빵.sell() #보너스 추가점수부분
슈크림_붕어빵.eat()
팥_붕어빵.sell()
팥_붕어빵.eat()

print((슈크림_붕어빵.total) + (팥_붕어빵.total))
