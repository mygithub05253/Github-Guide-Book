# 1-2. 코딩 입문 - 실전 프로젝트

> "책만 읽고 영상만 본다고 코딩이 늘지 않아요."
> 이 챕터는 **실제로 손을 움직여서 뭔가를 만들어보는** 실전 프로젝트 중심 레포들을 소개합니다.

!!! info "📌 핵심 요약"
    - **freeCodeCamp**: 무료로 수백 시간짜리 프로젝트 기반 커리큘럼
    - **TheOdinProject**: 풀스택 개발자가 되기 위한 오픈소스 로드맵
    - **build-your-own-x**: Git, Redis, Docker를 직접 만들어보며 내부 원리 이해

---

## freeCodeCamp/freeCodeCamp (410K+ Stars)

**링크**: https://github.com/freeCodeCamp/freeCodeCamp

**한 줄 소개**: 완전 무료, 브라우저에서 바로 실습 가능한 종합 코딩 부트캠프.
**왜 봐야 하는가**: 회원가입만 하면 **자동 채점 + 프로젝트 포트폴리오 + 수료증**까지 나옵니다. 비전공자에게 가장 친절한 입문 플랫폼이에요.
**난이도**: ⭐⭐

### 📋 이 레포가 다루는 내용

- Responsive Web Design (300시간) — HTML/CSS/Flexbox/Grid
- JavaScript Algorithms and Data Structures (300시간)
- Front End Development Libraries (React, Redux, Bootstrap)
- Data Visualization (D3.js)
- Back End Development and APIs (Node.js, Express, MongoDB)
- 각 과정마다 **5개 필수 프로젝트** 제출 후 수료증 발급

### 🚀 15분 퀵스타트

1단계. https://www.freecodecamp.org/ 에 회원가입 (GitHub 계정 연동 가능)

2단계. Responsive Web Design 코스 시작

3단계. 개발 환경은 브라우저만 있으면 OK. 로컬에서 하고 싶다면 아래 툴 설치.

```bash
# Node.js 설치 확인
node --version  # v20.x.x 이상
npm --version   # 10.x.x 이상

# VS Code 권장 확장
# - Live Server
# - Prettier
# - ESLint
```

예상 출력:

```
v20.11.0
10.2.4
```

4단계. 첫 도전 프로젝트 "Build a Survey Form" 시작하기

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Survey Form</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1 id="title">사용자 설문조사</h1>
  <p id="description">5분이면 충분해요!</p>
  <form id="survey-form">
    <label id="name-label">이름
      <input id="name" type="text" required>
    </label>
  </form>
</body>
</html>
```

!!! tip "💡 꿀팁: Responsive Web Design 5개 프로젝트 순서"
    1. Tribute Page (인물 소개) — HTML 기초
    2. Survey Form (설문 폼) — Form 요소
    3. Product Landing Page — Flexbox
    4. Technical Documentation Page — Grid
    5. Personal Portfolio — 종합 응용

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트: 접근성 리뷰"
    > "내가 만든 index.html과 style.css를 리뷰해줘. 반응형(@media 768px 기준)과 접근성(a11y) 관점에서 개선점을 구체적으로 알려줘."

!!! example "🤖 Claude Code 프롬프트: 프로젝트 요구사항 확인"
    > "freeCodeCamp의 Survey Form 프로젝트 요구사항 17개를 체크리스트로 만들고, 내 코드에서 빠진 항목만 표시해줘."

!!! example "🤖 Claude Code 프롬프트: 코드 리팩토링"
    > "내 JavaScript 코드가 너무 길어. 함수로 분리하고 변수명을 더 명확하게 리팩토링해줘. 변경 이유도 주석으로 남겨줘."

### 📚 학습 체크리스트

- [ ] freeCodeCamp 회원가입 + GitHub 연동
- [ ] Responsive Web Design 50% 이상 진행
- [ ] 필수 프로젝트 5개 중 3개 완료
- [ ] GitHub에 프로젝트 저장소 생성
- [ ] JavaScript 코스 시작

!!! warning "⚠️ 자주 하는 실수"
    **"모든 연습 문제를 100% 풀어야 한다"는 강박**.
    어려우면 건너뛰고 프로젝트 5개 완성에 집중하세요. 프로젝트가 곧 포트폴리오입니다.

---

## TheOdinProject/curriculum (10K+ Stars)

**링크**: https://github.com/TheOdinProject/curriculum

**한 줄 소개**: 무료 풀스택 웹 개발 커리큘럼 — HTML부터 배포까지 전 과정.
**왜 봐야 하는가**: freeCodeCamp가 "연습 중심"이라면 Odin Project는 "실전 프로젝트 중심"입니다. **GitHub에 커밋하며 포트폴리오를 쌓는** 스타일이에요.
**난이도**: ⭐⭐⭐

### 📋 이 레포가 다루는 내용

- Foundations (10~20주) — JavaScript, HTML, CSS, Flexbox/Grid
- JavaScript 심화 (12~20주) — DOM, OOP, Async, Testing
- React 또는 Ruby on Rails 선택
- Getting Hired — 포트폴리오, 이력서, 면접 준비

### 🚀 15분 퀵스타트

1단계. https://www.theodinproject.com/ 가입

2단계. Foundations 첫 프로젝트: **가위바위보 게임** 시작

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
  <h1>가위바위보</h1>
  <div>
    <button id="rock">✊ 바위</button>
    <button id="paper">✋ 보</button>
    <button id="scissors">✌️ 가위</button>
  </div>
  <p id="result"></p>
  <script src="game.js"></script>
</body>
</html>
```

```javascript
// game.js
function getComputerChoice() {
  const choices = ['rock', 'paper', 'scissors'];
  return choices[Math.floor(Math.random() * 3)];
}

function playRound(player, computer) {
  if (player === computer) return '무승부';
  if (
    (player === 'rock' && computer === 'scissors') ||
    (player === 'paper' && computer === 'rock') ||
    (player === 'scissors' && computer === 'paper')
  ) {
    return '승리';
  }
  return '패배';
}

document.querySelectorAll('button').forEach((btn) => {
  btn.addEventListener('click', () => {
    const computer = getComputerChoice();
    const result = playRound(btn.id, computer);
    document.getElementById('result').textContent =
      `컴퓨터: ${computer} → ${result}`;
  });
});
```

예상 동작: 버튼 클릭 시 "컴퓨터: scissors → 승리" 같은 결과 표시.

!!! tip "💡 꿀팁: Odin Project 학습법"
    - **"읽고 → 만들고 → 커밋"** 사이클을 지키세요.
    - 프로젝트마다 별도 Git 저장소를 만들고, 커밋 메시지는 한국어도 OK.
    - Discord 커뮤니티가 활발해서 막히면 바로 질문 가능.

### 주요 실습 프로젝트

1. **가위바위보** — `Math.random()`, DOM 이벤트, 상태 관리
2. **계산기** — ES6 Class, 상태(`currentOperand`/`previousOperand`), 데이터 속성
3. **Etch-a-Sketch** — 동적 DOM 생성, 마우스 이벤트
4. **도서관 앱** — localStorage, CRUD
5. **틱택토** — 모듈 패턴, Factory 함수

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트: 엣지 케이스 발견"
    > "내 계산기 앱 코드를 보고 '소수점 2번 입력', '0으로 나누기', '연속 연산자 입력' 같은 엣지 케이스를 어떻게 처리해야 하는지 알려줘."

!!! example "🤖 Claude Code 프롬프트: 요구사항 체크"
    > "The Odin Project의 Calculator 프로젝트 요구사항 리스트를 검색해서, 내 코드가 빠뜨린 기능을 표로 정리해줘."

!!! example "🤖 Claude Code 프롬프트: OOP 리팩토링"
    > "내 틱택토 코드를 Factory 함수와 모듈 패턴으로 리팩토링해줘. Odin Project 스타일에 맞게 해주고 왜 그렇게 했는지 설명해줘."

### 📚 학습 체크리스트

- [ ] Foundations 과정 완료
- [ ] 가위바위보, 계산기 프로젝트 완성
- [ ] 각 프로젝트를 GitHub Pages에 배포
- [ ] JavaScript 심화 과정 시작
- [ ] React 또는 Rails 중 하나 선택

---

## codecrafters-io/build-your-own-x (330K+ Stars)

**링크**: https://github.com/codecrafters-io/build-your-own-x

**한 줄 소개**: "Git, Docker, Redis를 직접 만들어보면서 내부 동작 원리 이해하기" 튜토리얼 모음.
**왜 봐야 하는가**: **"블랙박스 해체"** 경험은 개발자로서 격을 한 단계 올려줍니다. 단순 사용자를 넘어 "만들 수 있는 사람"이 되는 경험이에요.
**난이도**: ⭐⭐⭐⭐

### 📋 이 레포가 다루는 내용

- **Build Your Own Git** (Rust/Python/Go) — 객체 읽기, 커밋, 트리
- **Build Your Own Docker** (Go) — 네임스페이스, cgroups
- **Build Your Own Redis** (Python/Ruby/Go) — TCP 서버, RESP 프로토콜
- **Build Your Own Language** (Go/Python) — 렉서, 파서, 인터프리터
- 총 100개 이상의 프로젝트, 모든 언어 커버

### 🚀 15분 퀵스타트 — Mini Redis 만들기

1단계. Python 3.10+ 준비

2단계. 최소 TCP 서버 작성 (약 30줄)

```python
# mini_redis.py
import socket

HOST = '127.0.0.1'
PORT = 6380  # 6379는 진짜 Redis가 쓰므로 6380 사용
storage = {}

def handle_command(cmd: str) -> str:
    parts = cmd.strip().split()
    if not parts:
        return "ERROR: empty command"
    op = parts[0].upper()
    if op == 'SET' and len(parts) == 3:
        storage[parts[1]] = parts[2]
        return "OK"
    if op == 'GET' and len(parts) == 2:
        return storage.get(parts[1], "(nil)")
    if op == 'DEL' and len(parts) == 2:
        return "1" if storage.pop(parts[1], None) else "0"
    return "ERROR: unknown command"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
    srv.bind((HOST, PORT))
    srv.listen()
    print(f"Mini Redis listening on {HOST}:{PORT}")
    while True:
        conn, addr = srv.accept()
        with conn:
            data = conn.recv(1024).decode()
            response = handle_command(data)
            conn.sendall(response.encode())
```

3단계. 실행

```bash
python mini_redis.py
```

예상 출력:

```
Mini Redis listening on 127.0.0.1:6380
```

4단계. 다른 터미널에서 테스트

```bash
# PowerShell
echo "SET foo bar" | nc 127.0.0.1 6380
# 예상 출력: OK

echo "GET foo" | nc 127.0.0.1 6380
# 예상 출력: bar
```

!!! tip "💡 꿀팁: 작게 시작하기"
    build-your-own-x의 튜토리얼은 대부분 길고 어렵습니다.
    **"1주차엔 TCP 서버만, 2주차엔 RESP 프로토콜만"** 처럼 서브셋으로 쪼개세요.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트: 서브셋 쪼개기"
    > "build-your-own-x의 Build Your Own Redis 챕터를 읽고, 비전공자가 1주차에 구현해볼 수 있는 가장 작은 서브셋 3가지를 추천해줘. 각 서브셋마다 학습할 개념도 같이."

!!! example "🤖 Claude Code 프롬프트: 구현 가이드"
    > "내 Mini Redis에 EXPIRE (키 만료) 기능을 추가하고 싶어. Python `threading`과 `time` 모듈만 사용해서 최소 구현 예제 코드를 보여주고, 왜 그렇게 설계했는지 설명해줘."

!!! example "🤖 Claude Code 프롬프트: 비교 분석"
    > "내가 짠 Mini Redis 코드와 진짜 Redis의 아키텍처를 비교해서, 내 구현이 놓치고 있는 3가지 핵심 개념을 알려줘."

### 📚 학습 체크리스트

- [ ] Mini Redis SET/GET/DEL 동작 확인
- [ ] RESP 프로토콜 파싱 추가
- [ ] EXPIRE 기능 추가
- [ ] Build Your Own Git 중 `cat-file` 명령 구현
- [ ] 회고 블로그 1편 작성

### 📚 학습 로드맵

| 기간 | 프로젝트 | 목표 |
|------|---------|------|
| 1개월 | Git 기본 개념 + Mini TCP 서버 | 네트워크 기초 |
| 2~3개월 | Redis 서버 전체 구현 | 동시성 처리 |
| 3~6개월 | 언어 만들기 또는 Docker | 시스템 내부 |

!!! danger "🚨 자주 발생하는 에러"
    **에러**: `OSError: [Errno 98] Address already in use`
    **원인**: 이전 서버 프로세스가 포트를 점유 중
    **해결**:

    ```bash
    # Windows
    netstat -ano | findstr :6380
    taskkill /PID <PID> /F

    # macOS/Linux
    lsof -ti :6380 | xargs kill -9
    ```

---

!!! tip "💡 다음 단계"
    이제 프로젝트를 만들 줄 알게 되셨으니, 면접에서 이 경험을 어떻게 어필할지 배워볼 시간이에요.
    [1-3. 면접 준비](03-interview-prep.md)로 이동하세요.
