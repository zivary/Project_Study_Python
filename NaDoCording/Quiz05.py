# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정행집니다.
# 조건2: 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 :15분)
# [ ] 2번째 손님 (소요시간 :50분)
# [O] 3번째 손님 (소요시간 :5분)
# ...
# [ ] 1번째 손님 (소요시간 :16분)

# 총 탑승 승객 : 2분

from random import *
cnt = 0  # 총 탑승 승객 수
for i in range(1, 51):  # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 50)  # 5분 ~ 50분 소요시간 랜덤으로 설정(random range)
    if time >= 5 and time <= 15:  # 매칭 성공 - 5분 ~ 15분 이내의 손님, 팁승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:  # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("--------------------")
print("총 탑승 승객 : {}명".format(cnt))