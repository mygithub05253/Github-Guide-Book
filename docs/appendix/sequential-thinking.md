# 부록 B: Sequential Thinking 완전 가이드

> Sequential Thinking은 "즉답" 대신 "단계별 논리 전개"를 강제하는 기법입니다. 이 부록은 Part 5-7의 확장판입니다.

---

## B-1. 한 줄 정의

Claude가 "결론만" 말하지 않고, **가설 → 분석 → 검증 → 결론** 순서로 답하게 만드는 MCP 서버 + 프롬프트 패턴입니다.

---

## B-2. 일반 응답과의 차이 (짧은 예)

**질문:** "100을 소인수분해 해줘"

**일반 응답:**
```text
100 = 2² × 5²
```

**Sequential Thinking:**
```text
Step 1: 100 ÷ 2 = 50
Step 2: 50 ÷ 2 = 25
Step 3: 25 ÷ 5 = 5
Step 4: 5 ÷ 5 = 1

나온 소인수: 2, 2, 5, 5
결론: 2² × 5²
```

**장점:** 논리가 보이므로 검증·수정이 쉽다. 복잡한 문제일수록 차이가 극명해집니다.

---

## B-3. 설치

```bash
claude mcp add sequential-thinking -s local -- \
  npx -y @modelcontextprotocol/server-sequential-thinking
```

확인:
```bash
claude mcp list | grep sequential
```

!!! info "예상 출력"
    ```text
    ✓ sequential-thinking  (local scope)
    ```

---

## B-4. 작동 원리

```text
입력: 복잡한 문제
     ↓
┌─────────────────────────────┐
│ Step 1: 문제 분해            │
│  - 핵심 요소 식별            │
│  - 선행 조건 확인            │
└─────────────────────────────┘
     ↓
┌─────────────────────────────┐
│ Step 2: 단계별 분석          │
│  - 각 단계의 근거            │
│  - 중간 결과 검증            │
└─────────────────────────────┘
     ↓
┌─────────────────────────────┐
│ Step 3: 오류 확인            │
│  - 논리적 모순?              │
│  - 가정 재검토               │
└─────────────────────────────┘
     ↓
┌─────────────────────────────┐
│ Step 4: 결론 도출            │
│  - 신뢰도 명시               │
└─────────────────────────────┘
     ↓
출력: 검증된 답변
```

---

## B-5. 언제 쓰나 (결정 매트릭스)

| 상황 | Sequential Thinking? |
|------|---------------------|
| 알고리즘 설계 (시간복잡도 비교) | ✅ 강력 추천 |
| 아키텍처 결정 (A vs B vs C) | ✅ 강력 추천 |
| 버그 원인 분석 (가설 여러 개) | ✅ 강력 추천 |
| 성능 최적화 (병목 찾기) | ✅ 추천 |
| 보안 위협 모델링 | ✅ 추천 |
| 단순 문법 질문 | ❌ 오버킬 |
| 이미 정해진 작업 실행 | ❌ 오버킬 |
| 빠른 답변 필요 | ❌ 느려짐 |

---

## B-6. 실전 예제 3종

### 예제 1: 알고리즘 설계

!!! example "🤖 프롬프트"
    ```
    Sequential Thinking으로 분석해줘.

    문제: 1,000,000개 정수에서 중복을 제거하고 정렬.
    메모리 제한: 100MB.

    가능한 알고리즘을 최소 3개 비교하고,
    시간/공간 복잡도를 표로 정리해줘.
    가장 적합한 것을 추천하고 근거도.
    ```

**예상 응답 구조:**
```text
[Step 1 — 제약 분석]
- 1M 정수 × 4바이트 = 4MB (메모리는 여유)
- 정렬 필요 → O(n log n) 이하 필요

[Step 2 — 후보 알고리즘]
A. Set + Sort      : 시간 O(n log n), 공간 O(n)
B. HashSet + QuickSort : 시간 O(n log n), 공간 O(n)
C. BitMap (정수 범위 제한 시) : 시간 O(n), 공간 O(범위/8)

[Step 3 — 비교표]
| 알고리즘 | 시간    | 공간         | 구현 난이도 |
|---------|---------|-------------|------------|
| A       | n log n | n           | 쉬움       |
| B       | n log n | n           | 쉬움       |
| C       | n       | 범위/8 bits | 보통       |

[Step 4 — 결론]
정수 범위가 [0, 10^9]처럼 크면 A 또는 B.
범위가 [0, 10^7] 이하면 C가 10배 빠름.

추천: 정수 범위 모를 때 → A (Set + Sort, Python에선
sorted(set(arr)) 한 줄).
```

### 예제 2: 금융 시스템 동시성

!!! example "🤖 프롬프트"
    ```
    Sequential Thinking으로 설계해줘.

    금융 거래 플랫폼.
    시나리오: 잔액 $1000, 동시에 $600 출금 요청 2건.

    1. 문제 정의
    2. 원인 분석 (race condition)
    3. 해결 방안 3가지 (각각 SQL 예시)
    4. 금융권 규제 (PCI DSS) 적합성
    5. 최종 추천
    ```

**응답 흐름:**
- Step 1: 문제 = $400 잔액으로 둘 다 성공하면 -$200 (불가능)
- Step 2: SELECT-UPDATE 사이 원자성 결여
- Step 3:
  - **A. 비관적 잠금** `SELECT ... FOR UPDATE` — 간단/안전, 성능 ↓
  - **B. MVCC + SERIALIZABLE** — 동시성 ↑, 롤백 처리 필요
  - **C. 낙관적 잠금** version 컬럼 — 충돌 드물 때만
- Step 4: PCI DSS는 ACID 필수 → A 또는 B
- Step 5: 금융권은 A 추천 (검증 용이성)

### 예제 3: 버그 원인 분석

!!! example "🤖 프롬프트"
    ```
    Sequential Thinking으로 디버깅해줘.

    증상: 우리 API가 매일 새벽 3시에만 레이턴시 10배.
    스택: Node.js + Postgres + Redis.
    배포: AWS EC2 t3.medium × 2, RDS db.t3.small.

    가능한 원인 5개를 확률 순으로 나열하고,
    각각 30분 내에 확인할 수 있는 디버깅 방법을 제시해줘.
    ```

**예상 가설:**
1. **Postgres autovacuum (확률 40%)** — `pg_stat_progress_vacuum` 확인
2. **Redis 스냅샷 (RDB) (25%)** — Redis `SAVE` 설정 확인
3. **EC2 CPU credit 소진 (15%)** — CloudWatch `CPUCreditBalance`
4. **백업 잡 (10%)** — cron 확인
5. **네트워크 피크 (10%)** — VPC Flow Logs

---

## B-7. `/think` 슬래시 명령어

GSTACK 설치 시 `/think`는 Sequential Thinking을 자동 활성화합니다.

```text
/think
"우리 LLM 서비스 레이턴시를 500ms → 100ms로 줄이려면?"
```

---

## B-8. Sequential Thinking + Plan 모드 콤보

```text
Sequential Thinking (무엇을 바꿀지 결정)
         ↓
Plan 모드 (어떻게 바꿀지 미리보기)
         ↓
Apply
```

!!! example "🤖 프롬프트: 콤보"
    ```
    /plan
    Sequential Thinking으로 먼저 분석 후 Plan 생성:

    목표: src/legacy/ 의 PHP 코드 12개 파일을
    TypeScript + Express로 마이그레이션.

    1. Sequential Thinking으로 의존성 순서 결정
    2. 순서에 따른 파일별 변환 Plan
    3. 변환 후 pytest 대신 jest 테스트 추가
    ```

---

## B-9. 함정들

!!! danger "🚨 함정 1: 간단한 질문에 남용"
    "파이썬 리스트 뒤집기"도 Sequential Thinking으로 답하면 30초 낭비.

!!! danger "🚨 함정 2: 논리처럼 보이는 환각"
    Step 1-5가 매끄럽다고 결론이 옳은 건 아닙니다. 각 단계의 **근거**를 의심하세요.

!!! danger "🚨 함정 3: 사람보다 보수적일 수 있음"
    Claude는 종종 "안전한" 선택을 과도하게 권장합니다. 스타트업 상황에선 위험 감수가 필요할 때도 있습니다.

---

## 체크리스트

- [ ] `sequential-thinking` MCP 설치 완료
- [ ] "Sequential Thinking으로" 접두사 습관화
- [ ] 복잡한 결정 앞에서 `/think` 사용
- [ ] Plan 모드와 조합 시 효율 체감
- [ ] 함정 3가지를 인지
