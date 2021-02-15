<a align="left" href="https://www.notion.so/Notion2Github-91cf062b276b41cdb78a75672ba31cb3"><img src="docs/images/logo.png" alt="Notion2Github" width="120px"></a>

# Notion2Github

[![GitHub Action: View on Marketplace](https://img.shields.io/badge/GitHub%20Action-View_on_Marketplace-blue?style=flat-square&logo=github)](https://github.com/marketplace/actions/notion2github)
[![Demo: available](https://img.shields.io/badge/Demo-available-orange?style=flat-square)](.github/workflows/notion2github.yml)
[![Version: v1.0.1](https://img.shields.io/badge/Version-v1.0.1-brightgreen?style=flat-square)](https://github.com/younho9/notion2github/releases/tag/v1.0.1)
[![license: MIT](https://img.shields.io/badge/license-MIT-yellow.svg?style=flat-square)](./LICENSE)

| [English](/README.md) | [한국어](/docs/README.ko.md) |

**Automatic syncronization from Notion to Github**

---

> ⚠️ **NOTE:** Narkdown is dependent on [notion-py](https://github.com/jamalex/notion-py), the **_unofficial_** Notion API created by [Jamie Alexandre](https://github.com/jamalex).
> It can not gurantee it will stay stable. If you need to use in production, I recommend waiting for their official release.

---

## Usage

### Quick Start

1. Go to `github.com/{your_id}/{your_repo}/settings/secrets/actions`

2. Set `token_v2` of Notion to your repository secret.

   ![notion2github-image-0](docs/images/readme-image-0.png)

   [How To Find Your Notion v2 Token - Red Gregory](https://www.redgregory.com/notion/2020/6/15/9zuzav95gwzwewdu1dspweqbv481s5)

   [Encrypted secrets](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets#using-encrypted-secrets-in-a-workflow)

3. Create a workflow in `.github/workflows/**.yml` of your repository

Here are examples.

### Example Workflow

#### Example 1 (run on push & pull request in main)

```yaml
name: Notion2Github
on:
  pull_request:
  push:
    branches:
      - main
jobs:
  auto-sync-from-notion-to-github:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Notion2Github
        uses: younho9/notion2github@v1.0.2
        with:
          database-url: 'https://www.notion.so/acc3dfd0339e4cacb5baae8673fddfad'
          docs-directory: docs
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}

      - name: Format documents
        uses: creyD/prettier_action@v3.1
        with:
          prettier_options: --write ./docs/**/*.md
          commit_message: 'docs: Update docs (auto)'
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

#### Example 2 (scheduled)

```yaml
name: Notion2Github
on:
  schedule:
    - cron: '0 14 * * *'
jobs:
  auto-sync-from-notion-to-github:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Notion2Github
        uses: younho9/notion2github@v1.0.2
        with:
          database-url: 'https://www.notion.so/acc3dfd0339e4cacb5baae8673fddfad'
          docs-directory: docs
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}

      - name: Format documents
        uses: creyD/prettier_action@v3.1
        with:
          prettier_options: --write ./docs/**/*.md
          commit_message: 'docs: Update docs (auto)'
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

> [Useful site for crontab setting](https://crontab.guru/)

### Live examples

- [younho9/narkdown](https://github.com/younho9/narkdown/blob/main/.github/workflows/notion2github.yml)

- [younho9/TIL](https://github.com/younho9/til/blob/main/.github/workflows/notion2github.yml)

## Database template page for test

Here is an [database template page](https://www.notion.so/acc3dfd0339e4cacb5baae8673fddfad?v=be43c1c8dd644cfb9df9efd97d8af60a) for importing pages from the database. Move to that page, duplicate it, and test it.

<div align="center">
  <img width="80%" src="docs/images/readme-image-1.png" alt="notion2github-image-1">
</div>

## Configuration

### Parameters

| Name             | Description                                                    | Required   | Default  |
| ---------------- | -------------------------------------------------------------- | ---------- | -------- |
| `database-url`   | URL of the Notion database to extract.                         | `required` |          |
| `docs-directory` | Directory in which the Notion pages to extract will be stored. |            | `"docs"` |
| `filter-prop`    | Property of the filter to apply to the notion database.        |            | `""`     |
| `filter-value`   | Value of the filter to apply to the notion database.           |            | `""`     |

### Configuring Narkdown

Narkdown provides some configuration for how to extract documents. You can configure Narkdown via `narkdown.config.json` .

Create `narkdown.config.json` in root directory of your repository.

For more information on configure your environment, [see the document in Nakdown](https://github.com/younho9/narkdown#configuring-narkdown).

```json
// narkdown.config.json
{
  "exportConfig": {
    "recursiveExport": true,
    "createPageDirectory": true,
    "addMetadata": true,
    "appendCreatedTime": true,
    "generateSlug": true
  },
  "databaseConfig": {
    "categoryColumnName": "Category",
    "statusColumnName": "Status",
    "currentStatus": "✅ Completed",
    "nextStatus": "🖨 Published"
  }
}
```

### Used in combination with other actions

Notion2Github is a step in the workflow, just import the contents of notion to a running virtual machine in github action.

There are great actions to commit the imported content to your repository.

- [Git Auto Commit - GitHub Marketplace](https://github.com/marketplace/actions/git-auto-commit)

- [Prettier Action - GitHub Marketplace](https://github.com/marketplace/actions/prettier-action)

### License

MIT © [younho9](https://github.com/younho9)
