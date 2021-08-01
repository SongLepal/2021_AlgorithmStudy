# chapter3 - Greedy
# 예제 3-1
# hi kk
'''
# 문제 :
손님에게 거슬러 줘야 할 돈이 N원일 때, 거슬러줘야 할 동전의 최소 개수를 구하라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수.

# 풀이 :
가장 큰 화폐 단위부터 돈을 거슬러 주자.
'''

n = 1260    # 거슬러 줘야 할 돈 N
count = 0    # 최소 동전 개수

coin_types = [500, 100, 50, 10]    # 화폐 단위

for coin in coin_types:
    count += n // coin    # 해당 화폐로 거슬러 줄 수 있는 동전 개수
    n %= coin    # 해당 화폐로 거슬러 주고 남은 돈

print(count)
