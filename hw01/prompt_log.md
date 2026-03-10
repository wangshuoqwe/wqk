
---

## 📜 交互日志（AI辅助过程）
**文件**：`hw01/prompt_log.md`
```markdown
# 与 Claude Code 的交互日志

## 2026-03-10 工程初始化
**用户**：使用 Claude Code 初始化一个 Python 工程，包含 src/ 和 tests/ 目录，用于解决八皇后问题。

**AI**：已创建以下目录和文件：
- `hw01/src/__init__.py`
- `hw01/tests/__init__.py`
- 建议在 src/ 中创建 queens_solver.py，在 tests/ 中创建 test_queens.py。

## 2026-03-10 编写求解器
**用户**：请用回溯法实现一个 N 皇后求解器，类名为 NQueensSolver，包含 solve() 方法返回所有解的列表，每个解为每行皇后所在的列号列表。添加一个 format_solution 方法将解格式化为字符串棋盘。

**AI**：提供了初始代码（见最终版，但此处故意引入了一个 Bug：在 _is_safe 中只检查了列冲突，忽略了其中一个对角线方向，导致解的数量不正确）。

## 2026-03-10 运行测试发现 Bug
**用户**：运行 `pytest tests/ -v` 发现 test_8_queens_count 失败，实际解的数量是 0 而不是 92。错误日志如下：
