from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable




T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    
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





def main() -> None:
   
    pass


if __name__ == "__main__":
    main()