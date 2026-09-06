"""一组最小的统计函数，用来演示 LSP 和 PR 流程。"""


def mean(values: list[float]) -> float:
    """算术平均数。"""
    if not values:
        raise ValueError("values 不能为空")
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """中位数。"""
    if not values:
        raise ValueError("values 不能为空")
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
