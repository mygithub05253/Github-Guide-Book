# 5-6. GSTACK + MCP 시너지 워크플로우

> 역할 기반 GSTACK 스킬과 도구 기반 MCP 서버를 결합해 **프로젝트 라이프사이클 전체**를 자동화합니다.

---

## 핵심 개념: 역할 × 도구의 2D 매트릭스

- **GSTACK (세로 축)** = "어떤 관점에서 볼 것인가" (CEO, Engineer, QA...)
- **MCP (가로 축)** = "어떤 도구를 쓸 것인가" (GitHub, Filesystem, Postgres...)

두 축이 만나면 이런 작업이 가능해집니다.

```text
                GitHub MCP   Filesystem MCP   Postgres MCP   Playwright MCP
/office-hours     경쟁사 PR 분석   -              -              -
/plan-eng-review  -              아키텍처 스캔   스키마 리뷰     -
/review           PR diff 분석   소스 리팩토링   -              -
/qa               -              테스트 생성    쿼리 테스트     E2E 테스트
/ship             릴리스 노트   빌드 검증       마이그레이션   스모크 테스트
```

---

## 풀 사이클 예제: "AI 이메일 템플릿 생성기" SaaS

10주짜리 프로젝트를 GSTACK + MCP로 실행한 실제 흐름입니다.

### Week 1: 전략 수립

```text
CEO 역할 (/office-hours + /plan-ceo-review)
├─ 시장 조사 (Playwright MCP로 경쟁사 5개 스크랩)
├─ 가격대 분석 ($10-30/월 Saas 70개 조사)
├─ MVP 범위 정의 (1개 페르소나: 마케터)
└─ 6개월 로드맵
```

!!! example "🤖 프롬프트: 경쟁사 조사 자동화"
    ```
    /office-hours 와 Playwright MCP를 조합해서 다음을 수행해줘:
    1. G2.com에서 "email template" 카테고리 상위 10개 SaaS 스크랩
    2. 각 제품의 가격대, 핵심 기능, 리뷰 요약
    3. 공통적으로 부족한 기능(Claude가 보기에) TOP 3
    4. 위 데이터를 근거로 /office-hours 스타일 포지셔닝 전략
    ```

### Week 2: 기술 설계

```text
Engineer 역할 (/plan-eng-review + /think)
├─ 스택 선택: Next.js + FastAPI + PostgreSQL + GPT-4 API
├─ /think (Sequential Thinking): LLM 레이턴시 최적화 전략
└─ Filesystem MCP: 프로젝트 스캐폴딩
```

### Week 3-6: 개발 구현

```text
매일 루틴:
┌──────────────────────────────────┐
│ 아침: /daily + Memory MCP         │
│ 오전: 코딩                        │
│ 점심 전: /review + GitHub MCP     │
│ 오후: 코딩                        │
│ 저녁: /retro (작은 회고)          │
└──────────────────────────────────┘
```

### Week 7-8: 품질 보증

```text
QA 역할 (/qa + /qa-only)
├─ Filesystem MCP: 테스트 커버리지 스캔
├─ Playwright MCP: E2E 시나리오 자동화
├─ Postgres MCP: 부하 테스트 (10,000 rows insert)
└─ /cso: 보안 감사
```

!!! example "🤖 프롬프트: 통합 QA"
    ```
    /qa 를 다음 MCP와 조합해서 실행해줘:
    1. Filesystem MCP: src/ 전체 커버리지 측정
    2. Playwright MCP: 5개 핵심 사용자 시나리오 E2E 실행
    3. Postgres MCP: 부하 쿼리 100개 랜덤 실행 후 p99 측정
    4. /cso: 인증/인가 흐름 보안 검토

    종합 보고서를 docs/qa-report.md 로 저장.
    통과 기준 미달 항목은 명확히 표시.
    ```

### Week 9: 배포 준비

```text
Release 역할 (/document-release + /ship)
├─ GitHub MCP: 변경사항 집계 → 릴리스 노트 자동 생성
├─ Filesystem MCP: CHANGELOG.md 업데이트
├─ Docker MCP: 프로덕션 이미지 빌드 및 태깅
└─ /ship: 체크리스트 실행
```

### Week 10: 점진적 롤아웃

```text
/canary
├─ Phase 1: 5% 트래픽 (1시간)
│   └─ Playwright MCP: 5분마다 스모크 테스트
├─ Phase 2: 25% 트래픽 (30분)
│   └─ Postgres MCP: 에러 로그 쿼리
└─ Phase 3: 100%
    └─ /document-release: 최종 릴리스 공지
```

---

## 자동화 수준을 단계별로 올리기

!!! info "📌 핵심 요약: 4단계 자동화"
    - **Level 0** — 모든 것을 수동 (대학생 시작점)
    - **Level 1** — GSTACK 스킬 단독 사용 (`/review`, `/ship`)
    - **Level 2** — 단일 MCP 통합 (GitHub MCP + `/review`)
    - **Level 3** — 멀티 MCP 파이프라인 (이 페이지 예제들)
    - **Level 4** — GitHub Actions + 예약 실행 (Level 3을 CI에서 자동 실행)

처음부터 Level 4를 노리지 마세요. Level 1에서 한 달, Level 2에서 한 달 쌓아가세요.

---

## 시너지의 함정들

!!! danger "🚨 함정 1: 복잡성 폭발"
    4~5개 MCP를 한 프롬프트에 묶으면 디버깅이 지옥이 됩니다. **한 프롬프트당 MCP 2-3개가 스윗 스팟**입니다.

!!! danger "🚨 함정 2: 권한 과다 부여"
    배포 자동화를 위해 GitHub PAT에 `admin:org` 권한까지 주면, 사고 시 피해가 큽니다. **최소 권한 원칙**을 지키세요.

!!! danger "🚨 함정 3: '검토 없이 머지' 안티패턴"
    GSTACK이 짠 코드를 바로 머지하지 마세요. 사람이 최종 검토하는 단계는 **절대 빼지 마세요**.

!!! tip "💡 꿀팁: 자동화는 체크리스트부터"
    자동화 스크립트를 짜기 전에, **사람이 수동으로 그 워크플로우를 5번 실행**해보세요. 5번 동안 발견한 예외 상황들을 스크립트에 반영하면 훨씬 견고한 자동화가 됩니다.

---

## 체크리스트

- [ ] 내 프로젝트에 맞는 2D 매트릭스(역할×도구)를 종이에 그려봤다
- [ ] Level 1 자동화 (GSTACK 스킬 단독) 먼저 안정화했다
- [ ] 첫 MCP 통합 프롬프트를 Plan 모드로 실행했다
- [ ] 자동화 실패 시 수동 폴백 절차가 있다

다음 페이지에서는 **Plan 모드와 Sequential Thinking**을 깊이 다룹니다.
