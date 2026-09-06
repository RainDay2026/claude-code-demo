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


def mode(values: list[float]) -> float:
    """众数。出现次数相同时返回最小的那个。"""
    if not values:
        raise ValueError("values 不能为空")
    counts: dict[float, int] = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    top = max(counts.values())
    return min(k for k, c in counts.items() if c == top)


def variance(values: list[float], sample: bool = False) -> float:
    """方差。

    sample=False 为总体方差（除以 n），sample=True 为样本方差（除以 n-1）。
    """
    n = len(values)
    if n == 0:
        raise ValueError("values 不能为空")
    if sample and n < 2:
        raise ValueError("样本方差至少需要 2 个元素")
    m = mean(values)
    total = sum((v - m) ** 2 for v in values)
    return total / (n - 1 if sample else n)


def stdev(values: list[float], sample: bool = False) -> float:
    """标准差，即方差的平方根。"""
    return variance(values, sample=sample) ** 0.5
