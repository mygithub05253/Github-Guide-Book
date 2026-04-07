# 📘 Apache Kafka 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/apache/kafka.svg?style=social)](https://github.com/apache/kafka)

!!! info "레포지토리"
    **apache/kafka** · 28k+ ⭐ · Apache 2.0 · [kafka.apache.org](https://kafka.apache.org)

---

## 🧐 1. Kafka는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Apache Kafka는 **고처리량·내결함성을 갖춘 분산 이벤트 스트리밍 플랫폼**입니다. LinkedIn에서 시작되어 현재 거의 모든 빅데이터·MSA 아키텍처의 백본 역할을 합니다.

### 핵심 개념
- **Topic**: 메시지의 카테고리. 파티션으로 분할.
- **Partition**: 순서가 보장되는 로그 단위. 병렬성·확장성의 핵심.
- **Producer / Consumer**: 메시지 발행자/구독자.
- **Consumer Group**: 같은 그룹의 컨슈머가 파티션을 나눠 소비.
- **Broker**: Kafka 서버 노드.
- **Offset**: 컨슈머가 어디까지 읽었는지 추적.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **마이크로서비스 통신** | 비동기·결합도 낮춤 |
| **이벤트 소싱** | 모든 변경을 이벤트로 기록 |
| **로그 수집 파이프라인** | 앱 → Kafka → ES/DW |
| **실시간 분석** | Kafka Streams, Flink 연동 |

## 🚀 2. 10분 퀵스타트

```yaml
# compose.yml (KRaft 모드, ZooKeeper 없이)
services:
  kafka:
    image: bitnami/kafka:3.7
    ports:
      - "9092:9092"
    environment:
      KAFKA_CFG_NODE_ID: 1
      KAFKA_CFG_PROCESS_ROLES: controller,broker
      KAFKA_CFG_LISTENERS: PLAINTEXT://:9092,CONTROLLER://:9093
      KAFKA_CFG_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_CFG_CONTROLLER_QUORUM_VOTERS: 1@kafka:9093
      KAFKA_CFG_CONTROLLER_LISTENER_NAMES: CONTROLLER
```

```bash
docker compose up -d

# 토픽 생성
docker compose exec kafka kafka-topics.sh --create \
  --topic plaf-events --bootstrap-server localhost:9092

# 프로듀서
docker compose exec kafka kafka-console-producer.sh \
  --topic plaf-events --bootstrap-server localhost:9092
> hello plaf

# 컨슈머 (다른 터미널)
docker compose exec kafka kafka-console-consumer.sh \
  --topic plaf-events --from-beginning --bootstrap-server localhost:9092
```

## 🛠️ 3. 코드 해부학: Spring Boot 예제

```java
// Producer
@Service
@RequiredArgsConstructor
public class EventPublisher {
    private final KafkaTemplate<String, String> kafka;

    public void publish(String key, String payload) {
        kafka.send("plaf-events", key, payload);
    }
}

// Consumer
@Component
public class EventListener {
    @KafkaListener(topics = "plaf-events", groupId = "plaf-app")
    public void onMessage(ConsumerRecord<String, String> record) {
        log.info("Received: key={}, value={}", record.key(), record.value());
    }
}
```

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 우리 MSA에 Kafka를 도입하려고 한다:
- 토픽 네이밍 컨벤션
- 파티션 키 설계
- 컨슈머 그룹 전략
- exactly-once vs at-least-once 선택
- 스키마 관리(Avro/Protobuf + Schema Registry)
```

### 🔵 Gemini
```
Kafka vs RabbitMQ vs Redis Streams vs AWS SQS/SNS를 비교 표로.
처리량, 메시지 순서, 영속성, 운영 복잡도 기준.
```

### 🟢 ChatGPT
```
"전자상거래 주문 처리"를 Kafka 기반 이벤트 드리븐으로 설계해 줘.
토픽 목록, 이벤트 스키마, 컨슈머 서비스, Saga 패턴 포함.
```

### ⬛ Copilot
```java
// TODO: KafkaListenerContainerFactory - manual ack, retry, DLQ
```

## 🔗 5. 관련 레포 · 다음 단계
- Kafka 대안: [Redpanda](https://github.com/redpanda-data/redpanda) (C++ 재구현)
- 스트림 처리: [Kafka Streams](https://kafka.apache.org/documentation/streams/), [Apache Flink](https://github.com/apache/flink)
- UI: [Kafka UI](https://github.com/provectus/kafka-ui), [Conduktor](https://www.conduktor.io)
