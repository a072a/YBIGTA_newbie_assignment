from __future__ import annotations
from collections import deque





def create_circular_queue(n: int) -> deque[int]:
    
    return deque(range(1, n + 1))

def rotate_and_remove(queue: deque[int], k: int) -> int:
    
    queue.rotate(-(k-1))
    return queue.popleft()
    







def josephus_problem(n: int, k: int) -> list[int]:
    
    queue = create_circular_queue(n)
    result: list[int] = []
    
    while queue:
        eliminated = rotate_and_remove(queue, k)
        result.append(eliminated)
    
    return result

def solve_josephus() -> None:
    
    n: int
    k: int
    n, k = map(int, input().split())
    result: list[int] = josephus_problem(n, k)
    
   
    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    solve_josephus()