# 부록 C: 추천 학습 로드맵

> "뭐부터 배워야 해요?"라는 질문에 대한 세 가지 답. 자기 상황에 맞는 트랙을 고르세요.

---

## 트랙 선택 가이드

| 트랙 | 대상 | 기간 |
|------|------|------|
| [Track 1](#track-1) | 비전공자 → 풀스택 개발자 | 12개월 |
| [Track 2](#track-2) | 경험자 → 금융권 취업 가속 | 6개월 |
| [Track 3](#track-3) | AI 도구 중심 현대적 워크플로우 | 4주 |

---

## Track 1 — 비전공자 → 풀스택 개발자 (12개월) {#track-1}

### 전제
- 기본 PC 사용 능력
- 영어 문서 읽기 (번역기 OK)
- 주 20-30시간 학습 가능

### Month 1-2: 웹 기초

```text
Week 1-2: HTML + CSS
├─ freeCodeCamp "Responsive Web Design" (집중 40시간)
├─ HTML5 시맨틱, Flexbox, Grid
└─ 프로젝트: 반응형 포트폴리오 사이트

Week 3-4: JavaScript
├─ 변수, 함수, 조건문, 반복문
├─ DOM 조작, 이벤트
└─ 프로젝트: Todo 리스트, 계산기
```

### Month 3-4: React

```text
Week 1-2: React 기초
├─ JSX, 컴포넌트, Props, State
├─ Hooks (useState, useEffect)
└─ 프로젝트: 날씨 앱 (OpenWeather API)

Week 3-4: React 심화
├─ 커스텀 Hooks, Context
├─ React Router
└─ 프로젝트: GitHub 사용자 검색 앱
```

### Month 5-6: Spring Boot

```text
Week 1-2: Spring Boot 기초
├─ Controller / Service / Repository
├─ JPA + Hibernate
└─ 프로젝트: 블로그 CRUD API

Week 3-4: 심화
├─ Spring Security, JWT
├─ 에러 처리, 로깅
└─ 프로젝트: 사용자 관리 시스템
```

### Month 7-8: DB & 고급 API

```text
Week 1-2: SQL
├─ SELECT, JOIN, GROUP BY, 서브쿼리
├─ 인덱싱, 정규화
└─ LeetCode Database 20문제

Week 3-4: API 고도화
├─ 페이지네이션, 필터링
├─ Redis 캐싱
└─ Swagger 문서화
```

### Month 9-10: 포트폴리오 프로젝트

```text
Week 1: 요구사항 분석
Week 2-3: 풀스택 구현
Week 4: 배포 (Vercel + Railway) + CI/CD
```

**추천 주제:** 스터디 매칭, 가계부, 부동산 검색, 중고거래

### Month 11-12: 취업 준비

```text
Week 1-2: 알고리즘 (LeetCode Easy-Medium 50문제)
Week 3: 기술 면접 준비
Week 4: 자소서 + 포트폴리오 정리 + 지원
```

!!! tip "💡 꿀팁: 매달 한 편씩 블로그"
    공부한 것을 Velog/Tistory에 정리하면 실력 + 포트폴리오 + 취업 시 가점 3마리 토끼를 잡습니다.

---

## Track 2 — 금융권 가속 6개월 {#track-2}

### 전제
- 타 언어 경험 있음
- 금융/공기업 목표

### Month 1: Java + Spring Boot 집중

- Week 1: Java 심화 (컬렉션, 멀티스레딩, 람다)
- Week 2-3: Spring Boot 실전 (DI, JPA, Security)
- Week 4: 금융 도메인 기초 (PCI DSS, OAuth2)
- **프로젝트:** 은행 계좌 관리 API

### Month 2: SQL + DB 심화

- Week 1-2: 복잡한 쿼리, 윈도우 함수
- Week 3: 시계열 / 감사 로그
- Week 4: 쿼리 튜닝 (EXPLAIN)
- **프로젝트:** 거래 통계 쿼리 최적화

### Month 3: 코딩테스트

- Week 1-2: DP, 그래프, 정렬/탐색 (각 15문제)
- Week 3: 공기업 NCS 기출
- Week 4: 모의 면접 5회
- **플랫폼:** Baekjoon Gold, Programmers 3-4레벨

### Month 4: 보안 + 금융

- Week 1: ISMS, TLS, JWT
- Week 2: OWASP Top 10, SQLi, XSS
- Week 3: 2FA, 거래 한도, 부정 거래 탐지
- Week 4: 면접 대비
- **프로젝트:** 거래 이중 검증 시스템

### Month 5: DevOps

- Week 1: Docker + K8s 기초
- Week 2: GitHub Actions CI/CD
- Week 3: ELK 스택, Prometheus
- Week 4: 고가용성 설계
- **프로젝트:** 풀스택 자동 배포

### Month 6: 포트폴리오 + 취업

- Week 1-2: 종합 금융 플랫폼 완성 + AWS 배포
- Week 3: 시스템 디자인 면접 연습
- Week 4: 자소서 + 지원 집중

### 최종 체크리스트

```text
기술:
[ ] Java / Spring Boot 심화
[ ] SQL 최적화
[ ] 알고리즘 Gold Level
[ ] OWASP Top 10
[ ] Docker / K8s

포트폴리오:
[ ] 금융 주제 프로젝트 (배포 상태)
[ ] GitHub README 완성도
[ ] 성능 지표 증명

면접:
[ ] 시스템 디자인 설명 가능
[ ] 보안 사례 설명 가능
[ ] 금융 도메인 지식
```

---

## Track 3 — AI 도구 중심 4주 부트캠프 {#track-3}

### Week 1: 기초 세팅
- Day 1-2: Claude Code 설치, `Shift+Tab` 체득
- Day 3-4: Filesystem + GitHub MCP
- Day 5-7: 매일 `/review`, `/daily` 습관화

### Week 2: 도구 확장
- Day 1-2: Postgres + Playwright MCP
- Day 3-4: Sequential Thinking 프롬프트 5회
- Day 5-7: 첫 Plan 모드 대규모 리팩토링

### Week 3: GSTACK 도입
- Day 1: GSTACK 설치, 23개 스킬 훑기
- Day 2-3: `/office-hours`, `/plan-eng-review` 사용
- Day 4-5: `/qa`, `/ship` 사용
- Day 6-7: 매일 루틴 스킬 3개 정립

### Week 4: 통합 프로젝트
- Day 1-3: 미니 프로젝트 (스터디 매칭 MVP 등)
- Day 4-5: MCP 2-3개 조합 워크플로우
- Day 6: 회고 + 프롬프트 템플릿 5개 작성
- Day 7: 블로그 정리 발행

---

## 공통 조언

!!! info "📌 어떤 트랙이든"
    1. **매일 코드 커밋** (grass 심기)
    2. **배운 것을 글로 정리** (블로그/노션)
    3. **포트폴리오는 완성도 > 개수**
    4. **커뮤니티 참여** (오픈소스 이슈 1개라도)
    5. **멘토 찾기** (Claude Code로 `/office-hours` 시도)

!!! warning "⚠️ 하지 말아야 할 것"
    - 강의만 듣고 프로젝트 안 만들기
    - 프레임워크 문법 외우기 (구글링 가능)
    - 포트폴리오 5개 만들고 README 없음
    - 알고리즘만 파고 기본기 무시

---

## 체크리스트

- [ ] 내 상황에 맞는 트랙을 골랐다
- [ ] 첫 달 학습 스케줄을 캘린더에 등록했다
- [ ] 매주 회고 시간(30분)을 정했다
- [ ] 블로그 플랫폼을 결정했다
