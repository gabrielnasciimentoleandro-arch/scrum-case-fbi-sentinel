import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ProjectQualityTest(unittest.TestCase):
    def test_repository_validation(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_project.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
