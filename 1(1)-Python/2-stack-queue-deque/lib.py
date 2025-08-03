from __future__ import annotations
from collections import deque


"""
TODO:
- rotate_and_remove 구현하기 
"""


def create_circular_queue(n: int) -> deque[int]:
    """1부터 n까지의 숫자로 deque를 생성합니다."""
    return deque(range(1, n + 1))

def rotate_and_remove(queue: deque[int], k: int) -> int:
    """
    큐를 왼쪽으로 회전한 뒤, k번째 원소를 제거하여 반환

    Args:
        - queue(deque[int]): 정수로 구성된 deque
        - k (int): 제거할 원소의 순서
    Returns:
        - int: 제거된 원소의 값
    """
    # 구현하세요!
    queue.rotate(-(k-1))
    return queue.popleft()
    