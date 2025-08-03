
import sys





def fast_power(base: int, exp: int, mod: int) -> int:
    
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
    A, B, C = map(int, input().split()) 
    
    result: int = fast_power(A, B, C) 
    print(result) 

if __name__ == "__main__":
    main()
