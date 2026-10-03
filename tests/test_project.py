import subprocess
import sys
import unittest
from pathlib import Path

from scripts.generate_deliverables import SOURCE, find_font, iter_inline, parse_markdown

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

    def test_review_parser_finds_complete_structure(self):
        blocks = parse_markdown(SOURCE)
        headings = [block.text for block in blocks if block.kind == "heading"]
        references = [block for block in blocks if block.kind == "reference"]

        self.assertEqual(blocks[0].text, "Resumo")
        self.assertIn("1. Introdução", headings)
        self.assertIn("8. Conclusão", headings)
        self.assertIn("Referências", headings)
        self.assertEqual(len(references), 9)

    def test_inline_parser_preserves_formatting_and_citation(self):
        tokens = list(
            iter_inline(
                "Texto **forte**, *ênfase*, [fonte](https://example.com) e nota[^2]."
            )
        )
        kinds = [kind for kind, _, _ in tokens]

        self.assertIn("bold", kinds)
        self.assertIn("italic", kinds)
        self.assertIn("link", kinds)
        self.assertIn("footnote", kinds)

    def test_portable_font_fallback_is_available(self):
        self.assertTrue(find_font("Vera.ttf").is_file())
        self.assertTrue(find_font("VeraBd.ttf").is_file())

    def test_final_files_have_expected_signatures(self):
        pdf = ROOT / "entrega" / "Resenha_Critica_FBI_Sentinel.pdf"
        docx = ROOT / "entrega" / "Resenha_Critica_FBI_Sentinel.docx"

        self.assertTrue(pdf.read_bytes().startswith(b"%PDF-"))
        self.assertTrue(docx.read_bytes().startswith(b"PK"))


if __name__ == "__main__":
    unittest.main()
