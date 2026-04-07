# Part 5: AI 개발 도구 — Claude Code MCP & GSTACK

> Claude Code의 MCP 서버 생태계와 GSTACK 워크플로우를 통합하여 다룹니다.
> AI 도구를 활용한 개발 생산성 극대화 전략을 배울 수 있습니다.

## 학습 목표
- MCP 서버 개념과 핵심 서버 활용
- GSTACK 23개 스킬 실전 활용
- Plan 모드 & Sequential Thinking 활용법
- AI 도구 조합 전략

---

Claude Code와 통합되는 Model Context Protocol(MCP) 서버들을 체계적으로 설정하고 활용하는 방법입니다.

---

## 5-1. 핵심 MCP 서버

### MCP 소개

Model Context Protocol(MCP)은 Claude Code에서 외부 도구와 데이터에 접근하기 위한 표준 프로토콜입니다.

```
구조:
Claude Code
    ↓
MCP Client
    ↓
MCP Server (GitHub, Filesystem, PostgreSQL 등)
    ↓
External Services
```

### GitHub MCP - 레포지토리 관리

**설치**
```bash
claude mcp add github -s user -- npx -y @modelcontextprotocol/server-github
```

**설정** (`~/.claude/config.json`)
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

**활용 사례**
```
GitHub MCP로 가능한 작업:
1. 레포지토리 검색 및 정보 조회
2. Issue 생성, 조회, 수정
3. Pull Request 관리
4. 파일 조회 및 수정 제안
5. 커밋 이력 확인

사용 예시:
- "kubernetes/kubernetes 레포의 최신 이슈 10개 보여줘"
- "tensorflow/tensorflow의 PR #12345 내용 확인"
- "pytorch/pytorch에서 'performance' 라벨이 있는 이슈들 찾아줘"
```

### Filesystem MCP - 로컬 파일 시스템

**설치**
```bash
claude mcp add filesystem -s local -- npx -y @modelcontextprotocol/server-filesystem /path/to/workspace
```

**설정**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/user/projects"
      ]
    }
  }
}
```

**활용 시나리오**
```
Filesystem MCP로 가능한 작업:
1. 프로젝트 파일 구조 탐색
2. 코드 파일 읽기/쓰기
3. 설정 파일 관리
4. 로그 파일 분석
5. 대량 파일 처리

사용 예시:
- "src 디렉토리의 모든 Python 파일 목록 보여줘"
- "config.json 파일을 읽고 수정해줘"
- ".log 파일들을 분석해서 에러 패턴 찾아줘"
```

### PostgreSQL MCP - 데이터베이스 연동

**설치**
```bash
claude mcp add postgres -s user -- npx -y @modelcontextprotocol/server-postgres
```

**설정**
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb"
      }
    }
  }
}
```

**활용 예제**
```sql
-- MCP를 통해 Claude Code에서 직접 실행
-- 1. 테이블 스키마 확인
SELECT * FROM information_schema.tables
WHERE table_schema = 'public';

-- 2. 데이터 조회
SELECT * FROM users
WHERE created_at > NOW() - INTERVAL '7 days'
ORDER BY created_at DESC;

-- 3. 분석 쿼리
SELECT
    DATE(created_at) as date,
    COUNT(*) as user_count,
    AVG(age) as avg_age
FROM users
GROUP BY DATE(created_at)
ORDER BY date DESC;

-- Claude Code의 분석:
-- "지난 주 일일 사용자 수와 평균 나이를 조회했습니다.
--  데이터에 따르면 월요일에 가장 많은 신규 사용자가 가입했습니다."
```

### Sequential Thinking MCP - 복잡한 분석

**설치**
```bash
claude mcp add sequential-thinking -s local -- npx -y @modelcontextprotocol/server-sequential-thinking
```

**설정**
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

**활용 사례**
```
복잡한 분석이 필요한 경우:

1. 시스템 아키텍처 설계
   "우리 마이크로서비스 시스템을 PostgreSQL에서 MongoDB로 마이그레이션하려고 합니다.
    단계별로 어떻게 해야 할까요?"

   → Sequential Thinking으로 각 단계 논리적 분석

2. 코드 리팩토링 계획
   "이 12,000줄의 모놀리식 애플리케이션을 마이크로서비스로 분해하는
    최선의 방법을 알려주세요."

   → 각 컴포넌트별 분석 및 마이그레이션 전략 수립

3. 성능 최적화
   "데이터베이스 쿼리가 느립니다. 어디서 최적화해야 할까요?"

   → 쿼리 분석 → 인덱싱 전략 → 캐싱 전략 → 구현 단계 제시
```

---

## 5-2. 생산성 MCP 서버

### Playwright MCP - 브라우저 자동화

**설치**
```bash
claude mcp add playwright -s user -- npx -y @modelcontextprotocol/server-playwright
```

**활용 시나리오**
```
웹 자동화 작업:

1. 웹 스크래핑
   "airbnb.com에서 서울의 모든 숙박소 정보를 수집해줘"

2. 테스트 자동화
   "이 로그인 폼을 테스트해: username, password 입력 후 로그인"

3. 스크린샷 캡처
   "github.com의 스크린샷을 찍고 가독성을 평가해줘"

4. 폼 자동 작성
   "이 신청 폼을 내 정보로 채워줘"
```

**Claude Code 대화 예시**

> "GitHub에서 'machine learning' 키워드로 검색하고, 상위 10개 레포의 이름과 Stars 수를 표로 정리해줘."

Claude Code는 Playwright MCP를 통해 다음을 자동으로 수행합니다.
- 브라우저 실행 및 페이지 접속
- 검색어 입력 및 결과 탐색
- DOM 요소에서 데이터 추출
- 결과를 Markdown 표로 반환

> "이 로그인 폼이 잘못된 비밀번호일 때 어떤 에러 메시지를 보여주는지 확인해줘."

Claude Code가 시나리오를 실행한 뒤 스크린샷과 함께 결과를 요약합니다. 사용자는 코드를 직접 작성할 필요가 없습니다.

### Memory MCP - 지속적인 지식 관리

**설치**
```bash
claude mcp add memory -s user -- npx -y @modelcontextprotocol/server-memory
```

**활용**
```
세션 간 정보 유지:

1. 프로젝트 컨텍스트 저장
   "이 프로젝트의 주요 결정사항들을 메모리에 저장해줘"

   저장 내용:
   - 프로젝트 구조
   - 핵심 알고리즘
   - 성능 최적화 전략
   - 향후 계획

2. 학습 진행도 추적
   "지금까지 배운 내용과 다음에 배워야 할 내용을 정리해줘"

3. 버그 레지스트리
   "발견한 버그들과 해결 방법을 저장해줘"
```

### Docker MCP - 컨테이너 관리

**설치**
```bash
claude mcp add docker -s user -- npx -y @modelcontextprotocol/server-docker
```

**활용 예제**
```bash
# Docker 이미지 생성
docker build -t myapp:1.0 .

# 컨테이너 실행
docker run -d -p 8080:8080 --name myapp myapp:1.0

# 로그 확인
docker logs myapp

# 통계 보기
docker stats myapp

# Claude Code와의 연동:
# "이 Node.js 앱을 Docker화해줄래?"
# → Dockerfile 자동 생성
# → docker-compose.yml 생성
# → 이미지 빌드 및 실행
```

---

## 5-3. MCP 서버 조합 전략

### 개발 워크플로우 (완전한 예제)

```
목표: REST API 개발 프로젝트 자동화

1단계: 프로젝트 구조 생성 (Filesystem MCP)
├── src/
│   ├── main.py
│   ├── models.py
│   └── routes.py
├── tests/
│   └── test_api.py
├── docker/
│   └── Dockerfile
└── requirements.txt

2단계: GitHub에 레포 생성 (GitHub MCP)
├── 새 저장소 생성
├── README 작성
└── 초기 커밋

3단계: PostgreSQL 데이터베이스 설계 (PostgreSQL MCP)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

4단계: Docker 환경 설정 (Docker MCP)
docker-compose up -d  # PostgreSQL + API 서버

5단계: API 엔드포인트 구현
GET    /api/users      - 모든 사용자 조회
POST   /api/users      - 새 사용자 생성
GET    /api/users/:id  - 특정 사용자 조회
PUT    /api/users/:id  - 사용자 수정
DELETE /api/users/:id  - 사용자 삭제

6단계: 테스트 자동화
pytest tests/ -v
```

**Claude Code 대화 예시 (MCP 조합 활용)**

> "FastAPI + PostgreSQL로 사용자 관리 REST API 프로젝트를 만들어줘.
>  - Filesystem MCP로 src/, tests/, docker/ 구조 생성
>  - PostgreSQL MCP로 users 테이블 스키마 설계
>  - GitHub MCP로 새 레포 생성 및 초기 커밋
>  - Docker MCP로 docker-compose.yml 작성"

Claude Code가 각 MCP를 순차적으로 호출하여 프로젝트를 구성합니다. 사용자는 "생성된 models.py를 보여줘", "users 테이블에 role 컬럼을 추가해줘" 등 자연어로 후속 작업을 이어갈 수 있습니다.

핵심은 **사용자가 코드를 쓰지 않고 MCP에 작업을 위임**한다는 점입니다. Claude가 생성한 파일은 Plan 모드로 검토 후 승인할 수 있습니다.

### 문서 작업 워크플로우

```
목표: 기술 문서 자동 생성

1. Filesystem MCP: 프로젝트 코드 분석
2. Sequential Thinking MCP: 문서 구조 계획
3. GitHub MCP: 최신 변경사항 확인
4. Playwright MCP: 스크린샷 자동 캡처
5. 최종 문서 생성 (Markdown + PDF)
```

---

---

GSTACK은 Garry Tan의 23개 스킬 팩으로, Claude Code를 체계적으로 활용할 수 있게 합니다.

---

## 5-4. GSTACK 설치 및 설정

### 설치 방법

```bash
# GSTACK 설치
claude install-skill github.com/garrytan/gstack

# 설치 확인
claude --version  # Claude Code 버전 확인
claude skills list  # 설치된 스킬 목록
```

### 23개 GSTACK 스킬 설명

```
GSTACK Framework - 23 Skills

1️⃣ CEO / 전략 수립 (2개)
   /office-hours
   - 목적: 프로젝트 전략 상담
   - 사용 시기: 프로젝트 시작 또는 주요 결정 필요 시
   - 입력: 프로젝트 아이디어 또는 문제 상황
   - 출력: 전략적 조언, 우선순위 결정

   /plan-ceo-review
   - 목적: CEO 관점의 계획 리뷰
   - 사용 시기: 계획 수립 후 검토
   - 입력: 프로젝트 계획서
   - 출력: 비즈니스 임팩트 평가

2️⃣ Engineer / 기술 구현 (3개)
   /plan-eng-review
   - 목적: 엔지니어링 관점 기술 계획 리뷰
   - 확인 항목: 기술 스택 선택, 아키텍처 설계, 구현 가능성

   /review
   - 목적: 코드 품질 리뷰
   - 검토 항목: 코드 구조, 성능, 보안, 테스트 커버리지
   - 최적화 제안 제공

   /think
   - 목적: 깊은 기술적 사고와 분석
   - 사용 시기: 복잡한 기술 문제 해결 필요 시
   - Sequential Thinking MCP 활용

3️⃣ Designer / UX (2개)
   /design-consultation
   - 목적: UX/UI 전략 수립
   - 검토: 사용자 흐름, 접근성, 디자인 시스템

   /design-review
   - 목적: 디자인 상세 리뷰
   - 검토: 일관성, 가독성, 반응형 디자인

4️⃣ QA / 품질 보증 (2개)
   /qa
   - 목적: 종합 품질 보증 검사
   - 검토: 코드 + 테스트 + 성능
   - 결과: 테스트 코드 생성 및 개선안

   /qa-only
   - 목적: 테스트만 집중 실행
   - 결과: 테스트 커버리지 보고서

5️⃣ Release / 배포 (3개)
   /ship
   - 목적: 배포 준비 및 실행
   - 프로세스: 체크리스트 확인 → 배포 → 검증

   /land-and-deploy
   - 목적: 안전한 랜딩(병합) 및 배포
   - 프로세스: PR 리뷰 → 병합 → 배포 → 모니터링

   /canary
   - 목적: 카나리 배포 실행
   - 프로세스: 5% 사용자 → 25% → 100%

6️⃣ Security / 보안 (1개)
   /cso
   - 목적: 보안 최고 책임자(CSO) 관점 리뷰
   - 검토: 인증/인가, 데이터 보안, 규제 준수

7️⃣ Documentation (2개)
   /document-release
   - 목적: 릴리스 문서 자동 생성
   - 산출물: 변경사항, API 문서, 마이그레이션 가이드

   /retro
   - 목적: 회고 문서 작성
   - 산출물: 배운 점, 개선안, 다음 스프린트 계획

8️⃣ Planning & Analysis (7개)
   /weekly (주간 계획)
   /daily (일일 계획)
   /scope (범위 정의)
   /breakdown (작업 분해)
   /estimate (기간 산정)
   /risk (위험 분석)
   /deps (의존성 분석)
```

---

## 5-5. GSTACK 역할별 활용 가이드

### CEO 역할: 전략 수립

**시나리오: 새로운 SaaS 프로젝트 시작**

```bash
# 1단계: /office-hours로 전략 수립
claude /office-hours
입력:
"AI 기반 문서 자동화 SaaS를 만들려고 합니다.
 타겟: 중소 기업 (1-50명)
 핵심 기능: PDF/Word 문서 자동 생성, 템플릿 관리
 예상 MRR: $5,000
 우리의 강점: Python 개발팀, 머신러닝 경험"

출력:
✓ 시장 분석 및 경쟁사 분석
✓ GTM(Go-to-Market) 전략
✓ 단계별 마일스톤 (MVP → v1 → Scale)
✓ 펀딩 전략
✓ KPI 및 성공 지표

# 2단계: /plan-ceo-review로 계획 검증
claude /plan-ceo-review < sprint_plan.md

입력: 스프린트 계획서
출력:
✓ 비즈니스 임팩트 평가
✓ 리소스 할당 검토
✓ 일정 현실성 검토
✓ 위험 요소 식별
✓ 우선순위 재조정
```

### Engineer 역할: 기술 구현

**시나리오: 복잡한 마이크로서비스 아키텍처 설계**

```bash
# 1단계: /plan-eng-review로 기술 설계 검토
claude /plan-eng-review
입력:
"마이크로서비스 아키텍처 설계:
 - API Gateway (Kong)
 - User Service (Node.js)
 - Document Service (Python FastAPI)
 - AI Service (Python FastAPI + PyTorch)
 - Message Queue (RabbitMQ)
 - Database (PostgreSQL + Redis)"

출력:
✓ 기술 스택 타당성 검토
✓ 확장성/성능 분석
✓ 운영 복잡도 평가
✓ 마이그레이션 경로 제시
✓ 개선 제안

# 2단계: /think로 깊은 기술 분석
claude /think
입력: "AI Service의 레이턴시를 100ms 이하로 줄이려면?"

출력 (Sequential Thinking):
1️⃣ 현재 병목 분석
   - 모델 로드 시간: 50ms
   - 추론 시간: 40ms
   - I/O 오버헤드: 10ms

2️⃣ 해결 방안 개발
   - 모델 캐싱 (GPU 메모리)
   - 배치 처리
   - 요청 큐잉 최적화

3️⃣ 구현 계획
   - 단계 1: 모델 캐싱 구현 (5일)
   - 단계 2: 배치 처리 추가 (3일)
   - 단계 3: 성능 테스트 및 모니터링 (2일)

4️⃣ 예상 개선
   - 레이턴시: 100ms → 35ms 예상

# 3단계: /review로 코드 리뷰
claude /review < pull_request_123.diff

출력:
✓ 코드 품질 평가 (Pylint, SonarQube 기준)
✓ 성능 분석
✓ 보안 취약점 식별
✓ 테스트 커버리지 확인
✓ 개선 제안 + 수정 코드 제시
```

**/review 활용 시나리오**

> "/review 실행해줘. process_documents 함수가 for 루프 안에서 DB를 조회하고 있어서 느린 것 같아."

`/review` 스킬은 다음과 같은 관점에서 코드를 점검합니다.
- N+1 쿼리 패턴 감지 및 배치 쿼리 제안
- 동기 I/O를 비동기로 전환해야 할 부분 지적
- 에러 처리 및 로깅 누락 영역 표시
- 테스트 커버리지 부족 영역 리포트

리뷰 결과는 "Critical 2건, Warning 5건" 같은 요약과 함께 각 이슈에 대한 개선안을 제시합니다. 사용자는 "1번 이슈만 반영해줘"처럼 선택적으로 적용할 수 있습니다.

### QA 역할: 품질 보증

```bash
# 1단계: /qa로 종합 품질 검사
claude /qa
입력: src/ 디렉토리

출력:
✓ 코드 품질 점수: 8.5/10
✓ 테스트 커버리지: 78%
✓ 발견된 이슈:
  - 5개 중위험 (수정 필요)
  - 12개 저위험 (개선 권장)
✓ 테스트 코드 자동 생성 (미싱 부분)

# 2단계: /qa-only로 테스트만 집중
claude /qa-only
입력: src/ 디렉토리

출력:
✓ 테스트 실행 결과: 127 passed, 3 failed
✓ 새 테스트 코드 생성 (커버리지 보충)
✓ 성능 테스트 리포트
✓ 권장 사항
```

### Release 역할: 배포 관리

**시나리오: v2.0 릴리스 배포**

```bash
# 1단계: /ship로 배포 준비
claude /ship
입력:
"v2.0 배포:
 - Main branch commit: abc123...
 - Release notes: RELEASE_v2.0.md
 - Deployment target: Production"

출력:
배포 체크리스트:
☑ 모든 테스트 통과? ✓
☑ 코드 리뷰 완료? ✓
☑ 보안 검사 통과? ✓
☑ DB 마이그레이션 준비? ✓
☑ 롤백 계획 수립? ✓

배포 프로세스:
1️⃣ Staging 배포 및 검증
2️⃣ 성능 테스트 실행
3️⃣ Production 배포
4️⃣ 헬스 체크
5️⃣ 모니터링 설정

예상 다운타임: 0분 (무중단 배포)

# 2단계: /canary로 카나리 배포
claude /canary
입력:
"단계별 배포:
 - Phase 1: 5% 트래픽 (1시간)
 - Phase 2: 25% 트래픽 (30분)
 - Phase 3: 100% 트래픽"

배포 모니터링:
Phase 1 (5%):
  - Error rate: 0.01% (정상)
  - Latency: +2% (양호)
  → Phase 2 진행

Phase 2 (25%):
  - Error rate: 0.02% (정상)
  - Latency: +3% (양호)
  - Memory usage: +5% (양호)
  → Phase 3 진행

Phase 3 (100%):
  ✓ 배포 완료
  ✓ 모든 메트릭 정상
```

---

## 5-6. GSTACK + MCP 시너지 워크플로우

### 완전한 프로젝트 라이프사이클

```
📋 프로젝트: "AI 기반 이메일 템플릿 생성기"
목표: 사용자가 자연어로 이메일 템플릿을 생성하고 관리하는 SaaS

=====================================
1단계: 전략 수립 (1주)
=====================================

CEO: /office-hours
├─ 시장 분석 (Gmail, Outlook 사용자 타겟)
├─ MVP 범위 정의 (기본 템플릿 생성 + 저장)
└─ 6개월 로드맵 수립

┣━ /plan-ceo-review
  └─ 비즈니스 모델 검증 (구독형 vs 한번 구매)

=====================================
2단계: 기술 설계 (2주)
=====================================

Engineer: /plan-eng-review
├─ 기술 스택 선택
│  ├─ Frontend: Next.js (React + TypeScript)
│  ├─ Backend: Python FastAPI
│  ├─ AI: GPT-4 API
│  ├─ Database: PostgreSQL + Redis
│  └─ Infrastructure: Docker + Kubernetes
└─ 아키텍처 다이어그램 작성

┣━ /think (Sequential Thinking)
  └─ LLM 프롬프트 최적화 전략
    1️⃣ 현재 문제: 생성 속도 느림 (avg 5초)
    2️⃣ 분석: 토큰 수 많음, 스트리밍 미사용
    3️⃣ 솔루션: 스트리밍 + 프롬프트 최적화
    4️⃣ 예상 개선: 5초 → 2초

Designer: /design-consultation
└─ UI/UX 프로토타입 검토

=====================================
3단계: 개발 구현 (6주)
=====================================

GitHub MCP + Filesystem MCP:
프로젝트 구조 자동 생성
├── frontend/
│   ├── components/
│   ├── pages/
│   └── styles/
├── backend/
│   ├── app/
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── services.py
│   └── tests/
└── infra/
    ├── docker-compose.yml
    └── k8s/

Week 1-2: Backend API 개발
  Engineer: /review (매일)
  코드 품질 유지

Week 3-4: Frontend 개발
  Designer: /design-review
  UI 정확성 확인

Week 5-6: AI 통합
  Engineer: /think
  LLM API 최적화

=====================================
4단계: 품질 보증 (2주)
=====================================

QA: /qa
├─ 자동 테스트 커버리지: 85%로 목표
├─ 버그 식별 및 분류
└─ 성능 테스트

QA: /qa-only
├─ 엣지 케이스 테스트
├─ 부하 테스트 (1000 concurrent users)
└─ 보안 테스트

Security (CSO): /cso
├─ API 인증/인가 검증
├─ 데이터 암호화 확인
└─ GDPR 규제 준수 검토

=====================================
5단계: 배포 준비 (1주)
=====================================

Release: /document-release
├─ 변경사항 문서화
├─ API 문서 자동 생성 (OpenAPI)
└─ 마이그레이션 가이드

Release: /ship
├─ 배포 체크리스트 확인
├─ Staging 배포 및 검증
└─ Production 배포

Release: /canary (Progressive Rollout)
├─ Phase 1: 5% 사용자 (1시간)
├─ Phase 2: 25% 사용자 (30분)
└─ Phase 3: 100% 사용자

=====================================
6단계: 운영 및 최적화 (진행 중)
=====================================

모니터링 (PostgreSQL MCP + Memory MCP):
├─ 일일 사용자 수
├─ API 레이턴시
├─ 에러율
└─ AI 토큰 사용량

주간 /retro:
├─ 배운 점 정리
├─ 개선안 수집
└─ 다음 스프린트 계획
```

---

## 5-7. Plan 모드 & Sequential Thinking 활용법

### Plan 모드란?

Claude Code의 Plan 모드는 변경사항을 실제로 적용하기 전에 미리보기할 수 있는 기능입니다.

```
Plan Mode 장점:
✓ 예상치 못한 변경 방지
✓ 대량 파일 수정 시 검증
✓ 롤백 가능성 확보
✓ 팀 협업 시 코드 리뷰 용이
```

### Plan 모드 사용법

```bash
# 1. Plan 모드 활성화
claude --plan

# 2. 변경사항 요청
"이 프로젝트를 TypeScript로 마이그레이션해줘"

# 3. Claude Code가 변경 계획 제시
Plan Preview:
├─ 파일 생성: tsconfig.json
├─ 파일 생성: src/**/*.ts (15개 파일)
├─ 파일 수정: package.json
├─ 파일 삭제: src/**/*.js (15개 파일)
└─ 예상 소요 시간: 30분

# 4. 변경사항 확인 후 승인
"✓ 진행해줘"

# 5. 변경사항 적용
실제 파일 시스템에 변경 적용됨
```

### Sequential Thinking 활용법

Sequential Thinking은 복잡한 문제를 단계별로 논리적으로 분석합니다.

**시나리오: 성능 최적화 전략**

```bash
claude /think
입력:
"우리 API의 평균 응답 시간이 500ms입니다.
 현재 스택: Node.js + Express + PostgreSQL
 일일 요청: 1000만 건
 목표: 응답 시간을 100ms 이하로 줄이기"

Sequential Thinking 프로세스:

=====================================
Step 1: 문제 분석 (현재 상황 파악)
=====================================

병목 지점 식별:
1. Express 라우팅: 10ms
2. 비즈니스 로직: 150ms
3. 데이터베이스 쿼리: 300ms
4. 직렬화/응답: 40ms

가장 큰 문제: 데이터베이스 쿼리 (300ms = 60%)

=====================================
Step 2: 원인 분석 (왜?)
=====================================

DatabaseQuery 느린 이유:
1. 인덱스 부족
   - 자주 쿼리되는 컬럼에 인덱스 없음
   - 스캔 시간: 200ms

2. 캐싱 부재
   - 동일 쿼리 반복 실행
   - 불필요한 DB 부하

3. N+1 쿼리 문제
   - 부모 1개 쿼리 + 자식 100개 쿼리
   - 누적 시간: 100ms

=====================================
Step 3: 해결 방안 수립
=====================================

단기 (1주):
1. 핫 테이블에 인덱스 추가
   - 예상 개선: 200ms → 50ms

2. Redis 캐싱 추가
   - TTL: 300초
   - 캐시 히트율 목표: 70%
   - 예상 개선: 캐시 히트시 5ms

3. 쿼리 최적화
   - N+1 문제 해결 (JOIN으로 통합)
   - 예상 개선: 100ms → 20ms

중기 (1-2개월):
1. 데이터베이스 읽기 복제본 추가
   - Read-only 복제본 5개
   - Load balancing으로 부하 분산

2. GraphQL 도입
   - Over-fetching 방지
   - 필요한 필드만 쿼리

장기 (3개월):
1. Event-driven 아키텍처
   - 실시간 데이터 동기화
   - 이벤트 스트림 기반 업데이트

=====================================
Step 4: 구현 계획 (HOW?)
=====================================

Week 1: 데이터베이스 최적화
일정:
Mon-Tue: 인덱스 전략 수립 및 추가
  - EXPLAIN ANALYZE로 쿼리 분석
  - CREATE INDEX idx_user_status ON users(status, created_at)

Wed: Redis 캐싱 추가
  - Lua 스크립트로 원자성 보장
  - 캐시 무효화 전략 수립

Thu-Fri: 쿼리 최적화 (N+1 해결)
  - DataLoader 라이브러리 도입
  - 배치 쿼리 구현

테스트:
- Load 테스트: k6를 이용한 1만 RPS 테스트
- 캐시 히트율 모니터링
- 응답 시간 분포 분석

예상 결과:
- 응답 시간: 500ms → 120ms (76% 개선)

Week 2: 읽기 복제본 추가
- 복제 지연: < 100ms
- 장애 조치: 자동

Week 3: 모니터링 및 미세 조정

=====================================
Step 5: 검증 계획
=====================================

성공 기준:
✓ 평균 응답 시간 < 100ms
✓ p99 응답 시간 < 200ms
✓ 캐시 히트율 > 70%
✓ 에러율 < 0.01%

모니터링 메트릭:
- Prometheus + Grafana
- 리소스 사용률 (CPU, Memory)
- 데이터베이스 쿼리 시간 분포
- 캐시 히트/미스율

=====================================
Step 6: 위험 관리
=====================================

잠재적 위험:
1. 캐시 일관성 문제
   - 대책: Cache invalidation 전략 수립

2. 데이터베이스 마스터 부하 증가
   - 대책: 쓰기 배치 처리

3. 메모리 부족 (Redis)
   - 대책: LRU eviction 정책 설정

롤백 계획:
- 각 단계별 스냅샷 생성
- 문제 발견 시 이전 버전으로 즉시 복구
```

### 프로젝트 계획 통합 워크플로우

```
High-Level Project Planning Workflow:

1. /daily: 아침 회의
   "오늘의 일정과 우선순위"
   → 일일 계획 수립

2. /scope: 범위 정의
   "새로운 기능의 범위 명확히"
   → 요구사항 정의

3. /breakdown: 작업 분해
   "큰 작업을 작은 단위로"
   → User stories로 분해

4. /estimate: 기간 산정
   "각 작업의 예상 시간"
   → Story points 부여

5. /think + Sequential Thinking
   "복잡한 구현 전략 수립"
   → 상세 기술 계획

6. 개발 및 /review
   "코드 작성 및 리뷰"

7. /qa
   "품질 검사"

8. /ship
   "배포"

9. /retro
   "회고 및 학습"

This cycle repeats for continuous improvement.
```

---

## 5-8. 실전 통합 프로젝트 사례

### 사례: "AI 코드 리뷰 봇" SaaS 개발

**프로젝트 규모**: 2명 팀, 3개월 기간, $2,000 초기 MRR 목표

```
=====================================
Month 1: MVP 개발
=====================================

Week 1: CEO + Engineer 협업
1. /office-hours
   - 시장: GitHub 사용자 (개발자)
   - 차별점: LLM 기반 자동 코드 리뷰
   - GTM: Product Hunt 런칭

2. /plan-ceo-review
   - 비용 구조: OpenAI API 비용 고려
   - 가격 책정: 월 $29/$99/$299
   - KPI: 100명 가입 목표

3. /plan-eng-review
   - Backend: Python FastAPI
   - Frontend: Next.js
   - AI: GPT-4 API
   - 구현 기간: 4주

Week 2-3: 개발 집중
- Filesystem MCP: 프로젝트 구조 자동 생성
- /think: 복잡한 LLM 프롬프트 설계
  1️⃣ 코드 스타일 분석
  2️⃣ 버그 패턴 학습
  3️⃣ 성능 최적화 제안
  4️⃣ 보안 취약점 탐지

- GitHub MCP: 초기 커밋 및 자동화
- /review: 매일 코드 리뷰 (자동)

**GSTACK 워크플로우 시나리오 (MVP 개발 단계)**

Claude Code와의 실제 대화 흐름은 다음과 같습니다.

> "/think 로 LLM 코드 리뷰 프롬프트 전략을 설계해줘. 성능, 보안, 유지보수성, 테스트, 스타일 5가지 항목을 각각 점수화하고 JSON으로 반환하도록."

Sequential Thinking이 프롬프트 구조, few-shot 예시, 출력 스키마를 단계별로 설계합니다.

> "설계된 프롬프트로 CodeReviewer 서비스를 FastAPI 라우트로 구현해줘. Filesystem MCP로 backend/app/services/reviewer.py 에 생성."

> "/review 스킬로 방금 생성한 reviewer.py 를 점검해줘."

> "GitHub MCP로 dev 브랜치에 커밋하고 PR 초안을 만들어줘."

핵심은 **코드를 직접 쓰지 않고 GSTACK 스킬과 MCP 조합에 위임**한다는 점입니다. 사용자는 요구사항 정의와 의사결정에만 집중합니다.

Week 4: QA 및 배포 준비
- /qa: 테스트 커버리지 80% 확보
- /qa-only: 엣지 케이스 테스트
- /cso: 보안 검수 (API 키 관리, 데이터 암호화)

=====================================
Month 2: 베타 운영 및 개선
=====================================

Week 5-6: 초기 사용자 피드백
- Memory MCP: 피드백 저장 및 분석
- /daily: 우선순위 조정
- /think: 개선 전략 수립

주요 개선 사항:
1. 리뷰 정확도: 85% → 92%
2. 응답 시간: 8초 → 3초
3. 새 기능: GitHub Actions 통합

Week 7-8: 마케팅 준비
- /document-release: 변경사항 정리
- 블로그 포스트: "LLM으로 코드 리뷰 자동화"
- 데모 비디오 제작

=====================================
Month 3: 상용화 및 확장
=====================================

Week 9: Product Hunt 런칭
- /ship: 최종 배포 준비
- /canary: 트래픽 점진적 증대
  * Phase 1 (5%): 테스트 사용자
  * Phase 2 (25%): 초기 얼리 어댑터
  * Phase 3 (100%): 모든 사용자

주간 모니터링:
- 가입자: 50 → 150 → 400 (목표 500)
- 활성 사용자: 30% 유지율
- MRR: $500 → $1,500 → $2,200

Week 10-12: 팀 확장 및 로드맵
- /retro: 3개월 회고
  * 배운 점: LLM 프롬프트 엔지니어링의 중요성
  * 실수: 초기 인프라 스케일링 미비
  * 개선안: 자동 스케일링 구현

다음 분기 계획:
- 팀: 1명 엔지니어 추가
- 기능: GitLab, Bitbucket 지원
- 가격: 엔터프라이즈 플랜 추가
- 인프라: Kubernetes 마이그레이션

예상 12개월 MRR: $20,000
```

---

## 5-9. GSTACK 팁 및 베스트 프랙티스

### 효과적인 사용법

```
1. 올바른 스킬 선택
   ❌ /think로 단순 버그 수정 지시
   ✅ /think로 복잡한 알고리즘 설계 의뢰

   ❌ /review로 아이디어 브레인스토밍
   ✅ /review로 구현된 코드 평가

2. 입력 정보의 질이 출력 품질 결정
   ❌ "이 코드 리뷰해줘"
   ✅ "이 마이크로서비스의 N+1 쿼리를 해결하고 싶어.
        현재: 500ms, 목표: 100ms.
        스택: Node.js + PostgreSQL + Redis"

3. 반복적 개선
   /think → 계획 수립
   /plan-eng-review → 검증
   개발
   /review → 품질 확보
   /qa → 종합 검사

4. MCP 활용
   /think 후 GitHub MCP로 즉시 코드 작성
   Sequential Thinking 후 Filesystem MCP로 파일 생성
   계획 후 PostgreSQL MCP로 스키마 설계
```

