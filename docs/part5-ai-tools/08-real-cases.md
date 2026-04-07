# 5-8. 실전 통합 프로젝트 사례

> 앞에서 배운 모든 것(MCP + GSTACK + Plan 모드 + Sequential Thinking)을 **실제 프로젝트**에 적용한 세 가지 사례입니다.

---

## 사례 1: 이 가이드북 프로젝트 자체 (메타 사례)

### 프로젝트 개요
- **이름:** PLAF (GitHub 가이드북)
- **목표:** Markdown 원본을 MkDocs 웹 + DOCX + PDF로 자동 빌드
- **규모:** 7개 파트, 약 5000줄

### 활용한 도구
- **Filesystem MCP** — `src/` 디렉토리 스캔, 구조 재배치
- **GitHub MCP** — 원격 레포 푸시, 릴리스 노트 자동화
- **Sequential Thinking** — 파트 간 의존성 분석, 학습 흐름 최적화
- **Plan 모드** — 파일 분할 작업 전 미리보기
- **GSTACK `/plan-ceo-review`** — "대학생에게 진짜 가치가 있나" 점검
- **GSTACK `/review`** — 각 페이지 품질 리뷰

### 핵심 워크플로우

```text
[기획]
/office-hours → "대학생 독자 가설 검증"
     ↓
[구조 설계]
Sequential Thinking → Part 1-6 학습 흐름 분석
     ↓
[작성]
Filesystem MCP로 src/*.md 생성
     ↓
[분할 리팩토링]
Plan 모드 → src/*.md 를 docs/ 하위로 분할
     ↓
[빌드]
python scripts/build_guidebook.py
     ↓
[배포]
GitHub MCP → GitHub Pages 업로드
```

!!! info "📌 핵심 요약"
    이 가이드북은 "문서 자동화 라이브러리로 문서를 만든다"는 메타 접근을 Claude Code + MCP로 실현한 예입니다. **가장 좋은 예제는 자기 자신**입니다.

---

## 사례 2: 스타트업 MVP — 3주 개발 일지

### 프로젝트 개요
- **아이디어:** 대학생 스터디 매칭 플랫폼
- **스택:** Next.js + Supabase + Vercel
- **개발자:** 1명 (주당 30시간)

### Week 1: 검증과 설계

**Day 1-2 (`/office-hours`)**
- 수요 가설: "시험 기간 스터디 모집글이 카톡 오픈채팅에 하루 50개 이상 올라온다"
- 검증: Playwright MCP로 실제 오픈채팅 5개 스크래핑 → 가설 확인
- 경쟁사 조사: 없음 (블루오션) — 의심하라는 `/office-hours` 경고
- 재검증: "없는 게 아니라 수요가 작아서 없을 수도" → 설문 조사 50명 진행

**Day 3-5 (`/plan-eng-review`)**
- 초기 계획: NestJS + Postgres + Redis + Docker
- `/plan-eng-review` 지적: "MVP 3주인데 과도함"
- 수정: Next.js + Supabase (인증/DB/스토리지 일체형)

!!! example "🤖 이때의 프롬프트"
    ```
    /plan-eng-review

    3주 내 MVP 출시 목표. 혼자 개발.
    기능: 회원가입, 스터디 모집글, 신청/수락, 오픈채팅 URL 공유.
    사용자 예상 50명.

    내 계획은 NestJS + Postgres + Redis + Docker + K8s야.
    현실적인가? 아니면 더 가벼운 대안 제안해줘.
    ```

    **Claude 응답 요약:**
    > K8s는 10명 이하 사용자엔 명백한 오버엔지니어링입니다. Supabase 추천 이유:
    > - 인증, DB, 스토리지, 실시간 채널 모두 내장
    > - 무료 플랜이 50명 규모에 충분
    > - Next.js 템플릿이 공식 제공

### Week 2: 구현

**매일 아침 루틴:**
```text
/daily → 오늘 할 일 3개
GitHub MCP → 어제 PR 상태 확인
Memory MCP → 전날 중단 지점 복원
```

**Day 10 (`/review`)**
- PR 5개 대량 생성 후 `/review`
- Critical 3건 지적: Supabase RLS 정책 누락 → 데이터 접근 권한 취약
- 수정 후 재리뷰

**Day 12 (`/think`)**
- 문제: 스터디 검색 속도 느림 (5초)
- Sequential Thinking: Supabase Full-Text Search vs 직접 인덱스 vs Algolia
- 결론: Postgres `tsvector` + GIN 인덱스 (무료, 500ms로 단축)

### Week 3: QA와 배포

**Day 16-18 (`/qa` + Playwright MCP)**
- 5개 핵심 시나리오 E2E 자동화
- 모바일 뷰포트 테스트
- 회원가입 → 글 작성 → 신청 → 매칭 전체 플로우 검증

**Day 20 (`/ship` + Vercel)**
- 체크리스트 통과 후 Vercel 프로덕션 배포
- 친구 5명에게 테스트 요청

**Day 21 (`/retro`)**
- 배운 점: "Supabase RLS는 반드시 작성 후 `/cso` 리뷰 필수"
- 다음 개선: 알림 기능, 리뷰 시스템

### 결과
- 3주 내 MVP 출시 성공
- 첫 주 가입자 27명 (목표 20명)
- 혼자 개발한 것 같지 않은 수준의 품질

---

## 사례 3: 레거시 코드베이스 현대화

### 배경
- 대학 동아리에서 관리하던 5년 전 PHP 사이트
- 20,000줄, 테스트 0개, 문서 없음
- 목표: 3개월 내 Next.js + FastAPI로 재작성

### 활용한 워크플로우

**Phase 1 — 분석 (2주)**
```text
Filesystem MCP → 전체 코드 스캔
     ↓
Sequential Thinking → 모듈 의존성 그래프 생성
     ↓
/plan-eng-review → "점진적 vs 빅뱅 재작성"
     ↓
결정: Strangler Fig 패턴 (점진적 치환)
```

!!! example "🤖 의존성 분석 프롬프트"
    ```
    Filesystem MCP로 legacy/ 디렉토리의 모든 .php 파일을 스캔하고,
    Sequential Thinking으로 다음을 분석해줘:

    1. 파일 간 include/require 의존성 그래프 (Mermaid)
    2. 가장 많이 참조되는 파일 TOP 10 (이걸 마지막에 치환)
    3. 외부 의존성 없는 리프 파일 (이걸 먼저 치환)
    4. 치환 순서 추천 (Strangler Fig 기준)
    ```

**Phase 2 — 치환 (8주)**
```text
매주 금요일 루틴:
/retro → 이번 주 회고
/plan-ceo-review → 다음 주 우선순위
/breakdown → 작업 쪼개기
```

**Phase 3 — 문서화 (2주)**
```text
Filesystem MCP → 새 코드 스캔
     ↓
/document-release → API 문서, README 자동 생성
     ↓
GitHub MCP → 릴리스 태그 v2.0
```

### 결과
- 3개월 만에 100% 치환 완료
- 테스트 커버리지 0% → 72%
- 응답 시간 평균 2초 → 180ms

---

## 세 사례에서 배운 공통 교훈

!!! info "📌 공통 교훈"
    1. **작게 시작하라** — 첫 프로젝트는 MCP 2-3개, GSTACK 스킬 3-5개로 충분
    2. **매일 루틴을 자동화하라** — `/daily`, `/review`, `/retro`
    3. **큰 결정은 `/think`로** — Sequential Thinking이 감을 논리로 바꾼다
    4. **큰 변경은 Plan 모드로** — 30초의 검토가 하루를 구한다
    5. **문서화는 마지막이 아니라 처음부터** — GSTACK `/document-release`를 주기적으로

!!! tip "💡 꿀팁: 자기 프로젝트 메타 분석"
    여러분의 현재 프로젝트를 위 사례처럼 "어떤 스킬과 MCP를 어느 단계에 썼는지" 표로 정리해보세요. 다음 프로젝트 생산성이 2배 오릅니다.

---

## 체크리스트

- [ ] 세 사례 중 내 상황과 가장 닮은 것을 골랐다
- [ ] 그 사례의 워크플로우를 내 프로젝트에 맞게 각색했다
- [ ] 매일 루틴 스킬 3개를 정했다
- [ ] Plan 모드를 쓰는 기준(파일 N개 이상 등)을 정했다

다음은 마지막 페이지, **팁 & 베스트 프랙티스**입니다.
