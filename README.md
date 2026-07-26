# Repository Automation

Shared, reusable GitHub Actions workflows for repositories owned by `Mystery-Pryer`.

## Purpose

This repository centralizes generic quality-gate logic so project repositories only need small caller workflows. Repository-specific validation rules remain in each caller repository under `scripts/`.

## Reusable workflows

- `.github/workflows/repository-quality.yml` — Python, SQL, CSV, Markdown and repository-safety validation.
- `.github/workflows/resume-library-quality.yml` — resume-library validation, packaging and artifact upload.

## Versioning

Caller repositories should pin reusable workflows to the immutable release branch `v1` or, for maximum reproducibility, to a specific commit SHA. Changes are tested through pull requests before the `v1` reference is advanced.

## Security

The workflows use read-only repository permissions. They do not contain credentials, personal data or private business rules. Secrets remain in the calling repository and are not required by the current workflows.
