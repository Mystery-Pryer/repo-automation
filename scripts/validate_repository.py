#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
required=[".github/workflows/repository-quality.yml",".github/workflows/self-test.yml","fixtures/minimal-caller/scripts/validate_repository.py","CONTINUITY.md","governance/managed_repository_scope.md"]
errors=[f"missing: {p}" for p in required if not (root/p).is_file()]
workflow=(root/".github/workflows/repository-quality.yml").read_text(encoding="utf-8")
for token in ("workflow_call:","permissions:","contents: read","validator-path"):
    if token not in workflow: errors.append(f"workflow missing {token!r}")
if errors:
    print("\n".join(errors)); sys.exit(1)
print("repo-automation contract validation passed")
