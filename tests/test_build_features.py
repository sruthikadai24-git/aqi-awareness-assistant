
"""Basic tests for AQI feature engineering."""

import ast
from pathlib import Path


def test_season_function_exists():
    """Check that the season function exists in the project."""
    source_file = (
        Path(__file__).resolve().parents[1]
        / "src"
        / "features"
        / "build_features.py"
    )

    assert source_file.exists(), "build_features.py was not found"

    source = source_file.read_text(encoding="utf-8")
    tree = ast.parse(source)

    function_names = [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    ]

    assert "get_season_name" in function_names
