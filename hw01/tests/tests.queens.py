import pytest
from src.queens_solver import NQueensSolver

def test_4_queens_count():
    """测试4皇后问题的解的数量（应为2个）"""
    solver = NQueensSolver(4)
    solutions = solver.solve()
    assert len(solutions) == 2

def test_8_queens_count():
    """测试8皇后问题的解的数量（应为92个）"""
    solver = NQueensSolver(8)
    solutions = solver.solve()
    assert len(solutions) == 92

def test_solution_validity():
    """验证每个解是否真的有效（无冲突）"""
    solver = NQueensSolver(5)
    solutions = solver.solve()
    for sol in solutions:
        # 检查冲突
        for i in range(len(sol)):
            for j in range(i + 1, len(sol)):
                assert sol[i] != sol[j]  # 不同列
                assert abs(i - j) != abs(sol[i] - sol[j])  # 不在对角线上

def test_edge_cases():
    """边界情况：1皇后和2皇后"""
    solver1 = NQueensSolver(1)
    assert len(solver1.solve()) == 1  # 只有1个解

    solver2 = NQueensSolver(2)
    assert len(solver2.solve()) == 0  # 无解
