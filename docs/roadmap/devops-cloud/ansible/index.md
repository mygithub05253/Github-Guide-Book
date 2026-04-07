# 📘 Ansible 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/ansible/ansible.svg?style=social)](https://github.com/ansible/ansible)

!!! info "레포지토리"
    **ansible/ansible** · 62k+ ⭐ · GPL-3 · [ansible.com](https://www.ansible.com)

---

## 🧐 1. Ansible은 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Ansible은 **에이전트 없이 SSH만으로 수십~수천 대 서버에 동일한 설정·배포·운영 작업을 자동화하는 도구**입니다. YAML로 작성된 "Playbook"이 핵심입니다.

### 핵심 특성
- **에이전트리스**: 대상 서버에 별도 데몬 설치 불필요. SSH + Python만 있으면 됨.
- **선언형 YAML**: "이 패키지가 설치되어 있어야 한다" 방식으로 기술 → 멱등성 보장.
- **모듈 풍부**: 패키지·서비스·파일·클라우드·DB 등 수천 개 모듈.
- **인벤토리**: 호스트 그룹화 (`webservers`, `dbservers`).

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **레거시 서버 자동화** | VM·온프레미스 서버 운영 |
| **OS 설정 표준화** | 보안 패치, 사용자 계정, sshd 설정 |
| **K8s 전 단계** | 노드 프로비저닝, kubeadm 설치 |

## 🚀 2. 10분 퀵스타트

```bash
pip install ansible
```

```ini
# inventory.ini
[web]
192.168.1.10
192.168.1.11

[web:vars]
ansible_user=ubuntu
```

```yaml
# playbook.yml
- name: Nginx 설치 및 시작
  hosts: web
  become: true
  tasks:
    - name: Nginx 패키지 설치
      apt:
        name: nginx
        state: present
        update_cache: true

    - name: Nginx 서비스 시작·부팅 활성화
      service:
        name: nginx
        state: started
        enabled: true
```

```bash
ansible-playbook -i inventory.ini playbook.yml
```

## 🛠️ 3. 코드 해부학: Role 구조

```
roles/webserver/
├── tasks/main.yml
├── handlers/main.yml
├── templates/nginx.conf.j2
├── files/
├── vars/main.yml
└── defaults/main.yml
```

| 디렉터리 | 역할 |
|---|---|
| tasks | 실행 작업 목록 |
| handlers | 이벤트 기반 핸들러 (서비스 재시작 등) |
| templates | Jinja2 템플릿 |
| defaults | 기본 변수 (가장 낮은 우선순위) |

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 다음 Ansible playbook을 리뷰해 줘:
- 멱등성(같은 명령 두 번 실행해도 결과 동일)
- become/권한 최소화
- 비밀 정보 ansible-vault 처리
```

### 🔵 Gemini
```
Ansible vs Chef vs Puppet vs SaltStack의 차이점을 비교해 줘.
2026년 기준으로 신규 프로젝트에 어떤 것을 추천하는지 결론.
```

### 🟢 ChatGPT
```
"Ubuntu 서버 10대에 Docker + 모니터링 에이전트 + 보안 baseline"을
Ansible role로 설계해 줘.
```

### ⬛ Copilot
```yaml
# TODO: 사용자 계정 생성 + sudo 권한 + SSH 키 등록 task
```

## 🔗 5. 관련 레포 · 다음 단계
- 컬렉션 허브: [galaxy.ansible.com](https://galaxy.ansible.com)
- [Terraform 딥다이브](../terraform/index.md) (인프라 프로비저닝과 함께)
- 공식 문서: [docs.ansible.com](https://docs.ansible.com)
