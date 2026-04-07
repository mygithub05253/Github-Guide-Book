# 📘 Developer Roadmap 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/kamranahmedse/developer-roadmap.svg?style=social)](https://github.com/kamranahmedse/developer-roadmap)

!!! info "레포지토리"
    **kamranahmedse/developer-roadmap** · 290k+ ⭐ · 비독점 라이선스 · [roadmap.sh](https://roadmap.sh)

---

## 🧐 1. Developer Roadmap은 무엇이고, 어떻게 쓰이나요?

**한 줄 요약**: Developer Roadmap은 **"어떤 개발자가 되려면 무엇을 어떤 순서로 배워야 하는가"를 시각적 트리 다이어그램으로 정리한 가장 인기 있는 학습 가이드**입니다. 본 PLAF 가이드북의 카테고리 분류 기준이기도 합니다.

### 핵심 특성
- **40+ 로드맵**: Frontend, Backend, DevOps, Full Stack, AI, Data Analyst, Android, iOS, Game Dev, Blockchain 등.
- **인터랙티브 학습**: roadmap.sh에서 클릭하면 각 노드별 학습 자료 제공.
- **체크리스트**: 진도 관리 가능.
- **숙련도 표시**: "필수 / 선택 / 추천 안 함" 색상 구분.
- **AI 멘토 (유료)**: 각 노드에 대한 질문을 LLM에게 물어볼 수 있음.

### 사용 시나리오
| 상황 | 활용법 |
|---|---|
| 진로 선택 고민 | 모든 로드맵을 둘러본 뒤 끌리는 것 선택 |
| 신입 학습 우선순위 | 필수 노드만 1차로 끝내기 |
| 면접 준비 | 로드맵 노드별로 자가 점검 |
| 사이드 프로젝트 | 부족한 노드를 채우기 위한 미니 프로젝트 |

## 🚀 2. 10분 퀵스타트

### 1단계: 본인 트랙 선택
[roadmap.sh](https://roadmap.sh) 접속 → Role-based Roadmaps에서 본인 진로 선택.

추천 시작점:
- 풀스택 지망 → **Full Stack**
- 백엔드 집중 → **Backend** + **DevOps**
- AI 분야 → **AI Engineer** 또는 **AI Data Scientist**
- 데이터 → **Data Analyst** + **Data Engineer**

### 2단계: 진도 체크 시작
계정 생성 후 각 노드를 클릭하면 진도 저장됨. GitHub 레포 fork도 가능.

### 3단계: PLAF 가이드북과 매핑
| roadmap.sh 노드 | PLAF 딥다이브 |
|---|---|
| React | [딥다이브](../../frontend/react/index.md) |
| Spring Boot | [딥다이브](../../backend/springboot/index.md) |
| Kubernetes | [딥다이브](../../devops-cloud/kubernetes/index.md) |
| LangChain | [딥다이브](../../ai-ml/langchain/index.md) |

본 가이드북의 [로드맵 포털](../../index.md)이 정확히 이 매핑을 자동화한 것입니다.

## 🛠️ 3. 코드 해부학: 레포 구조

```
developer-roadmap/
├── src/
│   ├── data/roadmaps/     # 각 로드맵 JSON 정의
│   └── components/        # 시각화 컴포넌트 (Astro)
├── public/                # 정적 이미지
└── content/               # 노드별 콘텐츠
```

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 나는 비전공 대학 2학년이고 풀스택 백엔드를 목표로 한다.
roadmap.sh의 Backend 로드맵에서 "졸업 전 반드시" / "취업 후 학습" 노드로
구분해 우선순위 학습 계획을 만들어 줘.
```

### 🔵 Gemini
```
roadmap.sh의 Frontend, Backend, DevOps 로드맵을 비교해
"풀스택 개발자가 되기 위해 공통적으로 필요한 노드 Top 20"을 추출해 줘.
```

### 🟢 ChatGPT
```
나는 Spring Boot, React를 안다.
roadmap.sh Backend 로드맵에서 내가 모르는 노드를 식별하고
6개월 학습 계획을 짜 줘. 각 노드에 대해 학습 자료 1개씩 추천.
```

### ⬛ Copilot
```
// 사용 사례 외 - 학습 트래커 포맷 제안 등에 활용
```

## 🔗 5. 관련 레포 · 다음 단계
- 본 사이트: [roadmap.sh](https://roadmap.sh)
- [OSSU 딥다이브](../ossu/index.md) — CS 학사 수준 보완
- [Coding Interview University 딥다이브](../interview-university/index.md)
- [System Design Primer 딥다이브](../system-design/index.md)
