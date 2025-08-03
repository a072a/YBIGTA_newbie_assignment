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