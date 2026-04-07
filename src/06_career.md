# Part 6: 취업 준비 및 면접 전략

> 금융권/공기업을 포함한 IT 취업을 위한 실전 준비 가이드입니다.

## 학습 목표
- 기술 면접 핵심 주제 정리
- 코딩 테스트 준비 전략
- 포트폴리오/이력서 최적화
- 금융/공기업 맞춤 취업 전략

---

## 6-1. 기술 면접 준비

### yangshun/tech-interview-handbook (122K+ Stars)
**링크**: https://github.com/yangshun/tech-interview-handbook

개발자 면접을 위한 종합 가이드. 구성, 질문, 답변 전략까지 담고 있습니다.

#### 📋 면접 유형별 전략

**1. 코딩 면접 (Coding Interview)**

**인터뷰 전**: 회사 기술 스택 조사, 최근 프로젝트 복습, 인터뷰어 LinkedIn 확인, 자주 묻는 문제 3-5개 준비
**인터뷰 중**: 질문 명확히 이해, 접근 방법 설명, 엣지 케이스 고려, 시간복잡도 분석, 트레이드오프 논의
**코딩 후**: 코드 리뷰, 테스트 케이스 작성, 성능 개선 제시, 결과 검증

**2. 시스템 디자인 면접 프레임워크 (40분)**

1. **요구사항 명확히 (5분)**: 함수형/비함수형, Scale, QPS, Data volume
2. **API 설계 (5분)**: Endpoints, Request/Response, Rate limiting
3. **데이터 모델 (5분)**: 스키마, 인덱싱, Sharding 전략
4. **High-level 설계 (10분)**: Components, Data flow, Cache, MQ
5. **상세 설계 (10분)**: 핵심 컴포넌트 심화, 병목 분석, 최적화
6. **마무리 (5분)**: Monitoring, Logging, Future improvements

**실제 예: URL Shortener**

- **요구사항**: 쓰기 500/s, 읽기 100,000/s, 가용성 99.9%, Latency < 200ms
- **용량 산정**: 5년 기준 약 78.8B URLs × 100B ≈ 7.88 TB
- **API**: `POST /api/shorten` (long_url → short_url), `GET /api/{code}` → 301 리다이렉트
- **데이터 모델**: `URLMapping(id PK, short_code UNIQUE, long_url, created_at, expiration)`
- **아키텍처**: Client → LB → API Servers → Redis Cache → MySQL, 분석은 Kafka로 비동기
- **핵심 기법**: Base62 인코딩, Collision은 retry+increment, LRU 캐시, Consistent Hashing

---

### donnemartin/system-design-primer (290K+ Stars)
**링크**: https://github.com/donnemartin/system-design-primer

확장 가능한 시스템 설계를 위한 종합 리소스입니다.

#### 🏗️ 핵심 개념

**1. Scalability (확장성)**

- **Vertical Scaling**: CPU/메모리 업그레이드. 간단하지만 단일 기계 한계 있음.
- **Horizontal Scaling**: 서버를 여러 대 추가하고 Load Balancer로 분산. 대부분 이쪽이 더 효율적.
- 전형적 구조: Client → LB → App1/2/3 → Redis Cache → DB (Master-Slave 복제)

**2. 데이터베이스 설계**
```
SQL vs NoSQL 선택

SQL (관계형 데이터베이스)
장점:
- ACID 보장
- 복잡한 쿼리 가능
- 데이터 무결성
단점:
- 수평 확장 어려움
- 고정된 스키마

예: MySQL, PostgreSQL

NoSQL (비관계형 데이터베이스)
장점:
- 수평 확장 용이
- 빠른 읽기/쓰기
- 유연한 스키마
단점:
- ACID 보장 안 함
- 쿼리 능력 제한
- Consistency 문제

예: MongoDB, Cassandra, DynamoDB
```

**3. 캐싱 전략**

- LRU, LFU, Write-Through, Write-Back, Cache-Aside 다섯 가지 전략이 빈출 주제입니다.
- 면접 팁: 전략을 고를 때 "읽기/쓰기 비율", "정합성 요구", "히트율" 세 기준으로 설명하세요.
- Python `functools.lru_cache`, `collections.OrderedDict`로 직접 구현해본 경험을 면접에서 얘기할 수 있으면 강점.

---

### kdn251/interviews (63K+ Stars)
**링크**: https://github.com/kdn251/interviews

Java 기반 면접 준비용 알고리즘 및 자료구조 구현.

#### 🎯 Java 기반 면접 준비

- 이 레포는 LeetCode 빈출 문제의 Java 풀이를 Array/String/Tree/DP 등 카테고리별로 정리합니다.
- 추천 학습법: 문제를 직접 풀어본 뒤 레포 풀이와 비교, 시간/공간 복잡도를 꼭 따져보세요.
- 대기업 면접 빈출: Two Sum, Valid Palindrome, Reverse Integer, Merge Intervals, LRU Cache.

> Claude Code 활용 팁
> `> "kdn251/interviews 레포의 Dynamic Programming 섹션에서 금융권 면접 빈출 Top 5를 골라서 시간복잡도와 핵심 아이디어를 비교해줘"`

---

---

## 6-2. 금융/공기업 취업에 도움되는 레포지토리

### B-1. 금융 IT 관련 레포지토리

#### 1) QuantConnect/Lean - 알고리즘 트레이딩 엔진 (10K+ Stars)

**레포 개요**
- QuantConnect가 개발한 오픈소스 알고리즘 트레이딩 엔진
- C#과 Python을 지원하는 백테스팅 및 실시간 거래 플랫폼
- 금융권 퀀트/개발자 직무 면접에서 자주 언급되는 프로젝트

**설치 방법**

```bash
# Python을 이용한 기본 설치
git clone https://github.com/QuantConnect/Lean.git
cd Lean

# C# 환경 필요 (Linux/Mac)
dotnet --version  # .NET 5.0 이상

# Docker를 이용한 설치 (권장)
docker pull quantconnect/lean:latest
docker run -it quantconnect/lean:latest
```

**기본 사용법 - Python API**

```python
from AlgorithmImports import *

class BasicTradingAlgorithm(QCAlgorithm):
    def Initialize(self):
        # 1년의 데이터로 시뮬레이션
        self.SetStartDate(2023, 1, 1)
        self.SetEndDate(2024, 1, 1)

        # 초기 자본금
        self.SetCash(100000)

        # 거래할 주식 추가
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.bond = self.AddEquity("AGG", Resolution.Daily).Symbol

    def OnData(self, data):
        # 보유 자산이 없으면 60/40 포트폴리오 구성
        if not self.Portfolio.Invested:
            self.SetHoldings(self.spy, 0.6)
            self.SetHoldings(self.bond, 0.4)

        # 간단한 매매 신호 (SMA 활용)
        if not self.spy in data:
            return

        # 거래 로직 추가 가능
        price = data[self.spy].Close
        self.Debug(f"SPY Price: {price}")
```

**실전 활용 시나리오: 이동평균 교차 전략 (Moving Average Crossover)**

```python
from AlgorithmImports import *

class MovingAverageCrossover(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2024, 1, 1)
        self.SetCash(100000)

        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol

        # 단기 이동평균(50일)과 장기 이동평균(200일)
        self.fast_ma = self.SMA(self.spy, 50, Resolution.Daily)
        self.slow_ma = self.SMA(self.spy, 200, Resolution.Daily)

    def OnData(self, data):
        if not self.fast_ma.IsReady or not self.slow_ma.IsReady:
            return

        fast = self.fast_ma.Current.Value
        slow = self.slow_ma.Current.Value

        # Golden Cross: 단기 MA가 장기 MA를 위로 뚫고 올라감
        if fast > slow and not self.Portfolio[self.spy].Invested:
            self.SetHoldings(self.spy, 1.0)
            self.Debug(f"Golden Cross! Buy at {data[self.spy].Close}")

        # Death Cross: 단기 MA가 장기 MA를 아래로 뚫고 내려감
        elif fast < slow and self.Portfolio[self.spy].Invested:
            self.Liquidate(self.spy)
            self.Debug(f"Death Cross! Sell at {data[self.spy].Close}")
```

**금융권 면접 활용 팁**
- Lean을 이용한 백테스팅 경험을 포트폴리오에 추가하면 강점
- 면접에서 "자신의 트레이딩 전략을 구현해본 경험"을 증명 가능
- 코드 최적화, 위험 관리(Risk Management) 등 금융 개념을 함께 설명

**관련 레포 추천**
- `QuantConnect/Documentation` - 공식 문서
- `ranaroussi/yfinance` - Yahoo Finance 데이터 수집
- `quantopian/*` - 구 Quantopian 자산들

---

#### 2) OpenBB-finance/OpenBB - 투자 분석 플랫폼 (35K+ Stars)

**레포 개요**
- Bloomberg 터미널을 대체하는 오픈소스 투자 분석 플랫폼
- 주식, 암호화폐, 옵션 등 다양한 자산 분석 도구 제공
- 데이터 분석 + API 설계를 배우기에 최적

**설치 방법**

```bash
# pip를 이용한 설치
pip install openbb

# 또는 소스코드에서 설치
git clone https://github.com/OpenBB-finance/OpenBB.git
cd OpenBB
pip install -e .

# 설치 확인
python -c "import openbb; print(openbb.__version__)"
```

**기본 사용법 - 주식 데이터 조회**

```python
import openbb

# 개별 주식 가격 데이터
apple_data = openbb.stocks.get_historical_data("AAPL", start_date="2023-01-01")
print(apple_data.head())

# 주식 정보 조회
info = openbb.stocks.get_company_info("AAPL")
print(f"Apple Market Cap: {info['marketCap']}")

# 재무제표 조회
income_stmt = openbb.stocks.get_income_statement("AAPL", period="annual")
print(income_stmt)

# 기술적 분석 지표
rsi = openbb.stocks.indicators.relative_strength_index("AAPL", period=14)
print(f"AAPL RSI(14): {rsi}")
```

**실전 활용 시나리오: 다중 종목 비교 분석**

```python
import openbb
import pandas as pd

# 기술주 3개 종목 비교
stocks = ["AAPL", "GOOGL", "MSFT"]
comparison_data = {}

for stock in stocks:
    # 최근 1년 데이터
    data = openbb.stocks.get_historical_data(stock, start_date="2023-01-01")

    # 수익률 계산
    returns = data['Adj Close'].pct_change().dropna()

    # 통계 정보
    comparison_data[stock] = {
        "평균 수익률": returns.mean() * 252,  # 연간화
        "변동성": returns.std() * (252 ** 0.5),
        "Sharpe Ratio": (returns.mean() / returns.std()) * (252 ** 0.5),
        "최대 낙폭": (data['Adj Close'] / data['Adj Close'].cummax() - 1).min()
    }

# DataFrame으로 변환하여 비교
comparison_df = pd.DataFrame(comparison_data).T
print(comparison_df)

# 금융 지표 비교
print("\n=== 금융 지표 비교 ===")
for stock in stocks:
    pe_ratio = openbb.stocks.get_pe_ratio(stock)
    pb_ratio = openbb.stocks.get_pb_ratio(stock)
    print(f"{stock}: P/E = {pe_ratio:.2f}, P/B = {pb_ratio:.2f}")
```

**금융권 면접 활용 팁**
- OpenBB API 설계를 분석하면 좋은 학습 자료
- 금융 데이터 파이프라인 구축 경험을 어필 가능
- "데이터 기반 투자 의사결정 시스템" 포트폴리오 프로젝트 제작 권장

**관련 레포 추천**
- `OpenBB-finance/OpenBBTerminal` - CLI 버전
- `OpenBB-finance/docs` - 공식 문서

---

### B-2. 공기업 코딩테스트 준비

#### 1) TheAlgorithms/Python - 알고리즘 구현 (195K+ Stars)

**레포 개요**
- Python으로 구현된 모든 알고리즘 모음 (정렬, 탐색, 동적계획법 등)
- NCS(국가직무능력표준) 및 공기업 코딩테스트 대비에 최적
- 각 알고리즘의 시간복잡도와 설명이 상세함

**설치 방법**

```bash
git clone https://github.com/TheAlgorithms/Python.git
cd Python

# 폴더 구조 확인
ls -la
# output:
# sorts/          - 정렬 알고리즘
# searches/       - 탐색 알고리즘
# dynamic_programming/  - 동적계획법
# graphs/         - 그래프 알고리즘
# arrays/         - 배열 관련
# strings/        - 문자열 처리
```

**공기업 코딩테스트 추천 학습 순서**

```
Week 1: 정렬 & 탐색
├─ searches/linear_search.py (선형 탐색)
├─ searches/binary_search.py (이진 탐색)
└─ sorts/bubble_sort.py, merge_sort.py, quick_sort.py

Week 2: 자료구조
├─ arrays/ (배열 조작)
├─ linked_lists/ (연결 리스트)
└─ stacks_and_queues/ (스택/큐)

Week 3: 동적계획법
├─ dynamic_programming/fibonacci.py
├─ dynamic_programming/longest_increasing_subsequence.py
└─ dynamic_programming/knapsack.py

Week 4: 그래프
├─ graphs/breadth_first_search.py
├─ graphs/depth_first_search.py
└─ graphs/dijkstra.py (최단경로)

Week 5-8: 실전 문제
├─ 프로그래머스 Level 2-3 (공기업 기출)
├─ Baekjoon 실버~골드 (NCS 난이도)
└─ LeetCode Medium 풀이 검증
```

**기본 코드 예제: 이진 탐색**

```python
# TheAlgorithms/Python의 binary_search.py 분석

def binary_search(arr, target):
    """
    정렬된 배열에서 target을 찾는 이진 탐색
    시간복잡도: O(log n)
    공간복잡도: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # 오른쪽 절반 탐색
        else:
            right = mid - 1  # 왼쪽 절반 탐색

    return -1  # 찾지 못함

# 테스트
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(sorted_array, 7))  # 출력: 3
print(binary_search(sorted_array, 6))  # 출력: -1
```

**공기업 실전 문제: 최소공배수 (LCM) - NCS 유형**

```python
from math import gcd

def lcm(a, b):
    """최소공배수 계산"""
    return (a * b) // gcd(a, b)

def lcm_multiple(numbers):
    """여러 수의 최소공배수"""
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

# 예제: 공기업 코딩테스트 기출
# 문제: 3, 5, 7의 최소공배수를 구하시오
print(lcm_multiple([3, 5, 7]))  # 출력: 105
```

**동적계획법 예제: 피보나치 수열**

```python
def fibonacci_memo(n, memo={}):
    """메모이제이션을 이용한 피보나치"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

def fibonacci_dp(n):
    """DP 테이블을 이용한 피보나치 (더 빠름)"""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# 비교
print(f"메모이제이션: {fibonacci_memo(30)}")  # 832040
print(f"DP: {fibonacci_dp(30)}")  # 832040 (훨씬 빠름)
```

**관련 레포 추천**
- `neetcode-io/leetcode` - LeetCode 풀이 (다음 섹션)
- `Baekjoon-Online-Judge/` - 백준 풀이 참고

---

#### 2) neetcode-io/leetcode - LeetCode 풀이 및 코딩 테스트 가이드 (6K+ Stars)

**레포 개요**
- LeetCode 상위 150문제의 최적 풀이 모음
- 공기업 코딩테스트의 난이도와 유사한 문제들 포함
- 각 문제마다 풀이 설명 및 시간/공간복잡도 분석

**설치 및 사용**

```bash
git clone https://github.com/neetcode-io/leetcode.git
cd leetcode

# 구조 확인
ls -la
# 주요 폴더:
# 1-array-hashing/
# 2-two-pointers/
# 3-sliding-window/
# 4-stack/
# 5-binary-search/
# 6-linked-list/
# 7-trees/
# 8-tries/
# 9-heap-priority-queue/
# 10-graphs/
# 11-advanced-graphs/
# 12-1-d-dp/
# 13-2-d-dp/
# 14-greedy/
# 15-intervals/
# 16-math-geometry/
```

**공기업 코딩테스트 추천 우선순위**

```
높음 (반드시 풀어야 할 주제):
├─ Array & Hashing (배열, 해시맵)
├─ Two Pointers (투 포인터)
├─ Sliding Window (슬라이딩 윈도우)
└─ Binary Search (이진 탐색)

중간 (자주 출제):
├─ Stack & Queue (스택, 큐)
├─ Linked List (연결 리스트)
├─ Tree & Graph (트리, 그래프)
└─ Dynamic Programming (동적계획법)

낮음 (심화):
├─ Greedy (탐욕법)
├─ Math & Geometry (수학, 기하)
└─ Trie (트라이)
```

**Array & Hashing - Two Sum (LeetCode #1)**

```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
```

핵심 아이디어: "이전에 본 수"를 해시맵에 저장해 O(n)에 해결. 3Sum/4Sum으로 확장될 때는 정렬 후 투 포인터(O(n²))가 정석.

**Sliding Window - Longest Substring Without Repeating Characters**

```python
def lengthOfLongestSubstring(s):
    """
    반복되지 않는 가장 긴 부분 문자열의 길이
    슬라이딩 윈도우 활용 (O(n) 풀이)
    """
    char_index = {}
    max_length = 0
    start = 0

    for end, char in enumerate(s):
        # 문자가 현재 윈도우 내에 이미 존재하면
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        char_index[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# 테스트
print(lengthOfLongestSubstring("abcabcbb"))  # 출력: 3 ("abc")
print(lengthOfLongestSubstring("bbbbb"))      # 출력: 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))     # 출력: 3 ("wke")
```

**Binary Search - Search in Rotated Sorted Array**

```python
def search(nums, target):
    """
    회전된 정렬 배열에서 target 찾기
    예: [4,5,6,7,0,1,2] 에서 0 찾기
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # 왼쪽 절반이 정렬되어 있는 경우
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 오른쪽 절반이 정렬되어 있는 경우
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# 테스트
print(search([4, 5, 6, 7, 0, 1, 2], 0))  # 출력: 4
print(search([4, 5, 6, 7, 0, 1, 2], 3))  # 출력: -1
```

**학습 전략: 일일 1문제 풀이 계획**

```
Day 1-5: Array & Hashing (5문제)
Day 6-10: Two Pointers (5문제)
Day 11-15: Sliding Window (5문제)
Day 16-20: Stack & Queue (5문제)
Day 21-25: Binary Search (5문제)
Day 26-35: DP (10문제) - 공기업 필출 유형
Day 36-45: Tree & Graph (10문제)
Day 46-50: 기출 문제 풀이 (5문제)

총 50일 × 1문제 = 2-3개월 완성
```

**관련 레포 추천**
- `TheAlgorithms/Python` - 알고리즘 구현 (이전 섹션)
- `Baekjoon-Online-Judge/` - 백준 기출 풀이

---

### B-3. 보안 & 인프라 (금융권 필수)

#### 1) OWASP/CheatSheetSeries - 보안 체크시트 (28K+ Stars)

**레포 개요**
- OWASP(Open Web Application Security Project)의 공식 보안 체크시트
- 금융권, 공기업에서 필수적인 보안 규정 및 구현 가이드
- Web, API, Cloud 등 분야별 보안 베스트 프랙티스

**설치 및 접근**

```bash
git clone https://github.com/OWASP/CheatSheetSeries.git
cd CheatSheetSeries

# 주요 체크시트 확인
ls -la cheatsheets/

# 예: Authentication Cheat Sheet
cat cheatsheets/Authentication_Cheat_Sheet.md

# 또는 웹브라우저로 접근
# https://cheatsheetseries.owasp.org/
```

**금융권 필수 보안 항목**

```
1. Authentication Security (인증 보안)
   ├─ Password Storage Cheat Sheet
   ├─ Session Management Cheat Sheet
   └─ Multi-Factor Authentication (MFA) 구현

2. Cryptography (암호화)
   ├─ Cryptographic Storage Cheat Sheet
   ├─ HTTPS Implementation
   └─ Key Management

3. API Security (API 보안)
   ├─ REST Security Cheat Sheet
   ├─ GraphQL Cheat Sheet
   └─ OAuth 2.0 Implementation

4. Data Protection (데이터 보호)
   ├─ PCI DSS 준수
   ├─ GDPR 대응
   └─ 개인정보 암호화
```

**실전 예제: 안전한 비밀번호 저장 (Password Hashing)**

```python
# OWASP 권장: bcrypt 사용 (절대 평문 저장 금지!)

import bcrypt
from passlib.context import CryptContext

# bcrypt를 이용한 비밀번호 저장
def hash_password(password: str) -> str:
    """
    비밀번호를 안전하게 해시화
    OWASP: bcrypt with salt (최소 12라운드)
    """
    # salt는 자동으로 생성됨
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))
    return hashed.decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """해시된 비밀번호 검증"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# 사용 예제
original_password = "MySecurePassword123!"
hashed_password = hash_password(original_password)

print(f"해시된 비밀번호: {hashed_password}")
print(f"검증 성공: {verify_password(original_password, hashed_password)}")
print(f"검증 실패: {verify_password('WrongPassword', hashed_password)}")
```

**실전 예제: SQL Injection 방지 (준비된 명령문 사용)**

```python
# OWASP: Parameterized Queries 사용
import sqlite3

# 잘못된 방법 (SQL Injection 취약점!)
def unsafe_query(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    # 문제: username에 ' OR '1'='1 같은 악의적 입력 가능

# 올바른 방법 (OWASP 권장)
def safe_query(username):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # 파라미터화된 쿼리 사용 (?)
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    return cursor.fetchall()

# 사용 예제
safe_query("admin' OR '1'='1")  # 안전함 (문자열로 처리됨)
```

**실전 예제: HTTPS 및 SSL/TLS 구성**

```python
# Flask를 이용한 안전한 HTTPS 설정
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

# OWASP: 보안 헤더 설정
Talisman(app,
    force_https=True,  # HTTP를 HTTPS로 강제 리다이렉트
    strict_transport_security=True,  # HSTS 활성화
    content_security_policy={
        'default-src': "'self'",
        'script-src': "'self' 'unsafe-inline'",
        'style-src': "'self' 'unsafe-inline'"
    }
)

@app.route('/')
def hello():
    return 'Secure Connection'

if __name__ == '__main__':
    # SSL/TLS 인증서로 실행
    app.run(ssl_context='adhoc')  # 또는 'cert.pem', 'key.pem'
```

**금융권 면접 질문 대비**

```
Q1: SQL Injection이란? 방어 방법?
A: 악의적 SQL 코드를 입력하는 공격.
   파라미터화된 쿼리(Prepared Statements) 사용으로 방어

Q2: XSS(Cross-Site Scripting)와 방어?
A: 사용자 입력에 악의적 스크립트를 삽입하는 공격.
   입력 검증, 출력 인코딩, CSP(Content Security Policy) 사용

Q3: OWASP Top 10이란?
A: 웹 애플리케이션의 가장 위험한 10가지 보안 취약점
   (Injection, Broken Authentication, Sensitive Data Exposure 등)

Q4: 금융권에서 필수인 보안 표준?
A: PCI DSS (결제카드 산업 데이터 보안 표준)
   - 비암호화 민감 데이터 저장 금지
   - 강력한 액세스 제어
   - 정기적 보안 감사
```

**관련 레포 추천**
- `OWASP/OWASP-Top-10-2021` - OWASP Top 10 최신 버전
- `ircrazierii/owasp-top-10-labs` - 실습 랩

---

#### 2) trimstray/the-book-of-secret-knowledge - 시스템 관리자/DevOps 완전 가이드 (160K+ Stars)

**레포 개요**
- Linux, 네트워크, 보안, DevOps 관련 심화 지식 모음
- 금융권 인프라 엔지니어 필수 학습 자료
- 실무에서 자주 사용되는 명령어, 설정, 베스트 프랙티스

**설치 및 접근**

```bash
git clone https://github.com/trimstray/the-book-of-secret-knowledge.git
cd the-book-of-secret-knowledge

# README.md가 전체 내용의 목차
# 웹브라우저로도 접근 가능
# https://github.com/trimstray/the-book-of-secret-knowledge
```

**금융권 인프라 필수 주제**

```
1. Linux Administration (리눅스 관리)
   ├─ 파일 시스템 권한 설정 (chmod, chown)
   ├─ 프로세스 관리 (ps, kill, systemd)
   ├─ 네트워크 설정 (ip, netstat, ss)
   └─ 로그 관리 (journalctl, /var/log)

2. Security (보안)
   ├─ SSH 설정 및 키 관리
   ├─ 방화벽 설정 (iptables, firewalld)
   ├─ 접근 제어 (ACL, SELinux)
   └─ 감시 및 모니터링

3. Network (네트워크)
   ├─ TCP/IP 기초
   ├─ DNS 설정
   ├─ VPN 및 TLS/SSL
   └─ 로드 밸런싱

4. DevOps (데브옵스)
   ├─ Docker 컨테이너화
   ├─ 자동화 배포
   ├─ CI/CD 파이프라인
   └─ 모니터링 및 로깅
```

**실전 명령어: 보안 감시**

```bash
# 1. 열린 포트 확인 (nmap 사용)
nmap -sV localhost
# 결과: 어떤 서비스가 어떤 포트에서 실행 중인지 확인

# 2. 네트워크 연결 확인 (ss 사용, netstat은 deprecated)
ss -tlnp
# t: TCP, l: Listening, n: Numeric, p: Process

# 3. 파일 무결성 확인 (md5sum)
md5sum /path/to/critical/file
# 금융권: 중요 파일의 해시값을 정기적으로 검증

# 4. 방화벽 규칙 확인 (firewalld)
sudo firewall-cmd --list-all
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload

# 5. 시스템 보안 감사 (lynis)
sudo apt install lynis
sudo lynis audit system
```

**실전 명령어: 성능 모니터링**

```bash
# 1. CPU 사용률 모니터링
top -b -n 1 | head -20
# b: batch mode, n: 실행 횟수

# 2. 메모리 사용률 확인
free -h
# 금융 거래: 메모리 누수는 심각한 장애

# 3. 디스크 사용률 확인
df -h
du -sh /var/log/*  # 로그 파일 크기 확인

# 4. 네트워크 대역폭 모니터링
iftop -n  # 실시간 네트워크 모니터링

# 5. 프로세스별 리소스 사용 확인
ps aux --sort=-%mem | head -10  # 메모리 사용량 순
ps aux --sort=-%cpu | head -10  # CPU 사용량 순
```

**실전 예제: SSH 보안 설정**

```bash
# SSH 설정 파일 보안화 (/etc/ssh/sshd_config)

# 금융권 필수 설정:
# 1. 루트 로그인 비활성화
sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

# 2. 비밀번호 인증 비활성화 (키 기반 인증만 사용)
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

# 3. SSH 포트 변경 (기본 22 제외)
sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

# 4. 설정 검증
sshd -t

# 5. SSH 서비스 재시작
sudo systemctl restart sshd

# 6. SSH 키 쌍 생성 (클라이언트)
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa
# 결과: ~/.ssh/id_rsa (개인 키), ~/.ssh/id_rsa.pub (공개 키)

# 7. 공개 키를 서버에 배포
ssh-copy-id -i ~/.ssh/id_rsa.pub -p 2222 user@server.com

# 8. SSH 접속 (비밀번호 입력 없음)
ssh -i ~/.ssh/id_rsa -p 2222 user@server.com
```

**실전 예제: 시스템 로그 모니터링**

```bash
# 금융권에서 필수: 모든 접근 및 시스템 변경 기록

# 1. journalctl을 이용한 로그 조회
journalctl --unit=sshd -n 20  # SSH 최근 20개 로그
journalctl -u docker -n 20     # Docker 컨테이너 로그

# 2. 특정 시간대 로그 조회
journalctl -u sshd --since "2024-01-01" --until "2024-01-02"

# 3. 실시간 로그 모니터링
journalctl -f  # tail -f와 유사

# 4. 로그 필터링 (특정 사용자의 실패한 로그인)
grep "Failed password" /var/log/auth.log | grep "user@ip"

# 5. 로그 분석: 비정상 접속 탐지
journalctl -u sshd | grep "Failed\|Accepted" | tail -50
```

**금융권 인프라 면접 대비**

```
Q1: Linux 권한 설정 (chmod)의 의미?
A: chmod 755 = rwx r-x r-x (소유자:읽기+쓰기+실행, 그룹:읽기+실행, 기타:읽기+실행)
   금융권: 민감한 파일은 600 (소유자만 접근)

Q2: 방화벽 설정 필요 이유?
A: 불필요한 포트 차단으로 공격 표면 최소화
   금융권: 화이트리스트 방식 (필요한 포트만 개방)

Q3: SSH 키 기반 인증의 장점?
A: 비밀번호 탈취 불가, Brute-force 공격 방어
   금융권: 필수 요구사항

Q4: 로그 모니터링이 중요한 이유?
A: 침입 탐지, 감시 증적, 규제 준수
   금융권: 감시자 로그(audit log) 유지 의무
```

**관련 레포 추천**
- `OWASP/CheatSheetSeries` (이전 섹션)
- `awesome-selfhosted/awesome-selfhosted` - 자체 호스팅 가이드

---

### B-4. DevOps & CI/CD

#### 1) kubernetes/kubernetes - 컨테이너 오케스트레이션 (113K+ Stars)

**레포 개요**
- 구글에서 개발한 오픈소스 컨테이너 오케스트레이션 플랫폼
- 마이크로서비스 아키텍처의 표준 인프라
- 금융권 대규모 시스템에서 필수적인 기술

**설치 및 기본 설정**

```bash
# 1. kubectl 설치 (Kubernetes CLI)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# 2. kubectl 버전 확인
kubectl version --client

# 3. 로컬 테스트용 Minikube 설치
curl -minikube https://github.com/kubernetes/minikube/releases/download/latest/minikube-linux-amd64
chmod +x minikube-linux-amd64
sudo mv minikube-linux-amd64 /usr/local/bin/minikube

# 4. Minikube 시작
minikube start
minikube status

# 5. Kubernetes 클러스터 확인
kubectl cluster-info
kubectl get nodes
```

**기본 개념: Pod, Service, Deployment**

```bash
# 1. Pod: Kubernetes의 최소 배포 단위 (Docker 컨테이너 래퍼)
# pod.yaml 파일 작성
cat > pod.yaml << 'EOF'
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
EOF

# Pod 생성
kubectl apply -f pod.yaml

# Pod 확인
kubectl get pods
kubectl describe pod nginx-pod

# Pod 로그 확인
kubectl logs nginx-pod
```

**실전 예제: Deployment 핵심 필드**

`deployment.yaml`의 필수 요소는 다음과 같습니다.

- `apiVersion: apps/v1`, `kind: Deployment`
- `spec.replicas: 3` (Pod 복제본)
- `spec.selector.matchLabels`와 `spec.template.metadata.labels` 일치
- `containers[].image`, `containers[].ports.containerPort`
- `resources.requests/limits` (memory/cpu)
- `livenessProbe.httpGet` (헬스체크)

배포: `kubectl apply -f deployment.yaml`, 상태 확인: `kubectl get deployments/pods`, 업데이트: `kubectl set image deployment/web-app web=nginx:1.21`, 롤백: `kubectl rollout undo deployment/web-app`.

**실전 예제: Service / ConfigMap / Secret**

- **Service** (`type: LoadBalancer`): `selector.app`으로 Pod를 선택, `port` → `targetPort` 매핑
- **ConfigMap**: 환경 변수 주입용 (예: `DATABASE_HOST`, `LOG_LEVEL`)
- **Secret** (`type: Opaque`): 민감 정보는 base64 인코딩 — 금융권에선 Vault/KMS 연동 필수

**금융권 Kubernetes 필수 설정**

- **Namespace**: 팀/환경별 격리 (`kind: Namespace`, `metadata.name: finance`)
- **NetworkPolicy**: 기본 deny-all 후 화이트리스트. `policyTypes: [Ingress, Egress]`, `podSelector: {}`
- **RBAC**: `Role`(권한 정의) + `RoleBinding`(사용자-권한 연결). 예: `verbs: [get, list, watch]`만 허용

> Claude Code 활용 팁
> `> "내 Spring Boot 앱(8080 포트)을 K8s에 배포하는 deployment.yaml + service.yaml을 만들고, 금융권 기준 NetworkPolicy와 RBAC도 같이 정의해줘"`

**관련 레포 추천**
- `kubernetes/kubernetes` - 공식 저장소
- `kelseyhightower/kubernetes-the-hard-way` - Kubernetes 완전 학습

---

#### 2) actions/runner - GitHub Actions 실행 환경 (5K+ Stars)

**레포 개요**
- GitHub Actions의 공식 실행 환경 (runner)
- CI/CD 파이프라인 구축의 핵심
- 금융권에서 자동화 테스트 및 배포에 필수

**GitHub Actions 기본 개념**

```bash
# GitHub 저장소에서 .github/workflows 디렉토리 생성
mkdir -p .github/workflows

# 워크플로우 파일 작성
cat > .github/workflows/ci.yml << 'EOF'
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
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        pytest tests/ -v --cov=src

    - name: Security scan
      run: |
        bandit -r src/ -f json -o bandit-report.json

    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
EOF
```

**실전 예제: Python 프로젝트 CI/CD 파이프라인**

Python 앱의 전형적인 워크플로우는 3개 job으로 구성됩니다.

- **test job**: `actions/checkout` → `setup-python` (matrix로 3.8-3.11) → `pip install` → `flake8`, `mypy`, `pytest --cov` → `codecov-action`으로 커버리지 업로드
- **security job**: `bandit`, `semgrep --config=p/security-audit`, `safety check`
- **deploy job**: `needs: [test, security]`에 `if: github.ref == 'refs/heads/main'` 조건을 걸어 스테이징 배포

**금융권 필수 CI/CD 설정**

금융권은 위 기본 파이프라인에 아래 단계를 추가로 요구합니다.

- 코드 품질 게이트: `pylint --fail-under=9.0`, `black --check`, `isort --check-only`
- 의존성 취약점: `pip-audit`, `safety check`
- 암호화/컴플라이언스 자체 스크립트 (`verify-encryption.sh`, `check-compliance.sh`)
- 부하 테스트: `locust --headless -u 100 -r 10 --run-time 60s`
- SBOM 생성: `cyclonedx-bom -o sbom.xml`
- approval-gate: PR 승인 2인 이상 체크 (`actions/github-script`로 `pulls.listReviews` 검증)

> Claude Code 활용 팁
> `> "금융권 CI/CD 요구사항(코드 품질/보안/SBOM/2인 승인)을 모두 충족하는 GitHub Actions workflow를 내 Python 프로젝트에 맞게 만들어줘"`

**GitHub Actions 사용 예제: 자동 버전 관리**

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
    - uses: actions/checkout@v3

    - name: Create Release Notes
      run: |
        # 커밋 로그 기반 릴리스 노트 생성
        git log $(git describe --tags --abbrev=0)..HEAD --oneline > RELEASE_NOTES.md

    - name: Create GitHub Release
      uses: actions/create-release@v1
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        tag_name: ${{ github.ref }}
        release_name: Release ${{ github.ref }}
        body_path: RELEASE_NOTES.md
```

**학습 전략: GitHub Actions 마스터**

```
Step 1: 기본 워크플로우 작성 (1주)
├─ Checkout, Setup Python
├─ Install dependencies
└─ Run tests

Step 2: CI/CD 자동화 (1주)
├─ Code quality checks
├─ Security scans
└─ Automated testing

Step 3: 배포 자동화 (1주)
├─ Docker build & push
├─ Kubernetes deployment
└─ Health checks

Step 4: 고급 기능 (1주)
├─ Matrix builds (다양한 환경)
├─ Conditional steps
└─ Secrets 관리

총 4주 학습
```

**관련 레포 추천**
- `actions/runner` - 공식 저장소
- `awesome-actions/awesome-actions` - GitHub Actions 라이브러리 모음

---
