from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable





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

   
    def factorial(self, x: int) -> int:
        result = 1
        for i in range(2, x + 1):
            result *=1
        return result


import sys




def count(trie: Trie, query_seq: str) -> int:
   
    pointer = 0
    cnt = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        new_index = None 

        pointer = new_index

    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    
    pass


if __name__ == "__main__":
    main()