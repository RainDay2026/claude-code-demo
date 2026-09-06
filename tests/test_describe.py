import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.stats import describe


def test_describe_returns_all_metrics():
    result = describe([2, 4, 4, 4, 5, 5, 7, 9])
    assert result["count"] == 8
    assert result["mean"] == pytest.approx(5.0)
    assert result["median"] == pytest.approx(4.5)
    assert result["mode"] == 4
    assert result["variance"] == pytest.approx(4.0)
    assert result["stdev"] == pytest.approx(2.0)


def test_describe_propagates_empty_error():
    with pytest.raises(ValueError):
        describe([])
