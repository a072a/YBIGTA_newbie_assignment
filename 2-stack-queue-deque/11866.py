from lib import create_circular_queue, rotate_and_remove


"""
TODO:
- josephus_problem 구현하기
    # 요세푸스 문제 구현
        # 1. 큐 생성
        # 2. 큐가 빌 때까지 반복
        # 3. 제거 순서 리스트 반환
"""


def josephus_problem(n: int, k: int) -> list[int]:
    """
    요세푸스 문제를 시뮬레이션하여 제거되는 사람들의 순서를 반환

    Args:
        - n (int): 원형으로 앉아 있는 사람의 수
        - k (int): k번째 사람을 제거
    Returns:
        - list[int]:제거된 사람의 번호 순서를 담은 리스트
    """
    # 구현하세요!
    queue = create_circular_queue(n)
    result: list[int] = []
    
    while queue:
        eliminated = rotate_and_remove(queue, k)
        result.append(eliminated)
    
    return result

def solve_josephus() -> None:
    """입, 출력 format"""
    n: int
    k: int
    n, k = map(int, input().split())
    result: list[int] = josephus_problem(n, k)
    
    # 출력 형식: <3, 6, 2, 7, 5, 1, 4>
    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    solve_josephus()