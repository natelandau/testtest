# type: ignore
"""Test testtest CLI."""

from typer.testing import CliRunner

from tests.helpers import Regex
from testtest.cli import app

runner = CliRunner()


def test_version():
    """Test printing version and then exiting."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert result.output == Regex(r"testtest: \d+\.\d+\.\d+$")


def test_say() -> None:
    """Test that the say command works as expected."""
    message = "Hello world"
    result = runner.invoke(app, ["--message", message])
    assert result.exit_code == 0
    assert message in result.stdout
