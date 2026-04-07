# 3-2. 포트폴리오 & 오픈소스 기여

> "오픈소스 기여? 내가? 전문가들만 하는 거 아닌가요?" 라는 오해를 깨부수는 섹션이에요. 사실 **오타 수정 PR 하나**도 훌륭한 오픈소스 기여입니다. 여기서는 그 첫 걸음을 떼는 법을 선배가 옆에서 코칭하듯 설명합니다.

---

## 3-2-1. First Contributions (firstcontributions/first-contributions) — 46K+ Stars

**한 줄 소개**: "오픈소스 첫 PR 만들기"를 **단계별로 연습할 수 있도록 설계된** 교육용 레포.

**왜 봐야 하는가**: Fork → Clone → Branch → Commit → Push → PR이라는 Git/GitHub 기본 워크플로우를 **실전으로 한 번** 돌려볼 수 있어요. 이 레포의 첫 PR은 모든 개발자의 통과의례입니다.

**난이도**: ⭐ (가장 쉬움. 이걸 못하겠다면 Part 1 Git 기초로 돌아가세요)

### 📋 이 레포에서 배울 수 있는 것

- Fork의 개념과 Upstream 설정
- 브랜치 생성 → 커밋 → 푸시 → PR 제출의 완전한 플로우
- Conventional Commit 메시지 작성법
- PR 리뷰에 응답하는 방법
- 첫 "Your PR was merged!" 알림의 감동 (진지합니다)

### 🚀 15분 퀵스타트

#### Step 1: 레포 Fork

GitHub에서 https://github.com/firstcontributions/first-contributions 접속 후 우측 상단 **Fork** 버튼 클릭.

#### Step 2: 로컬에 클론

```bash
git clone https://github.com/<your-username>/first-contributions.git
cd first-contributions
```

!!! warning "⚠️ 주의"
    `<your-username>`은 **원본 레포 주인(firstcontributions)이 아닌 당신의 GitHub 아이디**여야 해요. 원본을 clone하면 push 권한이 없어서 나중에 막힙니다.

#### Step 3: Upstream 리모트 추가

```bash
git remote add upstream https://github.com/firstcontributions/first-contributions.git
git remote -v
```

!!! info "예상 출력"
    ```
    origin    https://github.com/<your-username>/first-contributions.git (fetch)
    origin    https://github.com/<your-username>/first-contributions.git (push)
    upstream  https://github.com/firstcontributions/first-contributions.git (fetch)
    upstream  https://github.com/firstcontributions/first-contributions.git (push)
    ```

#### Step 4: 브랜치 생성 → 이름 추가 → 커밋

```bash
git checkout -b add-<your-name>
# Contributors.md 파일 편집: 알파벳 순서에 맞게 당신 이름 추가
git add Contributors.md
git commit -m "Add <your-name> to Contributors list"
```

#### Step 5: Push & PR

```bash
git push origin add-<your-name>
```

GitHub 웹에서 **Compare & pull request** 버튼 클릭 → 제목/설명 작성 → Create pull request → 끝!

!!! tip "💡 꿀팁: 머지되기까지의 기다림을 즐기세요"
    보통 수 시간~수 일 내에 머지됩니다. 머지 알림이 오는 순간 당신은 "오픈소스 컨트리뷰터"가 됩니다. GitHub 프로필에 **Pull requests** 카운트가 +1 되는 걸 확인해보세요.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: Git 플로우 복습"
    ```
    방금 내가 한 Fork → Clone → Branch → Commit → Push → PR 과정을 Mermaid
    시퀀스 다이어그램으로 그려줘. 각 단계에서 "내 로컬", "내 Fork(origin)",
    "원본(upstream)"이 어떻게 변하는지 화살표로 표현해줘.
    ```

!!! example "🤖 Claude Code 프롬프트 2: Upstream 동기화"
    ```
    며칠 뒤에 원본 레포에 새 커밋이 생겼어. 내 Fork와 로컬 브랜치를 최신 상태로
    동기화하는 명령어를 순서대로 알려주고, 각 명령이 무엇을 하는지 한 줄씩 설명해줘.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 두 번째 기여 찾기"
    ```
    first-contributions 레포 기여가 끝났어. 이제 Python 관련 초보자 이슈가 있는
    레포 5개를 `awesome-for-beginners`에서 골라줘. 각각 난이도와 이유를 같이 적어줘.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `Permission denied (publickey)`"
    **원인**: SSH 키가 GitHub에 등록되지 않음
    **해결**: HTTPS URL을 쓰거나, `ssh-keygen` + GitHub Settings → SSH Keys 등록

!!! danger "🚨 에러 2: `rejected - fetch first`"
    **원인**: 원본에 새 커밋이 생겼는데 내 로컬이 뒤처짐
    **해결**:
    ```bash
    git fetch upstream
    git rebase upstream/main
    git push origin add-<your-name> --force-with-lease
    ```

!!! danger "🚨 에러 3: PR에 conflict가 표시됨"
    **원인**: 다른 기여자도 같은 줄을 편집함
    **해결**: 로컬에서 `git rebase upstream/main` 후 충돌 수동 해결 → force push

### 📚 학습 체크리스트

- [ ] Fork, Clone, Upstream 개념을 친구에게 설명할 수 있다
- [ ] 첫 PR이 머지됨
- [ ] PR URL을 LinkedIn/이력서에 추가함
- [ ] `git log --oneline --graph --all`을 읽을 수 있다
- [ ] 브랜치 네이밍 규칙(`feat/`, `fix/`, `docs/`)을 안다

---

## 3-2-2. Awesome for Beginners (MunGell/awesome-for-beginners) — 70K+ Stars

**한 줄 소개**: "good first issue"가 있는 **초보자 친화 오픈소스 레포**를 큐레이션한 거대 목록.

**왜 봐야 하는가**: First Contributions가 "첫 걸음마"였다면 여기는 **진짜 오픈소스 세계**입니다. 실제 사용되는 라이브러리에 기여하면 포트폴리오가 확 달라집니다.

**난이도**: ⭐⭐ (레포 고르기는 쉽지만, 실제 기여는 중급)

### 📋 이 레포에서 배울 수 있는 것

- 내 수준에 맞는 오픈소스 프로젝트 찾는 법
- Issue 분석하고 구현 계획 세우는 법
- 리뷰어와의 커뮤니케이션 (영어 작성 포함)
- 테스트 작성 및 CI 통과시키는 법

### 🔍 초보자용 추천 레포 필터

!!! tip "💡 꿀팁: 레포 고르는 6가지 기준"
    1. **Stars 1K ~ 20K** (너무 크면 PR이 묻히고, 너무 작으면 리뷰어 부재)
    2. **최근 1주일 내 활동** (죽은 프로젝트 제외)
    3. **CONTRIBUTING.md 존재** (기여 방법 명시)
    4. **`good first issue` 라벨 10개 이상**
    5. **내가 아는 언어**
    6. **테스트가 잘 갖춰진 프로젝트** (내 변경이 뭘 깨뜨리는지 바로 알 수 있음)

### 🚀 15분 퀵스타트

#### Step 1: 레포 탐색

```bash
# 브라우저에서:
open https://github.com/MunGell/awesome-for-beginners
```

Python 섹션으로 스크롤하거나 브라우저에서 `Ctrl+F` → "Python" 검색.

#### Step 2: 이슈 직접 검색 (GitHub 고급 검색)

```
label:"good first issue" language:python state:open no:assignee
```

이걸 GitHub 검색창에 그대로 붙여넣으세요.

#### Step 3: 이슈 선택 기준표

| 체크 항목 | 확인 방법 |
|---|---|
| 설명이 명확한가 | 이슈 본문을 처음부터 끝까지 읽고 3분 안에 이해되는가 |
| 재현 가능한가 | "to reproduce" 섹션이 있는가 |
| 누가 이미 작업 중인가 | 댓글에 "I'll work on this" 없는가 |
| 테스트가 필요한가 | "tests required" 언급 있는가 |
| 내 스킬로 가능한가 | 관련 파일 1개만 먼저 열어보고 판단 |

#### Step 4: 댓글로 의사 표시

```
Hi! I'd like to work on this issue. Can I be assigned?
I plan to approach it by <1-2 sentences about your approach>.
```

#### Step 5: 포크 → 구현 → PR

앞서 3-2-1에서 익힌 워크플로우 그대로 진행. PR 설명은 아래 템플릿을 사용하세요.

```markdown
## Summary
Fixes #<issue_number>

## Changes
- <변경 1>
- <변경 2>

## How I tested
```bash
pytest tests/test_affected_module.py -v
```

## Checklist
- [x] Tests added / updated
- [x] Docs updated if needed
- [x] Follows CONTRIBUTING.md style
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 이슈 분석"
    ```
    이 GitHub 이슈 URL을 읽고 (1) 무엇을 고쳐야 하는지 (2) 어떤 파일을 봐야 하는지
    (3) 예상 구현 단계 3단계 (4) 테스트 전략을 정리해줘.
    URL: https://github.com/...
    ```

!!! example "🤖 Claude Code 프롬프트 2: 구현 초안"
    ```
    <파일 경로>를 읽고, 이슈 #123에서 요구하는 "X 기능"을 추가하는 diff를 만들어줘.
    기존 코드 스타일과 네이밍 컨벤션을 그대로 따르고, 테스트 코드도 같이 작성해줘.
    ```

!!! example "🤖 Claude Code 프롬프트 3: PR 영문 작성"
    ```
    위 구현에 대한 PR 설명을 영어로 작성해줘. Summary, Changes, How I tested,
    Checklist 4개 섹션으로 구성해줘. 톤은 정중하지만 간결하게.
    ```

### 📚 학습 체크리스트

- [ ] awesome-for-beginners에서 Python/JS 추천 레포 3개 북마크
- [ ] `good first issue` GitHub 검색 쿼리 저장
- [ ] 본인 수준에 맞는 이슈 1개 선정 및 댓글 작성
- [ ] 2번째 PR 머지 경험
- [ ] 리뷰어 피드백에 영어로 응답한 경험

---

## 3-2-3. GitHub Opensource Guide (github/opensource.guide) — 14K+ Stars

**한 줄 소개**: 오픈소스 프로젝트를 **시작하고 운영하는** 방법에 대한 GitHub 공식 가이드.

**왜 봐야 하는가**: 지금까지는 "남의 레포에 기여하는 법"을 배웠다면, 이제는 **내가 오픈소스 메인테이너가 되는 법**을 배울 시간이에요. 본인 프로젝트를 오픈소스화할 때 필수 문서와 절차를 알려줍니다.

**난이도**: ⭐⭐ (문서 읽기는 쉬움. 실제 운영은 별개)

### 📋 이 레포에서 배울 수 있는 것

- 오픈소스 프로젝트에 필요한 **필수 문서 5종 세트**
- 라이선스 선택법 (MIT / Apache 2.0 / GPL의 차이)
- 기여자 온보딩 프로세스 설계
- CODE_OF_CONDUCT 중요성과 템플릿
- 커뮤니티 성장 전략

### 📝 필수 문서 5종 세트

| 문서 | 역할 | 없으면 생기는 문제 |
|---|---|---|
| `README.md` | 프로젝트 첫인상 | Star를 못 받음 |
| `LICENSE` | 법적 사용 조건 | 기업이 쓸 수 없음 |
| `CONTRIBUTING.md` | 기여 방법 안내 | PR 품질이 엉망이 됨 |
| `CODE_OF_CONDUCT.md` | 커뮤니티 규범 | 해로운 행동 발생 시 제재 근거 없음 |
| `.github/ISSUE_TEMPLATE` | 이슈 표준화 | "뭐가 문젠지 모르겠는" 이슈 폭증 |

### 🚀 15분 퀵스타트: 내 프로젝트 오픈소스화

#### Step 1: 가이드 읽기

```bash
open https://opensource.guide/starting-a-project/
```

#### Step 2: 라이선스 선택

```bash
# MIT 라이선스 추가 (가장 관대함, 대부분의 경우 추천)
open https://choosealicense.com/licenses/mit/
# 내용을 복사해서 LICENSE 파일로 저장
```

!!! tip "💡 꿀팁: 라이선스 한 줄 요약"
    - **MIT**: "자유롭게 쓰세요, 다만 저한테 책임 물으면 안 돼요" (가장 인기)
    - **Apache 2.0**: MIT + 특허 조항 명시 (기업 프로젝트 기본)
    - **GPL**: "파생 프로젝트도 무조건 오픈소스여야 함" (전염성 있음)
    - **결정 어려우면 MIT**를 고르세요.

#### Step 3: README 최소 구조

```markdown
# 프로젝트 이름

[![License](https://img.shields.io/github/license/user/repo)](LICENSE)
[![Stars](https://img.shields.io/github/stars/user/repo)](https://github.com/user/repo/stargazers)

> 한 줄 설명 (tagline)

## ✨ Features
- 기능 1
- 기능 2

## 🚀 Installation
\`\`\`bash
npm install my-package
\`\`\`

## 📖 Usage
\`\`\`javascript
const mypkg = require('my-package');
mypkg.doSomething();
\`\`\`

## 🤝 Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📝 License
MIT © 2026 Your Name
```

#### Step 4: CONTRIBUTING.md 최소 구조

```markdown
# Contributing

## Dev setup
\`\`\`bash
git clone <repo>
npm install
npm test
\`\`\`

## Commit convention
Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `chore:`

## PR process
1. Fork & branch from `main`
2. Write code + tests
3. `npm test` passes
4. PR with clear description
```

#### Step 5: CODE_OF_CONDUCT.md 추가

Contributor Covenant(https://www.contributor-covenant.org)의 템플릿을 그대로 사용하세요.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 문서 세트 일괄 생성"
    ```
    내 프로젝트는 "React + Tailwind로 만든 TODO 앱"이야.
    github/opensource.guide 기준에 맞는 README.md, CONTRIBUTING.md,
    CODE_OF_CONDUCT.md, LICENSE(MIT), .github/ISSUE_TEMPLATE/bug_report.md를
    전부 생성해줘. 한국어+영어 병기 버전으로.
    ```

!!! example "🤖 Claude Code 프롬프트 2: Shields.io 배지 구성"
    ```
    내 GitHub 레포 URL을 기준으로 README 상단에 들어갈 Shields.io 배지 6개를
    생성해줘: License, Stars, Forks, Issues, Last commit, Build status.
    Markdown 코드로 바로 붙여넣을 수 있게.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 라이선스 감사"
    ```
    내 package.json의 모든 의존성을 읽고 각각의 라이선스를 조사해서,
    내 프로젝트의 MIT 라이선스와 호환되는지 체크해줘. GPL이 섞여있으면
    경고해줘.
    ```

### 📚 학습 체크리스트

- [ ] MIT vs Apache 2.0 vs GPL 차이를 친구에게 설명 가능
- [ ] 내 레포에 LICENSE 파일 추가
- [ ] README에 Shields.io 배지 3개 이상
- [ ] CONTRIBUTING.md 작성 및 커밋
- [ ] Issue/PR 템플릿 설정
- [ ] 첫 외부 기여자로부터 PR 받기 (최종 목표)

---

## 🎯 이 섹션을 마친 당신에게

이제 당신은 **오픈소스 생태계의 참여자**예요. 다른 사람의 프로젝트에 기여할 수도 있고, 당신의 프로젝트를 세상에 내놓을 수도 있습니다. 다음은 짧은 시간 안에 반짝이는 프로젝트를 만들어야 하는 [3-3. 해커톤 & 공모전](03-hackathon.md)입니다.

!!! warning "⚠️ 자주 하는 실수"
    "첫 오픈소스 PR 하나만 쓰고 끝" 하지 마세요. **꾸준함이 포트폴리오**입니다. 월 1-2개의 작은 PR이라도 1년 누적되면 면접관의 눈이 달라져요.
