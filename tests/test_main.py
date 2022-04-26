"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner

from hmp_experiment import __main__
import torch


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0


def test_can_use_torch():
    A=torch.tensor([1.0])
    B = torch.tensor([2.0])
    torch.testing.assert_allclose(A, B/2)