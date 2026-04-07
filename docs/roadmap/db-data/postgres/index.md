# 📘 PostgreSQL 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/postgres/postgres.svg?style=social)](https://github.com/postgres/postgres)

!!! info "레포지토리"
    **postgres/postgres** (GitHub 미러) · 17k+ ⭐ · PostgreSQL License · [postgresql.org](https://www.postgresql.org)

---

## 🧐 1. PostgreSQL은 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: PostgreSQL("포스트그레스" 또는 "포스트그레SQL")은 **30년 이상 개발되어 온, 가장 강력한 오픈소스 객체-관계형 데이터베이스 시스템**입니다. SQL 표준 준수도가 매우 높고, 확장성·신뢰성·성능 모두에서 상용 DB와 견줄 수준입니다.

### 핵심 특성

- **ACID 완전 준수**: 트랜잭션·격리 수준·일관성 보장. 금융·결제 시스템도 안심하고 사용.
- **MVCC (Multi-Version Concurrency Control)**: 읽기와 쓰기가 서로를 막지 않음 → 높은 동시성.
- **풍부한 데이터 타입**: JSON/JSONB, 배열, 범위(Range), 지리정보(PostGIS), 전문검색(tsvector), UUID 등.
- **확장(Extension) 시스템**: `CREATE EXTENSION`으로 기능 추가. 대표적으로 **pgvector**(벡터 검색 → AI/RAG), **PostGIS**(GIS), **TimescaleDB**(시계열).
- **윈도우 함수·CTE·재귀 쿼리**: 복잡한 분석 쿼리를 SQL 한 방에 처리.
- **논리 복제·스트리밍 복제**: 고가용성·읽기 분산 구성 가능.

### 실무 도입 포인트

| 도입 이유 | 구체적 효과 |
|---|---|
| **"기본값으로 PostgreSQL"이 업계 컨센서스** | 새 프로젝트 DB 선택 고민 해결 |
| **JSON과 RDB 모두 지원** | JSONB 컬럼으로 유연한 스키마 + 인덱스로 빠른 검색 → MongoDB 대안 |
| **pgvector로 AI 워크로드 흡수** | 별도 벡터 DB 없이 RAG 구축 가능 → 운영 단순화 |
| **공기업·금융권 호환성** | 오픈소스이면서도 Oracle 기능을 상당 부분 대체 |

### 기존 방식 vs PostgreSQL

```
[MySQL]
간단·빠르지만 트랜잭션 격리·복잡한 쿼리·확장성에서 한계

[PostgreSQL]
SQL 표준 준수도 + JSON/벡터/GIS 지원 + 풍부한 인덱스 종류(B-tree, GIN, GiST, BRIN, Hash)
```

## 🚀 2. 10분 퀵스타트

### 환경 준비 (Docker 권장)

```bash
docker run --name plaf-pg \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=plaf \
  -p 5432:5432 \
  -d postgres:16-alpine
```

### 검증

```bash
docker exec -it plaf-pg psql -U postgres -d plaf
```

```
psql (16.x)
Type "help" for help.

plaf=#
```

### 첫 테이블 + 데이터

```sql
-- 사용자 테이블
CREATE TABLE users (
    id          BIGSERIAL PRIMARY KEY,
    email       TEXT NOT NULL UNIQUE,
    nickname    TEXT NOT NULL,
    profile     JSONB,                       -- 유연한 스키마
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- 인덱스
CREATE INDEX idx_users_profile_gin ON users USING GIN (profile);

-- 데이터 삽입
INSERT INTO users (email, nickname, profile) VALUES
  ('alice@example.com', 'Alice', '{"role": "student", "major": "CS"}'),
  ('bob@example.com',   'Bob',   '{"role": "student", "major": "Math"}');

-- JSONB 쿼리
SELECT email, profile->>'major' AS major
FROM users
WHERE profile @> '{"role": "student"}';
```

예상 출력:
```
       email       | major
-------------------+-------
 alice@example.com | CS
 bob@example.com   | Math
(2 rows)
```

## 🛠️ 3. 코드 해부학: postgres/postgres 모노레포

| 경로 | 역할 |
|---|---|
| `src/backend/parser/` | SQL 파서 (gram.y, scan.l) |
| `src/backend/optimizer/` | 쿼리 플래너·옵티마이저 — `EXPLAIN`이 보여주는 그 결정을 만드는 곳 |
| `src/backend/executor/` | 실행기 — 노드 단위로 쿼리 실행 |
| `src/backend/access/` | 저장 엔진 (heap, B-tree, GIN, GiST 등 인덱스 구현) |
| `src/backend/storage/` | 버퍼·WAL(Write-Ahead Log) — 신뢰성의 핵심 |
| `contrib/` | 공식 확장(pg_stat_statements, postgres_fdw 등) |

!!! tip "초보자는 EXPLAIN부터"
    소스코드보다 먼저 **`EXPLAIN ANALYZE`** 사용법을 익히세요. 쿼리가 왜 느린지 알게 되면 인덱스·통계·플래너 동작이 자연스럽게 이해됩니다.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude (쿼리 튜닝)
```
/think 다음 PostgreSQL 쿼리가 평균 3초 이상 걸린다.
EXPLAIN ANALYZE 결과를 함께 제공할 테니
1) 병목 노드 식별
2) 인덱스 추가 후보 (컬럼·종류)
3) 쿼리 재작성안 (JOIN 순서, CTE/서브쿼리 변환)
4) 통계 갱신(ANALYZE) 필요성
순서로 분석해 줘.

[SQL + EXPLAIN ANALYZE 출력]
```

### 🔵 Gemini (데이터 모델링 비교)
```
"중고 거래 플랫폼"의 PostgreSQL 스키마를 설계할 때
정규화 vs JSONB 컬럼 사용을 어떻게 결정해야 하는지
구체적인 예시(상품 옵션, 사용자 설정)와 함께 설명해 줘.
인덱스 전략과 쿼리 패턴도 함께 비교해 줘.
```

### 🟢 ChatGPT (학습 로드맵)
```
나는 SELECT/WHERE/JOIN까지는 안다.
PostgreSQL을 4주 만에 "실무에서 쿼리 튜닝까지 할 수 있는 수준"으로 학습하려고 한다.
주차별: 학습 주제, 실습 SQL 예시, 검증 기준을 마크다운 표로 만들어 줘.
```

### ⬛ GitHub Copilot / Codex (IDE 실시간 보조)
```sql
-- TODO: 게시판 게시글 테이블에 풀텍스트 검색 인덱스 추가
--   - 컬럼: title, content
--   - 한국어/영어 동시 지원 (simple 또는 pg_bigm 검토)
--   - GIN 인덱스 + tsvector 트리거로 자동 갱신
```

## 🔗 5. 관련 레포 · 다음 단계

- **공식 문서**: [postgresql.org/docs](https://www.postgresql.org/docs/) — 가장 잘 쓴 DB 매뉴얼 중 하나
- **벡터 검색**: [pgvector](https://github.com/pgvector/pgvector) (RAG·임베딩 검색)
- **GIS**: [PostGIS](https://postgis.net)
- **시계열**: [TimescaleDB](https://github.com/timescale/timescaledb)
- **GUI 클라이언트**: [pgAdmin](https://www.pgadmin.org), [DBeaver](https://dbeaver.io), [TablePlus](https://tableplus.com)
- **튜닝 도구**: [pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html), [pgBadger](https://github.com/darold/pgbadger)
- **캐시 결합**: [Redis 딥다이브](../redis/index.md)
