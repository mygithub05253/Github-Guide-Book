# 📘 Elasticsearch 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/elastic/elasticsearch.svg?style=social)](https://github.com/elastic/elasticsearch)

!!! info "레포지토리"
    **elastic/elasticsearch** · 70k+ ⭐ · Elastic License v2 / SSPL · [elastic.co](https://www.elastic.co)

---

## 🧐 1. Elasticsearch는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Elasticsearch는 **Lucene 위에 구축된 분산 전문(full-text) 검색·분석 엔진**입니다. 로그 분석, 사이트 검색, 관측성(observability) 분야에서 사실상 표준입니다.

### 핵심 특성
- **역색인(Inverted Index)**: 일반 RDB가 못하는 전문 검색을 빠르게.
- **분산 아키텍처**: 샤드·레플리카로 자동 분산·복제.
- **JSON REST API**: 모든 작업이 HTTP+JSON.
- **풍부한 분석**: 집계(aggregation), 패싯, 지리 검색, 벡터 검색.
- **ELK/Elastic Stack**: Logstash(수집) + Elasticsearch(저장) + Kibana(시각화).

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **로그 검색·분석** | 수십억 줄 로그에서 즉시 검색 |
| **사이트 검색** | 한국어 형태소 분석기(nori) 활용 |
| **벡터 검색** | RAG·시맨틱 검색 |
| **APM·관측성** | Elastic APM과 통합 |

## 🚀 2. 10분 퀵스타트

```bash
docker run --rm -d --name es \
  -p 9200:9200 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  docker.elastic.co/elasticsearch/elasticsearch:8.13.0
```

```bash
# 1) 인덱스 생성 + 문서 색인
curl -X POST "localhost:9200/posts/_doc" -H 'Content-Type: application/json' -d '{
  "title": "PLAF 가이드북",
  "content": "GitHub 인기 레포지토리 활용 가이드",
  "tags": ["github", "guide"]
}'

# 2) 검색
curl "localhost:9200/posts/_search?q=가이드"
```

## 🛠️ 3. 코드 해부학: 핵심 개념

| 개념 | RDB 비유 |
|---|---|
| Index | 데이터베이스 |
| Document | 행(row), JSON |
| Field | 컬럼 |
| Mapping | 스키마 |
| Shard | 파티션 |
| Replica | 복제본 |

### 한국어 검색을 위한 nori 분석기
```json
PUT /korean_posts
{
  "settings": {
    "analysis": {
      "analyzer": {
        "nori_analyzer": {
          "type": "custom",
          "tokenizer": "nori_tokenizer"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "content": { "type": "text", "analyzer": "nori_analyzer" }
    }
  }
}
```

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 우리 서비스 검색 결과 품질을 높이려고 한다.
- 한국어 분석기(nori) 설정
- 동의어 사전
- BM25 파라미터 튜닝
- 멀티 매치 + 필드 부스팅
- function_score로 인기도 가중
설계와 매핑 예시를 작성해 줘.
```

### 🔵 Gemini
```
Elasticsearch vs OpenSearch vs Meilisearch vs Typesense를 비교해 줘.
라이선스, 한국어 지원, 학습 곡선, 호스팅 옵션 기준.
```

### 🟢 ChatGPT
```
"중고 거래 앱"의 상품 검색 기능을 Elasticsearch로 설계해 줘.
매핑, 색인 파이프라인, 검색 쿼리(필터 + 정렬), 자동완성 포함.
```

### ⬛ Copilot
```json
// TODO: 게시글 인덱스 매핑 - title(text+nori), content(text+nori), tags(keyword), created_at(date)
```

## 🔗 5. 관련 레포 · 다음 단계
- 포크: [OpenSearch](https://github.com/opensearch-project/OpenSearch) (AWS 주도, Apache 2.0)
- 시각화: [Kibana](https://github.com/elastic/kibana)
- 로그 수집: [Logstash](https://github.com/elastic/logstash), [Fluent Bit](https://github.com/fluent/fluent-bit)
- 경량 검색: [Meilisearch](https://github.com/meilisearch/meilisearch), [Typesense](https://github.com/typesense/typesense)
