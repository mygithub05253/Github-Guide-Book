# 6-2. 금융/공기업 취업에 도움되는 레포지토리

> 기술 면접만으로는 부족해요. 금융권/공기업은 **도메인 지식**과 **보안/안정성 마인드셋**을 중요하게 봅니다.
> 이 챕터에서는 면접관이 "오, 이 친구 우리 업계 좀 아네?"라고 느끼게 만들 레포들을 소개합니다.

!!! info "📌 핵심 요약"
    - **금융 IT**: QuantConnect/Lean (트레이딩), OpenBB (투자 분석)
    - **공기업 코테**: TheAlgorithms/Python, neetcode-io/leetcode
    - **보안 & 인프라**: OWASP/CheatSheetSeries, the-book-of-secret-knowledge
    - **DevOps**: kubernetes, actions/runner (GitHub Actions)

---

## B-1. 금융 IT 관련 레포지토리

### 1) QuantConnect/Lean — 알고리즘 트레이딩 엔진 (10K+ Stars)

**링크**: https://github.com/QuantConnect/Lean

**한 줄 소개**: C#/Python 기반 오픈소스 알고리즘 트레이딩 엔진.
**왜 봐야 하는가**: 금융권 **퀀트/백엔드 직무 면접**에서 "자신만의 트레이딩 전략을 구현해본 경험"을 증명하기에 최고입니다.
**난이도**: ⭐⭐⭐⭐

### 🚀 15분 퀵스타트

```bash
# 1. 저장소 클론
git clone https://github.com/QuantConnect/Lean.git
cd Lean

# 2. Docker로 간편 실행 (권장)
docker pull quantconnect/lean:latest
docker run -it quantconnect/lean:latest

# 3. .NET 환경에서 직접 실행
dotnet --version  # .NET 5.0 이상 필요
```

### 💻 기본 예제: 60/40 포트폴리오

```python
from AlgorithmImports import *

class BasicTradingAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2023, 1, 1)
        self.SetEndDate(2024, 1, 1)
        self.SetCash(100000)

        # 거래할 자산
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.bond = self.AddEquity("AGG", Resolution.Daily).Symbol

    def OnData(self, data):
        # 60/40 포트폴리오 (주식 60%, 채권 40%)
        if not self.Portfolio.Invested:
            self.SetHoldings(self.spy, 0.6)
            self.SetHoldings(self.bond, 0.4)
```

### 💻 실전 전략: Moving Average Crossover

```python
from AlgorithmImports import *

class MovingAverageCrossover(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2024, 1, 1)
        self.SetCash(100000)

        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        # 단기 50일 / 장기 200일 이동평균
        self.fast_ma = self.SMA(self.spy, 50, Resolution.Daily)
        self.slow_ma = self.SMA(self.spy, 200, Resolution.Daily)

    def OnData(self, data):
        if not self.fast_ma.IsReady or not self.slow_ma.IsReady:
            return

        fast = self.fast_ma.Current.Value
        slow = self.slow_ma.Current.Value

        # 골든 크로스 → 매수
        if fast > slow and not self.Portfolio[self.spy].Invested:
            self.SetHoldings(self.spy, 1.0)
            self.Debug(f"Golden Cross! Buy at {data[self.spy].Close}")

        # 데드 크로스 → 매도
        elif fast < slow and self.Portfolio[self.spy].Invested:
            self.Liquidate(self.spy)
            self.Debug(f"Death Cross! Sell at {data[self.spy].Close}")
```

!!! tip "💡 꿀팁: 포트폴리오 어필 포인트"
    1. **백테스팅 결과 지표**: Sharpe Ratio, Max Drawdown, Annual Return
    2. **리스크 관리**: Position Sizing, Stop Loss
    3. **성능 최적화**: 벡터화 연산, 메모리 효율

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "QuantConnect Lean으로 RSI 기반 단타 전략을 만들고 싶어. Python 코드와 함께, Sharpe Ratio 0.8 이상 나오는지 백테스팅 지표도 계산해줘."

!!! example "🤖 Claude Code 프롬프트: 면접 대비"
    > "'본인의 트레이딩 전략을 설명해주세요'라는 면접 질문에 답할 수 있도록, 내 Lean 백테스팅 결과를 3분 발표 스크립트로 정리해줘."

### 📚 학습 체크리스트

- [ ] Docker로 Lean 실행 성공
- [ ] 60/40 포트폴리오 백테스팅 완료
- [ ] Moving Average Crossover 구현
- [ ] Sharpe Ratio 계산 코드 작성
- [ ] GitHub에 전략 저장소 공개

**관련 레포**
- `QuantConnect/Documentation` — 공식 문서
- `ranaroussi/yfinance` — Yahoo Finance 데이터 수집

---

### 2) OpenBB-finance/OpenBB — 투자 분석 플랫폼 (35K+ Stars)

**링크**: https://github.com/OpenBB-finance/OpenBB

**한 줄 소개**: Bloomberg 터미널을 대체하는 오픈소스 투자 분석 플랫폼.
**왜 봐야 하는가**: 주식/암호화폐/옵션 등 **다양한 자산 분석 API**를 학습하며 **데이터 파이프라인 구축 경험**을 쌓을 수 있습니다.
**난이도**: ⭐⭐⭐

### 🚀 15분 퀵스타트

```bash
# pip 설치
pip install openbb

# 설치 확인
python -c "import openbb; print(openbb.__version__)"
```

예상 출력:

```
4.x.x
```

### 💻 기본 사용: 주식 데이터

```python
import openbb

# 1. 가격 데이터
apple_data = openbb.stocks.get_historical_data("AAPL", start_date="2023-01-01")
print(apple_data.head())

# 2. 회사 정보
info = openbb.stocks.get_company_info("AAPL")
print(f"Apple Market Cap: {info['marketCap']}")

# 3. 재무제표
income = openbb.stocks.get_income_statement("AAPL", period="annual")
print(income)

# 4. 기술적 지표
rsi = openbb.stocks.indicators.relative_strength_index("AAPL", period=14)
print(f"AAPL RSI(14): {rsi}")
```

### 💻 실전: 다중 종목 Sharpe Ratio 비교

```python
import openbb
import pandas as pd

stocks = ["AAPL", "GOOGL", "MSFT"]
comparison = {}

for stock in stocks:
    data = openbb.stocks.get_historical_data(stock, start_date="2023-01-01")
    returns = data['Adj Close'].pct_change().dropna()

    comparison[stock] = {
        "평균 수익률(연)": returns.mean() * 252,
        "변동성(연)": returns.std() * (252 ** 0.5),
        "Sharpe Ratio": (returns.mean() / returns.std()) * (252 ** 0.5),
        "최대 낙폭": (data['Adj Close'] / data['Adj Close'].cummax() - 1).min()
    }

df = pd.DataFrame(comparison).T
print(df)
```

!!! tip "💡 꿀팁: 금융권 면접에서 써먹기"
    "데이터 기반 투자 의사결정 시스템"을 포트폴리오 프로젝트로 만들고,
    **OpenBB + Streamlit** 조합으로 대시보드를 만들어 배포하세요.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "OpenBB로 코스피 Top 10 종목의 PER/PBR을 매일 수집해 CSV로 저장하는 스크립트를 만들어줘. GitHub Actions로 매일 자동 실행되도록 workflow도 같이."

!!! example "🤖 Claude Code 프롬프트"
    > "OpenBB로 수집한 내 데이터를 Streamlit 대시보드로 보여주고 싶어. KPI 카드 + 가격 차트 + 포트폴리오 비중 원형 차트를 포함해서."

### 📚 학습 체크리스트

- [ ] OpenBB 설치 및 기본 API 3개 사용
- [ ] Sharpe Ratio 계산 스크립트 작성
- [ ] Streamlit 대시보드 배포
- [ ] GitHub Actions로 일별 자동 수집 구현

---

## B-2. 공기업 코딩테스트 준비

### 1) TheAlgorithms/Python — 알고리즘 구현 (195K+ Stars)

**링크**: https://github.com/TheAlgorithms/Python

**한 줄 소개**: Python으로 구현된 거의 모든 알고리즘 모음.
**왜 봐야 하는가**: **NCS(국가직무능력표준) 및 공기업 코딩테스트** 대비에 최적입니다. 시간복잡도 설명이 상세해요.
**난이도**: ⭐⭐

### 🚀 15분 퀵스타트

```bash
git clone https://github.com/TheAlgorithms/Python.git
cd Python

# 주요 폴더 구조
# sorts/               - 정렬
# searches/            - 탐색
# dynamic_programming/ - DP
# graphs/              - 그래프
# data_structures/     - 자료구조
```

### 📅 공기업 8주 학습 로드맵

| 주차 | 주제 | 학습 파일 |
|------|------|----------|
| 1 | 정렬 & 탐색 | `sorts/merge_sort.py`, `searches/binary_search.py` |
| 2 | 자료구조 | `data_structures/stacks/`, `linked_lists/` |
| 3 | 동적계획법 | `dynamic_programming/fibonacci.py`, `knapsack.py` |
| 4 | 그래프 | `graphs/breadth_first_search.py`, `dijkstra.py` |
| 5-6 | 프로그래머스 Lv2~3 | 공기업 기출 |
| 7 | 백준 실버~골드 | NCS 난이도 |
| 8 | 모의 테스트 | 시간 재며 실전 |

### 💻 이진 탐색 템플릿

```python
def binary_search(arr, target):
    """
    정렬된 배열에서 target을 찾는 이진 탐색
    시간복잡도: O(log n)
    """
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

# 테스트
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
assert binary_search(sorted_array, 7) == 3
assert binary_search(sorted_array, 6) == -1
print("이진 탐색 통과")
```

### 💻 NCS 유형: 최소공배수

```python
from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_multiple(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

# NCS 기출: 3, 5, 7의 최소공배수
print(lcm_multiple([3, 5, 7]))  # 105
```

### 💻 DP: 피보나치 (메모이제이션 vs 테이블)

```python
def fibonacci_dp(n):
    """Bottom-up DP로 피보나치"""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(fibonacci_dp(30))  # 832040
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "TheAlgorithms/Python의 graphs/ 폴더에서 공기업 코테 빈출 알고리즘 Top 5를 골라 각 파일의 핵심 로직을 3줄로 요약해줘."

!!! example "🤖 Claude Code 프롬프트"
    > "NCS 코딩테스트 기출 유형 10개(문자열, 수학, 구현)를 Python으로 풀이해주고, 각 풀이에 왜 이 접근법을 썼는지 주석으로 설명해줘."

### 📚 학습 체크리스트

- [ ] 정렬 알고리즘 5개 직접 구현
- [ ] BFS/DFS 템플릿 암기
- [ ] DP 빈출 문제 10개 풀이
- [ ] 프로그래머스 Lv2 20문제
- [ ] 백준 실버 30문제

---

### 2) neetcode-io/leetcode — LeetCode 풀이 가이드 (6K+ Stars)

**링크**: https://github.com/neetcode-io/leetcode

**한 줄 소개**: LeetCode 상위 150문제의 최적 풀이 모음.
**왜 봐야 하는가**: NeetCode YouTube와 연동된 **카테고리 우선순위**가 명확해서 코테 준비 효율이 극대화됩니다.
**난이도**: ⭐⭐⭐

### 🏆 공기업 코테 우선순위

**높음 (반드시)**: Array & Hashing, Two Pointers, Sliding Window, Binary Search
**중간 (자주)**: Stack & Queue, Linked List, Tree & Graph, DP
**낮음 (심화)**: Greedy, Math & Geometry, Trie

### 💻 Sliding Window: Longest Substring Without Repeating

```python
def lengthOfLongestSubstring(s):
    """
    반복되지 않는 가장 긴 부분 문자열의 길이
    시간복잡도: O(n)
    """
    char_index = {}
    max_length = 0
    start = 0

    for end, char in enumerate(s):
        # 이미 윈도우 내에 있는 문자면 시작점 이동
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        char_index[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# 테스트
assert lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
assert lengthOfLongestSubstring("bbbbb") == 1     # "b"
assert lengthOfLongestSubstring("pwwkew") == 3    # "wke"
print("Sliding Window 통과")
```

### 💻 Binary Search: Rotated Sorted Array

```python
def search(nums, target):
    """회전된 정렬 배열에서 target 찾기 O(log n)"""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            # 왼쪽 절반이 정렬됨
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # 오른쪽 절반이 정렬됨
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
print("Rotated Binary Search 통과")
```

### 📅 일일 1문제 50일 플랜

| Day | 주제 | 문제 수 |
|-----|------|--------|
| 1-5 | Array & Hashing | 5 |
| 6-10 | Two Pointers | 5 |
| 11-15 | Sliding Window | 5 |
| 16-20 | Stack | 5 |
| 21-25 | Binary Search | 5 |
| 26-35 | DP (공기업 필출) | 10 |
| 36-45 | Tree & Graph | 10 |
| 46-50 | 기출 실전 | 5 |

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "내가 Sliding Window 유형을 공략하려고 해. neetcode 150 중 이 유형 문제 5개를 난이도 순으로 골라서 각각 핵심 아이디어와 반복 학습 포인트를 알려줘."

### 📚 학습 체크리스트

- [ ] NeetCode 150 중 Easy 완주
- [ ] Sliding Window 5문제 풀이
- [ ] Binary Search 템플릿 암기
- [ ] DP 10문제 풀이

---

## B-3. 보안 & 인프라 (금융권 필수)

### 1) OWASP/CheatSheetSeries — 보안 체크시트 (28K+ Stars)

**링크**: https://github.com/OWASP/CheatSheetSeries

**한 줄 소개**: 전 세계 웹 보안 전문가들이 만든 공식 보안 체크시트 모음.
**왜 봐야 하는가**: 금융권은 **보안 규정 준수(Compliance)**가 채용의 핵심입니다. OWASP Top 10은 필수 암기.
**난이도**: ⭐⭐⭐⭐

### 🔐 금융권 필수 보안 항목

1. **Authentication**: Password Storage, Session Management, MFA
2. **Cryptography**: Cryptographic Storage, HTTPS, Key Management
3. **API Security**: REST, GraphQL, OAuth 2.0
4. **Data Protection**: PCI DSS, GDPR, 개인정보 암호화

### 💻 실전: 안전한 비밀번호 저장 (bcrypt)

```python
import bcrypt

def hash_password(password: str) -> str:
    """
    OWASP 권장: bcrypt with salt (최소 12라운드)
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))
    return hashed.decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# 사용 예제
original = "MySecurePassword123!"
hashed = hash_password(original)
print(f"해시: {hashed}")
print(f"검증 성공: {verify_password(original, hashed)}")
print(f"검증 실패: {verify_password('WrongPassword', hashed)}")
```

!!! warning "⚠️ 절대 금지 사항"
    - **평문 저장**: 절대 금지
    - **MD5/SHA-1**: 암호 저장용으로는 절대 금지
    - **자체 알고리즘**: 검증되지 않은 암호는 쓰지 마세요

### 💻 실전: SQL Injection 방지

```python
import sqlite3

# 잘못된 방법 (SQL Injection 취약!)
def unsafe_query(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    # 악의적 입력: admin' OR '1'='1 → 모든 사용자 노출

# 올바른 방법 (OWASP 권장)
def safe_query(username):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    # 파라미터화된 쿼리 (?)
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchall()
```

### 💻 Flask HTTPS + 보안 헤더

```python
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app,
    force_https=True,
    strict_transport_security=True,
    content_security_policy={
        'default-src': "'self'",
        'script-src': "'self'",
    }
)

@app.route('/')
def hello():
    return 'Secure Connection'
```

### 🎤 금융권 면접 Q&A

!!! info "📌 Q1: SQL Injection이란?"
    **A**: 사용자 입력에 악의적 SQL 코드를 삽입하는 공격. **파라미터화된 쿼리(Prepared Statements)** 사용으로 방어합니다.

!!! info "📌 Q2: XSS 방어 방법?"
    **A**: 입력 검증 + 출력 인코딩 + CSP(Content Security Policy) 3단계로 방어합니다.

!!! info "📌 Q3: OWASP Top 10이란?"
    **A**: 웹 애플리케이션의 가장 위험한 10가지 보안 취약점 목록 (2021년 기준 A01~A10).

!!! info "📌 Q4: 금융권 필수 보안 표준?"
    **A**: **PCI DSS** (결제카드 산업 보안 표준) — 민감 데이터 암호화, 강력한 액세스 제어, 정기 감사 필수.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "내 Spring Boot 앱의 로그인 로직을 OWASP Authentication Cheat Sheet 기준으로 검토해줘. 취약점이 있으면 Java 코드로 개선안 제시."

!!! example "🤖 Claude Code 프롬프트"
    > "OWASP Top 10 2021 버전 10개 항목을 금융권 면접용으로 각각 30초 답변 스크립트로 만들어줘."

### 📚 학습 체크리스트

- [ ] OWASP Top 10 모두 설명 가능
- [ ] bcrypt로 비밀번호 해싱 구현
- [ ] Prepared Statements로 SQL Injection 방어
- [ ] Flask/Spring Boot에 CSP 적용
- [ ] PCI DSS 핵심 요구사항 3개 암기

---

### 2) trimstray/the-book-of-secret-knowledge (160K+ Stars)

**링크**: https://github.com/trimstray/the-book-of-secret-knowledge

**한 줄 소개**: Linux/네트워크/보안/DevOps 실무 지식 모음집.
**왜 봐야 하는가**: **금융권 인프라 엔지니어**가 실무에서 쓰는 명령어·설정·베스트 프랙티스가 전부 있어요.
**난이도**: ⭐⭐⭐⭐

### 🛠️ 금융권 인프라 핵심 명령어

```bash
# 1. 열린 포트 확인 (보안 감사)
nmap -sV localhost

# 2. 현재 네트워크 연결 확인
ss -tlnp  # t=TCP, l=Listening, n=Numeric, p=Process

# 3. 파일 무결성 확인
md5sum /path/to/critical/file

# 4. 방화벽 설정 확인
sudo firewall-cmd --list-all

# 5. 시스템 보안 감사
sudo apt install lynis
sudo lynis audit system
```

### 🛠️ 성능 모니터링

```bash
# CPU 사용률 Top 10
ps aux --sort=-%cpu | head -10

# 메모리 사용률 Top 10
ps aux --sort=-%mem | head -10

# 디스크 사용량
df -h
du -sh /var/log/*

# 실시간 네트워크 모니터링
iftop -n
```

### 🛠️ SSH 보안 설정 (금융권 필수)

```bash
# /etc/ssh/sshd_config 보안화

# 1. 루트 로그인 비활성화
sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

# 2. 비밀번호 인증 비활성화 (키 기반만)
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

# 3. 포트 변경 (기본 22 → 2222)
sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

# 4. 설정 검증 후 재시작
sshd -t
sudo systemctl restart sshd

# 5. SSH 키 쌍 생성
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519

# 6. 서버에 공개 키 배포
ssh-copy-id -i ~/.ssh/id_ed25519.pub -p 2222 user@server.com
```

### 🛠️ 로그 모니터링 (감사 증적)

```bash
# SSH 최근 로그
journalctl --unit=sshd -n 20

# 특정 기간 로그
journalctl -u sshd --since "2026-04-01" --until "2026-04-07"

# 실시간 로그 스트리밍
journalctl -f

# 실패한 로그인 시도 탐지
grep "Failed password" /var/log/auth.log | tail -50
```

### 🎤 금융권 인프라 면접 Q&A

!!! info "📌 Q1: chmod 755의 의미?"
    **A**: `rwx r-x r-x` = 소유자(읽기+쓰기+실행), 그룹(읽기+실행), 기타(읽기+실행). **금융권에서 민감 파일은 `600`** (소유자만 접근).

!!! info "📌 Q2: 방화벽이 필요한 이유?"
    **A**: 불필요한 포트 차단으로 **공격 표면(Attack Surface) 최소화**. 금융권은 **화이트리스트** 방식(필요한 포트만 개방) 필수.

!!! info "📌 Q3: SSH 키 기반 인증의 장점?"
    **A**: 비밀번호 탈취 불가, Brute-force 공격 방어. 금융권에선 **필수 요구사항**.

!!! info "📌 Q4: 로그 모니터링이 중요한 이유?"
    **A**: 침입 탐지, 감사 증적, 규제 준수. 금융권은 **감사자 로그(audit log) 유지 의무**가 법으로 정해져 있음.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "내 CentOS 서버를 금융권 보안 기준으로 하드닝(hardening)해줘. SSH, 방화벽, 로그 수집 3개 영역으로 나눠서 체크리스트와 명령어 모두 제공해줘."

### 📚 학습 체크리스트

- [ ] Linux 권한 관리 (chmod/chown) 숙달
- [ ] SSH 키 기반 인증 실습
- [ ] journalctl로 로그 조회 가능
- [ ] 방화벽 화이트리스트 설정 가능
- [ ] lynis로 시스템 감사 실행

---

## B-4. DevOps & CI/CD

### 1) kubernetes/kubernetes (113K+ Stars)

**링크**: https://github.com/kubernetes/kubernetes

**한 줄 소개**: 구글이 개발한 컨테이너 오케스트레이션의 사실상 표준.
**왜 봐야 하는가**: 금융권 대규모 MSA는 **K8s 기반이 기본**. Deployment, Service, RBAC 이해는 필수입니다.
**난이도**: ⭐⭐⭐⭐⭐

### 🚀 15분 퀵스타트

```bash
# 1. kubectl 설치
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl && sudo mv kubectl /usr/local/bin/

# 2. Minikube 설치 (로컬 테스트용)
minikube start
kubectl cluster-info
kubectl get nodes
```

### 💻 기본: Pod 생성

```yaml
# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
```

```bash
kubectl apply -f pod.yaml
kubectl get pods
kubectl describe pod nginx-pod
kubectl logs nginx-pod
```

### 💻 실전: Deployment 핵심 요소

`deployment.yaml`의 필수 요소:

- `apiVersion: apps/v1`, `kind: Deployment`
- `spec.replicas: 3` (Pod 복제본 수)
- `spec.selector.matchLabels`와 `spec.template.metadata.labels` 일치 필수
- `containers[].image`, `containers[].ports.containerPort`
- `resources.requests/limits` (memory/cpu 제한)
- `livenessProbe.httpGet` (헬스체크)

**주요 명령어**

```bash
# 배포
kubectl apply -f deployment.yaml

# 상태 확인
kubectl get deployments
kubectl get pods

# 이미지 업데이트
kubectl set image deployment/web-app web=nginx:1.21

# 롤백
kubectl rollout undo deployment/web-app
```

### 💻 Service / ConfigMap / Secret

- **Service** (`type: LoadBalancer`): `selector.app`으로 Pod 선택, `port` → `targetPort` 매핑
- **ConfigMap**: 환경 변수 주입 (예: `DATABASE_HOST`, `LOG_LEVEL`)
- **Secret** (`type: Opaque`): 민감 정보는 base64 인코딩 — **금융권은 Vault/KMS 연동 필수**

### 🔒 금융권 Kubernetes 필수 설정

- **Namespace**: 팀/환경별 격리

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: finance
```

- **NetworkPolicy**: 기본 deny-all 후 화이트리스트

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
```

- **RBAC**: `Role`(권한) + `RoleBinding`(연결). 예: `verbs: [get, list, watch]`만 허용

!!! warning "⚠️ 금융권 K8s 실수 1순위"
    **Secret을 base64만 믿고 관리하는 것**.
    base64는 인코딩이지 암호화가 아닙니다. 반드시 **HashiCorp Vault** 또는 **AWS KMS/Secrets Manager**와 연동하세요.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "내 Spring Boot 앱(8080 포트)을 K8s에 배포하는 deployment.yaml + service.yaml + configmap.yaml을 만들고, 금융권 기준 NetworkPolicy와 RBAC도 같이 정의해줘."

!!! example "🤖 Claude Code 프롬프트"
    > "K8s 면접 빈출 질문 20개에 대한 답변을 만들어줘. Deployment vs StatefulSet, Service Type 4가지, RBAC 등 핵심 개념 위주로."

### 📚 학습 체크리스트

- [ ] Minikube로 Pod/Deployment 실습
- [ ] Service LoadBalancer 타입 이해
- [ ] ConfigMap/Secret 차이 설명 가능
- [ ] NetworkPolicy deny-all 설정 가능
- [ ] Role/RoleBinding 예제 작성

**관련 레포**
- `kelseyhightower/kubernetes-the-hard-way` — K8s 심화 학습

---

### 2) actions/runner — GitHub Actions (5K+ Stars)

**링크**: https://github.com/actions/runner

**한 줄 소개**: GitHub Actions의 공식 실행 환경.
**왜 봐야 하는가**: **금융권 CI/CD 자동화**의 표준 도구 중 하나. 테스트, 보안 스캔, 배포를 파이프라인으로 묶을 수 있어요.
**난이도**: ⭐⭐⭐

### 🚀 15분 퀵스타트: 첫 CI 파이프라인

`.github/workflows/ci.yml`

```yaml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: pytest tests/ -v --cov=src

    - name: Security scan
      run: bandit -r src/ -f json -o bandit-report.json

    - name: Upload coverage
      uses: codecov/codecov-action@v4
```

### 🔒 금융권 CI/CD 필수 추가 단계

Python 앱의 전형적 파이프라인은 3개 job으로 구성:

- **test job**: checkout → setup-python (matrix 3.8~3.11) → `flake8`, `mypy`, `pytest --cov` → codecov 업로드
- **security job**: `bandit`, `semgrep --config=p/security-audit`, `safety check`
- **deploy job**: `needs: [test, security]` + `if: github.ref == 'refs/heads/main'` 조건

금융권은 위 기본 파이프라인에 아래 단계를 추가로 요구합니다.

- [ ] **코드 품질 게이트**: `pylint --fail-under=9.0`, `black --check`, `isort --check-only`
- [ ] **의존성 취약점 스캔**: `pip-audit`, `safety check`
- [ ] **암호화/컴플라이언스**: 자체 스크립트 (`verify-encryption.sh`, `check-compliance.sh`)
- [ ] **부하 테스트**: `locust --headless -u 100 -r 10 --run-time 60s`
- [ ] **SBOM 생성**: `cyclonedx-bom -o sbom.xml`
- [ ] **2인 승인 gate**: `actions/github-script`로 `pulls.listReviews` 검증

### 💻 자동 릴리스 워크플로우

```yaml
# .github/workflows/release.yml
name: Automated Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    - name: Create Release Notes
      run: |
        git log $(git describe --tags --abbrev=0)..HEAD --oneline > RELEASE_NOTES.md

    - name: Create GitHub Release
      uses: softprops/action-gh-release@v1
      with:
        tag_name: ${{ github.ref_name }}
        body_path: RELEASE_NOTES.md
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "금융권 CI/CD 요구사항(코드 품질 / 보안 스캔 / SBOM / 2인 승인)을 모두 충족하는 GitHub Actions workflow를 내 Python Flask 프로젝트에 맞게 만들어줘."

!!! example "🤖 Claude Code 프롬프트"
    > "내 Spring Boot 프로젝트를 Docker로 빌드해 AWS ECR에 푸시하고, EKS에 배포하는 GitHub Actions workflow를 작성해줘. 보안 스캔(Trivy)과 롤백 단계도 포함."

### 📅 GitHub Actions 4주 마스터 플랜

| 주차 | 목표 | 산출물 |
|------|------|--------|
| 1주 | 기본 워크플로우 | checkout, setup, test |
| 2주 | 품질 + 보안 | lint, pylint, bandit |
| 3주 | 배포 자동화 | Docker build/push, K8s deploy |
| 4주 | 고급 기능 | matrix, conditional, secrets |

### 📚 학습 체크리스트

- [ ] 첫 CI 워크플로우 실행 성공
- [ ] Matrix build로 다중 Python 버전 테스트
- [ ] Secrets로 환경변수 관리
- [ ] 자동 릴리스 워크플로우 구성
- [ ] SBOM + 보안 스캔 추가

!!! danger "🚨 자주 발생하는 에러"
    **에러**: `Error: Resource not accessible by integration`
    **원인**: `GITHUB_TOKEN`의 권한 부족
    **해결**: workflow 파일 상단에 권한 명시

    ```yaml
    permissions:
      contents: write
      pull-requests: write
    ```

---

!!! tip "💡 축하합니다!"
    Part 6을 완주하셨다면 **금융권/공기업 기술 면접의 기본기**는 갖추신 거예요.
    이제 Part 4(문서 처리 라이브러리)와 Part 5(AI 개발 도구) 내용을 활용해
    **"나만의 포트폴리오 + 자동화된 CI/CD"**를 완성해보세요.

    당신의 취업을 응원합니다! 🎉
