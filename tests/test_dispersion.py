import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.stats import stdev, variance


@pytest.mark.parametrize(
    "values,expected",
    [
        ([2, 4, 4, 4, 5, 5, 7, 9], 4.0),
        ([1, 1, 1], 0.0),
    ],
)
def test_variance_population(values, expected):
    assert variance(values) == pytest.approx(expected)


def test_variance_sample_divides_by_n_minus_1():
    # 总体方差 4.0，样本方差 = 4.0 * 8 / 7
    assert variance([2, 4, 4, 4, 5, 5, 7, 9], sample=True) == pytest.approx(32 / 7)


def test_stdev_is_sqrt_of_variance():
    assert stdev([2, 4, 4, 4, 5, 5, 7, 9]) == pytest.approx(2.0)


@pytest.mark.parametrize(
    "values,sample",
    [
        ([], False),      # 空列表
        ([], True),
        ([42], True),     # 样本方差需要至少 2 个元素
    ],
)
def test_rejects_insufficient_data(values, sample):
    with pytest.raises(ValueError):
        variance(values, sample=sample)


def test_single_value_population_variance_is_zero():
    assert variance([42]) == 0.0
