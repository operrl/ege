ninetteen = '012345689ABCDEFGIH'

for x in ninetteen:
    expr = int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)
    if expr % 18 == 0:
        print(expr // 18)
        break
