# 1-3. 면접 준비

> 코딩 실력이 좋아도 면접에서 제대로 보여주지 못하면 취업이 어렵습니다.
> 이 챕터에서는 **"아는 걸 잘 보여주는 기술"**을 익히는 레포 3개를 소개합니다.

!!! info "📌 핵심 요약"
    - **tech-interview-handbook**: 면접 전/중/후 체크리스트, 시스템 디자인 프레임워크
    - **system-design-primer**: 대규모 시스템 설계의 "국룰" 가이드 (한국어 번역 존재)
    - **interviews**: Java 기반 LeetCode 빈출 풀이 모음

---

## yangshun/tech-interview-handbook (122K+ Stars)

**링크**: https://github.com/yangshun/tech-interview-handbook

**한 줄 소개**: Facebook 엔지니어가 만든 기술 면접 종합 가이드 — 이력서부터 시스템 디자인까지.
**왜 봐야 하는가**: 기술 지식이 아니라 **"면접 프로세스 자체를 꿰뚫는 인사이트"**가 담겨 있어요. 실전 노하우의 보고입니다.
**난이도**: ⭐⭐⭐

### 📋 이 레포가 다루는 내용

- 코딩 면접 전/중/후 체크리스트
- 시스템 디자인 40분 프레임워크
- 이력서 작성 팁 (한 페이지 원칙)
- 행동 면접 STAR 기법
- 연봉 협상 가이드

### 🚀 15분 퀵스타트

1단계. 레포 방문 → https://www.techinterviewhandbook.org (웹 버전이 더 편해요)

2단계. "Coding Interview Cheatsheet" 페이지 읽기

3단계. 아래 3단계 체크리스트를 내 면접 날 그대로 따라하기

**면접 전**

- [ ] 회사 기술 스택 조사 (JobPost + 팀 블로그)
- [ ] 최근 프로젝트 2~3개 한 줄 요약 암기
- [ ] 인터뷰어 LinkedIn 확인
- [ ] 자주 묻는 문제 유형 3~5개 복습

**면접 중**

- [ ] 질문을 내 말로 다시 설명 (확인)
- [ ] 브루트포스 → 최적화 순서로 접근 설명
- [ ] 엣지 케이스 먼저 언급
- [ ] 코드 작성 중 계속 말하기 (think-aloud)
- [ ] 완성 후 시간/공간 복잡도 분석

**면접 후**

- [ ] 테스트 케이스 2개 이상 직접 실행
- [ ] 개선 방향 한 마디 (예: "캐시를 추가하면 O(1)")
- [ ] 질문 기회에 팀 문화/기술 부채 질문

### 🏗️ 시스템 디자인 40분 프레임워크

| 단계 | 시간 | 할 일 |
|------|------|-------|
| 1. 요구사항 명확화 | 5분 | 함수형/비함수형, Scale, QPS, Data volume |
| 2. API 설계 | 5분 | Endpoints, Request/Response, Rate limiting |
| 3. 데이터 모델 | 5분 | 스키마, 인덱싱, Sharding 전략 |
| 4. High-level 설계 | 10분 | Components, Data flow, Cache, MQ |
| 5. 상세 설계 | 10분 | 병목 분석, 최적화 |
| 6. 마무리 | 5분 | Monitoring, Logging, Future work |

### 🎯 실전 예시: URL Shortener 설계

**1단계 요구사항**

- 함수형: 긴 URL → 짧은 URL, 리다이렉트
- 비함수형: 500 writes/sec, 100,000 reads/sec, Latency < 200ms, 가용성 99.9%

**2단계 용량 산정**

```
5년 쓰기: 500 * 86400 * 365 * 5 ≈ 78.8B URLs
저장 용량: 78.8B * 100B ≈ 7.88 TB
```

**3단계 API**

```http
POST /api/shorten
{ "long_url": "https://example.com/very/long/url" }

Response:
{ "short_url": "https://short.url/abc123" }

GET /api/{code} → 301 Redirect
```

**4단계 데이터 모델**

```sql
CREATE TABLE URLMapping (
  id          BIGINT PRIMARY KEY,
  short_code  VARCHAR(10) UNIQUE,
  long_url    VARCHAR(2048),
  created_at  TIMESTAMP,
  expiration  TIMESTAMP
);
```

**5단계 아키텍처**

```
Client → Load Balancer → API Servers
                            ↓
                       Redis Cache (LRU)
                            ↓
                       MySQL (Master-Slave)
                            ↓
                       Kafka (Analytics 비동기)
```

**6단계 핵심 기법**

- Short code 생성: **Base62** (0-9, a-z, A-Z)
- 충돌 처리: Retry with increment
- 캐싱: Redis LRU
- 부하 분산: Consistent Hashing

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트: 모의 면접"
    > "나는 백엔드 주니어 지원자야. URL Shortener 시스템 디자인을 40분 기준으로 모의 면접 해줘. 단계별로 질문하고, 내 답변 후 피드백 줘."

!!! example "🤖 Claude Code 프롬프트: 이력서 리뷰"
    > "내 이력서(아래 텍스트)를 보고 tech-interview-handbook의 원칙에 맞춰 한 줄씩 개선안을 제시해줘. 숫자 중심, 임팩트 중심으로 리팩토링해줘."

!!! example "🤖 Claude Code 프롬프트: 행동 질문 답변"
    > "'팀에서 갈등이 있었을 때 어떻게 해결했나요?'라는 질문에 STAR 기법(Situation-Task-Action-Result)으로 답변 템플릿을 만들어줘."

### 📚 학습 체크리스트

- [ ] Coding Interview Cheatsheet 완독
- [ ] 시스템 디자인 4개 주제 연습 (URL Shortener, 채팅, 피드, 검색)
- [ ] STAR 기법 스토리 3개 준비
- [ ] 이력서 한 페이지 정리
- [ ] 모의 면접 3회 이상 진행

---

## donnemartin/system-design-primer (290K+ Stars)

**링크**: https://github.com/donnemartin/system-design-primer

**한 줄 소개**: 시스템 디자인 면접의 바이블 — **한국어 번역본 존재**!
**왜 봐야 하는가**: 확장성, 일관성, 캐싱, 샤딩 등 **대규모 시스템의 모든 키워드**가 예제와 함께 정리되어 있어요.
**난이도**: ⭐⭐⭐⭐

### 📋 이 레포가 다루는 내용

- Scalability, Availability, Consistency 핵심 개념
- SQL vs NoSQL 선택 기준
- 캐싱 전략 (LRU, LFU, Write-Through, Write-Back, Cache-Aside)
- Load Balancer, CDN, Reverse Proxy
- Message Queue (RabbitMQ, Kafka)
- **실전 면접 질문 + 모범 답안**

### 🚀 15분 퀵스타트

1단계. 한국어 README 열기

```bash
git clone https://github.com/donnemartin/system-design-primer.git
cd system-design-primer
# README-ko.md 파일을 에디터로 열기
```

2단계. 첫 3개 섹션만 속독 (각 15분)

- Performance vs scalability
- Latency vs throughput
- Availability vs consistency

3단계. Python으로 LRU 캐시 직접 구현

```python
from collections import OrderedDict

class LRUCache:
    """면접 빈출: LRU 캐시 O(1) 구현"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 최근 사용으로 이동
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # 가장 오래된 항목 제거
            self.cache.popitem(last=False)

# 테스트
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)  # 2를 쫓아냄
assert cache.get(2) == -1
print("LRU Cache 통과")
```

예상 출력:

```
LRU Cache 통과
```

### 🏗️ 핵심 개념 치트시트

**1. Scalability (확장성)**

| 방식 | 설명 | 한계 |
|------|------|------|
| Vertical (수직) | CPU/메모리 업그레이드 | 단일 기계 물리 한계 |
| Horizontal (수평) | 서버 추가 + LB 분산 | 복잡도 증가 (대부분의 경우 권장) |

**2. SQL vs NoSQL**

| | SQL | NoSQL |
|---|-----|-------|
| 장점 | ACID, 복잡한 쿼리 | 수평 확장, 유연한 스키마 |
| 단점 | 확장 어려움, 고정 스키마 | ACID 보장 X, 쿼리 제한 |
| 대표 | MySQL, PostgreSQL | MongoDB, Cassandra, DynamoDB |

**3. 캐싱 전략**

- **Cache-Aside** (가장 많이 쓰임): 앱이 캐시 미스 시 DB 조회 후 캐시에 저장
- **Write-Through**: 쓰기 시 캐시와 DB 동시 갱신 (정합성 ↑)
- **Write-Back**: 캐시만 먼저 쓰고 DB는 나중에 (성능 ↑, 유실 위험)
- **LRU**: 가장 오래 안 쓴 것 제거
- **LFU**: 가장 적게 쓴 것 제거

!!! tip "💡 꿀팁: 면접에서 캐싱 전략 고를 때"
    **읽기/쓰기 비율 → 정합성 요구 → 히트율** 세 기준으로 설명하면 면접관이 감탄합니다.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "system-design-primer의 한국어 README를 기반으로, 주니어 백엔드 지원자가 꼭 외워야 할 시스템 디자인 핵심 개념 Top 10을 한 줄 요약으로 뽑아줘."

!!! example "🤖 Claude Code 프롬프트"
    > "내가 Cache-Aside 전략을 Python Flask 앱에 적용하고 싶어. Redis를 캐시로 쓰는 최소 예제 코드를 작성하고 각 줄마다 주석 달아줘."

!!! example "🤖 Claude Code 프롬프트"
    > "Instagram 피드 시스템을 설계한다면 어떤 DB(SQL/NoSQL)를 쓸 것이고 왜 그런지 trade-off 분석을 해줘."

### 📚 학습 체크리스트

- [ ] 한국어 README 1회 완독
- [ ] LRU Cache 직접 구현
- [ ] CAP Theorem 설명할 수 있음
- [ ] Sharding 전략 3가지 설명 가능
- [ ] 실전 면접 질문 5개 풀이 연습

---

## kdn251/interviews (63K+ Stars)

**링크**: https://github.com/kdn251/interviews

**한 줄 소개**: Java로 정리된 LeetCode/HackerRank 빈출 문제 풀이 모음.
**왜 봐야 하는가**: 네이버/카카오/라인 같은 **Java 기반 국내 빅테크 면접** 준비에 가장 적합합니다.
**난이도**: ⭐⭐⭐

### 📋 이 레포가 다루는 내용

- Array, String, Tree, Graph, DP 카테고리별 풀이
- 각 문제마다 Java 코드 + 설명
- 복잡도 분석 (Big-O)
- 대기업 빈출 문제 필터링

### 🚀 15분 퀵스타트

1단계. 레포 클론 + 첫 문제 열기

```bash
git clone https://github.com/kdn251/interviews.git
cd interviews
```

2단계. Two Sum (Array 카테고리) 열기 → Java 풀이 확인

```java
// Two Sum - Hash Map 활용 O(n)
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[] { seen.get(complement), i };
            }
            seen.put(nums[i], i);
        }
        return new int[] {};
    }

    public static void main(String[] args) {
        TwoSum solver = new TwoSum();
        int[] result = solver.twoSum(new int[] { 2, 7, 11, 15 }, 9);
        System.out.println(result[0] + ", " + result[1]);
        // 예상 출력: 0, 1
    }
}
```

3단계. 같은 문제를 **내가 먼저 풀어본 뒤** 비교하기

!!! warning "⚠️ 자주 하는 실수"
    **코드를 보고 "나도 이렇게 풀 줄 알아"라고 넘어가는 것**.
    반드시 빈 파일에서 직접 타이핑하면서 풀어보세요. 눈으로 볼 때와 손으로 칠 때의 격차가 엄청납니다.

### 🏆 국내 대기업 빈출 Top 10

| # | 문제 | 카테고리 | 난이도 |
|---|------|---------|--------|
| 1 | Two Sum | Array + HashMap | Easy |
| 2 | Valid Palindrome | Two Pointers | Easy |
| 3 | Reverse Linked List | LinkedList | Easy |
| 4 | Valid Parentheses | Stack | Easy |
| 5 | Merge Intervals | Sorting | Medium |
| 6 | LRU Cache | Design + LinkedHashMap | Medium |
| 7 | Number of Islands | BFS/DFS | Medium |
| 8 | Longest Substring Without Repeating | Sliding Window | Medium |
| 9 | Course Schedule | Topological Sort | Medium |
| 10 | Word Break | DP | Medium |

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "kdn251/interviews 레포의 Dynamic Programming 섹션에서 금융권 면접 빈출 Top 5를 골라 시간복잡도와 핵심 아이디어를 비교 표로 만들어줘."

!!! example "🤖 Claude Code 프롬프트"
    > "내가 Java로 푼 Two Sum 코드를 리뷰해줘. 시간/공간 복잡도 분석과, 같은 문제를 Python/TypeScript로 다시 풀었을 때 어떤 점이 달라지는지 비교해줘."

!!! example "🤖 Claude Code 프롬프트"
    > "국내 대기업 빈출 Top 10 문제를 Java로 2주 동안 완주하는 학습 계획을 만들어줘. 매일 어떤 문제를 풀고 왜 그 순서인지 근거도 달아줘."

### 📚 학습 체크리스트

- [ ] Array/String 섹션 20문제 완료
- [ ] LinkedList/Tree 15문제 완료
- [ ] DP 10문제 완료
- [ ] Java HashMap/PriorityQueue API 숙달
- [ ] Top 10 문제 모두 코드 보지 않고 풀기

!!! danger "🚨 자주 발생하는 에러: Java 컴파일"
    **에러**: `error: class TwoSum is public, should be declared in a file named TwoSum.java`
    **원인**: 파일명과 public 클래스명 불일치
    **해결**: 파일명을 `TwoSum.java`로 정확히 맞춰주세요.

---

!!! tip "💡 다음 단계"
    알고리즘 면접이 탄탄해졌다면, 이제 데이터 분석 기초를 다져볼 차례입니다.
    요즘은 개발자도 SQL/Pandas 정도는 기본이에요.
    [1-4. 데이터 분석 & 시각화](04-data-analysis.md)로 가볼까요?
