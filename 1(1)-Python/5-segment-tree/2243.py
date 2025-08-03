from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    """
    사탕 정보를 SegmentTree를 이용하여 처리하는 함수

    1 b: b번째 사탕을 꺼내 출력하고 그 수를 1 줄임
    2 b c: 맛이 b인 사탕을 c개 추가 or 제거
    """
    # 구현하세요!
    input = sys.stdin.readline
    MAX = 1000000
    tree: SegmentTree = SegmentTree([0]*(MAX+1))

    n=int(input())
    for _ in range(n):
        command = list(map(int, input().split()))

        if command[0] == 1:
            b = command[1]
            left, right = 1, MAX
            while left < right:
                mid = (left + right) //2
                if tree.query(1, mid)>=b:
                    right = mid
                else:
                    left = mid+1
            print(left)
            tree.update(left, tree.query(left,left) -1)

        elif command[0] ==2:
            b,c = command[1],command[2]
            current = tree.query(b,b)
            tree.update(b, current +c)
    


if __name__ == "__main__":
    main()