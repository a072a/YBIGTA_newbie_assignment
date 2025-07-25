from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    """
    SegmentTree 구현 클래스

    Attributes:
        -n (int): 원본 배열의 길이
        -tree (list[int]): 구간 합 정보를 저장하는 세그먼트 트리 배열
    Methods:
        -query(l: int, r: int) -> int:
            인덱스 1부터 r까지의 원소들의 합을 반환
        -update(idx: int, value: int) -> None:
            주어진 index의 값을 새로운 값으로 바꾸고 트리를 다시 저장
    """
    # 구현하세요!
    def __init__(self, data: list[int]):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self._build(data, 1, 0, self.n-1)

    def _build(self, data: list[int], node: int, start: int, end: int):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) //2
            self._build(data, 2 * node, start, mid)
            self._build(data, 2 * node + 1, mid + 1, end)
            self.tree[node]=self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, l: int, r: int) -> int:
        def rec(node: int, start: int, end: int) -> int:
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return self.tree[node]
            mid = (start + end)//2
            left = rec(2 * node, start, mid)
            right = rec(2 * node+1, mid+1,end)
            return left + right
        return rec(1,0,self.n-1)
    
    def update(self, idx: int, value: int) -> None:
        def rec(node: int, start: int, end: int) -> None:
            if start == end:
                self.tree[node] = value
            else: 
                mid = (start + end)//2
                if idx <= mid:
                    rec(2*node, start, mid)
                else:
                    rec(2* node +1, mid +1, end)
                self.tree[node] = self.tree[2* node]+ self.tree[2* node +1]
        rec(1,0,self.n-1)


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