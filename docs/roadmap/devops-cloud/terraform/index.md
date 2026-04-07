# 📘 Terraform 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/hashicorp/terraform.svg?style=social)](https://github.com/hashicorp/terraform)

!!! info "레포지토리"
    **hashicorp/terraform** · 43k+ ⭐ · BUSL-1.1 · [terraform.io](https://www.terraform.io)

---

## 🧐 1. Terraform은 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Terraform은 **클라우드 인프라(서버·DB·네트워크 등)를 코드(HCL 언어)로 선언적으로 관리하는 IaC(Infrastructure as Code) 도구**입니다. AWS·GCP·Azure·Cloudflare 등 수천 개의 Provider를 동일한 워크플로우로 다룹니다.

### 핵심 개념
- **선언형 HCL**: "원하는 상태"를 기술 → Terraform이 차이만 적용.
- **State 파일**: 현재 인프라의 실제 상태를 추적 (S3·Terraform Cloud에 원격 저장).
- **Provider**: 클라우드별 어댑터 (`aws`, `google`, `kubernetes` 등).
- **Module**: 재사용 가능한 인프라 컴포넌트.
- **Plan / Apply**: 변경사항 미리보기 → 승인 후 적용.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **재현 가능한 인프라** | 개발·스테이징·운영 동일하게 |
| **변경 이력 추적** | Git 커밋 = 인프라 변경 이력 |
| **멀티 클라우드** | 동일 도구로 여러 클라우드 관리 |
| **GitOps 기반** | PR 리뷰 → 인프라 변경 |

## 🚀 2. 10분 퀵스타트

### 설치
```bash
# macOS
brew install terraform

# 검증
terraform -v
```

### 첫 모듈: 로컬 파일 생성
```hcl
# main.tf
terraform {
  required_providers {
    local = { source = "hashicorp/local", version = "~> 2.5" }
  }
}

resource "local_file" "hello" {
  content  = "Hello PLAF from Terraform!"
  filename = "${path.module}/hello.txt"
}
```

```bash
terraform init       # provider 다운로드
terraform plan       # 변경 미리보기
terraform apply      # 적용 (yes 입력)
cat hello.txt
terraform destroy    # 정리
```

### AWS S3 버킷 예제
```hcl
provider "aws" {
  region = "ap-northeast-2"
}

resource "aws_s3_bucket" "plaf_assets" {
  bucket = "plaf-assets-${random_id.suffix.hex}"
}

resource "random_id" "suffix" {
  byte_length = 4
}
```

## 🛠️ 3. 코드 해부학: 권장 디렉터리

```
infra/
├── main.tf          # 리소스 정의
├── variables.tf     # 입력 변수
├── outputs.tf       # 출력 값
├── providers.tf     # provider 설정
├── backend.tf       # state 원격 저장 (S3+DynamoDB)
└── modules/
    ├── vpc/
    └── eks/
```

!!! warning "초보자 함정"
    - **State 파일을 절대 Git에 커밋하지 마세요** (시크릿 포함). 원격 백엔드 사용.
    - `terraform apply` 전에 반드시 `plan` 검토.
    - 인스턴스 직접 콘솔 수정 금지 → drift 발생.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 다음 Terraform 모듈을 리뷰해 줘:
- 변수·출력 명확성
- 보안 그룹 최소 권한
- 태그 일관성
- backend 설정 누락
- destroy 시 데이터 손실 위험
```

### 🔵 Gemini
```
Terraform vs Pulumi vs AWS CDK vs CloudFormation을 비교 표로 정리해 줘.
언어, 멀티 클라우드, 학습 곡선, 채용 시장 기준.
```

### 🟢 ChatGPT
```
"AWS에 EKS 클러스터 + RDS PostgreSQL + ALB"를 Terraform 모듈로 설계해 줘.
변수, 출력, 환경별 분리(dev/prod) 구조 포함.
```

### ⬛ Copilot
```hcl
# TODO: VPC 모듈 - public/private 서브넷 3 AZ, NAT Gateway, 라우팅 테이블
```

## 🔗 5. 관련 레포 · 다음 단계
- 모듈 레지스트리: [registry.terraform.io](https://registry.terraform.io)
- 정책: [OPA](https://www.openpolicyagent.org), [Sentinel](https://www.hashicorp.com/sentinel)
- 차세대/포크: [OpenTofu](https://opentofu.org)
- [Kubernetes 딥다이브](../kubernetes/index.md)
