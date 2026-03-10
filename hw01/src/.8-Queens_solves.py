def solve_n_queens(n: int) -> list[list[str]]:

"""
八皇后问题求解器（回溯法）
支持求解任意 N 皇后的所有有效布局。
"""

from typing import List, Tuple

class NQueensSolver:
    """N皇后问题求解器"""

    def __init__(self, n: int):
        self.n = n
        self.solutions: List[List[int]] = []  # 每个解用长度为n的列表表示，索引为行，值为列

    def solve(self) -> List[List[int]]:
        """返回所有解"""
        self.solutions.clear()
        self._backtrack([])
        return self.solutions

    def _backtrack(self, queens: List[int]):
        """
        回溯递归
        :param queens: 当前已放置的皇后列表，queens[i] 表示第 i 行皇后所在的列
        """
        row = len(queens)
        if row == self.n:
            # 找到一个完整解
            self.solutions.append(queens[:])
            return

        for col in range(self.n):
            if self._is_safe(queens, row, col):
                queens.append(col)
                self._backtrack(queens)
                queens.pop()

    def _is_safe(self, queens: List[int], row: int, col: int) -> bool:
        """
        检查在 (row, col) 放置皇后是否安全
        :param queens: 已放置的皇后列表
        :param row: 当前行
        :param col: 当前列
        """
        for r, c in enumerate(queens):
            # 检查同一列或对角线
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def format_solution(self, queens: List[int]) -> List[str]:
        """将解格式化为字符串棋盘"""
        board = []
        for col in queens:
            row_str = ['.'] * self.n
            row_str[col] = 'Q'
            board.append(''.join(row_str))
        return board
