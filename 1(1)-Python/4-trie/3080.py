from lib import Trie
import sys


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    # 구현하세요!
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