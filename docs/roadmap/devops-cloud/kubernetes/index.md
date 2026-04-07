# 📘 Kubernetes 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/kubernetes/kubernetes.svg?style=social)](https://github.com/kubernetes/kubernetes)

!!! info "레포지토리"
    **kubernetes/kubernetes** · 110k+ ⭐ · Apache 2.0 · [kubernetes.io](https://kubernetes.io)

---

## 🧐 1. Kubernetes는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Kubernetes(K8s)는 **컨테이너화된 애플리케이션의 배포·확장·운영을 자동화하는 오픈소스 오케스트레이션 시스템**입니다. Google 내부 Borg 시스템에서 출발해 현재 클라우드 네이티브의 사실상 표준이 되었습니다.

### 핵심 특성

- **선언형 API**: "원하는 상태(desired state)"를 YAML로 작성하면 K8s가 현재 상태와 비교해 자동으로 맞춤. 명령형 스크립트가 아닌 GitOps 방식의 핵심.
- **셀프 힐링**: 컨테이너가 죽으면 자동으로 재시작, 노드가 죽으면 다른 노드로 옮김.
- **수평 확장**: 트래픽이 늘면 Pod 수를 자동 증가(HPA), 노드 자체도 자동 추가(Cluster Autoscaler).
- **서비스 디스커버리·로드밸런싱**: Service 리소스가 자동으로 DNS 이름과 가상 IP를 부여.
- **롤링 업데이트·롤백**: 무중단 배포가 기본. 문제 발생 시 한 줄로 이전 버전 복원.

### 주요 개념(리소스)

| 리소스 | 역할 | 비유 |
|---|---|---|
| **Pod** | 1개 이상 컨테이너의 실행 단위 | 컨테이너의 "방" |
| **Deployment** | Pod의 원하는 상태 선언 (replicas, image, 업데이트 전략) | 매니저 |
| **Service** | Pod 집합에 안정적인 IP/DNS 부여 | 로드밸런서 |
| **Ingress** | 외부 HTTP 트래픽을 Service로 라우팅 | 리버스 프록시 |
| **ConfigMap / Secret** | 환경설정·민감정보를 컨테이너에 주입 | .env 파일 |
| **PersistentVolume** | 컨테이너가 죽어도 보존되는 저장소 | 외장 디스크 |

### 실무 도입 포인트

| 도입 이유 | 구체적 효과 |
|---|---|
| **무중단 배포 표준** | 롤링 업데이트로 사용자 영향 없이 새 버전 출시 |
| **멀티 클라우드 호환** | AWS EKS, GCP GKE, Azure AKS 어디서나 동일한 매니페스트 |
| **마이크로서비스 운영** | 수십 개 서비스의 의존성·네트워크·스케일링을 한 곳에서 관리 |
| **공기업·금융권 인프라 현대화** | 컨테이너 기반 PaaS 도입 트렌드 → 채용 시장 수요 급증 |

### 기존 방식 vs Kubernetes

```
[기존 (가상머신 + 수동 배포)]
스크립트로 SSH 접속 → 코드 복사 → 서버 재시작 → 헬스체크 수동 확인
서버 1대 죽으면 새벽에 알람 → 사람이 손으로 복구

[Kubernetes]
kubectl apply -f deploy.yaml 한 줄 → K8s가 알아서 배포·복구·확장
```

## 🚀 2. 10분 퀵스타트

!!! warning "프로덕션 K8s ≠ 학습용 K8s"
    실제 클러스터는 복잡합니다. 학습은 **로컬 단일 노드 K8s**(minikube, kind, Docker Desktop)로 시작하세요.

### 환경 준비 (옵션 A: Docker Desktop)

1. [Docker Desktop](https://www.docker.com/products/docker-desktop/) 설치
2. Settings → Kubernetes → **Enable Kubernetes** 체크 → Apply

### 환경 준비 (옵션 B: kind)

```bash
# kind 설치 (macOS)
brew install kind kubectl

# Windows (Chocolatey)
choco install kind kubernetes-cli

# 클러스터 생성
kind create cluster --name plaf-demo
```

### 검증

```bash
kubectl version --short
kubectl get nodes
```

예상 출력:
```
NAME                    STATUS   ROLES           AGE   VERSION
plaf-demo-control-plane Ready    control-plane   1m    v1.30.x
```

### 첫 Deployment + Service

```yaml
# nginx-demo.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-demo
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-demo
  template:
    metadata:
      labels:
        app: nginx-demo
    spec:
      containers:
        - name: nginx
          image: nginx:1.27-alpine
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-demo
spec:
  type: NodePort
  selector:
    app: nginx-demo
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
```

```bash
kubectl apply -f nginx-demo.yaml
kubectl get pods -w        # 3개 Pod이 Running 상태로 변경되는지 확인
kubectl get svc nginx-demo
```

브라우저: `http://localhost:30080` → Nginx Welcome 페이지.

## 🛠️ 3. 코드 해부학: kubernetes/kubernetes 모노레포

거대한 모노레포(1500만 줄+)지만 핵심은 다음 디렉터리입니다.

| 경로 | 역할 |
|---|---|
| `cmd/kube-apiserver/` | API 서버 진입점. 모든 명령이 여기서 시작 |
| `pkg/scheduler/` | Pod을 어느 노드에 배치할지 결정하는 스케줄러 |
| `pkg/controller/` | Deployment, ReplicaSet 등 컨트롤러 루프 (desired vs current 비교) |
| `pkg/kubelet/` | 각 노드에서 컨테이너를 실제로 띄우는 에이전트 |
| `staging/src/k8s.io/api/` | 모든 리소스의 Go 타입 정의 (Pod, Deployment 등) |

!!! tip "초보자는 소스코드보다 공식 튜토리얼"
    K8s 소스코드는 K8s를 **만들고 싶을 때** 보는 것입니다. **사용하는 법**을 배우려면 [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/)부터 끝까지 따라하세요.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude (매니페스트 리뷰)
```
/think 다음 Kubernetes Deployment 매니페스트를 production-readiness 관점에서 리뷰해 줘:
- Resource limits/requests 누락
- liveness/readiness probe 누락
- 보안 컨텍스트(non-root, readOnlyRootFilesystem)
- ImagePullPolicy, ImageTag 고정 여부
- HPA 추천 여부
지적 후 수정된 YAML을 제시해 줘.

[YAML 붙여넣기]
```

### 🔵 Gemini (개념 비교)
```
Kubernetes의 Deployment, StatefulSet, DaemonSet, Job, CronJob의 차이를
"언제 어떤 것을 써야 하는가" 관점에서 비교 표로 정리해 줘.
각 워크로드 타입의 실제 사용 예시(예: PostgreSQL, Prometheus, 백업 스크립트)를 함께 제시해 줘.
```

### 🟢 ChatGPT (학습 로드맵)
```
나는 Spring Boot로 백엔드를 만들 줄 안다.
이 앱을 Docker로 컨테이너화하고 Kubernetes에 배포하는 4주 학습 로드맵을 짜 줘.
주차별 목표, 실습 리소스(Deployment/Service/Ingress/HPA),
취업 면접에서 어필할 수 있는 결과물을 포함해 줘.
```

### ⬛ GitHub Copilot / Codex (IDE 실시간 보조)
```yaml
# TODO: Spring Boot 앱(이미지 myapp:1.0.0)을 위한 K8s 리소스
#   - Deployment: replicas 3, resource limits 512Mi/500m
#   - Service: ClusterIP, port 8080
#   - Ingress: host plaf.example.com, TLS via cert-manager
#   - HPA: CPU 70% 기준, min 3, max 10
```

## 🔗 5. 관련 레포 · 다음 단계

- **공식 문서**: [kubernetes.io/docs](https://kubernetes.io/docs)
- **로컬 클러스터**: [kind](https://kind.sigs.k8s.io), [minikube](https://minikube.sigs.k8s.io), [k3d](https://k3d.io)
- **패키지 매니저**: [Helm](https://helm.sh) (K8s의 npm)
- **GitOps**: [ArgoCD](https://argo-cd.readthedocs.io), [Flux](https://fluxcd.io)
- **모니터링**: [Prometheus 딥다이브](../prometheus/index.md)
- **컨테이너 빌드**: [Docker 딥다이브](../docker/index.md)
- **IaC로 클러스터 관리**: [Terraform 딥다이브](../terraform/index.md)
