# 与 Claude Code 的交互日志

## 阶段一：描述需求（工程初始化与求解器编写）
**用户**：请使用 Claude Code 帮我初始化一个 Python 工程，要求包含 `src/` 和 `tests/` 目录，并基于回溯法实现八皇后问题的求解器。需要有一个 `NQueensSolver` 类，包含 `solve()` 方法返回所有解（每个解为一个列表，记录每行皇后所在的列），以及 `format_solution()` 方法将解格式化为字符串棋盘。另外，在 `tests/` 中编写单元测试，验证 4 皇后（2个解）和 8 皇后（92个解）的数量。

**AI**：已创建目录结构，并提供了初始代码。但测试发现 `test_8_queens_count` 失败（实际解为0），原因是 `_is_safe` 方法中只检查了列冲突，未检查对角线。

## 阶段二：发现并处理 Bug
**用户**：运行 `pytest tests/ -v` 后得到以下错误日志：从日志看，8皇后未找到任何解，请分析原因并修复。

**AI**：错误表明回溯过程中所有放置尝试都被拒绝，说明冲突检测逻辑可能过于严格。检查代码发现 `_is_safe` 仅判断了列冲突，遗漏了对角线检查。已修改为同时检查两个对角线方向：
```python
def _is_safe(self, queens: List[int], row: int, col: int) -> bool:
    for r, c in enumerate(queens):
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True
