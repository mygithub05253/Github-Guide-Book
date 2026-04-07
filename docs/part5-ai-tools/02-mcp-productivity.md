# 5-2. 생산성 MCP 서버

> Playwright, Memory, Docker — 개발 생산성을 한 단계 끌어올리는 MCP들을 다룹니다.

---

## 1) Playwright MCP — 브라우저 자동화

### 이걸 언제 써야 하는가

- 웹사이트에서 반복 작업(로그인, 폼 작성, 데이터 수집)을 자동화할 때
- E2E 테스트 자동화
- UI 버그 스크린샷 자동 캡처

### 설치

```bash
claude mcp add playwright -s user -- npx -y @modelcontextprotocol/server-playwright
```

!!! warning "⚠️ 주의: 브라우저 바이너리 설치 필요"
    최초 사용 시 Chromium 바이너리가 다운로드됩니다 (~200MB). 네트워크가 느리면 몇 분 걸립니다.

### 실전 대화 예시

!!! example "🤖 Claude Code 프롬프트: 웹 스크래핑"
    ```
    github.com/trending 페이지에 접속해서 오늘의 인기 Python 레포
    상위 10개를 가져와줘. 각 레포의 이름, stars, 설명을 표로 정리하고
    결과를 trending.md 파일로 저장해줘.
    ```

!!! example "🤖 Claude Code 프롬프트: 폼 테스트"
    ```
    우리 스테이징 서버(https://staging.myapp.com/login)에 접속해서
    잘못된 비밀번호로 로그인을 시도했을 때 어떤 에러 메시지가 뜨는지
    스크린샷과 함께 확인해줘. 그 다음 올바른 비밀번호(.env의 TEST_PASS)로
    로그인해서 대시보드가 정상 렌더되는지 검증해줘.
    ```

!!! danger "🚨 자주 발생하는 에러: `TimeoutError: page.goto timeout 30000ms exceeded`"
    - **원인:** 네트워크 느림 또는 사이트가 봇 차단
    - **해결:** 프롬프트에 "waitUntil은 domcontentloaded로, timeout은 60초로 설정해줘" 명시

!!! tip "💡 꿀팁: 헤드풀 모드로 디버깅"
    "브라우저를 headless: false 모드로 열어서 실제로 뭘 하는지 보여줘" 라고 하면 실제 브라우저 창이 뜨면서 동작합니다. 무슨 일이 벌어지는지 눈으로 확인할 수 있어 디버깅에 최고입니다.

---

## 2) Memory MCP — 세션 간 지식 유지

### 이걸 언제 써야 하는가

- Claude와의 대화가 세션마다 초기화되는 게 답답할 때
- 프로젝트 컨텍스트, 결정 사항, 학습 기록을 지속 저장
- 여러 날에 걸친 장기 프로젝트

### 설치

```bash
claude mcp add memory -s user -- npx -y @modelcontextprotocol/server-memory
```

### 실전 대화 예시

!!! example "🤖 Claude Code 프롬프트: 컨텍스트 저장"
    ```
    우리 프로젝트의 핵심 정보를 메모리에 저장해줘:
    - 프로젝트명: PLAF (GitHub 가이드북)
    - 기술 스택: Python, MkDocs Material, WeasyPrint
    - 현재 단계: Part 5 리팩토링 중
    - 중요 결정: docx/pdf는 자동 생성, 원본은 md만 유지

    다음 세션에서 "프로젝트 상태 알려줘" 라고 물어보면 이 정보를 참고해줘.
    ```

!!! example "🤖 Claude Code 프롬프트: 학습 진도 추적"
    ```
    메모리에서 내 Spring Boot 학습 진도를 조회하고,
    지금까지 완료한 주제와 다음에 배울 주제를 알려줘.
    오늘 @Transactional 을 공부했으니 그것도 추가해줘.
    ```

!!! info "📌 핵심 요약"
    Memory MCP는 로컬 JSON/SQLite에 지식 그래프를 저장합니다. 민감한 정보(API 키, 비밀번호)는 절대 저장하지 마세요.

---

## 3) Docker MCP — 컨테이너 관리

### 이걸 언제 써야 하는가

- Dockerfile을 직접 쓰기 귀찮을 때
- `docker-compose.yml` 자동 생성
- 실행 중인 컨테이너 로그·통계 조회

### 설치

```bash
claude mcp add docker -s user -- npx -y @modelcontextprotocol/server-docker
```

!!! warning "⚠️ 주의: Docker Desktop이 먼저 실행 중이어야 함"
    `docker ps` 명령어가 에러 없이 동작해야 MCP도 동작합니다.

### 실전 대화 예시

!!! example "🤖 Claude Code 프롬프트: Dockerfile 자동 생성"
    ```
    내 프로젝트(package.json이 있는 Next.js 앱)를 Docker화해줘.
    - 멀티 스테이지 빌드 사용 (builder / runner)
    - node:20-alpine 베이스
    - 프로덕션 최적화 (standalone output)
    - 포트 3000 노출
    - 파일은 ./Dockerfile 에 저장
    ```

!!! example "🤖 Claude Code 프롬프트: docker-compose 구성"
    ```
    FastAPI + PostgreSQL + Redis 조합의 docker-compose.yml을 만들어줘.
    - 개발용 환경 (볼륨 마운트로 hot reload)
    - Postgres는 15-alpine
    - Redis는 7-alpine
    - 환경 변수는 .env 파일에서 읽기
    - 헬스체크 추가
    ```

!!! example "🤖 Claude Code 프롬프트: 실행 중 컨테이너 디버깅"
    ```
    지금 실행 중인 컨테이너 목록을 보여주고,
    'myapp' 컨테이너의 최근 로그 100줄을 분석해서
    에러가 있으면 원인과 해결 방법을 알려줘.
    ```

!!! danger "🚨 자주 발생하는 에러: `Cannot connect to the Docker daemon`"
    - **원인:** Docker Desktop이 꺼져 있거나 재시작 필요
    - **해결:** Docker Desktop 실행 확인 → `docker info` 로 테스트
    - **WSL2 사용 시:** Docker Desktop 설정에서 WSL Integration 활성화

---

## 3개 MCP를 조합한 시나리오

!!! example "🤖 Claude Code 프롬프트: 통합 자동화"
    ```
    다음을 순서대로 수행해줘:
    1. (Playwright) my-staging.com 에 접속해서 스모크 테스트 실행
    2. 실패한 페이지가 있으면 스크린샷 저장
    3. (Memory) 실패 내역을 오늘 날짜로 메모리에 기록
    4. (Docker) 로컬 Docker의 my-app 컨테이너 로그에서 해당 시간대 에러를 추출
    5. 종합 보고서를 report.md 로 저장
    ```

이 한 줄 요청으로 세 MCP가 유기적으로 협력합니다. 혼자 손으로 하면 1시간 걸릴 작업이 몇 분으로 줄어듭니다.

---

## 체크리스트

- [ ] Playwright MCP 설치 + 브라우저 바이너리 다운로드 완료
- [ ] Memory MCP 로 프로젝트 컨텍스트 한 번 저장해봤다
- [ ] Docker Desktop 실행 확인 후 Docker MCP로 `docker ps` 동등 작업 해봤다
- [ ] 3개 MCP 조합 프롬프트를 최소 1개 직접 시도했다

다음 페이지에서는 여러 MCP를 조합하는 **전략적 워크플로우**를 다룹니다.
