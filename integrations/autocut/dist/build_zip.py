#!/usr/bin/env python3
"""Monta o pacote de release da ponte AutoCut.

Uso:  python3 integrations/autocut/dist/build_zip.py 0.1.0 <pasta-de-saida>
Gera: <saida>/autocut-filmcraft-v0.1.0.zip  e  <saida>/release-notes.md
"""
import sys
import zipfile
from pathlib import Path

DIST = Path(__file__).resolve().parent
SRC = DIST.parent


def render(text, version):
    return text.replace("{{VERSION}}", version)


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    version, out = sys.argv[1].lstrip("v"), Path(sys.argv[2])
    if not version or not all(c.isdigit() or c in ".-abcdefghijklmnopqrstuvwxyz" for c in version):
        raise SystemExit(f"versao invalida: {version!r}")
    out.mkdir(parents=True, exist_ok=True)
    root = f"autocut-filmcraft-v{version}"
    # no pacote os scripts ficam na raiz, entao o caminho do docstring muda
    files = {
        "autocut_free.py": (SRC / "autocut_free.py").read_text(encoding="utf-8"),
        "filmcraft_autocut.py": (SRC / "filmcraft_autocut.py").read_text(encoding="utf-8")
        .replace("integrations/autocut/", ""),
        "README.md": render((DIST / "README.md").read_text(encoding="utf-8"), version),
        "LICENSE": (SRC / "LICENSE-AUTOCUT").read_text(encoding="utf-8"),
    }
    zip_path = out / f"{root}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, text in files.items():
            z.writestr(f"{root}/{name}", text)
    notes = render((DIST / "RELEASE_NOTES.md").read_text(encoding="utf-8"), version)
    (out / "release-notes.md").write_text(notes, encoding="utf-8")
    print(zip_path)


if __name__ == "__main__":
    main()
