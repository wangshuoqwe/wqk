# tests/test_eight_queens.py
import pytest
from src.eight_queens import solve_n_queens

def is_valid_solution(board, n):
    """验证一个解是否合法"""
    # 检查是否有重复的列（行是自动保证不重复的，因为每个位置代表一行）
    if len(set(board)) != n:
        return False
    # 检查对角线
    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def test_n4_solution_count():
    """测试N=4时解的数量是否为2"""
    solutions = solve_n_queens(4)
    assert len(solutions) == 2, f"N=4应该有2个解，但得到了{len(solutions)}个"

def test_n8_solution_count():
    """测试N=8时解的数量是否为92"""
    solutions = solve_n_queens(8)
    assert len(solutions) == 92, f"N=8应该有92个解，但得到了{len(solutions)}个"

def test_n4_solutions_valid():
    """测试N=4的所有解是否合法"""
    solutions = solve_n_queens(4)
    for sol in solutions:
        assert is_valid_solution(sol, 4), f"非法解: {sol}"

def test_n8_solutions_valid():
    """测试N=8的所有解是否合法"""
    solutions = solve_n_queens(8)
    for sol in solutions:
        assert is_valid_solution(sol, 8), f"非法解: {sol}"

def test_n1_boundary():
    """测试边界情况N=1，应有1个解"""
    solutions = solve_n_queens(1)
    assert len(solutions) == 1
    assert is_valid_solution(solutions[0], 1)

def test_n2_boundary():
    """测试边界情况N=2，应有0个解"""
    solutions = solve_n_queens(2)
    assert len(solutions) == 0

def test_n3_boundary():
    """测试边界情况N=3，应有0个解"""
    solutions = solve_n_queens(3)
    assert len(solutions) == 0
