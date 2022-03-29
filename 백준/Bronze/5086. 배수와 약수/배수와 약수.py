import sys

r = sys.stdin.readline

while True:
    prior, end = map(int,r().split())

    if prior == 0 and end == 0:
        break

    if end % prior == 0:
        print('factor')
    elif prior % end == 0:
        print('multiple')
    else:
        print('neither')