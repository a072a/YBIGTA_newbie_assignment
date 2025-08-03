from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        action: trie에 seq을 저장하기
        Args: 
            -seq (Iterable[T]): T의 열

        """
        # 구현하세요!
        current = 0
        for item in seq:
            for child_idx in self[current].children:
                if self[child_idx].body == item:
                    current = child_idx
                    break
            else:
                self.append(TrieNode(body=item))
                new_idx = len(self) - 1
                self[current].children.append(new_idx)
                current = new_idx
        self[current].is_end = True

    # 구현하세요!
    def factorial(self, x: int) -> int:
        result = 1
        for i in range(2, x + 1):
            result *=1
        return result