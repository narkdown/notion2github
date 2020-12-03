<a align="left" href="https://www.notion.so/Notion2Github-ko-c6842704d6e9473386cd1ab3662c1191"><img src="images/logo.png" alt="Notion2Github" width="120px"></a>

# Notion2Github

[![GitHub Action: View on Marketplace](https://img.shields.io/badge/GitHub%20Action-View_on_Marketplace-blue?style=flat-square&logo=github)](https://github.com/marketplace/actions/notion2github)
[![Demo: available](https://img.shields.io/badge/Demo-available-orange?style=flat-square)](.github/workflows/notion2github.yml)
[![Version: v1.0.1](https://img.shields.io/badge/Version-v1.0.1-brightgreen?style=flat-square)](https://github.com/younho9/notion2github/releases/tag/v1.0.1)
[![license: MIT](https://img.shields.io/badge/license-MIT-yellow.svg?style=flat-square)](./LICENSE)

| [English](/README.md) | [한국어](/docs/README.ko.md) |

**노션에서 깃헙으로의 자동 동기화**

---

> ⚠️ **유의사항:** Notion2Github은 [Jamie Alexandre](https://github.com/jamalex)이 만든 **_비공식_** 노션 API인 [notion-py](https://github.com/jamalex/notion-py) 프로젝트에 의존하고 있습니다. 공식 API가 아니기 때문에 안정적이지 않을 수 있습니다. 프로덕션 환경에서 사용하고자 한다면, 노션 공식 API 출시를 기다리는 것을 권장합니다.

---

## 사용법

### 바로 시작하기

1. `github.com/{your_id}/{your_repo}/settings/secrets/actions` 으로 이동합니다.

1. 노션의 `token_v2` 를 레포지토리의 Secrets으로 설정합니다.

   ![notion2github-image-0](images/readme-image-0.png)

   [How To Find Your Notion v2 Token - Red Gregory](https://www.redgregory.com/notion/2020/6/15/9zuzav95gwzwewdu1dspweqbv481s5)

   [Encrypted secrets](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets#using-encrypted-secrets-in-a-workflow)

1. 레포지토리의 `.github/workflows/**.yml` 파일에 워크플로우를 생성합니다.

몇 가지 예시입니다.

### 워크플로우 예제

#### 예제 1 (main 브랜치에 push & pull request 시에 실행)

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

#### 예제 2 (정해진 시간에 실행)

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

> [크론탭 설정에 유용한 사이트](https://crontab.guru/)

### 실사용 예제

- [younho9/narkdown](https://github.com/younho9/narkdown/blob/main/.github/workflows/notion2github.yml)

- [younho9/TIL](https://github.com/younho9/til/blob/main/.github/workflows/notion2github.yml)

## 테스트를 위한 데이터베이스 템플릿 페이지

데이터베이스로부터 페이지들을 가져올 수 있는 [데이터베이스 템플릿 페이지](https://www.notion.so/acc3dfd0339e4cacb5baae8673fddfad?v=be43c1c8dd644cfb9df9efd97d8af60a)가 있습니다.

페이지로 이동해서 복제하고 테스트해볼 수 있습니다.

<div align="center">
  <img width="80%" src="images/readme-image-1.png" alt="notion2github-image-1">
</div>

## 환경설정

| Name             | Description                                 | Required   | Default  |
| ---------------- | ------------------------------------------- | ---------- | -------- |
| `database-url`   | 추출할 노션 데이터베이스의 URL              | `required` |          |
| `docs-directory` | 추출된 노션 페이지들이 저장될 디렉토리      |            | `"docs"` |
| `filter-prop`    | 노션 데이터베이스에 적용할 필터의 속성 이름 |            | `""`     |
| `filter-value`   | 노션 데이터베이스에 적용할 필터의 값 이름   |            | `""`     |

### Narkdown 환경설정

Narkdown은 문서들을 어떻게 추출할 것인지에 대해 몇가지 환경설정을 제공합니다. `narkdown.config.json` 파일을 통해서 Narkdown을 환경설정할 수 있습니다.

레포지토리의 root에 `narkdown.config.json` 파일을 생성하세요.

환경에 따라 환경설정하는 방법에 대한 더 많은 정보를 보려면 [Narkdown의 문서를 확인하세요](https://github.com/younho9/narkdown#configuring-narkdown).

```json
// narkdown.config.json
{
  "exportConfig": {
    "recursiveExport": true,
    "createPageDirectory": true,
    "addMetadata": false,
    "lowerPathname": false,
    "lowerFilename": false,
    "lineBreak": false
  },
  "databaseConfig": {
    "categoryColumnName": "Category",
    "tagsColumnName": "Tags",
    "createdTimeColumnName": "Created Time",
    "statusColumnName": "Status",
    "currentStatus": "✅ Completed",
    "nextStatus": "🖨 Published"
  }
}
```

### 다른 액션과 조합하여 사용

Notion2Github은 워크플로우의 한 step으로 단지 github action으로 실행되는 가상 머신으로 노션의 콘텐츠들을 가져올 뿐입니다.

노션의 콘텐츠들을 레포지토리로 커밋할 수 있는 훌륭한 action들이 있습니다.

- [Git Auto Commit - GitHub Marketplace](https://github.com/marketplace/actions/git-auto-commit)

- [Prettier Action - GitHub Marketplace](https://github.com/marketplace/actions/prettier-action)

### License

MIT © [younho9](https://github.com/younho9)
