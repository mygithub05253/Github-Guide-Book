# 5-4. GSTACK 설치 및 설정

> GSTACK(Garry Tan's Skill Pack)은 YC CEO 개리 탄이 만든 23개 Claude Code 스킬 팩입니다. 역할 기반 슬래시 명령어로 워크플로우를 체계화합니다.

---

## GSTACK이 풀고자 하는 문제

혼자 Claude Code를 쓰다 보면 이런 고민이 생깁니다.

- "같은 스타일로 코드 리뷰 받고 싶은데 매번 프롬프트를 처음부터 적어야 하네"
- "배포 전 체크리스트를 매번 까먹는다"
- "아키텍처 결정을 감으로 하고 있다"

GSTACK은 이런 반복 프롬프트를 **슬래시 명령어**로 캡슐화합니다. `/review`, `/ship`, `/office-hours` 한 줄이면 "YC 멘토가 옆에서 코칭하는 것처럼" 작동합니다.

---

## 설치

### 1) gstack CLI 설치 (추천)

```bash
# gstack 공식 설치 스크립트 (github.com/garrytan/gstack)
curl -fsSL https://raw.githubusercontent.com/garrytan/gstack/main/install.sh | bash

# 설치 확인
gstack --version
```

### 2) Claude Code에 스킬 등록

```bash
claude install-skill github.com/garrytan/gstack
```

### 3) 설치 확인

```bash
claude skills list
```

!!! info "예상 출력"
    ```text
    Installed skills (23):
    - office-hours       YC 스타일 전략 상담
    - plan-ceo-review    CEO 관점 계획 리뷰
    - plan-eng-review    엔지니어링 관점 리뷰
    - review             코드 리뷰
    - think              Sequential Thinking 기반 분석
    - design-consultation
    - design-review
    - qa
    - qa-only
    - ship
    - land-and-deploy
    - canary
    - cso                보안 최고 책임자 관점
    - document-release
    - retro
    - ... (나머지 8개)
    ```

!!! danger "🚨 자주 발생하는 에러: `skill not found`"
    - **원인:** `claude skills list`에 등록되지 않음
    - **해결 1:** `claude install-skill` 재실행
    - **해결 2:** `~/.claude/skills/` 디렉토리 수동 확인 후 symbolic link 재생성

---

## 23개 스킬 한눈에 보기

### 1️⃣ CEO / 전략 수립 (2개)

| 명령어 | 목적 | 사용 시기 |
|--------|------|-----------|
| `/office-hours` | YC 스타일 전략 상담 | 프로젝트 시작, 방향 고민 |
| `/plan-ceo-review` | 계획을 비즈니스 관점에서 리뷰 | 스프린트 계획 직후 |

### 2️⃣ Engineer / 기술 구현 (3개)

| 명령어 | 목적 | 사용 시기 |
|--------|------|-----------|
| `/plan-eng-review` | 기술 계획 리뷰 | 아키텍처 설계 직후 |
| `/review` | 코드 리뷰 (PR 단위) | PR 생성 전 |
| `/think` | Sequential Thinking 기반 심층 분석 | 복잡한 기술 결정 |

### 3️⃣ Designer / UX (2개)

| 명령어 | 목적 |
|--------|------|
| `/design-consultation` | UX 전략 수립 |
| `/design-review` | UI 일관성/접근성 리뷰 |

### 4️⃣ QA / 품질 보증 (2개)

| 명령어 | 목적 |
|--------|------|
| `/qa` | 코드 + 테스트 + 성능 종합 검사 |
| `/qa-only` | 테스트 커버리지 보고서만 |

### 5️⃣ Release / 배포 (3개)

| 명령어 | 목적 |
|--------|------|
| `/ship` | 배포 체크리스트 + 실행 |
| `/land-and-deploy` | PR 머지 + 배포 + 모니터링 |
| `/canary` | 점진적 롤아웃 (5% → 25% → 100%) |

### 6️⃣ Security (1개)

| 명령어 | 목적 |
|--------|------|
| `/cso` | 인증/인가, 암호화, 규제 준수 리뷰 |

### 7️⃣ Documentation (2개)

| 명령어 | 목적 |
|--------|------|
| `/document-release` | 릴리스 노트 자동 생성 |
| `/retro` | 회고 문서 작성 |

### 8️⃣ Planning & Analysis (8개)

| 명령어 | 목적 |
|--------|------|
| `/weekly` | 주간 계획 |
| `/daily` | 일일 계획 |
| `/scope` | 범위 정의 |
| `/breakdown` | 작업 분해 (User Stories) |
| `/estimate` | Story Points 산정 |
| `/risk` | 위험 분석 |
| `/deps` | 의존성 분석 |
| `/learn` | 학습 기록 |

---

## 첫 실행 — /office-hours 로 몸풀기

!!! example "🤖 Claude Code 프롬프트: 첫 `/office-hours`"
    ```
    /office-hours

    제가 지금 Spring Boot + React로 사용자 후기 플랫폼을 만들려고 합니다.
    대상: 대학생 창업 동아리
    예상 규모: 초기 사용자 500명
    개발 기간: 2개월
    팀: 저 혼자 (풀스택)

    YC 스타일로 이 계획의 현실성을 평가해주세요.
    6개 포싱 질문을 던지고, 제 답변에 따라 전략을 조정해주세요.
    ```

GSTACK의 `/office-hours`는 개리 탄의 실제 YC 오피스 아워 스타일로 질문을 던집니다. 6개 핵심 질문(수요 증거, 기존 대안, 구체성, 웨지, 관찰, 미래 적합성)으로 당신의 가정을 부숩니다.

!!! tip "💡 꿀팁: 슬래시 명령어를 파이프라인으로"
    `/office-hours` → `/plan-ceo-review` → `/plan-eng-review` → `/breakdown` → `/ship` 순서로 흐르게 설계하면, YC 스타일 풀 사이클 워크플로우가 완성됩니다.

---

## 업데이트 / 제거

```bash
# 업데이트
claude update-skill github.com/garrytan/gstack

# 제거
claude uninstall-skill gstack
```

!!! warning "⚠️ 주의: 업데이트 시 커스텀 프롬프트 덮어쓰기"
    GSTACK 스킬을 커스터마이즈한 경우(예: 한국어 톤 추가), 업데이트 전에 로컬 변경사항을 별도 브랜치에 백업하세요.

---

## 체크리스트

- [ ] `gstack --version` 성공
- [ ] `claude skills list` 에 23개 스킬 표시
- [ ] `/office-hours` 한 번 실행해봤다
- [ ] 어떤 스킬이 어떤 역할인지 이 페이지를 북마크했다

다음 페이지에서는 각 역할(CEO, Engineer, QA, Release)별로 실전 활용 시나리오를 살펴봅니다.
