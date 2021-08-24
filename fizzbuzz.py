# fizzbuzz 1 to 30


for i in range(1, 30 + 1):
# 1부터 30까지 출력하는 반복문
    if i % 3 == 0 or i % 5 == 0:
        print('fizz' * (i % 3 == 0) + 'buzz' * (i % 5 == 0))
# 3의 배수에는 fizz 출력, 5의 배수에는 buzz 출력, 15의 배수에는 fizzbuzz 출력
    else:
        print(i)
# 그 외에는 숫자를 출력
print('-' * 30)
print('finish!')
# 끝!
