# 6-1. 기술 면접 준비

> Part 1-3에서 기초 면접 준비 레포를 소개했다면, 이번 챕터는 **실전 압축판**입니다.
> 면접 2개월 전부터 집중적으로 파고들 때 유용한 3대 레포를 중심으로 정리했어요.

!!! info "📌 핵심 요약"
    - **tech-interview-handbook**: 면접 프로세스 + 코딩/시스템 디자인 치트시트
    - **system-design-primer**: 대규모 시스템 설계의 바이블
    - **interviews (kdn251)**: Java 기반 빅테크 면접 빈출 풀이

---

## yangshun/tech-interview-handbook (122K+ Stars)

**링크**: https://github.com/yangshun/tech-interview-handbook

**한 줄 소개**: 기술 면접의 모든 단계를 정리한 종합 가이드.
**왜 봐야 하는가**: 단순 알고리즘 문제가 아니라 **"면접 프로세스 자체"**를 이해할 수 있어요. 이력서, 행동 면접, 연봉 협상까지 포함.
**난이도**: ⭐⭐⭐

### 📋 이 레포가 다루는 내용

- 코딩 면접 치트시트
- 시스템 디자인 프레임워크
- 행동 면접 STAR 기법
- 이력서 원페이지 원칙
- 연봉 협상 시나리오

### 📋 면접 단계별 체크리스트

!!! tip "💡 꿀팁: 면접 전날엔 이것만"
    새로운 지식을 채우려 하지 말고 **"내가 이미 아는 걸 빠르게 복기"** 하는 데 집중하세요.

**1. 코딩 면접 (Coding Interview)**

| 단계 | 할 일 |
|------|-------|
| 면접 전 | 회사 기술 스택 조사, 최근 프로젝트 복습, 인터뷰어 LinkedIn 확인, 자주 묻는 문제 3-5개 준비 |
| 면접 중 | 질문 명확히 이해, 접근 방법 설명, 엣지 케이스 고려, 시간복잡도 분석, 트레이드오프 논의 |
| 코딩 후 | 코드 리뷰, 테스트 케이스 작성, 성능 개선 제시, 결과 검증 |

**2. 시스템 디자인 면접 40분 프레임워크**

1. **요구사항 명확히 (5분)**: 함수형/비함수형, Scale, QPS, Data volume
2. **API 설계 (5분)**: Endpoints, Request/Response, Rate limiting
3. **데이터 모델 (5분)**: 스키마, 인덱싱, Sharding 전략
4. **High-level 설계 (10분)**: Components, Data flow, Cache, MQ
5. **상세 설계 (10분)**: 핵심 컴포넌트 심화, 병목 분석, 최적화
6. **마무리 (5분)**: Monitoring, Logging, Future improvements

### 🎯 실전 예시: URL Shortener

- **요구사항**: 쓰기 500/s, 읽기 100,000/s, 가용성 99.9%, Latency < 200ms
- **용량 산정**: 5년 기준 약 78.8B URLs × 100B ≈ 7.88 TB
- **API**:

```http
POST /api/shorten
{ "long_url": "https://example.com/very/long/url" }
→ { "short_url": "https://short.url/abc123" }

GET /api/{code} → 301 Redirect
```

- **데이터 모델**:

```sql
URLMapping (
  id PK,
  short_code VARCHAR(10) UNIQUE,
  long_url VARCHAR(2048),
  created_at, expiration
)
```

- **아키텍처**: Client → LB → API Servers → Redis Cache → MySQL. 분석은 Kafka로 비동기.
- **핵심 기법**: Base62 인코딩, 충돌 처리는 retry+increment, LRU 캐시, Consistent Hashing

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트: 회사 맞춤 면접 시뮬레이션"
    > "나는 토스뱅크 백엔드 지원자야. 최근 토스 기술 블로그 3개를 반영해서 예상 면접 질문 10개와 모범 답변을 만들어줘. 각 질문마다 난이도와 평가 포인트도."

!!! example "🤖 Claude Code 프롬프트: STAR 답변 생성"
    > "내 경험(캡스톤 프로젝트에서 팀 리더로 갈등 중재)을 STAR 기법으로 2분 답변 스크립트로 만들어줘. 구체적인 숫자와 결과를 포함해서."

!!! example "🤖 Claude Code 프롬프트: 실시간 피드백"
    > "URL Shortener 시스템 디자인을 할 건데, 내가 한 단계씩 설명할 때마다 놓친 부분을 물어봐줘. 40분 안에 끝내는 게 목표야."

### 📚 학습 체크리스트

- [ ] Coding Interview Cheatsheet 완독
- [ ] 시스템 디자인 4개 주제 연습
- [ ] STAR 기법 스토리 3개 준비
- [ ] 이력서 한 페이지로 정리
- [ ] 모의 면접 3회 이상 진행

---

## donnemartin/system-design-primer (290K+ Stars)

**링크**: https://github.com/donnemartin/system-design-primer

**한 줄 소개**: 시스템 디자인 면접 대비의 국제 표준 — **한국어 번역본 존재**!
**왜 봐야 하는가**: 확장성, 일관성, 캐싱 같은 개념이 **실무 사례**와 함께 정리되어 있어요.
**난이도**: ⭐⭐⭐⭐

### 🏗️ 핵심 개념 압축

**1. Scalability (확장성)**

- **Vertical Scaling**: CPU/메모리 업그레이드. 간단하지만 단일 기계 한계.
- **Horizontal Scaling**: 서버 여러 대 + Load Balancer. 대부분 이쪽이 효율적.
- 전형 구조: `Client → LB → App1/2/3 → Redis Cache → DB(Master-Slave)`

**2. SQL vs NoSQL**

| | SQL | NoSQL |
|---|-----|-------|
| 장점 | ACID, 복잡한 쿼리 가능, 데이터 무결성 | 수평 확장 용이, 빠른 읽기/쓰기, 유연한 스키마 |
| 단점 | 수평 확장 어려움, 고정 스키마 | ACID 미보장, 쿼리 제한, Consistency 문제 |
| 대표 | MySQL, PostgreSQL | MongoDB, Cassandra, DynamoDB |

**3. 캐싱 전략 5가지**

- **LRU** (Least Recently Used)
- **LFU** (Least Frequently Used)
- **Write-Through**: 쓸 때 캐시+DB 동시
- **Write-Back**: 캐시만 먼저, DB는 나중
- **Cache-Aside**: 앱이 캐시 미스 시 DB에서 로드

!!! tip "💡 꿀팁: 캐싱 전략 고르는 3기준"
    **"읽기/쓰기 비율 → 정합성 요구 → 히트율"** 이 순서대로 설명하면
    면접관이 "이 친구 실무 감각 있네" 싶어합니다.

### 💻 LRU 캐시 O(1) 구현 (빈출)

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
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

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "system-design-primer 한국어 README에서 주니어 백엔드 지원자가 암기해야 할 핵심 용어 Top 30을 뽑고, 각각을 한 문장으로 정의해줘."

!!! example "🤖 Claude Code 프롬프트"
    > "'Instagram 피드 시스템'을 설계한다면 Pull vs Push 모델 중 어떤 걸 선택할지, 각 방식의 Trade-off를 표로 비교해줘."

!!! example "🤖 Claude Code 프롬프트"
    > "내 Spring Boot 앱에 Cache-Aside 전략을 Redis로 구현하고 싶어. `@Cacheable` 어노테이션 대신 직접 RedisTemplate으로 구현한 예제 코드와 해설 줘."

### 📚 학습 체크리스트

- [ ] 한국어 README 1회 완독
- [ ] LRU Cache 직접 구현
- [ ] CAP Theorem 설명 가능
- [ ] Sharding 3가지 방식 비교 가능
- [ ] 실전 면접 질문 5개 풀이

---

## kdn251/interviews (63K+ Stars)

**링크**: https://github.com/kdn251/interviews

**한 줄 소개**: Java 기반 LeetCode 빈출 풀이의 한국판 바이블.
**왜 봐야 하는가**: **네이버/카카오/라인 등 국내 빅테크는 Java 선호**. 영어 자료보다 접근성이 높고 빈출 문제 위주입니다.
**난이도**: ⭐⭐⭐

### 🎯 Java 기반 면접 전략

- 이 레포는 LeetCode 빈출 문제의 Java 풀이를 Array/String/Tree/DP 등 카테고리별로 정리합니다.
- **추천 학습법**: 문제를 직접 풀어본 뒤 레포 풀이와 비교, 시간/공간 복잡도를 꼭 따져보세요.
- **대기업 빈출 Top 5**: Two Sum, Valid Palindrome, Reverse Integer, Merge Intervals, LRU Cache

### 🏆 국내 빅테크 면접 Top 10 문제

| # | 문제 | 카테고리 | 난이도 | 핵심 기법 |
|---|------|---------|--------|-----------|
| 1 | Two Sum | Array + Hash | Easy | 해시맵으로 O(n) |
| 2 | Valid Palindrome | Two Pointers | Easy | 양쪽 포인터 |
| 3 | Merge Intervals | Sorting | Medium | 정렬 후 병합 |
| 4 | LRU Cache | Design | Medium | LinkedHashMap |
| 5 | Number of Islands | BFS/DFS | Medium | 그래프 탐색 |
| 6 | Longest Substring w/o Repeat | Sliding Window | Medium | 슬라이딩 윈도우 |
| 7 | Course Schedule | Topological Sort | Medium | 진입 차수 |
| 8 | Word Break | DP | Medium | 1D DP |
| 9 | Kth Largest Element | Heap | Medium | PriorityQueue |
| 10 | Trapping Rain Water | Two Pointers | Hard | 양쪽 최대 |

### 💻 Java 샘플: LRU Cache (LinkedHashMap 활용)

```java
import java.util.LinkedHashMap;
import java.util.Map;

public class LRUCache extends LinkedHashMap<Integer, Integer> {
    private final int capacity;

    public LRUCache(int capacity) {
        super(capacity, 0.75f, true);  // accessOrder=true가 핵심
        this.capacity = capacity;
    }

    public int get(int key) {
        return super.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        super.put(key, value);
    }

    @Override
    protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
        return size() > capacity;
    }
}
```

!!! warning "⚠️ 자주 하는 실수"
    **`LinkedHashMap`의 `accessOrder` 파라미터**를 `true`로 안 주면 삽입 순서 기준이 됩니다.
    LRU 구현엔 반드시 `true`를 넣으세요.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "kdn251/interviews 레포의 Dynamic Programming 섹션에서 금융권 면접 빈출 Top 5를 골라서 시간복잡도와 핵심 아이디어를 Java 코드와 함께 비교해줘."

!!! example "🤖 Claude Code 프롬프트"
    > "내가 Java로 푼 Two Sum 코드를 성능/가독성/확장성 3가지 관점에서 리뷰해줘. 개선할 점이 있다면 코드와 이유를 함께."

!!! example "🤖 Claude Code 프롬프트"
    > "국내 대기업 빈출 Top 10을 2주 완주할 수 있는 학습 계획을 Java 기준으로 만들어줘. 매일 어떤 문제 풀고 어떤 개념을 익힐지 구체적으로."

### 📚 학습 체크리스트

- [ ] Array/String 섹션 20문제 완료
- [ ] LinkedList/Tree 15문제 완료
- [ ] DP 10문제 완료
- [ ] Top 10 문제 "코드 보지 않고" 풀기
- [ ] 각 문제의 시간/공간 복잡도 설명 가능

!!! danger "🚨 자주 발생하는 에러"
    **에러**: 면접에서 "이 코드 시간복잡도는요?"라는 질문에 얼어붙기
    **원인**: 코드만 외우고 개념을 안 봄
    **해결**: 매 문제마다 **"이 풀이의 Big-O와 그 이유"**를 말로 설명하는 연습을 하세요.

---

!!! tip "💡 다음 단계"
    기술 면접 공통 과목이 정리되셨다면, 이제 **금융권/공기업 특화** 레포로 차별화할 시간입니다.
    [6-2. 금융/공기업 취업 레포](02-finance-public.md)로 이동하세요.
