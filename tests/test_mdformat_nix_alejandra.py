from pathlib import Path

from markdown_it.utils import read_fixture_file
import mdformat
import pytest
from unittest.mock import patch

# Exception handling for file reading
try:
    TEST_CASES = read_fixture_file(Path(__file__).parent / "data" / "fixtures.md")
except FileNotFoundError:
    raise FileNotFoundError(
        "Unable to find the fixture file for the tests. Check the file path and try again."
    )


@pytest.mark.parametrize(
    "line,title,text,expected", TEST_CASES, ids=[f[1] for f in TEST_CASES]
)
def test_fixtures(line, title, text, expected):
    """Test fixtures in tests/data/fixtures.md."""
    # Explicitly test the nix formatter
    assert (
        "nix" in mdformat.plugins.CODEFORMATTERS
    ), "nix formatter is not in mdformat's code formatters."

    md_new = mdformat.text(text, codeformatters={"nix"})

    # Use pytest's assert message
    assert (
        md_new.strip() == expected.strip()
    ), f"Formatted (unexpected) Markdown:\n{md_new}"


@pytest.mark.skip
def test_alejandra_not_found():
    """Test that format_nix handles a missing alejandra correctly."""
    valid_nix_code = "{}"

    # Mock subprocess.run to simulate an error when running alejandra
    with patch("subprocess.run", side_effect=FileNotFoundError):
        with pytest.raises(Exception) as excinfo:
            mdformat.text(text, codeformatters={"nix"})

    print(excinfo.value)

    # Check if the exception message contains the expected error message
    assert "Failed to format Nix code with alejandra:" in str(excinfo.value)
