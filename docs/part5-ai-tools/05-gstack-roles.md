# 5-5. GSTACK 역할별 활용 가이드

> CEO / Engineer / QA / Release 네 역할별로 GSTACK 스킬을 실전에서 어떻게 쓰는지 보여드립니다.

---

## CEO 역할 — 전략을 먼저 세운다

### 쓰는 이유
코드를 짜기 전에 "이게 왜 필요한가"를 검증해야 합니다. 그렇지 않으면 6개월 후 "아무도 안 쓰네" 하는 프로젝트가 됩니다.

### 주요 스킬
- `/office-hours` — 초기 전략 상담
- `/plan-ceo-review` — 계획서 비즈니스 임팩트 평가

!!! example "🤖 `/office-hours` 실제 대화"
    ```
    /office-hours

    AI 기반 문서 자동화 SaaS를 만들려 합니다.
    - 타겟: 중소기업 (1-50명)
    - 핵심 기능: PDF/Word 자동 생성, 템플릿 관리
    - 예상 MRR: $5,000
    - 강점: Python 팀, ML 경험
    ```

    **Claude (GSTACK /office-hours) 응답 요약:**
    > **Q1 (Demand Reality):** 실제로 돈을 낼 10명을 찾았나요? 인터뷰 기록이 있나요?
    >
    > **Q2 (Status Quo):** 지금 그들은 어떻게 해결하고 있죠? 구글 독스 + 수작업? 기존 SaaS?
    >
    > **Q3 (Desperate Specificity):** 10명 중 "지금 당장 돈 내고 쓰고 싶다"는 사람이 몇 명?
    >
    > **Q4 (Narrow Wedge):** MVP 범위를 1개 산업(예: 변호사 사무소)으로 좁힐 수 있나요?
    >
    > **Q5 (Observation):** 잠재 고객 옆에서 하루 일과를 관찰했나요?
    >
    > **Q6 (Future-fit):** 5년 후에도 이 문제가 존재할까요?
    >
    > 당신의 답변에 따라 다음 스텝을 제안드리겠습니다.

!!! example "🤖 `/plan-ceo-review` 프롬프트"
    ```
    /plan-ceo-review

    다음 스프린트 계획을 리뷰해주세요:
    [sprint_plan.md 내용 붙여넣기]

    특히 다음 관점으로 봐주세요:
    - 리소스 할당이 핵심 가설 검증에 집중되어 있는가?
    - 일정이 현실적인가?
    - 가장 큰 위험은 무엇인가?
    ```

!!! warning "⚠️ 주의: CEO 모드는 쓴소리를 합니다"
    `/office-hours`와 `/plan-ceo-review`는 의도적으로 불편한 질문을 던집니다. 기분 상하지 말고 "내가 보지 못한 각도"를 얻는 기회로 활용하세요.

---

## Engineer 역할 — 기술적 타당성을 검증한다

### 주요 스킬
- `/plan-eng-review` — 아키텍처·기술 스택 리뷰
- `/review` — 코드 리뷰 (PR 단위)
- `/think` — Sequential Thinking 기반 심층 분석

### 시나리오: 마이크로서비스 설계 리뷰

!!! example "🤖 `/plan-eng-review` 프롬프트"
    ```
    /plan-eng-review

    다음 아키텍처를 리뷰해주세요:
    - API Gateway: Kong
    - User Service: Node.js (Fastify)
    - Document Service: Python FastAPI
    - AI Service: Python FastAPI + PyTorch
    - Queue: RabbitMQ
    - DB: PostgreSQL (주), Redis (캐시)
    - Infra: Docker + K8s on AWS EKS

    특히 다음을 확인해주세요:
    - 서비스 경계가 합리적인가?
    - 단일 장애점(SPOF)은 어디인가?
    - 초기 MVP에 오버엔지니어링이 아닌가?
    ```

    **GSTACK 응답 방향:**
    - 서비스 수가 팀 크기(1명)에 비해 과도 → 모놀리식부터 시작 권장
    - User Service와 Document Service는 동일 DB 트랜잭션이 필요할 가능성 → 분리 근거 재검토
    - K8s는 운영 복잡도 높음 → Fargate 또는 Fly.io 권장

### 시나리오: 코드 리뷰

!!! example "🤖 `/review` 프롬프트"
    ```
    /review

    내 PR #42 를 리뷰해줘. 주요 변경 파일은 services/payment.py.
    특히 다음 관점으로 봐줘:
    - 동시성 문제 (여러 요청 동시 처리 시)
    - 에러 처리 누락
    - 보안 (SQL Injection, XSS)
    - N+1 쿼리 패턴
    ```

    Claude는 다음 형태로 응답합니다.

    ```text
    REVIEW SUMMARY
    ==============
    Critical: 2건
    Warning:  5건
    Info:     3건

    [CRITICAL 1] services/payment.py:87
    > 동시성 문제 — SELECT balance 와 UPDATE 사이에 트랜잭션이
    > 없어 race condition 가능. SELECT ... FOR UPDATE 필요.

    [CRITICAL 2] services/payment.py:134
    > SQL Injection — f-string으로 쿼리 조립. 파라미터 바인딩 필요.

    [WARNING 1] ...
    ```

!!! tip "💡 꿀팁: `/review`는 PR 머지 전 습관으로"
    GitHub Actions에 `/review` 결과를 PR 코멘트로 자동 등록하는 워크플로우를 짜두면, 팀 전체가 일관된 품질 기준을 공유하게 됩니다.

### 시나리오: 심층 분석

!!! example "🤖 `/think` 프롬프트"
    ```
    /think

    우리 AI 서비스의 평균 레이턴시가 500ms인데
    100ms 이하로 줄여야 합니다.
    현재 스택: FastAPI + PyTorch + GPU 인스턴스 1대
    Sequential Thinking으로 병목 → 원인 → 솔루션 →
    구현 계획 → 검증 순서로 분석해주세요.
    ```

---

## QA 역할 — 품질 안전망을 만든다

### 주요 스킬
- `/qa` — 코드 + 테스트 + 성능 종합
- `/qa-only` — 테스트 커버리지만 집중

!!! example "🤖 `/qa` 프롬프트"
    ```
    /qa

    src/ 디렉토리 전체를 검사해줘.
    - 코드 품질 점수 (0-10)
    - 테스트 커버리지 %
    - 중/고 위험 이슈 목록
    - 부족한 테스트 케이스 제안 (+ 코드 초안)
    ```

!!! example "🤖 `/qa-only` 프롬프트"
    ```
    /qa-only

    tests/ 폴더의 기존 pytest 스위트를 실행하고
    실패 케이스를 분석해줘.
    커버리지가 80% 이하인 모듈에 대해
    부족한 테스트를 자동 생성해서 추가해줘.
    추가 전에 Plan 모드로 미리보기.
    ```

!!! danger "🚨 자주 발생하는 함정: '100% 커버리지 맹신'"
    커버리지 100%가 품질 100%는 아닙니다. `/qa`는 커버리지와 함께 **엣지 케이스 누락**도 지적합니다. 숫자만 보지 마세요.

---

## Release 역할 — 안전하게 배포한다

### 주요 스킬
- `/ship` — 체크리스트 + 배포
- `/land-and-deploy` — PR 머지 + 배포 + 모니터링
- `/canary` — 점진적 롤아웃

!!! example "🤖 `/ship` 프롬프트"
    ```
    /ship

    v2.0 배포 준비해줘.
    - 대상 브랜치: main
    - 대상 환경: production
    - 릴리스 노트: RELEASE_v2.0.md

    체크리스트를 하나씩 확인하고, 각 항목에 대해
    통과/실패를 보고해줘. 실패 항목이 있으면 배포 중단.
    ```

    **예상 체크리스트:**
    ```text
    ☑ 모든 테스트 통과?          (pytest, jest)
    ☑ 코드 리뷰 완료?            (최소 1명 승인)
    ☑ 보안 검사 통과?            (bandit, npm audit)
    ☑ DB 마이그레이션 dry-run?    (alembic)
    ☑ 롤백 스크립트 준비?         (db_rollback.sql)
    ☑ 모니터링 대시보드 준비?     (Grafana)
    ☑ on-call 알림 등록?         (PagerDuty)
    ```

!!! example "🤖 `/canary` 프롬프트"
    ```
    /canary

    v2.0을 3단계로 롤아웃해줘:
    - Phase 1: 5% 트래픽, 1시간 관찰
    - Phase 2: 25% 트래픽, 30분 관찰
    - Phase 3: 100%

    각 단계에서 에러율 > 0.5% 또는 p99 > 500ms 이면 자동 롤백.
    단계 전환 전에 나한테 확인받아줘.
    ```

!!! warning "⚠️ 주의: 첫 배포는 반드시 금요일 오후 금지"
    개발 업계 유명한 농담 "Don't deploy on Friday"에는 진짜 이유가 있습니다. 주말에 문제가 생기면 대응이 늦습니다. `/ship`의 체크리스트에 "오늘이 금요일 오후인가?" 항목도 넣어두세요.

---

## 역할 간 전환 흐름

```text
[기획]    /office-hours → /plan-ceo-review
[설계]    /plan-eng-review → /think
[구현]    ...코드 작성...
[검증]    /review → /qa
[배포]    /ship → /canary → /land-and-deploy
[회고]    /retro → /document-release
```

!!! info "📌 핵심 요약"
    GSTACK의 진짜 가치는 **한 명이 여러 역할을 오가며 일관된 기준**으로 판단할 수 있게 해주는 것입니다. 혼자 개발하는 대학생이 CEO, 엔지니어, QA, 배포 엔지니어의 체크리스트를 각각 들고 있기는 어렵거든요.

다음 페이지에서는 GSTACK과 MCP를 묶어 **프로젝트 라이프사이클 전체**를 자동화하는 방법을 다룹니다.
