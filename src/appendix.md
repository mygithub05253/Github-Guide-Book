# 부록

---

## 부록 A: Claude Code Plan 모드 완전 가이드

### A-1. Plan 모드란?

Plan 모드는 Claude Code의 **변경사항을 미리 보여준 후** 적용하는 안전한 작업 방식입니다.

**일반 모드 vs Plan 모드**

```
┌─ 일반 모드 (Direct Mode)
│  └─ 명령 실행 → 즉시 결과 반영
│     장점: 빠름
│     단점: 실수 수정 어려움
│
└─ Plan 모드 (Preview Mode)
   └─ 계획 작성 → 미리 보기 → 승인 후 실행
      장점: 안전, 검토 가능
      단점: 약간의 추가 시간
```

### A-2. Plan 모드 활성화 방법

**방법 1: 키보드 단축키**
```
1. Shift + Tab 을 두 번 연속으로 누름
2. 또는 Shift + Tab + Tab (한 번에)
3. Claude Code 인터페이스의 "Plan Mode" 토글 활성화
```

**방법 2: 명령어 사용**
```
메시지 입력창에서 다음 중 하나 입력:
- /plan (또는 /plan-mode)
- "이것을 Plan 모드로 실행해줘"
- "미리 보기를 보여줘"

예: "/plan 이 파일의 코드를 리팩토링해주세요"
```

**방법 3: 메뉴 버튼**
```
Claude Code 우측 상단 메뉴 → Plan Mode 선택
```

### A-3. Plan 모드 vs Direct 모드 사용 시기

**Plan 모드 추천:**
```
✓ 프로젝트 구조 변경 (파일 생성/이동/삭제)
✓ 기존 코드 대폭 수정
✓ 설정 파일 변경 (database.yml, config.json 등)
✓ 중요한 파일 편집
✓ 팀 프로젝트 작업
✓ 프로덕션 코드 변경
```

**Direct 모드 추천:**
```
✓ 간단한 오류 수정
✓ 주석 추가
✓ 문서 작성
✓ 로그 파일 검토
✓ 빠른 테스트
✓ 개인 프로젝트 소규모 작업
```

### A-4. Plan 모드 단계별 워크플로우

**예제: React 컴포넌트 리팩토링**

**Step 1: Plan 모드 활성화**

사용자가 `/plan React 컴포넌트를 함수형으로 리팩토링해줘`라고 입력하면, Claude가 다음과 같은 계획을 보여줍니다.

- 클래스형 → 함수형 변환
- Hooks 적용 (useState, useEffect)
- 라이프사이클 메서드 제거
- PropTypes 유지

**Step 2: 미리보기 확인**

변경 전 (클래스형):

```javascript
class UserProfile extends React.Component {
  constructor(props) {
    super(props);
    this.state = { user: null };
  }
  componentDidMount() {
    fetchUser(this.props.userId).then(user => this.setState({ user }));
  }
  render() {
    return <div>{this.state.user?.name}</div>;
  }
}
```

변경 후 (함수형 + Hooks):

```javascript
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]);
  return <div>{user?.name}</div>;
}
```

**Step 3: 변경 사항 승인**

버튼 옵션: `Apply Changes` / `Edit Plan` / `Discard`. "Apply Changes"를 클릭합니다.

**Step 4: 최종 적용**

- 컴포넌트 리팩토링 완료
- 파일: `src/components/UserProfile.jsx`
- 변경 라인: 8 → 13 (5줄 단축)

### A-5. Plan 편집 (Ctrl+G)

계획을 생성한 후 내용을 조정할 수 있습니다.

```
Plan 생성 후:
┌─────────────────────────────────────
│ 📋 PLAN: 함수 추상화
│ ├─ 1. getUser() 함수 추출
│ ├─ 2. formatUserData() 함수 추출
│ └─ 3. 테스트 코드 추가
│
│ [🔧 Ctrl+G로 편집] [ ✓ 적용 ] [ ✗ 취소 ]
└─────────────────────────────────────

편집 모드:
┌─────────────────────────────────────
│ 1. getUser() 함수 추출 ✓
│ 2. formatUserData() 함수 추출 ✓
│ 3. 테스트 코드 추가 ✓
│ 4. (새로 추가) JSDoc 주석 추가
│
│ [완료]
└─────────────────────────────────────
```

### A-6. Plan 모드 베스트 프랙티스

**좋은 Plan 모드 사용:**
```python
# ✓ 좋은 예: 구체적인 지시
"Plan 모드로 다음을 해주세요:
1. User 클래스의 validate_email() 메서드를 unittest로 테스트
2. 테스트 케이스: 유효한 이메일, 잘못된 형식, None 값
3. 테스트 파일: tests/test_user.py에 추가"

# ✗ 나쁜 예: 너무 모호함
"코드 개선해줘"
```

**Plan 모드 검토 체크리스트:**
```
변경 사항 미리보기 확인 시:
☑ 변경된 파일 목록 확인
☑ 삭제되는 코드 없는지 확인 (의도하지 않은 삭제)
☑ 신규 코드의 로직 검증
☑ 기존 테스트 영향도 확인
☑ 설정 파일 변경이 있으면 특히 주의

의심스러운 부분:
☑ "?" 또는 "..." 표시된 부분 재확인
☑ 대량 삭제 작업은 특히 주의
☑ 데이터베이스 스키마 변경은 double-check
```

---
## 부록 B: Sequential Thinking 완전 가이드

### B-1. Sequential Thinking MCP란?

Sequential Thinking은 **단계별 논리적 추론**을 통해 복잡한 문제를 해결하는 MCP(Message Collection Protocol) 도구입니다.

**특징:**
```
일반 응답:
Q: "100을 소인수분해 해줄래?"
A: 100 = 2² × 5² (즉시 답변)

Sequential Thinking:
Q: "100을 소인수분해 해줄래?"
→ Step 1: 100을 2로 나누면? 50
→ Step 2: 50을 2로 나누면? 25
→ Step 3: 25를 5로 나누면? 5
→ Step 4: 5를 5로 나누면? 1
→ 결론: 2² × 5²

장점: 논리 검증 가능, 실수 수정 용이
```

### B-2. Sequential Thinking 설치

**설치 명령어:**
```bash
# Claude Code CLI에서 설치
claude-code install sequential-thinking-mcp

# 또는 수동 설치
npm install -g sequential-thinking-mcp

# 설치 확인
claude-code mcp list | grep sequential
```

**Claude Code 설정 파일 (`claude.json`):**
```json
{
  "mcps": {
    "sequential-thinking": {
      "enabled": true,
      "timeout": 30000
    }
  }
}
```

### B-3. Sequential Thinking 작동 원리

**다단계 추론 프로세스:**

```
입력: 복잡한 문제
  ↓
[Step 1] 문제 분해
  - 주요 요소 파악
  - 선행 조건 확인
  ↓
[Step 2] 단계별 분석
  - 각 단계의 근거 제시
  - 중간 결과 검증
  ↓
[Step 3] 오류 확인
  - 논리적 모순 탐지
  - 가정 재검토
  ↓
[Step 4] 결론 도출
  - 최종 답변 생성
  - 신뢰도 제시
  ↓
출력: 검증된 답변
```

### B-4. Sequential Thinking 사용 시기

**추천 시나리오:**

```
✓ 알고리즘 설계 및 분석
  예: "N-Queen 문제의 백트래킹 알고리즘을 설계해주세요"

✓ 아키텍처 결정
  예: "마이크로서비스 vs 모놀리식 아키텍처 비교"

✓ 버그 분석
  예: "메모리 누수 원인을 단계별로 찾아주세요"

✓ 복잡한 요구사항 분석
  예: "금융 거래 시스템의 보안 요구사항 정리"

✓ 성능 최적화
  예: "데이터베이스 쿼리 최적화 전략"

✗ 부추천 시나리오:
  - 간단한 질문 ("Python 문법 확인")
  - 빠른 답변 필요 (실시간 채팅)
  - 이미 검증된 일반 지식
```

### B-5. Sequential Thinking 실제 예제

**예제 1: 복잡한 알고리즘 설계**

```
사용자 요청:
"Sequential Thinking으로 분석해줄래?
 1000개의 정렬된 배열에서 target을 찾는
 가장 효율적인 방법을 설계해줘"

Sequential Thinking 프로세스:
──────────────────────────────

[THINKING Step 1: 문제 분석]
- 입력: 정렬된 배열 (크기 1000), target 값
- 제약: 효율성 중심
- 가능한 방법:
  1. 선형 탐색: O(n)
  2. 이진 탐색: O(log n) ← 가장 효율적
  3. 해시 테이블: O(1) but 전처리 필요

[THINKING Step 2: 이진 탐색 상세 분석]
- 시간복잡도: O(log 1000) ≈ 10번 비교
- 공간복잡도: O(1)
- 구현: 재귀 vs 반복
  └─ 반복이 스택 오버플로우 방지

[THINKING Step 3: 코드 설계]
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

[THINKING Step 4: 검증]
- 최악의 경우: log₂(1000) = ~10회 → 가장 효율적
- 엣지 케이스:
  - target이 배열에 없음: -1 반환 ✓
  - target이 처음/마지막: 정상 동작 ✓

[결론]
이진 탐색이 최적 (O(log n) 시간복잡도)
```

**예제 2: 금융 거래 시스템 설계**

```
사용자 요청:
"Sequential Thinking으로 설계해줄래?
 금융 거래 플랫폼에서
 '동시에 2개 거래가 같은 계좌에서 발생하면?'
 이 문제를 단계별로 분석해줘"

Sequential Thinking 프로세스:
──────────────────────────────

[THINKING Step 1: 문제 정의]
- 시나리오: 사용자 계좌 잔액 $1000
  - 거래 A: $600 출금 (동시)
  - 거래 B: $600 출금 (동시)
- 문제:
  - Race condition (동시성 문제)
  - 둘 다 성공하면 -$200 (불가능!)

[THINKING Step 2: 원인 분석]
Database 레벨에서 문제:
```
시간  거래 A              거래 B
t1    select balance=1000 -
t2    -                   select balance=1000
t3    update balance=400  -
t4    -                   update balance=400
결과: 최종 balance = $400 (오류!)
```

[THINKING Step 3: 해결 방안 3가지]

방안 1: Database Lock (비관적 잠금)
```sql
BEGIN TRANSACTION;
SELECT balance FROM accounts WHERE id=1 FOR UPDATE;
-- 이 행을 다른 트랜잭션이 접근 불가
UPDATE accounts SET balance = balance - 600 WHERE id=1;
COMMIT;
```
장점: 간단, 안전
단점: 성능 저하 (다른 거래 대기)

방안 2: MVCC (다중 버전 동시성 제어)
```sql
-- PostgreSQL, MySQL InnoDB
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
SELECT balance FROM accounts WHERE id=1;
UPDATE accounts SET balance = balance - 600 WHERE id=1;
COMMIT; -- 충돌 감지 시 자동 롤백
```
장점: 높은 동시성
단점: 복잡, 롤백 처리 필요

방안 3: Optimistic Locking (낙관적 잠금)
```sql
-- version 컬럼 사용
SELECT balance, version FROM accounts WHERE id=1;
UPDATE accounts
  SET balance = balance - 600, version = version + 1
  WHERE id=1 AND version = 1;
-- 실패 시 재시도
```

[THINKING Step 4: 금융권 규정 검토]
- PCI DSS: 트랜잭션 원자성 필수
- 은행법: ACID 보장 의무
└─ Atomicity (원자성): 모두 성공 또는 모두 실패

[결론]
금융권에서는 "Database Lock" 또는 "MVCC"로
ACID 보장 필수. 성능은 차선책.
```

### B-6. Sequential Thinking과 GSTACK 통합

**GSTACK 워크플로우 + Sequential Thinking:**

```
프로젝트 계획 단계:
1. /office-hours
   └─ "Sequential Thinking으로 분석해줄래?
      우리 프로젝트의 아키텍처 선택지"

2. Sequential Thinking으로 비교:
   ├─ 마이크로서비스 (장단점 분석)
   ├─ 모놀리식 (장단점 분석)
   └─ 하이브리드 (절충안)

3. /plan-ceo-review
   └─ 위 분석 결과를 비즈니스 관점에서 평가

4. 최종 결정
   └─ 근거 기반 아키텍처 선택 완료
```

---
## 부록 C: 추천 학습 로드맵

### C-1. 비전공자 → 풀스택 개발자 (12개월 로드맵)

**전제 조건:**
- 기본 컴퓨터 활용 능력
- 영어 기술 문서 읽기 능력 (번역기 사용 가능)
- 주 20-30시간 학습 시간

**Month 1-2: 웹 기초 (4주, 80시간)**

```
학습 목표: HTML/CSS/JavaScript 기초 완성

Week 1-2: HTML & CSS
├─ freeCodeCamp "Responsive Web Design" (300시간 → 40시간 집중)
├─ HTML5 시맨틱 요소
├─ CSS Grid & Flexbox
└─ 프로젝트: 포트폴리오 웹사이트 (반응형)

Week 3-4: JavaScript 기초
├─ 변수, 자료형, 연산자
├─ 조건문, 반복문, 함수
├─ DOM 조작
└─ 프로젝트: 계산기, Todo 리스트

추천 자료:
- freeCodeCamp JavaScript (4시간 강의)
- MDN Web Docs (레퍼런스)
- Codepen (코드 샘플)
```

**Month 3-4: React 기초 (4주, 80시간)**

```
학습 목표: React 컴포넌트 기반 개발

Week 1-2: React 기초
├─ JSX 문법
├─ 컴포넌트 (함수형)
├─ Props와 State
├─ Hooks (useState, useEffect, useContext)
└─ 프로젝트: 날씨 앱, 영화 검색

Week 3-4: React 심화
├─ 커스텀 Hooks
├─ 성능 최적화 (React.memo, useMemo)
├─ 라우팅 (React Router)
└─ 프로젝트: SNS 피드, 블로그

추천 자료:
- React Official Tutorial
- Dave Ceddia "Pure React"
- Scrimba React Course
- 프로젝트: GitHub API를 이용한 사용자 검색
```

**Month 5-6: Spring Boot 백엔드 (4주, 80시간)**

```
학습 목표: REST API 개발 및 데이터베이스 연동

Week 1-2: Spring Boot 기초
├─ 프로젝트 구조 (MVC 패턴)
├─ Controller, Service, Repository
├─ JPA/Hibernate ORM
├─ 데이터베이스 연동 (MySQL)
└─ 프로젝트: 간단한 CRUD API

Week 3-4: Spring Boot 심화
├─ Spring Security (인증/인가)
├─ JWT 토큰 인증
├─ 에러 처리
├─ 로깅 및 모니터링
└─ 프로젝트: 사용자 관리 시스템

추천 자료:
- Spring Boot Official Guide
- Baeldung (튜토리얼 사이트)
- Java Spring Framework 강의 (인프런/Udemy)
- 프로젝트: 블로그 API (CRUD + 댓글 기능)
```

**Month 7-8: 데이터베이스 & API (4주, 80시간)**

```
학습 목표: 데이터베이스 설계 및 고급 API 개발

Week 1-2: 데이터베이스
├─ SQL 기본 (SELECT, INSERT, UPDATE, DELETE)
├─ JOIN, GROUP BY, 서브쿼리
├─ 인덱싱 및 최적화
├─ 정규화 (1NF, 2NF, 3NF)
└─ 실습: Leetcode Database 문제 (Medium Level)

Week 3-4: 고급 API
├─ 페이지네이션
├─ 필터링 및 정렬
├─ 캐싱 (Redis)
├─ API 문서화 (Swagger/OpenAPI)
└─ 프로젝트: 전자상거래 API (상품 필터링, 주문 관리)

추천 자료:
- SQL Tutorial (W3Schools)
- Database Design Basics (Stanford)
- Redis 공식 문서
- 프로젝트: 금융 데이터 API (시계열 데이터)
```

**Month 9-10: 실전 프로젝트 & 포트폴리오 (4주, 80시간)**

```
학습 목표: 풀스택 포트폴리오 프로젝트 완성

Week 1: 요구사항 분석 & 설계
├─ 프로젝트 선정 (비즈니스 가치 있는 주제)
├─ API 설계
├─ 데이터베이스 스키마 설계
└─ UI/UX 디자인

Week 2-3: 개발
├─ 백엔드 API 개발
├─ 프론트엔드 구현
├─ 테스트 작성 (Jest, JUnit)
└─ 배포 준비

Week 4: 완성 & 배포
├─ 문서 작성 (README, API 문서)
├─ 배포 (Heroku, AWS, Vercel)
├─ CI/CD 설정 (GitHub Actions)
└─ 포트폴리오 정리

추천 프로젝트 아이디어:
1. 금융 관리 앱 (예산 관리, 수입/지출 추적)
2. 스터디 그룹 매칭 플랫폼
3. 부동산 검색 시스템
4. 온라인 쇼핑몰
5. 실시간 협업 문서 편집기
```

**Month 11-12: 면접 준비 & 취업 (4주)**

```
Week 1-2: 알고리즘 & 코딩테스트
├─ LeetCode Easy → Medium (50문제)
├─ 자료구조 (Array, String, Tree, Graph, DP)
└─ 모의 면접

Week 3: 기술 면접 준비
├─ 시스템 디자인 (마이크로서비스, 캐싱, 데이터베이스)
├─ 포트폴리오 프로젝트 설명 연습
├─ 기술 질문 준비
└─ 행동 면접 (Behavioral Interview)

Week 4: 취업 활동
├─ 이력서 작성
├─ 포트폴리오 정리
├─ 채용공고 지원 (매일 3-5개)
└─ 면접 스케줄링

추천 자료:
- Leetcode + 알고리즘 강의
- "시스템 디자인 면접" 책
- Cracking the Coding Interview
```

---

### C-2. 금융권 취업 준비 로드맵 (6개월 가속화 과정)

**전제 조건:**
- 기본 프로그래밍 능력 (다른 언어 경험 있음)
- 금융권 취업 목표

**Month 1: Java & Spring Boot 집중 (4주)**

```
주 목표: 금융권 표준 스택 습득

Week 1: Java 심화
├─ 객체지향 프로그래밍 (OOP)
├─ 컬렉션 프레임워크 (List, Map, Set)
├─ 멀티스레딩 (Thread, Synchronization)
└─ 람다식 및 스트림 API

Week 2-3: Spring Boot 실전
├─ Dependency Injection
├─ Spring Data JPA
├─ Spring Security (OAuth2, JWT)
├─ 트랜잭션 관리 (ACID)
└─ 프로젝트: 계좌 관리 시스템

Week 4: 금융 도메인 지식
├─ 주식 거래 프로토콜
├─ 결제 시스템 (PCI DSS)
├─ 암호화 통신
└─ 금융 API (OpenBanking)

프로젝트: 은행 계좌 관리 API
(이체, 거래 내역, 계좌 잔액)
```

**Month 2: SQL & 데이터베이스 (4주)**

```
주 목표: 금융권 데이터 처리 능력

Week 1-2: SQL 마스터
├─ 복잡한 쿼리 최적화
├─ 윈도우 함수 (ROW_NUMBER, RANK)
├─ 트리거 및 스토어드 프로시저
├─ 인덱스 전략
└─ 실습: LeetCode Database 문제 (Medium)

Week 3: 금융 데이터 모델
├─ 계좌/거래 테이블 설계
├─ 시계열 데이터 처리
├─ 감사 로그 (Audit Log)
└─ 데이터 정규화

Week 4: 성능 튜닝
├─ 쿼리 실행 계획 분석
├─ 인덱스 최적화
├─ 캐싱 전략 (Redis)
└─ 프로젝트: 금융 데이터 분석 쿼리

프로젝트: "사용자별 월간 거래 통계" 쿼리 최적화
(복합 인덱싱, 파티셔닝)
```

**Month 3: 코딩테스트 (4주)**

```
주 목표: 공기업/대기업 채용 대비

Week 1-2: 알고리즘 (60문제)
├─ 동적계획법 (DP) - 15문제
├─ 그래프 (BFS, DFS) - 15문제
├─ 정렬 및 탐색 - 15문제
├─ 문자열 처리 - 15문제
└─ 실습: Baekjoon Gold Level

Week 3: NCS 유형 코딩테스트
├─ "한국은행" 기출 (구글 검색)
├─ "공기업" 기출 문제풀이
├─ 제한 시간 내 풀이 (60분/1문제)
└─ 프로젝트: 모의고사 5회

Week 4: 모의 면접
├─ 알고리즘 설명하기 (화이트보드)
├─ 코드 리뷰 (시간복잡도, 공간복잡도)
├─ 최적화 과정 설명
└─ 예상 질문 대비

추천 플랫폼:
- LeetCode (영문, 상세 설명)
- Baekjoon (한국 온라인저지, 기출)
- Programmers (카카오/네이버 기출)
```

**Month 4: 금융 & 보안 (4주)**

```
주 목표: 금융권 보안 및 규정 이해

Week 1: 금융 IT 기초
├─ 금융감독 규정 (ISMS, PCI DSS)
├─ 암호화 통신 (TLS/SSL)
├─ 토큰 기반 인증 (JWT, OAuth2)
└─ 프로젝트: 안전한 로그인 시스템

Week 2: 보안 검사
├─ OWASP Top 10 분석
├─ SQL Injection 방어
├─ XSS, CSRF 방어
└─ 보안 코드 리뷰

Week 3: 금융 도메인 심화
├─ 이중 인증 (2FA)
├─ 거래 한도 관리
├─ 부정 거래 탐지
└─ PCI DSS 준수

Week 4: 면접 대비
├─ "금융권에서 중요한 보안은?"
├─ "암호화 알고리즘 선택 기준"
├─ "거래 시스템 설계"
└─ 프로젝트: 거래 검증 시스템

프로젝트: "거래 이중 검증 시스템"
(OTP, 전자서명, 부정 거래 탐지)
```

**Month 5: DevOps & 인프라 (4주)**

```
주 목표: 금융권 운영 능력

Week 1: Docker & Kubernetes
├─ 컨테이너 기초 (Docker)
├─ 오케스트레이션 (Kubernetes)
├─ 배포 자동화
└─ 프로젝트: Spring Boot 앱 컨테이너화

Week 2: CI/CD 파이프라인
├─ GitHub Actions
├─ 자동 테스트
├─ 자동 배포
└─ 프로젝트: 풀스택 자동 배포

Week 3: 모니터링 & 로깅
├─ ELK 스택 (Elasticsearch, Logstash, Kibana)
├─ 성능 모니터링 (Prometheus)
├─ 로그 분석
└─ 금융권 감시 로그 수집

Week 4: 고가용성 설계
├─ 로드 밸런싱
├─ 데이터베이스 복제 (Replication)
├─ 재해 복구 (DR) 계획
└─ 프로젝트: 고가용성 시스템 설계

추천 학습:
- Kubernetes Official Tutorial
- GitHub Actions Documentation
- ELK Stack 공식 문서
```

**Month 6: 포트폴리오 & 면접 (4주)**

```
Week 1-2: 금융 프로젝트 완성
├─ 프로젝트: 종합 금융 관리 플랫폼
│  ├─ 사용자 계좌 관리
│  ├─ 주식 거래 시뮬레이션
│  ├─ 거래 내역 분석
│  └─ 이중 인증 및 보안
├─ 배포 (AWS/Azure)
├─ 성능 최적화 (응답시간 < 200ms)
└─ 문서화 (API 명세, 아키텍처)

Week 3: 기술 면접 준비
├─ 시스템 디자인 (금융 시스템)
├─ 성능 최적화 사례
├─ 보안 사례
├─ 운영 경험 설명
└─ 모의 면접 3회

Week 4: 취업 활동
├─ 이력서/자소서 작성
├─ 포트폴리오 발표 준비
├─ 금융사 채용공고 지원
└─ 최종 면접 스케줄링
```

**금융권 취업 최종 체크리스트:**
```
기술 스킬:
☑ Java/Spring Boot (심화)
☑ SQL (최적화까지)
☑ 알고리즘 (Gold Level)
☑ 보안 (OWASP Top 10)
☑ DevOps (Docker, K8s)

포트폴리오:
☑ 금융 주제 프로젝트 (완성도 높음)
☑ GitHub README 상세 작성
☑ 배포 가능한 상태
☑ 성능/보안 최적화 증명

면접 준비:
☑ 알고리즘 설명 능력
☑ 시스템 디자인 경험
☑ 금융 도메인 지식
☑ 팀 협업 경험 설명
☑ 자신만의 기술 인사이트

지원 전략:
☑ 대형 금융사 (은행, 증권, 보험)
☑ 핀테크 (토스, 뱅샐, 당근페이)
☑ 공기업 (우정사업본부, 교보 등)
☑ 면접일정 집중 공략
```

---
## 부록 D: 유용한 리소스 링크 모음

### D-1. 한국 개발자 커뮤니티

**블로그 플랫폼:**
```
1. Velog (https://velog.io/)
   - 개발자 블로그 플랫폼
   - 추천: 기술 글 품질 높음
   - 팔로우: "해시코드", "코딩알림", "노드버드"

2. Tistory (https://www.tistory.com/)
   - 개인 기술 블로그
   - 추천 블로그: "기억보다는 기록을", "코딩하는 생각"

3. Medium 한국 (https://medium.com/)
   - 국제 기술 글
   - 추천: "Better Programming", "Towards Data Science"

4. dev.to (https://dev.to/)
   - 개발자 커뮤니티
   - 영문이지만 예제 풍부
```

**개발자 커뮤니티:**
```
1. GitHub 한국 (https://github.com/korean-developers)
   - 한국 개발자 네트워크
   - 채용 정보, 프로젝트 협업

2. 프로그래머스 (https://programmers.co.kr/)
   - 코딩테스트 + 채용
   - 월간 코딩 챌린지

3. 백준 온라인 저지 (https://www.acmicpc.net/)
   - 알고리즘 문제 풀이
   - 한국 수준 높음

4. 인프런 (https://www.inflearn.com/)
   - 온라인 코딩 강의
   - 가성비 최고 (한국)

5. 노마드 코더 (https://nomadcoders.co/)
   - 웹 개발 강의
   - YouTube 채널 추천
```

### D-2. 온라인 저지 (Online Judge)

**알고리즘 연습:**
```
1. LeetCode (https://leetcode.com/)
   주소: 영문
   특징: 상세 분석, 상위 풀이 학습
   추천: 비전공자는 Easy → Medium
   료: 유료 구독 권장 ($35/월)

2. Baekjoon (https://www.acmicpc.net/)
   주소: 한국
   특징: 한국 대학 경시대회 기출
   추천: 공기업/대기업 코딩테스트 대비
   료: 무료

3. Programmers (https://programmers.co.kr/learn/challenges)
   특징: 카카오/네이버 기출
   추천: 취업 준비생 필수
   료: 무료

4. Codeforces (https://codeforces.com/)
   특징: 경쟁 프로그래밍
   추천: 고급 알고리즘
   료: 무료

학습 전략:
Week 1-4: LeetCode Easy (50문제)
Week 5-8: LeetCode Medium (50문제)
Week 9-12: Baekjoon Silver (50문제)
Week 13-16: Baekjoon Gold (50문제)
총 3-4개월에 200문제
```

**시뮬레이션 환경:**
```
1. HackerRank (https://www.hackerrank.com/)
   - 회사 채용 문제
   - C, Java, Python 지원

2. TopCoder (https://www.topcoder.com/)
   - 알고리즘 경시대회
   - 상금 대회

3. AtCoder (https://atcoder.jp/)
   - 일본 알고리즘 대회
   - 한국 수준보다 높음
```

### D-3. 무료 온라인 강좌

**기본부터 심화까지:**
```
1. freeCodeCamp (https://www.freecodecamp.org/)
   - 완전 무료
   - 영상 강좌 (최고 품질)
   추천 코스:
   ├─ Responsive Web Design (5시간)
   ├─ JavaScript Algorithms (4시간)
   ├─ React (12시간)
   └─ Backend Development (12시간)

2. Khan Academy (https://www.khanacademy.org/)
   - 컴퓨터 과학 기초
   - 영상 + 문제 풀이

3. Codecademy (https://www.codecademy.com/)
   - 인터랙티브 학습
   - 유료 구독 권장

4. Udemy (https://www.udemy.com/)
   - 저가 강의 ($10-15)
   - 추천: "The Complete JavaScript Course"
          "The Complete Python Course"

한국 강의:
5. 인프런 (https://www.inflearn.com/)
   - 한국 강사, 한국어
   - 가격: 15,000원 (세일 시 3,000원)
   추천: "부트캠프" 시리즈

6. 웹개발 종합반 (https://spartacodingclub.kr/)
   - 입문자 친화적
   - 무료 + 유료 모두 제공
```

**전문 기술 학습:**
```
1. Docker (https://www.docker.com/101-tutorial/)
   - 공식 튜토리얼 무료

2. Kubernetes (https://kubernetes.io/docs/tutorials/)
   - 공식 문서, 완전 무료

3. Spring Boot (https://spring.io/guides)
   - 공식 가이드 무료

4. React 공식 (https://react.dev/)
   - 최신 React 학습
   - 완전히 리뉴얼됨 (2022)
```

### D-4. 도서 추천

**필독서:**
```
1. "Cracking the Coding Interview"
   - 저자: Gayle Laakmann McDowell
   - 대상: 취업 준비 필수
   - 가격: $40 (한국어 번역본: 45,000원)

2. "System Design Interview"
   - 저자: Alex Xu
   - 대상: 시니어 준비
   - 가격: $50 (한국어 번역본: 50,000원)

3. "Clean Code"
   - 저자: Robert C. Martin
   - 대상: 코드 품질 개선
   - 가격: $45 (한국어: 40,000원)

4. "Effective Java"
   - 저자: Joshua Bloch
   - 대상: Java 심화
   - 가격: $55 (한국어: 45,000원)

5. "데이터베이스 설계와 구현"
   - 저자: 정정수
   - 대상: 한국 저자, SQL 완벽 학습
   - 가격: 35,000원
```

**알고리즘 & 자료구조:**
```
1. "알고리즘 문제 풀이 핸드북"
   - 저자: 하용호
   - 한국 고등학생이 쓴 저자
   - 가격: 35,000원

2. "코딩 인터뷰 완전 분석"
   - 저자: 한빛 미디어
   - LeetCode 스타일 문제
   - 가격: 32,000원
```

**금융 & DevOps:**
```
1. "금융 시스템 설계"
   - 저자: 구글 엔지니어 (강추)
   - 가격: Udemy $40

2. "쿠버네티스 완벽 가이드"
   - 저자: Kelsey Hightower
   - 무료: "Kubernetes The Hard Way"
   - 가격: 온라인 무료

3. "마이크로서비스 아키텍처"
   - 저자: Sam Newman
   - 가격: 35,000원
```

### D-5. 유튜브 채널 추천

**기초부터 심화까지:**
```
영어 채널:
1. freeCodeCamp (https://www.youtube.com/@freeCodeCamp)
   - 완전 무료, 고품질
   - 인기: "100 Days of Code", "Web Development"

2. Traversy Media (https://www.youtube.com/@TraversyMedia)
   - 프론트엔드 심화
   - 인기: "React Crash Course", "Node.js Tutorial"

3. The Net Ninja (https://www.youtube.com/@NetNinja)
   - 웹 개발 완전 입문
   - 재미있고 명확한 설명

4. CodeWithHarry (https://www.youtube.com/@CodeWithHarry)
   - Python 입문 최고
   - 100개 이상 영상

한국 채널:
5. 노마드 코더 (https://www.youtube.com/@nomadcoders)
   - 웹 개발 전문
   - 한국인, 한국어

6. 코딩애플 (https://www.youtube.com/@CodingApple)
   - HTML/CSS/JS 입문
   - 영상 퀄리티 높음

7. 우디 (https://www.youtube.com/@woodywood6)
   - Spring Boot, Java
   - 실무급 심화 강의

8. 동빈나 (https://www.youtube.com/@dongbinna)
   - 알고리즘 및 경제
   - 한국 최고의 알고리즘 채널
```

**라이브 코딩 & 면접:**
```
1. Google Developers (https://www.youtube.com/@GoogleDevelopers)
   - Google 엔지니어 강의
   - 시스템 디자인 고급

2. Back to Back SWE (https://www.youtube.com/@BackToBackSWE)
   - 면접 완벽 준비
   - 실무 경험 공유

3. Fireship (https://www.youtube.com/@Fireship)
   - 기술 트렌드 설명
   - 10분 완성 영상 (추천!)
```

### D-6. 채용 정보 플랫폼

**대기업/공기업:**
```
1. 사람인 (https://www.saramin.co.kr/)
   - 대형 포탈
   - 필터: 개발자 > 신입

2. 잡코리아 (https://www.jobkorea.co.kr/)
   - 공기업 주로 게재
   - 필터: 공공기관

3. 워크넷 (https://www.work.go.kr/)
   - 정부 공식 플랫폼
   - 공기업/공공기관 집중

4. 공기업아이 (https://www.gonggigeop.ai/)
   - 공기업 전문 플랫폼
   - 추천 많음
```

**스타트업/핀테크:**
```
1. 원티드 (https://www.wanted.co.kr/)
   - 스타트업 채용 전문
   - 필터: "개발자 경력 신입"

2. 프로그래머스 채용 (https://programmers.co.kr/jobs)
   - 코딩테스트 + 채용
   - 통합 플랫폼

3. 정글 (https://jungle.co.kr/)
   - 초기 스타트업
   - 보상: 스톡옵션 + 급여

4. 앤젤리스트 (https://wellfound.com/)
   - 세계 스타트업
   - 한국 시작업도 있음
```

**금융권 채용:**
```
1. 금융감독원 (https://www.fss.or.kr/)
   - 공식 채용 정보
   - "IT 연봉 높음" 검색어

2. 각 은행 사이트
   - 신한은행 (https://www.shinhan.com/shbank/recruit)
   - 국민은행 (https://www.kbbank.com/recruit)
   - 우리은행 (https://www.wooribank.com/)

3. 핀테크 채용
   - 토스 (https://toss.im/career)
   - 당근 (https://about.daangn.com/jobs/)
   - 뱅샐 (https://banksalad.com/careers)
```

### D-7. 학습 효율을 위한 Tip

**최고의 학습 방법:**
```
Tip 1: 80/20 원칙
- 20%의 핵심 개념으로 80%의 문제 해결
- 예: React hooks만으로 90% 프로젝트 가능
- 시작: 기초만 완벽하게 (심화는 나중)

Tip 2: 프로젝트 기반 학습
- 책만 읽기 vs 프로젝트 하면서 배우기
- 70% 프로젝트 경험이 필수
- 추천: 3-4개 포트폴리오 프로젝트

Tip 3: 반복학습 (Spaced Repetition)
- 배운 것을 다음날, 1주 후, 1개월 후 복습
- 앱: Anki (플래시카드)
- 추천: 알고리즘 패턴 외우기

Tip 4: 설명하기 (Teaching Others)
- 배운 내용을 블로그로 쓰기
- 남에게 설명하기
- 면접처럼 화이트보드에 설명해보기

Tip 5: 코드 리뷰 받기
- GitHub에 올리고 피드백 받기
- 오픈소스 PR 보내기
- 멘토에게 검토받기

Tip 6: 습관화
- 하루 3시간 × 3개월 > 일주일 30시간
- 매일 정해진 시간에 학습
- 추천: 아침 1시간 + 저녁 2시간
```

**학습 일정 관리:**
```
월요일: 새로운 개념 학습
화-목요일: 프로젝트 구현
금요일: 복습 + 코드 리뷰
토-일요일: 개인 프로젝트 진행

주간 목표:
- 강의 3시간
- 프로젝트 10시간
- 알고리즘 7시간
- 복습 및 글쓰기 5시간
총 25시간/주
```

---

---

## 부록 E: 가이드북 빌드 파이프라인 사용법

이 가이드북은 `scripts/` 디렉토리의 Python 스크립트로 자동 생성됩니다.

### 빌드 방법

```bash
# 의존성 설치
pip install -r scripts/requirements.txt

# 전체 빌드 (MD + DOCX + PDF)
python scripts/build_guidebook.py

# 특정 포맷만 빌드
python scripts/build_guidebook.py --format md
python scripts/build_guidebook.py --format docx
python scripts/build_guidebook.py --format pdf
```

### 파이프라인 구조

```
src/*.md → md_merger.py → output/Guidebook.md
                              ↓
                    ┌─────────┴─────────┐
                    ↓                   ↓
              md_to_docx.py       md_to_pdf.py
                    ↓                   ↓
           output/Guidebook.docx  output/Guidebook.pdf
```

### 사용된 라이브러리

| 라이브러리 | 용도 | Part 4 참조 |
|-----------|------|------------|
| python-docx | MD → DOCX 변환 | 4-1 |
| WeasyPrint | HTML → PDF 렌더링 | 4-4 (확장) |
| markdown | MD → HTML 변환 | - |
| Pygments | 코드 구문 강조 | - |
