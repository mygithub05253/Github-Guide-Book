# Part 2. 프레임워크 및 언어별 학습 레포지토리

> "프레임워크를 배우고 싶은데, 공식 문서는 너무 방대하고 유튜브는 너무 얕아요."
> 이 파트는 **10,000+ Stars 오픈소스 레포를 교재처럼 활용하는 방법**을 알려줍니다.

---

## 이 파트에서 얻어갈 것

여러분이 이 파트를 끝까지 따라오면, 다음 세 가지 능력을 얻게 됩니다.

1. **대형 오픈소스 레포를 무서워하지 않게 됩니다.** 76,000 Stars짜리 `spring-boot` 레포도, 244,000 Stars짜리 `facebook/react` 레포도 "어느 디렉토리부터 열어야 하는지" 알게 됩니다.
2. **Claude Code를 코드 읽기 과외 선생님처럼 쓰게 됩니다.** 수천 개의 파일을 혼자 헤매는 대신, 질문을 던져 30분 만에 구조를 파악할 수 있습니다.
3. **실전 스택 조합**을 익히게 됩니다. Spring Boot + React + Next.js는 금융권·공기업·스타트업 모두에서 통용되는 "안전한 풀스택 조합"입니다.

!!! info "📌 핵심 요약"
    이 파트는 레포 전체 코드를 옮겨 적지 않습니다. 대신 **"어디를 먼저 읽을지, 무엇을 Claude에게 물어볼지, 어떤 에러가 나올지"** 를 안내하는 실전 매뉴얼입니다.

---

## 학습 목표

- [ ] 백엔드 프레임워크 **Spring Boot** 생태계의 5대 필수 레포를 파악한다
- [ ] 프론트엔드 **React** 생태계에서 "무엇을 배우고 무엇은 건너뛸지" 구분한다
- [ ] **Next.js** App Router의 모범 사례를 읽을 수 있는 레포를 안다
- [ ] 각 레포에 대해 **Claude Code 프롬프트 3개 이상**을 스스로 작성할 수 있다
- [ ] 자주 발생하는 빌드/실행 에러 Top 3를 미리 알고 대비한다

---

## 어떤 순서로 배워야 할까요?

학습 순서는 여러분의 현재 상태에 따라 다릅니다. 아래 표를 참고해서 **건너뛸 것은 과감히 건너뛰세요.**

| 현재 상태 | 추천 순서 | 예상 기간 |
| --- | --- | --- |
| 백엔드/프론트엔드 경험 0 | 01 → 02 → 03 → 04 | 4주 |
| Java는 좀 아는데 Spring Boot는 처음 | 01 → 04 → (여유되면 02, 03) | 2주 |
| React는 익숙한데 Next.js는 처음 | 03 → 02 (보강) → 04 | 2주 |
| 풀스택 포트폴리오 준비 | 01 + 03 병행 → 04 | 3주 |

!!! tip "💡 꿀팁: 세 마리 토끼는 없어요"
    Spring Boot, React, Next.js를 **동시에** 배우려 하지 마세요. 한 번에 하나씩, 작은 예제 하나를 완전히 실행해보는 것이 수백 시간 강의보다 낫습니다. "내가 만든 게 브라우저에서 움직였다"는 경험이 학습의 80%입니다.

---

## 이 파트에서 다루는 레포 한눈에 보기

### 2-1. Spring Boot 생태계 (→ [01-spring-boot.md](01-spring-boot.md))
- `spring-projects/spring-boot` (76K+) — 프레임워크 본체
- `eugenp/tutorials` (37K+) — Baeldung 예제 보물창고
- `macrozheng/mall` (83K+) — 실전 전자상거래 시스템
- `iluwatar/java-design-patterns` (90K+) — 디자인 패턴 교과서
- `gothinkster/realworld` (80K+) — 동일 스펙 다중 구현 비교

### 2-2. React 생태계 (→ [02-react.md](02-react.md))
- `facebook/react` (244K+) — React 본체
- `typescript-cheatsheets/react` (45K+) — TS+React 치트시트
- `alan2207/bulletproof-react` (29K+) — 실무 구조 모범 답안

### 2-3. Next.js 생태계 (→ [03-nextjs.md](03-nextjs.md))
- `vercel/next.js` (130K+) — 프레임워크 본체 + 100+ 예제
- `vercel/commerce` (11K+) — App Router 프로덕션 템플릿

### 2-4. 학습 체크리스트 (→ [04-checklist.md](04-checklist.md))

---

## 시작하기 전에 준비할 것

!!! warning "⚠️ 이게 없으면 뒤에서 계속 막힙니다"
    - **Java 17 이상** (Spring Boot 3.x는 Java 17+ 필수)
    - **Node.js 20 LTS 이상** (React, Next.js 실행용)
    - **Git 2.40+** (`--depth 1` shallow clone 쓸 예정)
    - **IDE**: IntelliJ IDEA Community (Java용), VS Code (JS/TS용)
    - **Docker Desktop** (`macrozheng/mall` 실행 시 필요, 나머지는 선택)

설치 확인 명령어는 각 페이지 "사전 준비" 섹션에 친절히 적어두었으니 걱정 마세요.

!!! example "🤖 Claude Code 프롬프트: 내 환경 점검"
    > "내 PC에 Java, Node.js, Git, Docker가 설치되어 있는지 각각 버전 확인 명령어를 알려주고, 설치 안 된 게 있으면 Windows 환경 기준 설치 방법을 step-by-step으로 알려줘."

준비가 됐다면 [01-spring-boot.md](01-spring-boot.md)부터 시작합시다. 선배가 옆에 앉아있다 생각하고, 천천히 따라오세요.
