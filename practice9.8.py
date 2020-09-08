import random

deck = []

# num과 shape 정의
shapes = '♥♣♠◆'
nums = []
for i in range(2,11):
    nums.append(str(i))
for c in 'JQKA':
    nums.append(c)

# 덱 만들기
for shape in shapes:
    for num in nums:
        deck.append((shape, num))

deck.append(('Joker', 'black'))
deck.append(('Joker', 'colored'))
random.shuffle(deck)

# 플레이어에게 카드 나누기

player = []
computer = []

for i in range(7):
    player.append(deck.pop())
    computer.append(deck.pop())

# 낸 카드에 하나 올려놓기
put = []
put.append(deck.pop())

    
# 게임 시작
while True:

    # 플레이어의 차례
    print("플레이어의 차례입니다.")
    print("현재 패 >>", player)
    print("놓여진 카드 >>", put[-1])

    # 가능한 카드
    available = []
    for card in player:
        if (card[0] == put[-1][0]
            or card[1] == put[-1][1]
            or card[0] == 'Joker'
            or put[-1][0] == 'Joker'):
            available.append(card)
        
    print("낼 수 있는 카드:", available)

    # 낼 수 있는 카드가 있는 경우
    if len(available) > 0:
        i = int(input("몇 번째 카드를 내시겠습니까?"))
        i -= 1
        selected = available[i]
        player.remove(selected)
        put.append(selected)

    # 낼 수 있는 카드가 없는 경우
    else:
        print("낼 수 있는 카드가 없어 먹습니다.")
        player.append(deck.pop())

    if len(player) == 0:
        print("플레이어가 이겼습니다!")
        break

    # 컴퓨터의 차례
    print("컴퓨터의 차례입니다.")
    print("놓여진 카드 >>", put[-1])

    # 가능한 카드
    available = []
    for card in computer:
        if (card[0] == put[-1][0]
            or card[1] == put[-1][1]
            or card[0] == 'Joker'
            or put[-1][0] == 'Joker'):
            available.append(card)

    # 낼 수 있는 카드가 있는 경우
    if len(available) > 0:
        selected = random.choice(available)
        computer.remove(selected)
        put.append(selected)
        print("컴퓨터가", selected, "를 냈습니다.")

    # 낼 수 있는 카드가 없는 경우
    else:
        print("낼 수 있는 카드가 없어 먹습니다.")
        computer.append(deck.pop())

    if len(computer) == 0:
        print("컴퓨터가 이겼습니다!")
        break