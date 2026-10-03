#!/usr/bin/env python3
"""Validação local do repositório e dos artefatos finais."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "LICENSE",
    "ENTREGA_DIO.md",
    "CONTRIBUTING.md",
    "Makefile",
    "requirements.txt",
    "docs/RESENHA_CRITICA.md",
    "docs/LINHA_DO_TEMPO.md",
    "docs/MATRIZ_SCRUM.md",
    "docs/REFERENCIAS.md",
    "docs/APRESENTACAO.md",
    "assets/capa.svg",
    "assets/capa-documento.png",
    "assets/ciclo-scrum.svg",
    "assets/linha-do-tempo.svg",
    "scripts/generate_deliverables.py",
    "scripts/validate_project.py",
    "tests/test_project.py",
    "entrega/Resenha_Critica_FBI_Sentinel.docx",
    "entrega/Resenha_Critica_FBI_Sentinel.pdf",
]

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDERS = [
    r"\bTODO\b",
    r"\bFIXME\b",
    r"SEU[_ ]NOME",
    r"COLE[_ ]AQUI",
    r"Lorem ipsum",
]


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def validate_required(errors: list[str]) -> None:
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"arquivo obrigatório ausente: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"arquivo vazio: {relative}")


def validate_markdown_links(errors: list[str]) -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_target = unquote(target.split("#", 1)[0])
            if not clean_target:
                continue
            resolved = (path.parent / clean_target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"link sai do repositório em {path.relative_to(ROOT)}: {target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"link local quebrado em {path.relative_to(ROOT)}: {target}"
                )


def validate_content(errors: list[str]) -> None:
    combined = "\n".join(path.read_text(encoding="utf-8") for path in markdown_files())
    for pattern in PLACEHOLDERS:
        # Placeholders de template são escritos em caixa alta; não confundir
        # palavras legítimas em português, como “todo o” e “seu nome”.
        if re.search(pattern, combined):
            errors.append(f"placeholder encontrado: {pattern}")

    review = (ROOT / "docs/RESENHA_CRITICA.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for number in range(1, 10):
        if f"[^{number}]:" not in review:
            errors.append(f"referência [^{number}] ausente na resenha")
        if not re.search(rf"\[\^{number}\](?!:)", review):
            errors.append(f"referência [^{number}] não é citada no texto")
    if "Originalidade do trabalho" not in readme:
        errors.append("README não contém declaração de originalidade")
    if len(review.split()) < 1800:
        errors.append("resenha parece curta demais para a entrega completa")


def validate_svg(errors: list[str]) -> None:
    for path in sorted((ROOT / "assets").glob("*.svg")):
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as exc:
            errors.append(f"SVG inválido em {path.relative_to(ROOT)}: {exc}")
            continue
        if not root.tag.endswith("svg"):
            errors.append(f"elemento raiz inesperado em {path.relative_to(ROOT)}")
        if root.find("{http://www.w3.org/2000/svg}title") is None:
            errors.append(f"SVG sem título acessível: {path.relative_to(ROOT)}")


def validate_docx(errors: list[str]) -> None:
    path = ROOT / "entrega/Resenha_Critica_FBI_Sentinel.docx"
    if not path.exists():
        return
    try:
        with zipfile.ZipFile(path) as archive:
            bad = archive.testzip()
            if bad:
                errors.append(f"DOCX corrompido no item: {bad}")
            names = set(archive.namelist())
            for expected in (
                "[Content_Types].xml",
                "word/document.xml",
                "docProps/core.xml",
            ):
                if expected not in names:
                    errors.append(f"DOCX sem componente: {expected}")
            xml = archive.read("word/document.xml").decode("utf-8")
            for phrase in ("Scrum no FBI", "Análise crítica", "Referências"):
                if phrase.casefold() not in xml.casefold():
                    errors.append(f"DOCX não contém texto esperado: {phrase}")
    except (zipfile.BadZipFile, KeyError) as exc:
        errors.append(f"DOCX inválido: {exc}")


def validate_pdf(errors: list[str]) -> None:
    path = ROOT / "entrega/Resenha_Critica_FBI_Sentinel.pdf"
    if not path.exists():
        return
    data = path.read_bytes()
    if not data.startswith(b"%PDF-"):
        errors.append("PDF não possui cabeçalho válido")
    if b"%%EOF" not in data[-2048:]:
        errors.append("PDF não possui marcador final")
    page_count = len(re.findall(rb"/Type\s*/Page(?!s)", data))
    if page_count < 5:
        errors.append(f"PDF possui poucas páginas ({page_count})")


def main() -> int:
    errors: list[str] = []
    validate_required(errors)
    validate_markdown_links(errors)
    validate_content(errors)
    validate_svg(errors)
    validate_docx(errors)
    validate_pdf(errors)

    if errors:
        print("VALIDAÇÃO: FALHOU")
        for error in errors:
            print(f"  ✗ {error}")
        return 1

    print("VALIDAÇÃO: OK")
    print(f"  ✓ {len(REQUIRED)} arquivos obrigatórios")
    print(f"  ✓ {len(markdown_files())} documentos Markdown")
    print("  ✓ links locais, referências, SVG, DOCX e PDF")
    return 0


if __name__ == "__main__":
    sys.exit(main())
