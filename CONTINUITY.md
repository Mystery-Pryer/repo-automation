# Repository Continuity Rules

## Purpose

This repository provides shared GitHub Actions workflows used by other repositories. Changes must remain reproducible, reviewable, securely versioned, and safe for downstream callers.

GitHub is the durable source of truth. Local workflow experiments, editor state, chat history, and uncommitted files are temporary execution context only.

## Source-of-truth and authority

1. Safety, privacy, authorization, and non-destructive constraints always govern.
2. Current explicit user intent governs intended changes.
3. Verified remote state governs facts, history, and progress.
4. Committed workflows, policies, tests, and caller documentation govern execution unless deliberately changed.
5. Verified Actions evidence governs validation claims; local/chat context is temporary.

## Session start

Before substantive work:

1. Confirm the repository, `origin`, branch, requested workflow, and affected callers.
2. Run `git fetch --prune` and inspect `git status -sb`.
3. Compare local and remote history; fast-forward only when the tree is clean and the branch is only behind.
4. On a dirty checkout, fetch and inspect without altering it; when safe, create an isolated worktree from the verified remote default branch. Stop if that cannot be done safely.
5. Re-read `README.md`, affected workflow files, current release references, and known caller expectations.
6. Record the governing commit SHA in substantive change notes or pull requests.

Never reset, rebase, force-push, auto-stash, overwrite, discard, or silently merge existing work.

## Shared-workflow change control

Every substantive workflow change must document:

- the workflow and behavior being changed;
- the reason and expected caller impact;
- permissions, secrets, inputs, outputs, artifacts, and path assumptions;
- compatibility with existing callers;
- validation performed in a branch or pull request;
- release-reference or pinning implications;
- the exact commit containing the durable result.

Generic checks belong in this repository. Repository-specific business rules, private paths, credentials, and sensitive validation logic must remain in the caller repository.

## Versioning and caller safety

- Critical callers should pin reusable workflows to an immutable commit SHA; `v1` is a compatibility convenience.
- Do not move `v1` until the exact proposed commit passes this repository's self-validation and minimal caller fixture in a pull request.
- Breaking behavior requires an explicit compatibility decision and normally a new immutable release reference.
- Do not silently change required inputs, permissions, artifact names, supported file types, or failure semantics.
- Keep workflows read-only unless a reviewed requirement justifies broader permissions.
- Never place credentials, personal data, private business rules, or caller-specific secrets in shared workflow files.
- Record downstream caller updates when a shared change requires them.

## Canonical locations

- Reusable workflows belong under `.github/workflows/`.
- Documentation belongs in `README.md` or a clearly named root document.
- Tests and fixtures, when added, must have one canonical location and must not contain sensitive caller data.

Do not create duplicate workflow files with overlapping responsibilities unless a versioned compatibility reason is documented.

## Session end

A meaningful session is complete only when:

1. workflow syntax and available tests have run;
2. permissions, inputs, outputs, and caller compatibility have been reviewed;
3. limitations and rollout requirements are documented;
4. only scoped, non-sensitive files are committed;
5. the branch is pushed;
6. the remote is fetched again;
7. the intended commit and paths are confirmed remotely;
8. the pull request records validation and downstream impact;
9. release references are updated only after successful review.

Do not claim completion when validation failed, downstream impact is unknown, or remote verification was not performed.

## Clean-caller test

Periodically test the reusable workflow from a minimal caller repository pinned to the intended reference. Record undocumented permissions, path assumptions, missing inputs, artifact mismatches, and caller-specific dependencies as continuity defects.
