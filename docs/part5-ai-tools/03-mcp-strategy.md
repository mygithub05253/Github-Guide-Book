# 5-3. MCP 서버 조합 전략

> 개별 MCP는 도구 하나일 뿐입니다. 진짜 힘은 **여러 MCP를 조합**했을 때 나옵니다. 이 페이지는 실전 워크플로우 4가지를 소개합니다.

---

## 조합 설계의 기본 원칙

!!! info "📌 핵심 요약"
    1. **입력 → 분석 → 변형 → 출력** 4단계를 먼저 그려라
    2. 각 단계에 어떤 MCP가 맞는지 매핑하라
    3. Plan 모드로 전체 흐름을 먼저 검토하라
    4. 실패 시 롤백 계획을 함께 세우라

---

## 워크플로우 1 — REST API 프로젝트 자동 부트스트랩

### 목표
FastAPI + PostgreSQL + Docker 조합의 신규 프로젝트를 몇 분 안에 생성.

### MCP 조합

| 단계 | MCP | 역할 |
|------|------|------|
| 1. 구조 생성 | Filesystem | `src/`, `tests/`, `docker/` 디렉토리 및 보일러플레이트 |
| 2. GitHub 레포 | GitHub | 원격 저장소 생성, 초기 커밋 |
| 3. DB 스키마 | PostgreSQL | `users`, `posts` 테이블 생성 |
| 4. 컨테이너화 | Docker | `Dockerfile`, `docker-compose.yml` |
| 5. 실행 검증 | Docker + Playwright | `/health` 엔드포인트 응답 확인 |

!!! example "🤖 Claude Code 프롬프트: 원샷 부트스트랩"
    ```
    FastAPI + PostgreSQL 블로그 API 프로젝트를 처음부터 만들어줘.

    요구사항:
    1. Filesystem MCP로 표준 구조 생성 (src/, tests/, docker/)
    2. users, posts 테이블 스키마를 PostgreSQL MCP로 설계하고 생성
    3. 기본 CRUD 엔드포인트 구현 (GET/POST/PUT/DELETE)
    4. Dockerfile + docker-compose.yml 작성 (postgres 포함)
    5. GitHub MCP로 새 레포 생성하고 초기 커밋 푸시
    6. 마지막에 docker-compose up 으로 실행하고 /health 응답 확인

    실행 전에 Plan 모드로 전체 변경 계획을 먼저 보여줘.
    ```

!!! warning "⚠️ 주의: Plan 모드 필수"
    여러 MCP를 연속으로 호출하는 작업은 중간에 실수가 누적되기 쉽습니다. 반드시 Plan 모드로 미리 검토하세요.

---

## 워크플로우 2 — 기존 프로젝트 문서화 자동화

### 목표
코드베이스를 훑고 README, API 문서, 아키텍처 다이어그램 초안을 자동 생성.

### MCP 조합

```text
Filesystem MCP → 코드 스캔
      ↓
Sequential Thinking MCP → 구조 분석 및 문서 아웃라인 설계
      ↓
GitHub MCP → 최근 커밋 내역 참고
      ↓
Filesystem MCP → README.md, docs/ 생성
```

!!! example "🤖 Claude Code 프롬프트"
    ```
    현재 프로젝트를 분석해서 문서를 자동 생성해줘.

    1. Filesystem MCP로 src/ 전체 구조 파악
    2. Sequential Thinking으로 모듈 간 의존성 분석
    3. GitHub MCP로 최근 50개 커밋을 참고해 주요 변경 이력 요약
    4. 다음 파일들 생성:
       - README.md (설치/실행/기여 방법)
       - docs/architecture.md (모듈 구조 + Mermaid 다이어그램)
       - docs/api.md (엔드포인트 목록 + 파라미터)
    5. 모든 생성 파일은 Plan 모드로 먼저 미리보기
    ```

---

## 워크플로우 3 — 버그 트리아지 & 재현 테스트 생성

### 목표
GitHub 이슈를 읽고 재현 테스트 코드를 짜서 PR 초안까지 만들기.

### MCP 조합

| 단계 | MCP | 작업 |
|------|------|------|
| 1 | GitHub | 열린 버그 이슈 top 10 조회 |
| 2 | Sequential Thinking | 각 이슈의 재현 가능성 평가 |
| 3 | Filesystem | 관련 소스 파일 탐색 |
| 4 | Filesystem | 재현 테스트 케이스 작성 |
| 5 | GitHub | 브랜치 생성 + PR 초안 |

!!! example "🤖 Claude Code 프롬프트"
    ```
    myname/myproject 레포의 'bug' 라벨이 붙은 열린 이슈 중
    최근 10개를 분석해줘.

    각 이슈에 대해:
    - 재현 가능성 (상/중/하)
    - 추정 원인 (Sequential Thinking으로 3단계 분석)
    - 관련 소스 파일 경로
    - 재현 pytest 테스트 코드 초안

    가장 재현 가능성이 높은 이슈 1개에 대해:
    - 새 브랜치 fix/issue-NNN 생성
    - 테스트 코드 커밋
    - PR 초안 생성 (Draft 상태)

    모든 파일 변경은 Plan 모드로 먼저 검토.
    ```

!!! tip "💡 꿀팁: Draft PR로 시작"
    Claude가 생성한 PR은 반드시 **Draft 상태**로 시작하게 하세요. 당신이 수동 검토 후 Ready for review로 승격합니다.

---

## 워크플로우 4 — 일일 개발 루틴 자동화

### 목표
매일 아침 10분을 절약하는 '루틴 브리핑'.

```text
08:30 — 하루 시작
  ↓
[GitHub MCP] 어제 닫힌 이슈/머지된 PR 조회
  ↓
[Memory MCP] 어제 작업 중단 지점 불러오기
  ↓
[Sequential Thinking] 오늘의 우선순위 TOP 3 추천
  ↓
[Filesystem MCP] TODO.md 업데이트
  ↓
08:40 — 브리핑 완료
```

!!! example "🤖 Claude Code 프롬프트: 아침 브리핑"
    ```
    오늘의 개발 브리핑을 만들어줘.

    1. GitHub MCP: 어제(24시간 내) 내가 리뷰어인 PR과 할당된 이슈 목록
    2. Memory MCP: 어제 저장한 "오늘 할 일"을 불러오기
    3. Sequential Thinking: 위 두 정보를 종합해 오늘의 우선순위 TOP 3
    4. Filesystem MCP: TODO.md 의 맨 위에 오늘 날짜로 이 내용을 추가

    브리핑은 한국어로, 이모지 없이, 간결하게.
    ```

---

## 조합 설계 시 체크리스트

- [ ] 각 단계가 실패했을 때 다음 단계가 안전하게 중단되는가?
- [ ] Plan 모드로 전체 변경 계획을 한 번에 볼 수 있는가?
- [ ] 민감한 작업(DB 쓰기, GitHub push)은 명시적 승인이 필요한가?
- [ ] 같은 프롬프트를 다른 프로젝트에 재사용할 수 있게 일반화됐는가?

!!! danger "🚨 자주 발생하는 함정: 'MCP 과신'"
    모든 것을 MCP로 자동화하려 하지 마세요. **검토가 필요한 단계**는 중간에 "사람 확인" 지점을 넣는 게 장기적으로 안전합니다. "이 단계까지 하고 나한테 확인 받고 나서 다음 단계 진행해줘" 라는 한 마디를 잊지 마세요.

---

## 다음 단계

MCP 파트는 여기서 마무리합니다. 다음은 **GSTACK**입니다. 설치와 23개 스킬 개요로 넘어갑니다.
