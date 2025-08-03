from __future__ import annotations
from collections import deque





def create_circular_queue(n: int) -> deque[int]:
    
    return deque(range(1, n + 1))

def rotate_and_remove(queue: deque[int], k: int) -> int:
   
    queue.rotate(-(k-1))
    return queue.popleft()
    







def simulate_card_game(n: int) -> int:
    
    queue = create_circular_queue(n)
    while len(queue) >1:
        queue.popleft()
        queue.append(queue.popleft())
    return queue[0]

def solve_card2() -> None:
    
    n: int = int(input())
    result: int = simulate_card_game(n)
    print(result)

if __name__ == "__main__":
    solve_card2()