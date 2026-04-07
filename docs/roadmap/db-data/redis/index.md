# 📘 Redis 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/redis/redis.svg?style=social)](https://github.com/redis/redis)

!!! info "레포지토리"
    **redis/redis** · 67k+ ⭐ · RSAL/SSPL · [redis.io](https://redis.io)

---

## 🧐 1. Redis는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Redis("REmote DIctionary Server")는 **메모리에 데이터를 저장하는 초고속 키-값 스토어**입니다. 단순 캐시를 넘어 자료구조 서버, 메시지 브로커, 세션 스토어, 분산 락 등 다양한 역할을 합니다.

### 핵심 특성
- **In-memory**: 디스크 대신 RAM에 저장 → 마이크로초 수준 응답.
- **풍부한 자료구조**: String, List, Set, Sorted Set, Hash, Stream, Bitmap, HyperLogLog, Geo.
- **영속성 옵션**: RDB 스냅샷, AOF 로그.
- **Pub/Sub**: 단순 메시지 브로커.
- **Lua 스크립팅**: 원자적 복합 연산.
- **Cluster·Sentinel**: 고가용성·샤딩.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **DB 부하 감소** | 자주 읽는 데이터 캐싱 |
| **세션 스토어** | 멀티 인스턴스 환경에서 세션 공유 |
| **Rate Limiting** | INCR + EXPIRE 조합 |
| **분산 락** | Redlock 알고리즘 |
| **실시간 랭킹** | Sorted Set으로 리더보드 |

## 🚀 2. 10분 퀵스타트

```bash
docker run --rm -d --name plaf-redis -p 6379:6379 redis:7-alpine
docker exec -it plaf-redis redis-cli
```

```
127.0.0.1:6379> SET user:1 "Alice"
OK
127.0.0.1:6379> GET user:1
"Alice"
127.0.0.1:6379> EXPIRE user:1 60
(integer) 1
127.0.0.1:6379> ZADD leaderboard 100 alice 200 bob 150 charlie
127.0.0.1:6379> ZREVRANGE leaderboard 0 -1 WITHSCORES
1) "bob"
2) "200"
3) "charlie"
4) "150"
5) "alice"
6) "100"
```

## 🛠️ 3. 코드 해부학: 자료구조 별 사용 패턴

| 자료구조 | 사용 사례 | 핵심 명령 |
|---|---|---|
| String | 캐시, 카운터 | `SET`, `GET`, `INCR` |
| Hash | 객체 캐시 | `HSET`, `HGETALL` |
| List | 큐, 최근 항목 | `LPUSH`, `RPOP`, `LRANGE` |
| Set | 태그, 유니크 사용자 | `SADD`, `SISMEMBER` |
| Sorted Set | 랭킹, 시간순 정렬 | `ZADD`, `ZRANGEBYSCORE` |
| Stream | 이벤트 로그 | `XADD`, `XREAD` |

!!! warning "주의"
    - **TTL 없이 SET**은 메모리 누수의 원인.
    - `KEYS *` 명령은 운영에서 금지 (`SCAN` 사용).
    - 라이선스가 RSAL/SSPL로 변경되어 일부 클라우드 사용에 제약이 있습니다. 대안으로 [Valkey](https://github.com/valkey-io/valkey) 검토.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think Spring Boot 앱에 Redis 캐시를 도입하려고 한다:
- 캐시 키 네이밍 컨벤션
- TTL 전략 (짧은/긴 캐시 분리)
- Cache-Aside vs Write-Through
- 캐시 무효화 패턴
- 장애 시 fallback
설계 가이드를 작성해 줘.
```

### 🔵 Gemini
```
Redis vs Memcached vs Hazelcast vs Valkey를 비교 표로.
2026년 기준 라이선스 변화도 포함.
```

### 🟢 ChatGPT
```
"실시간 채팅 + 알림" 서비스에 Redis를 어떻게 활용할 수 있는지
Pub/Sub, Stream, Sorted Set, Hash 각각의 사용처를 설계해 줘.
```

### ⬛ Copilot
```python
# TODO: Redis 기반 분산 락 (set NX EX) + 자동 갱신 데코레이터
```

## 🔗 5. 관련 레포 · 다음 단계
- 포크 대안: [Valkey](https://github.com/valkey-io/valkey) (Linux Foundation)
- 클러스터: [KeyDB](https://github.com/Snapchat/KeyDB), [Dragonfly](https://github.com/dragonflydb/dragonfly)
- 모듈: RedisJSON, RediSearch, RedisGraph
- [PostgreSQL 딥다이브](../postgres/index.md) (영속 저장소와 조합)
