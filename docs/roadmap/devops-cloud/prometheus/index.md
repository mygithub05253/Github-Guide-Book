# 📘 Prometheus 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/prometheus/prometheus.svg?style=social)](https://github.com/prometheus/prometheus)

!!! info "레포지토리"
    **prometheus/prometheus** · 56k+ ⭐ · Apache 2.0 · [prometheus.io](https://prometheus.io)

---

## 🧐 1. Prometheus는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Prometheus는 **시계열 데이터베이스 + 모니터링·알림 시스템**입니다. SoundCloud에서 시작해 CNCF의 대표 졸업 프로젝트가 되었으며, Kubernetes 모니터링의 사실상 표준입니다.

### 핵심 특성
- **Pull 모델**: Prometheus가 주기적으로 대상의 `/metrics` 엔드포인트를 긁어옴.
- **다차원 데이터 모델**: 메트릭에 레이블(label)을 붙여 유연한 쿼리.
- **PromQL**: 강력한 시계열 쿼리 언어.
- **Alertmanager**: 알림 규칙 → 이메일·Slack·PagerDuty.
- **Exporter 생태계**: node_exporter(서버), mysqld_exporter, blackbox_exporter 등.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **K8s 모니터링 표준** | kube-prometheus-stack Helm 차트 한 줄 설치 |
| **SRE 4 황금 시그널** | latency·traffic·errors·saturation 측정 |
| **Grafana와 환상의 콤비** | 시각화는 Grafana, 데이터는 Prometheus |

## 🚀 2. 10분 퀵스타트

```bash
docker run --rm -d --name prom -p 9090:9090 prom/prometheus
```

`http://localhost:9090` → 자기 자신의 메트릭을 즉시 조회 가능.

### 간단한 쿼리 예시
```promql
# 1분 평균 HTTP 요청 비율
rate(prometheus_http_requests_total[1m])

# 에러율
sum(rate(http_requests_total{status=~"5.."}[5m]))
  / sum(rate(http_requests_total[5m]))
```

### Spring Boot + Prometheus
1. `spring-boot-starter-actuator` + `micrometer-registry-prometheus` 추가
2. `application.yml`에 `management.endpoints.web.exposure.include=prometheus`
3. `/actuator/prometheus` 엔드포인트가 자동 노출됨
4. Prometheus `prometheus.yml`에 scrape 등록

## 🛠️ 3. 코드 해부학: prometheus.yml

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'spring-app'
    metrics_path: '/actuator/prometheus'
    static_configs:
      - targets: ['app:8080']

  - job_name: 'node'
    static_configs:
      - targets: ['node-exporter:9100']
```

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 우리 서비스에 SRE 4 황금 시그널을 적용하려고 한다.
PromQL 쿼리, Alertmanager 규칙, Grafana 대시보드 패널 구성을
"latency·traffic·errors·saturation" 4가지에 대해 작성해 줘.
```

### 🔵 Gemini
```
Prometheus vs Datadog vs New Relic vs Grafana Cloud를 비교해 줘.
오픈소스 자가호스팅 vs SaaS 관점에서 비용·기능·운영 부담.
```

### 🟢 ChatGPT
```
"Spring Boot 마이크로서비스 5개"의 모니터링 스택을 설계해 줘.
Prometheus + Grafana + Loki + Tempo 구성과 핵심 대시보드.
```

### ⬛ Copilot
```yaml
# TODO: alert rule - 5분 평균 5xx 에러율 1% 초과 시 critical 알림
```

## 🔗 5. 관련 레포 · 다음 단계
- 시각화: [Grafana](https://github.com/grafana/grafana)
- 로그: [Loki](https://github.com/grafana/loki) / 트레이싱: [Tempo](https://github.com/grafana/tempo)
- 차세대: [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics), [Mimir](https://github.com/grafana/mimir)
- [Kubernetes 딥다이브](../kubernetes/index.md)
