# lib.py의 Matrix 클래스를 참조하지 않음
import sys


"""
TODO:
- fast_power 구현하기 
"""


def fast_power(base: int, exp: int, mod: int) -> int:
    """
    분할 정복 알고리즘을 이용하여 거듭제곱된 수의 나머지를 빠르게 계산
    
    Args:
        - base (int): 밑
        - exp (int): 지수
        - mod (int): 나머지를 계산할 수
    Returns:
        - int: % mod의 결과(나머지) 
    """
    # 구현하세요!
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2, mod)
    if exp % 2 == 0:
        return (half*half) % mod
    else:
        return (half*half*base) % mod

def main() -> None:
    A: int
    B: int
    C: int
    A, B, C = map(int, input().split()) # 입력 고정
    
    result: int = fast_power(A, B, C) # 출력 형식
    print(result) 

if __name__ == "__main__":
    main()
