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





def main() -> None:
   
    sys.setrecursionlimit(10**6)
    trie = Trie[int]()
    n = int(sys.stdin.readline())

    for _ in range(n):
        word = sys.stdin.readline().strip()
        trie.push([ord(ch) for ch in word])
    
    factorial = [1] * (n + 1)
    for i in range(2, n + 1):
        factorial[i]= factorial[i-1]*i
                 

    def count_cases(idx: int) -> int:
        total = 1
        child_counts = 0
        for child_idx in trie[idx].children:
            subtotal = count_cases(child_idx)
            total *= subtotal
            child_counts += 1
        total *= trie.factorial(child_counts)
        return total
    
    print(count_cases(0))


if __name__ == "__main__":
    main()