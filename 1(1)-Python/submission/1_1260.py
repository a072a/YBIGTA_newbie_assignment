from __future__ import annotations
import copy
from collections import deque
from collections import defaultdict
from typing import DefaultDict, List


"""
TODO:
- __init__ �����ϱ�
- add_edge �����ϱ�
- dfs �����ϱ� (��� �Ǵ� ���� ��� ����)
- bfs �����ϱ�
"""


class Graph:
    def __init__(self, n: int) -> None:
        """
        �׷��� �ʱ�ȭ
        n: ������ ���� (1������ n������)
        """
        self.n = n
        # �����ϼ���!
        self.graph: DefaultDict[int, list[int]] = defaultdict(list)


    
    def add_edge(self, u: int, v: int) -> None:
        """
        ����� ���� �߰�
        Args:
            u(int): ������ �߰��ؾ��� ��� 1
            v(int): ������ �߰��ؾ��� ��� 2
        
        """
        # �����ϼ���!
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    
    def dfs(self, start: int) -> list[int]:
        """
        ���� �켱 Ž�� (DFS)
        
        ���� ��� ����:
        1. ��� ���: �Լ� ���ο��� ��� �Լ� �����Ͽ� ����
        
        Args:
            -start (int): ���۵Ǵ� ���

        Returns:
            -list[int]: �׷����� DFS�� Ž���� ���
        """
        # �����ϼ���!
        visited = [False] * (self.n+1)
        result = []

        def recurse(v: int):
            visited[v] = True
            result.append(v)
            for u in sorted(self.graph[v]):
                if not visited[u]:
                    recurse(u)
        recurse(start)
        return result
    
    def bfs(self, start: int) -> list[int]:
        """
        �ʺ� �켱 Ž�� (BFS)
        ť�� ����Ͽ� ����
        Args:
           -start (int): ���۵Ǵ� ���

        Returns:
            -list[int]: �׷����� BFS�� Ž���� ���
        """
        # �����ϼ���!
        visited = [False] * (self.n+1)
        result = []
        queue: deque = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            v=queue.popleft()
            result.append(v)
            for u in sorted(self.graph[v]):
                if not visited[u]:
                    queue.append(u)
                    visited[u] = True
        return result
    
    def search_and_print(self, start: int) -> None:
        """
        DFS�� BFS ����� ���
        """
        dfs_result = self.dfs(start)
        bfs_result = self.bfs(start)
        
        print(' '.join(map(str, dfs_result)))
        print(' '.join(map(str, bfs_result)))



from typing import Callable
import sys


"""
-�ƹ��͵� �������� ������!
"""


def main() -> None:
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    lines: list[str] = sys.stdin.readlines()

    N, M, V = intify(lines[0])
    
    graph = Graph(N)  # �׷��� ����
    
    for i in range(1, M + 1): # ���� ���� �Է�
        u, v = intify(lines[i])
        graph.add_edge(u, v)
    
    graph.search_and_print(V) # DFS�� BFS ���� �� ���


if __name__ == "__main__":
    main()
