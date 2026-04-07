# Part 5: AI 개발 도구 — Claude Code, MCP, GSTACK

> Claude Code의 MCP 서버 생태계와 GSTACK 워크플로우를 통합해서 다룹니다.
> "AI와 함께 개발한다"가 실제로 뭘 의미하는지, 명령어와 대화 예시로 보여드립니다.

---

## 5분 만에 이해하는 Claude Code + MCP + GSTACK

### Claude Code가 뭔가요?

**한 줄 요약:** 터미널에서 자연어로 명령하면 코드를 읽고 고치고 커밋까지 해주는 AI 에이전트입니다.

```bash
# 설치 (npm)
npm install -g @anthropic-ai/claude-code

# 실행
claude
```

!!! info "📌 핵심 요약"
    - ChatGPT처럼 "대화"하지만, 실제로 **당신의 파일을 읽고 수정**합니다.
    - VS Code, Cursor, IntelliJ 어디서든 터미널만 있으면 동작합니다.
    - `Shift+Tab` 두 번으로 **Plan 모드** 진입 → 변경사항 미리 보고 승인.

### MCP가 뭔가요?

**한 줄 요약:** Claude Code가 GitHub, 파일시스템, DB, 브라우저 같은 **외부 도구**와 통신하는 표준 프로토콜입니다.

```text
[당신] → [Claude Code] → [MCP] → [GitHub / Postgres / Playwright / ...]
```

USB-C 포트를 생각하면 쉽습니다. 어떤 도구든 MCP 규격만 맞으면 Claude가 즉시 쓸 수 있습니다. 2025년 기준 공식 MCP 서버가 수십 개이고, 커뮤니티 서버는 수백 개입니다.

!!! tip "💡 꿀팁: MCP는 '도구 상자'"
    - **GitHub MCP** → 이슈, PR 관리
    - **Filesystem MCP** → 로컬 파일 탐색/수정
    - **Postgres MCP** → SQL 쿼리 실행
    - **Playwright MCP** → 브라우저 자동화
    - **Sequential Thinking MCP** → 단계별 논리 추론

### GSTACK이 뭔가요?

**한 줄 요약:** YC CEO Garry Tan이 만든 Claude Code용 23개 스킬 팩입니다. `/office-hours`, `/review`, `/ship` 같은 슬래시 명령어로 역할별 워크플로우를 제공합니다.

```bash
# 설치
claude install-skill github.com/garrytan/gstack
```

GSTACK은 "CEO처럼 전략을 짜라", "엔지니어처럼 코드 리뷰해라", "QA처럼 테스트 짜라" 같은 **역할 기반 프롬프트**를 슬래시 명령어로 캡슐화한 것입니다.

---

## Part 5 페이지 구조

| 페이지 | 내용 |
|--------|------|
| [5-1. 핵심 MCP 서버](01-mcp-core.md) | GitHub, Filesystem, Postgres, Sequential Thinking |
| [5-2. 생산성 MCP 서버](02-mcp-productivity.md) | Playwright, Memory, Docker |
| [5-3. MCP 조합 전략](03-mcp-strategy.md) | 여러 MCP를 엮어 자동화 파이프라인 만들기 |
| [5-4. GSTACK 설치 및 설정](04-gstack-install.md) | 설치, 23개 스킬 개요 |
| [5-5. GSTACK 역할별 가이드](05-gstack-roles.md) | CEO, Engineer, QA, Release 실전 활용 |
| [5-6. GSTACK + MCP 시너지](06-gstack-mcp-synergy.md) | 프로젝트 라이프사이클 전체 자동화 |
| [5-7. Plan 모드 & Sequential Thinking](07-plan-sequential.md) | 안전한 변경 + 단계별 추론 |
| [5-8. 실전 통합 사례](08-real-cases.md) | 실제 프로젝트에 적용한 예시 |
| [5-9. 팁 및 베스트 프랙티스](09-best-practices.md) | 시행착오에서 뽑아낸 노하우 |

!!! example "🤖 Claude Code 프롬프트: 나한테 맞는 시작점 찾기"
    ```
    나는 Spring Boot + React 풀스택 개발자 지망생이고,
    Claude Code를 막 설치했어. 어떤 MCP부터 설정하는 게 좋을지,
    그리고 가장 먼저 익혀야 할 GSTACK 스킬 3개를 추천해줘.
    이유도 함께 알려줘.
    ```

!!! example "🤖 Claude Code 프롬프트: 현재 환경 점검"
    ```
    claude mcp list 명령어를 실행해서 현재 설치된 MCP 서버를 보여주고,
    풀스택 개발에 꼭 필요한데 빠져있는 MCP가 있으면 설치 명령어를 추천해줘.
    ```

---

## 이 파트를 읽기 전 준비물

- [ ] Claude Code 설치 완료 (`claude --version` 으로 확인)
- [ ] Node.js 18 이상 (`node --version`)
- [ ] GitHub 계정 + Personal Access Token
- [ ] 기본 터미널 사용 경험 (`cd`, `ls`, 환경 변수)

!!! warning "⚠️ 주의: API 키는 절대 커밋하지 마세요"
    `GITHUB_TOKEN`, `DATABASE_URL` 같은 값은 `~/.claude/config.json` 혹은 `.env` 파일에 저장하고, 반드시 `.gitignore`에 추가하세요. 공개 레포에 토큰이 올라가면 수 분 내에 자동 스캐너에 걸려 악용됩니다.

!!! danger "🚨 자주 발생하는 에러: `claude: command not found`"
    - **원인:** npm 글로벌 경로가 PATH에 없음
    - **해결 (macOS/Linux):** `export PATH="$(npm config get prefix)/bin:$PATH"` 를 `~/.zshrc`에 추가
    - **해결 (Windows):** `npm config get prefix` 로 경로 확인 후 시스템 환경 변수 Path에 추가

---

## 이 파트에서 얻게 될 것

이 파트를 다 읽고 나면 다음과 같은 대화를 자연스럽게 할 수 있게 됩니다.

> **당신:** "이 레포의 최근 PR 10개를 훑어보고, 비슷한 버그가 반복되는 패턴이 있는지 분석해줘. 그리고 재발 방지용 테스트 케이스 초안까지 짜줘."
>
> **Claude:** *(GitHub MCP로 PR 조회 → Sequential Thinking으로 패턴 분석 → Filesystem MCP로 테스트 파일 생성 → Plan 모드로 변경사항 미리보기)*

이게 바로 "AI와 함께 개발한다"의 실체입니다. 다음 페이지부터 하나씩 직접 세팅해봅시다.
