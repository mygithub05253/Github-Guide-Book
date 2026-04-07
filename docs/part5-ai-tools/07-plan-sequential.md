# 5-7. Plan 모드 & Sequential Thinking 활용법

> Plan 모드와 Sequential Thinking은 Claude Code를 **안전하면서도 똑똑하게** 쓰는 두 축입니다. 하나는 '손을 조심히', 하나는 '머리를 깊게'.

---

## Plan 모드 — 변경사항 미리보기

### 한 줄 요약
"실제로 파일을 바꾸기 전에, 무엇을 바꿀 예정인지 먼저 보여주는 모드"입니다.

### 일반 모드 vs Plan 모드

```text
일반 모드                Plan 모드
───────                 ────────
사용자 요청              사용자 요청
    ↓                       ↓
즉시 파일 수정           계획 작성
    ↓                       ↓
결과 반영                사용자 검토
                            ↓
                        승인 / 편집 / 취소
                            ↓
                        실제 파일 수정
```

### 진입 방법

1. **키보드 단축키** — `Shift + Tab` 두 번 (가장 빠름)
2. **명령어** — `/plan` 또는 "Plan 모드로 실행해줘"
3. **메뉴** — Claude Code 우측 상단 토글

### 언제 켜야 하나

!!! info "📌 Plan 모드 추천 상황"
    - 파일 10개 이상 수정
    - 기존 코드 대규모 리팩토링
    - 설정 파일 변경 (`database.yml`, `config.json`, `package.json`)
    - 마이그레이션 스크립트 실행
    - 처음 써보는 MCP 조합

!!! tip "💡 꿀팁: 의심스러우면 일단 Plan 모드"
    '켤까 말까' 고민되는 순간은 거의 항상 켜는 게 맞습니다. 3초 더 걸릴 뿐이고, 하루를 날리지 않습니다.

### 실전 예제: React 리팩토링

!!! example "🤖 Claude Code 프롬프트"
    ```
    /plan
    src/components/UserProfile.jsx 의 클래스형 컴포넌트를
    함수형 + Hooks 로 리팩토링해줘.
    PropTypes는 유지. 테스트가 있으면 같이 업데이트.
    ```

    **Plan Preview 예시:**
    ```diff
    PLAN: React 리팩토링
    ────────────────────
    1. src/components/UserProfile.jsx
       - 클래스형 → 함수형
       - this.state → useState
       - componentDidMount → useEffect
       - 라인 수: 42 → 28 (-33%)

    2. src/components/UserProfile.test.jsx
       - shallow() → render() (RTL)
       - instance() 호출 제거

    Files: 2
    Estimated time: 30 seconds

    [Apply] [Edit Plan] [Cancel]
    ```

### Plan 편집 (`Ctrl+G`)

계획을 보고 "이건 뺐으면" 싶으면 `Ctrl+G`로 편집 모드 진입:

```text
Original Plan:
1. UserProfile.jsx 리팩토링 ✓
2. UserProfile.test.jsx 업데이트 ✓
3. Storybook 스토리 업데이트 ✓

Edited:
1. UserProfile.jsx 리팩토링 ✓
2. UserProfile.test.jsx 업데이트 ✓
3. (삭제) Storybook은 나중에
4. (추가) JSDoc 주석 작성
```

### Plan 모드 체크리스트 (검토할 때)

- [ ] 변경 파일 목록이 내 의도와 일치하는가?
- [ ] 삭제되는 코드가 실제로 불필요한가?
- [ ] 신규 코드의 핵심 로직을 이해하는가?
- [ ] 테스트 파일도 함께 업데이트되는가?
- [ ] DB 마이그레이션이나 config 변경이 포함되어 있는가? (있으면 특히 주의)

!!! danger "🚨 자주 발생하는 함정: 'Apply 연타'"
    Plan 내용을 제대로 안 읽고 Apply를 누르는 게 Plan 모드를 쓰는 의미를 없앱니다. 리뷰에 **최소 30초** 써야 진짜 Plan 모드입니다.

---

## Sequential Thinking — 단계별 논리 추론

### 한 줄 요약
"Claude가 한 번에 답하지 않고, 가설→검증→결론을 단계별로 작성하게 만드는 기법"입니다.

### 일반 응답 vs Sequential Thinking

**일반:**
> Q: "100을 소인수분해 해줘"
> A: `100 = 2² × 5²` *(끝)*

**Sequential Thinking:**
> **Step 1:** 100 ÷ 2 = 50
> **Step 2:** 50 ÷ 2 = 25
> **Step 3:** 25 ÷ 5 = 5
> **Step 4:** 5 ÷ 5 = 1
> **결론:** `2² × 5²`

소인수분해 같은 간단한 문제는 의미 없지만, **복잡한 문제**에서 이 차이는 정답률을 크게 좌우합니다.

### 언제 쓰나

!!! info "📌 추천 시나리오"
    - 알고리즘 설계 (시간/공간 복잡도 근거)
    - 아키텍처 결정 (A vs B 비교)
    - 버그 원인 분석 (가설 3개 → 검증 순서)
    - 성능 최적화 (병목 식별 → 솔루션 우선순위)
    - 보안 위협 모델링 (STRIDE)

!!! warning "⚠️ 비추천 시나리오"
    - 단순 문법 질문 ("파이썬 리스트 뒤집기")
    - 빠른 답변이 필요할 때
    - 이미 결정 난 구현 작업

### 호출 방법

1. **MCP 방식** — `sequential-thinking` MCP 설치 후 Claude가 자동 호출
2. **프롬프트 방식** — "Sequential Thinking으로 분석해줘" 한 마디 추가
3. **GSTACK 방식** — `/think` 슬래시 명령어

### 실전 예제 1: 성능 최적화

!!! example "🤖 프롬프트"
    ```
    Sequential Thinking으로 분석해줘.

    우리 Spring Boot API의 GET /api/posts 엔드포인트가
    평균 1.2초 걸려. 목표는 200ms.
    - 일일 요청: 50만
    - DB: PostgreSQL, posts 테이블 50만 행
    - ORM: JPA / Hibernate
    - 캐시: 없음

    병목 식별 → 원인 → 솔루션 우선순위 → 구현 계획 순서로.
    ```

    **예상 응답 구조:**
    ```text
    [Step 1 — 병목 식별]
    측정 필요 지표: DB query time, serialization time, network
    추정 분포: DB 800ms / 직렬화 200ms / 네트워크 200ms

    [Step 2 — 원인 분석]
    DB 800ms의 원인 후보:
    - 후보 A: N+1 쿼리 (JPA 기본 LAZY) — 확률 70%
    - 후보 B: 인덱스 부재 — 확률 20%
    - 후보 C: 커넥션 풀 경합 — 확률 10%

    [Step 3 — 검증 방법]
    - A: Hibernate SQL 로그 활성화 후 쿼리 수 카운트
    - B: EXPLAIN ANALYZE 실행
    - C: HikariCP 메트릭 확인

    [Step 4 — 솔루션 우선순위]
    1. N+1 해결: JOIN FETCH or @EntityGraph (예상 효과 600ms↓)
    2. 인덱스 추가: created_at, author_id 복합 인덱스 (100ms↓)
    3. Redis 캐시: TTL 60초, 핫 페이지만 (50ms↓)

    [Step 5 — 구현 계획]
    Day 1: 로그 활성화 + 가설 검증
    Day 2: N+1 수정 + 성능 측정
    Day 3: 인덱스 추가 + 측정
    Day 4: Redis 캐시 + 측정
    Day 5: 부하 테스트 + 모니터링 설정
    ```

### 실전 예제 2: 보안 위협 분석

!!! example "🤖 프롬프트"
    ```
    Sequential Thinking + STRIDE 모델로 분석해줘.
    우리 금융 거래 API에 다음 위협이 있을 수 있나?

    시나리오: 사용자 잔액 1000원, 동시에 600원 출금 요청 2건.

    Step별로 가능한 공격 → 영향 → 대응책 → 테스트 방법 순서.
    ```

---

## Plan 모드 + Sequential Thinking 조합

두 기법은 같이 쓰면 시너지가 큽니다.

```text
Sequential Thinking → 무엇을 바꿀지 논리적 결정
        ↓
Plan 모드 → 어떻게 바꿀지 미리보기
        ↓
Apply → 안전하게 실행
```

!!! example "🤖 프롬프트: 조합 예시"
    ```
    /plan
    다음 작업을 Sequential Thinking으로 먼저 설계하고,
    설계 결과를 Plan으로 변환해줘:

    "src/legacy/*.js 파일 12개를 TypeScript로 마이그레이션.
     각 파일의 의존성 그래프를 고려해 변환 순서를 결정.
     단일 책임 원칙에 어긋나는 파일은 쪼개서 변환."
    ```

---

## 체크리스트

- [ ] Plan 모드 단축키(`Shift+Tab ×2`)를 몸으로 기억했다
- [ ] 대규모 변경은 언제나 Plan 모드로 시작한다
- [ ] Sequential Thinking MCP를 설치했다
- [ ] 복잡한 결정에는 "Sequential Thinking으로" 접두사를 붙인다
- [ ] 두 기법을 조합한 프롬프트를 최소 1번 실행했다

다음 페이지에서는 **실전 통합 프로젝트 사례**를 봅니다.
