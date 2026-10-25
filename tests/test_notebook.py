"""Notebook integrity checks; do not execute model training."""
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
NOTEBOOK = ROOT / "notebook.ipynb"


def test_notebook_is_valid_json_and_has_no_saved_outputs():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4
    assert notebook["cells"]
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            assert cell.get("outputs", []) == []
            assert cell.get("execution_count") is None


def test_project_has_setup_documentation():
    assert (ROOT / "README.md").is_file()
    requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    assert "tensorflow" in requirements.lower()
