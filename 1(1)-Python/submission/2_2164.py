from __future__ import annotations
from collections import deque


"""
TODO:
- rotate_and_remove �����ϱ� 
"""


def create_circular_queue(n: int) -> deque[int]:
    """1���� n������ ���ڷ� deque�� �����մϴ�."""
    return deque(range(1, n + 1))

def rotate_and_remove(queue: deque[int], k: int) -> int:
    """
    ť���� k��° ���Ҹ� �����ϰ� ��ȯ�մϴ�.
    """
    # �����ϼ���!
    queue.rotate(-(k-1))
    return queue.popleft()
    




"""
TODO:
- simulate_card_game �����ϱ�
    # ī�� ���� �ùķ��̼� ����
        # 1. ť ����
        # 2. ī�尡 1�� ���� ������ �ݺ�
        # 3. ������ ���� ī�� ��ȯ
"""


def simulate_card_game(n: int) -> int:
    """
    ī��2 ������ �ùķ��̼��Ͽ� ���������� ���� ī�带 ��ȯ
    
    Args:
        - n (int): ī���� ����
    Returns:
        - int: ���������� ���� ī�� ��ȣ
    """
    # �����ϼ���!
    queue = create_circular_queue(n)
    while len(queue) >1:
        queue.popleft()
        queue.append(queue.popleft())
    return queue[0]

def solve_card2() -> None:
    """��, ��� format"""
    n: int = int(input())
    result: int = simulate_card_game(n)
    print(result)

if __name__ == "__main__":
    solve_card2()