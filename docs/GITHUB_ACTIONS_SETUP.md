# GitHub Actions Matrix Build Setup

## Overview

This repository contains a GitHub Actions workflow that demonstrates multi-platform matrix builds with artifact management.

## Workflow File

**Location:** `.github/workflows/matrix-build.yml`

## Features

✅ **Matrix Strategy**: 3 variants across different OS and Node.js versions
- Ubuntu + Node.js 20
- Windows + Node.js 18  
- macOS + Node.js 20

✅ **Parallel Execution**: All 3 jobs run simultaneously

✅ **Artifact Management**: 
- Each job generates unique artifacts
- Artifact naming: `build-91fbe9f-<variant>`
- Artifacts include build output and metadata JSON

✅ **Required Step Identifier**: Contains step named `matrix-91fbe9f`

## Workflow Triggers

- Push to `main` or `master` branch
- Pull requests to `main` or `master` branch
- Manual trigger via `workflow_dispatch`

## Artifacts Generated

Each matrix job creates:
1. `build-output.txt` - Build information and Node.js version
2. `artifact-metadata.json` - JSON metadata with build details

## Artifact Names

- `build-91fbe9f-ubuntu-node20`
- `build-91fbe9f-windows-node18`
- `build-91fbe9f-macos-node20`

## Validation Checklist

- ✅ At least 3 matrix variants configured
- ✅ Step with identifier `matrix-91fbe9f` included
- ✅ Artifacts named with prefix `build-91fbe9f-<variant>`
- ✅ Artifacts contain non-empty content
- ✅ README.md includes email address

## Testing

To test the workflow:

1. Push to the repository (triggers on push to main/master)
2. Or use GitHub UI: Actions → Multi-Platform Matrix Build → Run workflow
3. Check the Actions tab to see all 3 jobs running in parallel
4. Verify artifacts are uploaded with correct naming

## Contact

See README.md for contact information.

