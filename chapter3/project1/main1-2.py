"""
랜덤 숫자를 추출해서 사용자가 숫자를 맞추는 게임
"""
import random

random_number = random.randint(1, 100)

game_count = 1

while True:
    try:
        my_number = int(input("1~100 사이의 숫자를 입력하세요:"))

        if my_number > random_number:
            print("다운")
        if my_number < random_number:
            print("업")
        elif my_number == random_number:
            print(f"축하합니다. {game_count}회 만에 맞췄습니다.")
            break

        game_count = game_count+1
    except:
        print("숫자를 입력해주세요!!!")