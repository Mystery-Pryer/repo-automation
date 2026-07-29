from pathlib import Path
assert Path("README.md").is_file()
Path("artifacts").mkdir(exist_ok=True)
Path("artifacts/repository-quality-summary.json").write_text('{"ok": true, "fixture": "minimal-caller"}\n',encoding="utf-8")
print("minimal caller fixture passed")
