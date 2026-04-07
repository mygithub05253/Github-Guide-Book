# 📘 Docker / Compose 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/docker/compose.svg?style=social)](https://github.com/docker/compose)

!!! info "레포지토리"
    **docker/compose** · 35k+ ⭐ · Apache 2.0 · [docs.docker.com](https://docs.docker.com)

---

## 🧐 1. Docker는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Docker는 **애플리케이션과 그 의존성을 "컨테이너"라는 격리된 경량 패키지로 묶어, 어디서나 동일하게 실행할 수 있게 하는 기술**입니다. "내 컴퓨터에선 됐는데..." 문제를 근본적으로 해결합니다.

### 핵심 개념
- **이미지(Image)**: 컨테이너의 청사진. `Dockerfile`로 정의.
- **컨테이너(Container)**: 이미지의 실행 인스턴스.
- **레지스트리(Registry)**: 이미지 저장소 (Docker Hub, GHCR).
- **볼륨(Volume)**: 컨테이너 외부 영속 저장소.
- **네트워크(Network)**: 컨테이너 간 통신.
- **Compose**: 여러 컨테이너를 YAML로 한 번에 정의·실행.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **개발 환경 통일** | 신입이 첫 날에 `docker compose up`만 치면 됨 |
| **CI/CD 표준** | GitHub Actions·GitLab CI 모두 컨테이너 기반 |
| **마이크로서비스 기반** | Kubernetes의 전제 조건 |
| **로컬 인프라 시뮬레이션** | DB·캐시·메시지 큐를 한 줄로 띄움 |

## 🚀 2. 10분 퀵스타트

### 첫 Dockerfile
```dockerfile
# Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

```bash
docker build -t plaf-app:1.0 .
docker run --rm -p 3000:3000 plaf-app:1.0
```

### Compose로 풀스택 띄우기
```yaml
# compose.yml
services:
  api:
    build: .
    ports: ["3000:3000"]
    environment:
      DATABASE_URL: postgres://postgres:secret@db:5432/plaf
    depends_on: [db]

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: plaf
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine

volumes:
  pgdata:
```

```bash
docker compose up -d
docker compose logs -f api
docker compose down
```

## 🛠️ 3. 코드 해부학: Dockerfile 모범 사례

| 패턴 | 효과 |
|---|---|
| **멀티 스테이지 빌드** | 빌드 도구는 최종 이미지에서 제외 → 크기 80% 감소 |
| **`.dockerignore`** | `node_modules`, `.git` 제외 → 빌드 속도·캐시 개선 |
| **레이어 캐시 활용** | `COPY package.json` → `RUN npm ci` 먼저 → 코드 변경에도 의존성 캐시 유지 |
| **non-root 사용자** | `USER node` 추가로 보안 강화 |
| **태그 고정** | `node:20.11-alpine` (latest 금지) |

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 다음 Dockerfile을 리뷰해 줘:
- 멀티 스테이지 적용 가능성
- 레이어 캐시 최적화
- 보안(non-root, 최소 권한)
- 이미지 크기
수정된 Dockerfile 제시.
```

### 🔵 Gemini
```
Docker Compose vs Kubernetes를 "스타트업 5명 팀의 백엔드 운영" 관점에서 비교해 줘.
언제 Compose에 머물러야 하고 언제 K8s로 가야 하는지.
```

### 🟢 ChatGPT
```
"Spring Boot + PostgreSQL + Redis + Nginx" 풀스택 앱의 compose.yml을 작성해 줘.
healthcheck, depends_on, .env 분리, 운영용 override 파일 포함.
```

### ⬛ Copilot
```dockerfile
# TODO: Python FastAPI 멀티 스테이지 Dockerfile - poetry 의존성 빌드 분리
```

## 🔗 5. 관련 레포 · 다음 단계
- [Kubernetes 딥다이브](../kubernetes/index.md)
- 경량 이미지: [distroless](https://github.com/GoogleContainerTools/distroless)
- 보안 스캔: [Trivy](https://github.com/aquasecurity/trivy)
- 빌드 가속: [BuildKit](https://github.com/moby/buildkit), [Buildx](https://github.com/docker/buildx)
