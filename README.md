# Repository Automation

Shared, reusable GitHub Actions workflows for repositories owned by `Mystery-Pryer`.

## Purpose

This repository centralizes generic quality-gate logic so project repositories only need small caller workflows. Repository-specific validation rules remain in each caller repository under `scripts/`.

## Reusable workflows

- `.github/workflows/repository-quality.yml` — Python, SQL, CSV, Markdown and repository-safety validation.
- `.github/workflows/resume-library-quality.yml` — resume-library validation, packaging and artifact upload.

## Versioning

Critical callers should pin reusable workflows to a full immutable commit SHA. The movable `v1` reference is a compatibility convenience and may advance only to an exact commit that passed self-validation and the minimal caller fixture in a pull request. Update caller pins through separate reviewed PRs with successful checks.

## Security

The workflows use read-only repository permissions. They do not contain credentials, personal data or private business rules. Secrets remain in the calling repository and are not required by the current workflows.
