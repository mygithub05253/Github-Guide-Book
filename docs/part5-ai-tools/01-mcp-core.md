# 5-1. 핵심 MCP 서버

> 개발자가 매일 쓰는 4개의 핵심 MCP 서버 — GitHub, Filesystem, PostgreSQL, Sequential Thinking — 를 설치하고 실전에서 활용하는 방법을 다룹니다.

---

## MCP가 다시 한번 뭐였죠?

Model Context Protocol(MCP)은 Claude Code가 외부 도구와 통신하기 위한 표준입니다. 아래 구조를 기억하면 됩니다.

```text
Claude Code (LLM)
      ↓  자연어 명령
MCP Client (Claude 내장)
      ↓  표준 프로토콜
MCP Server (GitHub / Filesystem / Postgres / ...)
      ↓  각 서비스의 API
External Services
```

!!! info "📌 핵심 요약"
    MCP 서버는 대부분 **npm 패키지**로 제공됩니다. `claude mcp add` 명령어 한 줄로 설치되고, `~/.claude/config.json` 에 설정이 저장됩니다.

---

## 1) GitHub MCP — 레포지토리 관리 자동화

### 이걸 언제 써야 하는가

- 이슈를 수십 개 한 번에 정리하거나 라벨링하고 싶을 때
- PR 변경사항을 Claude에게 보여주고 리뷰를 요청할 때
- "이 레포의 최근 커밋 100개 중 security 관련 커밋만 뽑아줘" 같은 복합 질의

### 설치

```bash
claude mcp add github -s user -- npx -y @modelcontextprotocol/server-github
```

환경 변수로 GitHub Personal Access Token을 지정해야 합니다.

```bash
# macOS / Linux
export GITHUB_TOKEN=ghp_your_token_here

# Windows PowerShell
$env:GITHUB_TOKEN="ghp_your_token_here"
```

### 설정 파일 (`~/.claude/config.json`)

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

!!! info "예상 출력"
    ```text
    ✓ Added MCP server 'github' to user scope
    ✓ Configuration written to ~/.claude/config.json
    ```

!!! danger "🚨 자주 발생하는 에러: 401 Unauthorized"
    - **원인:** PAT에 `repo` 권한이 없거나 만료됨
    - **해결:** [github.com/settings/tokens](https://github.com/settings/tokens)에서 `repo`, `read:org` 권한을 포함한 classic token 재발급
    - **주의:** Fine-grained token은 일부 API 호환성 문제가 있습니다. 처음엔 classic token을 권장합니다.

### 실제 대화 예시

!!! example "🤖 Claude Code 프롬프트: 이슈 분석"
    ```
    facebook/react 레포의 최근 열린 이슈 20개를 가져와서
    카테고리별(버그/기능 요청/문서)로 분류하고,
    가장 많이 언급된 API를 알려줘.
    ```

    **Claude 응답 (요약):**
    > GitHub MCP로 이슈 20개를 조회했습니다. 분류 결과:
    > - 버그: 12건 (useEffect 관련 4건, Suspense 3건...)
    > - 기능 요청: 5건
    > - 문서: 3건
    >
    > 가장 많이 언급된 API는 `useEffect`와 `<Suspense>`입니다.

!!! example "🤖 Claude Code 프롬프트: PR 리뷰"
    ```
    내 레포 myname/myproject 의 PR #42 를 열어보고,
    변경사항을 분석해서 잠재적인 버그나 성능 이슈가 있는지 리뷰해줘.
    특히 N+1 쿼리 패턴과 에러 처리 누락을 중점으로 봐줘.
    ```

!!! warning "⚠️ 주의: Rate Limit"
    GitHub API는 인증된 요청 기준 시간당 5,000회 제한이 있습니다. 큰 레포에서 수백 개 이슈를 한 번에 당기면 금방 소진되니, "상위 20개"처럼 범위를 명시하는 습관을 들이세요.

---

## 2) Filesystem MCP — 로컬 파일 시스템 접근

### 이걸 언제 써야 하는가

- 프로젝트 전체를 Claude에게 탐색시키고 싶을 때
- 특정 디렉토리 하위의 파일만 대량 수정할 때
- 로그 파일에서 에러 패턴을 찾을 때

### 설치

```bash
claude mcp add filesystem -s local -- \
  npx -y @modelcontextprotocol/server-filesystem /path/to/workspace
```

!!! warning "⚠️ 주의: 경로는 절대 경로"
    상대 경로(`./workspace`)는 동작하지 않습니다. Windows에서는 `C:/Users/kik32/workspace` 처럼 **슬래시**를 쓰는 편이 안전합니다.

### 설정 파일

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:/Users/kik32/workspace"
      ]
    }
  }
}
```

### 실전 대화 예시

!!! example "🤖 Claude Code 프롬프트: 프로젝트 탐색"
    ```
    workspace/PLAF 디렉토리 구조를 tree 형태로 보여주고,
    각 디렉토리의 역할을 한 줄씩 설명해줘.
    너무 깊게 내려가지는 말고 2단계까지만.
    ```

!!! example "🤖 Claude Code 프롬프트: 로그 분석"
    ```
    logs/ 디렉토리의 모든 .log 파일을 스캔해서
    "ERROR" 레벨 로그만 추출하고, 가장 빈번한 에러 메시지
    상위 5개를 빈도와 함께 표로 정리해줘.
    ```

!!! danger "🚨 자주 발생하는 에러: Permission Denied"
    - **원인:** Filesystem MCP는 허용된 루트 디렉토리 밖으로 나갈 수 없음
    - **해결:** `claude mcp add` 시 지정한 경로를 충분히 상위로 잡거나, 필요하면 여러 루트를 동시에 허용

---

## 3) PostgreSQL MCP — 데이터베이스 연동

### 이걸 언제 써야 하는가

- SQL을 직접 치기 귀찮을 때 (자연어 → SQL 자동 변환)
- 쿼리 결과를 바로 분석·시각화하고 싶을 때
- 스키마를 읽고 Claude에게 ORM 모델을 생성시킬 때

### 설치

```bash
claude mcp add postgres -s user -- npx -y @modelcontextprotocol/server-postgres
```

### 설정 파일

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

!!! warning "⚠️ 주의: 프로덕션 DB에는 절대 붙이지 마세요"
    MCP는 편리하지만 Claude가 의도치 않게 `DELETE`를 실행할 수도 있습니다. **읽기 전용 계정**(`GRANT SELECT ...`)을 따로 만들어서 연결하는 게 안전합니다.

### 실전 대화 예시

!!! example "🤖 Claude Code 프롬프트: 스키마 탐색"
    ```
    현재 연결된 DB의 모든 테이블 목록을 보여주고,
    각 테이블의 행 수와 주요 컬럼을 요약해줘.
    그리고 users 테이블과 orders 테이블의 관계를 ERD 형태로 설명해줘.
    ```

!!! example "🤖 Claude Code 프롬프트: 자연어 쿼리"
    ```
    지난 30일 동안 주문 금액이 10만 원 이상인 사용자를
    주문 횟수 순으로 상위 20명 뽑아줘. 가명 처리해서 보여줘.
    ```

    Claude는 내부적으로 다음과 비슷한 SQL을 생성해 실행합니다.

    ```sql
    SELECT
      LEFT(MD5(u.id::text), 8) AS user_hash,
      COUNT(o.id) AS order_count,
      SUM(o.amount) AS total
    FROM users u
    JOIN orders o ON o.user_id = u.id
    WHERE o.created_at > NOW() - INTERVAL '30 days'
      AND o.amount >= 100000
    GROUP BY u.id
    ORDER BY order_count DESC
    LIMIT 20;
    ```

!!! tip "💡 꿀팁: EXPLAIN ANALYZE도 맡기세요"
    "이 쿼리가 왜 느린지 EXPLAIN ANALYZE 실행해서 분석해줘" 라고 하면 실행 계획을 읽고 인덱스 추가 제안까지 해줍니다.

---

## 4) Sequential Thinking MCP — 단계별 논리 추론

### 이걸 언제 써야 하는가

- 즉답보다 **근거 있는 결론**이 필요한 문제
- 알고리즘 설계, 아키텍처 결정, 복잡한 버그 원인 분석
- "왜 그런 선택을 했는지" 과정이 중요할 때

### 설치

```bash
claude mcp add sequential-thinking -s local -- \
  npx -y @modelcontextprotocol/server-sequential-thinking
```

### 설정 파일

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

### 일반 응답 vs Sequential Thinking

**일반 응답:**

> Q: "PostgreSQL에서 MongoDB로 마이그레이션은 어떻게 하나요?"
> A: "pg_dump로 내보내고 스크립트로 변환하면 됩니다." *(끝)*

**Sequential Thinking:**

> Q: 동일
>
> **Step 1** — 현재 스키마 분석: 관계형 vs 문서형의 적합성 평가
>
> **Step 2** — 데이터 모델 재설계: 임베딩 vs 참조 전략
>
> **Step 3** — 마이그레이션 순서: 참조 테이블 → 트랜잭션 테이블 순
>
> **Step 4** — 검증 전략: 행 수 비교, 샘플링 검증, 쿼리 성능 비교
>
> **Step 5** — 롤백 계획

### 실전 대화 예시

!!! example "🤖 Claude Code 프롬프트: 버그 원인 분석"
    ```
    Sequential Thinking으로 분석해줘.
    우리 API 서버가 매일 새벽 3시에만 응답 시간이 10배 느려져.
    가능한 원인을 단계별로 가설-검증 형태로 나열하고,
    가장 의심스러운 원인 TOP 3에 대해 구체적인 확인 방법을 제시해줘.
    ```

!!! example "🤖 Claude Code 프롬프트: 알고리즘 설계"
    ```
    Sequential Thinking으로 설계해줘.
    10만 명 규모의 실시간 리더보드를 만들어야 해.
    Redis ZSET vs PostgreSQL 인덱스 vs Elasticsearch를 비교하고,
    우리 환경(월 활성 사용자 5만, Spring Boot)에 가장 적합한 선택을 추천해줘.
    ```

!!! tip "💡 꿀팁: 'Sequential Thinking으로' 라고 명시하세요"
    프롬프트 맨 앞에 이 한 마디만 추가해도 Claude가 훨씬 체계적인 단계별 답변을 생성합니다.

!!! warning "⚠️ 주의: 간단한 질문엔 오히려 느려요"
    "파이썬에서 리스트 뒤집기 방법" 같은 간단 질의에는 Sequential Thinking이 오버엔지니어링입니다. 복잡도가 중간 이상일 때만 쓰세요.

---

## 이 페이지를 마치고 나면

- [ ] 4개 MCP 서버를 모두 설치했다 (`claude mcp list` 로 확인)
- [ ] GitHub PAT, `DATABASE_URL`을 환경 변수로 등록했다
- [ ] 각 MCP별 예제 프롬프트를 최소 1개씩 직접 돌려봤다
- [ ] 에러가 나도 당황하지 않고 `claude mcp list` + 설정 파일을 확인할 줄 안다

다음 페이지에서는 Playwright, Memory, Docker 같은 **생산성 MCP**를 다룹니다.
