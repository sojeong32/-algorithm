king, stone, count = input().split()
dict_dir = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}
king_x = ord(king[0])-65
king_y = int(king[1])-1
stone_x = ord(stone[0])-65
stone_y = int(stone[1])-1
count = int(count)

moves = list(input() for _ in range(count))

while moves:
    x, y = dict_dir[moves.pop(0)]
    king_x = king_x + x
    king_y = king_y + y
    if 0 <= king_x < 8 and 0 <= king_y < 8:
        if (king_x == stone_x) and (king_y == stone_y):
            stone_x = stone_x + x
            stone_y = stone_y + y
            if 0 <= stone_x < 8 and 0 <= stone_y < 8:
                continue
            else:
                stone_x -= x
                stone_y -= y
                if (king_x == stone_x) and (king_y == stone_y):
                    king_x -= x
                    king_y -= y
    else:
        king_x -= x
        king_y -= y

king = chr(king_x + 65) + str(king_y + 1)
stone = chr(stone_x + 65) + str(stone_y + 1)
print(king)
print(stone)