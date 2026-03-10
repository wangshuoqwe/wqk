# 与 Claude Code 的交互日志

## 2026-03-10 09:00 – 项目初始化（需求描述）
**用户**：  
> 请使用 Claude Code 帮我初始化一个 Python 工程，用于解决八皇后问题。工程需要包含 `src/` 和 `tests/` 两个目录，符合标准 Python 包结构。请创建必要的 `__init__.py` 文件，并告诉我后续如何添加代码。

**AI 响应**：  
已创建以下目录结构：
- `hw01/src/__init__.py`
- `hw01/tests/__init__.py`
建议在 `src/` 中创建 `queens_solver.py` 实现核心逻辑，在 `tests/` 中创建 `test_queens.py` 编写单元测试。后续您可以通过 `from src.queens_solver import NQueensSolver` 来使用求解器。

## 2026-03-10 09:15 – 编写求解器（需求描述）
**用户**：  
> 请在 `src/queens_solver.py` 中实现一个 `NQueensSolver` 类，使用回溯法求解 N 皇后问题。要求：
> - `__init__(self, n)` 接收棋盘大小 n。
> - `solve(self)` 方法返回所有解的列表，每个解是一个长度为 n 的列表，表示每行皇后所在的列号。
> - 添加一个 `format_solution(self, queens)` 方法，将解格式化为字符串棋盘（用 `'Q'` 表示皇后，`'.'` 表示空格）。
> - 请包含类型注解和基本的文档字符串。

**AI 响应**：  
提供了初始代码（见下方摘要）。代码中 `_is_safe` 方法仅检查了列冲突，但故意遗漏了对角线检查（这是一个模拟的“AI 生成 Bug”）。

## 2026-03-10 09:30 – 运行测试发现 Bug（发现 Bug）
**用户**：  
> 我已经在 `tests/test_queens.py` 中编写了单元测试，包括：
> - `test_4_queens_count`（预期 2 个解）
> - `test_8_queens_count`（预期 92 个解）
> - `test_solution_validity`（验证每个解的有效性）
> - `test_edge_cases`（边界情况）
>
> 运行 `pytest tests/ -v` 后，`test_8_queens_count` 失败，错误日志如下：
