# Uploading the collection to GitLab

## Use a new, clean project

Extract the ZIP and open a terminal in `tech-projects-public`. Create a new blank GitLab project in the intended account or namespace. Keep it private for the first review. Do not initialize the remote with a README when following the push commands below; this folder already contains one. GitLab's official project guide is listed in [S22](SOURCES.md#s22).

A ZIP uploaded as one file is an attachment, not a browsable source repository. Commit the extracted files to preserve folders, source viewing and the validation pipeline. No upload has been performed by this package.

## Verify locally

```bash
python tools/privacy_scan.py
python tools/check_repository.py
python -m unittest discover -s tests -v
python tools/run_demo.py
```

Before committing, choose a suitable public Git author identity. Git commits expose name and email; project visibility does not automatically anonymize these fields. Replace the two uppercase strings below locally. Do not leave them as author values, and do not use a sensitive corporate identity in a public portfolio without approval.

```bash
git init -b main
git config user.name "REPLACE_WITH_PUBLIC_DISPLAY_NAME"
git config user.email "REPLACE_WITH_APPROVED_PUBLIC_OR_NOREPLY_EMAIL"
git add .
git diff --cached --stat
git diff --cached --check
git diff --cached
```

Inspect the staged diff, including `.gitlab-ci.yml`, all fixtures, file names and any values you changed. `.gitignore` does not remove already tracked files. Run `git status --short` and ensure runtime files are not staged.

```bash
git commit -m "Add public reference projects and synthetic examples"
git remote add origin REPLACE_WITH_YOUR_GITLAB_REPOSITORY_URL
git push -u origin main
```

The remote placeholder is intentionally not a working address. Obtain the actual HTTPS or SSH clone URL from the new project. Use GitLab's approved authentication flow; never embed a token in the remote URL, a script, a commit, a shell-history example or a screenshot.

## Review CI and visibility

The pipeline only runs local analysis and synthetic tests. It has no live service credentials, deployment job or production report artifacts. Review approved image sources and runner availability, then inspect the first pipeline result. A pipeline template in the ZIP is not proof that the pipeline passed on your GitLab installation.

Optional native secret scanning and push protection depend on the GitLab offering, configuration and license. Check [S22](SOURCES.md#s22) rather than assuming they are available. The local heuristic scanner is independent of those features and is not a substitute for them.

Decide the license and publication rights before making the project public. Review profile identity, repository description, issue templates, commit authors and project visibility. The included `LICENSE` file explicitly records that no open-source license has been selected.

## Publishing updates

Keep actual credentials and operational data outside the repository. Add new synthetic tests for changes. Review branches and CI logs before merging. Use the supplied merge-request checklist to document what was tested and whether API or hardware verification is still pending.

To produce a fresh shareable ZIP after updates, run the index generator and packager. Choose a destination outside this repository and a filename that does not already exist:

```bash
python tools/build_index.py
python tools/package_release.py ../public-reference-release.zip
```

Packaging checks the current public file boundary and creates normalized ZIP metadata plus `MANIFEST.sha256`. It does not inspect old Git history, revoke leaked secrets, upload anything or change GitLab settings. Do not package an old private working tree as a shortcut.
