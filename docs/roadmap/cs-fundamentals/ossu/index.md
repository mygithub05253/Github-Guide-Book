# 📘 OSSU Computer Science 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/ossu/computer-science.svg?style=social)](https://github.com/ossu/computer-science)

!!! info "레포지토리"
    **ossu/computer-science** · 180k+ ⭐ · MIT License · [Open Source Society University](https://github.com/ossu/computer-science)

---

## 🧐 1. OSSU Computer Science는 정확히 무엇이고, 누구에게 필요한가요?

**한 줄 요약**: OSSU는 **세계 최고 수준 대학(MIT, Harvard, Princeton, Stanford 등)의 무료 온라인 강의를 모아 "학사 학위 수준의 컴퓨터 과학 커리큘럼"으로 재구성한 자율 학습 가이드**입니다. 누구나 무료로, 본인의 페이스로 따라갈 수 있습니다.

### 핵심 특성

- **학위 수준 커리큘럼**: 입문 → 코어 CS → 고급 선택 → 최종 프로젝트로 이어지는 정규 학과 모방 구조.
- **무료 자료 우선**: Coursera audit 트랙, edX, MIT OCW 등 모두 무료로 수강 가능.
- **커뮤니티 학습**: Discord·GitHub Discussions에서 같은 단계 학생들과 진도·과제를 공유.
- **언어 무관**: 일반적으로 Python·C·JavaScript 등을 사용하지만, 핵심은 **개념과 사고력**.
- **자기 페이스**: 마감이 없으므로 직장인·재학생·비전공자 모두 적합.

### 커리큘럼 구조 (요약)

| 단계 | 내용 | 예시 강의 |
|---|---|---|
| **Intro CS** | 프로그래밍 입문 | Harvard CS50, MIT 6.0001 |
| **Core CS** | 자료구조·알고리즘·OS·네트워크·DB·이론 | MIT 6.006, OSTEP, CMU DB |
| **Advanced CS** | 컴파일러·분산 시스템·머신러닝·보안 | 학생 선택 |
| **Final Project** | 본인의 포트폴리오 프로젝트 | 자유 주제 |

### 비전공자에게 왜 필요한가?

| 비전공자가 자주 부딪히는 벽 | OSSU가 해결해 주는 것 |
|---|---|
| "코딩은 되는데 시간 복잡도가 뭔지 모르겠어" | Core CS의 자료구조·알고리즘 |
| "면접에서 OS·네트워크 질문에 막힘" | OSTEP, Computer Networking 강의 |
| "DB 설계를 어떻게 해야 할지 감이 없음" | CMU Intro to Database Systems |
| "내가 짠 코드가 왜 느린지 모름" | Computer Architecture, Performance 강의 |

### 기존 방식 vs OSSU

```
[부트캠프·온라인 강의 단편적 수강]
"React 강의 → Spring 강의 → AWS 강의" 식으로 도구만 학습 → 면접에서 CS 질문에 막힘

[OSSU]
"개념의 바닥부터" 위로 쌓아올림 → 새 기술이 등장해도 빠르게 흡수 가능
```

## 🚀 2. 10분 퀵스타트: 학습 시작하기

OSSU는 설치할 코드가 아니라 **학습 가이드**입니다. 시작 절차는 다음과 같습니다.

### 1단계: 레포 클론 (참고용)

```bash
git clone https://github.com/ossu/computer-science.git
cd computer-science
```

`README.md` 자체가 전체 커리큘럼 문서입니다.

### 2단계: 자신의 출발점 결정

| 현재 수준 | 추천 시작점 |
|---|---|
| 코딩 처음 | **Harvard CS50x** (영상이 가장 친절) |
| Python 기초 있음 | **MIT 6.0001 + 6.0002** (계산적 사고) |
| 코딩 경험 있고 CS 기초만 부족 | **Core CS 자료구조부터** 바로 시작 |

### 3단계: 학습 트래커 만들기

```bash
mkdir my-ossu-journey && cd my-ossu-journey
```

`progress.md`를 만들어 강의별 완료일·과제 링크를 기록하세요. GitHub에 공개하면 그 자체가 포트폴리오가 됩니다.

### 4단계: 커뮤니티 합류

- **OSSU Discord**: README의 초대 링크
- **#cs-general** 채널에서 질문·진도 공유

### 검증 (1주 차 체크리스트)

```
[ ] OSSU README 전체 1회 통독
[ ] 본인 출발점 강의 1개 결정
[ ] progress.md 작성 시작
[ ] CS50 Week 0 또는 MIT 6.0001 Lecture 1 시청 완료
[ ] Discord 가입 + 자기소개
```

## 🛠️ 3. 코드 해부학: 레포 구조

OSSU 레포 자체는 **마크다운 문서 모음**입니다.

| 경로 | 역할 |
|---|---|
| `README.md` | 전체 커리큘럼 가이드 (영문) |
| `intro-cs.md` | 입문 단계 강의 목록 |
| `extras/` | 추천 도서, 보너스 자료, FAQ |
| `coding-interviews.md` | 코딩 인터뷰 준비 자료 |
| `LICENSE` | MIT |

번역본도 있습니다 — `README-한국어.md` 또는 별도 fork 리포지토리를 검색해 보세요.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude (학습 계획 수립)
```
/think 나는 비전공 대학 3학년이고, 졸업까지 1.5년 남았다.
주당 15시간을 OSSU에 투자할 수 있다.
졸업 시점에 "코딩 인터뷰에서 자료구조·알고리즘·OS 질문에 답할 수 있는 수준"이 되도록
강의 순서·완료 목표일·중간 점검 기준을 포함한 학습 계획을 만들어 줘.
```

### 🔵 Gemini (강의 비교)
```
OSSU가 추천하는 알고리즘 강의(Princeton Algorithms vs Stanford Algorithms vs MIT 6.006)의
난이도, 사용 언어, 과제 양, 한국 학생 후기 측면에서 비교해 줘.
"Python만 아는 비전공자"에게 추천하는 1순위와 그 이유를 결론으로 제시해 줘.
```

### 🟢 ChatGPT (개념 질문)
```
나는 OSTEP의 "가상 메모리" 챕터를 읽고 있다.
페이지 테이블이 "왜" 필요한지 비유를 들어 설명해 줘.
그리고 이 개념이 실제 Linux 명령(`top`, `vmstat`, `/proc/meminfo`)에서
어떤 수치로 드러나는지 예시를 보여 줘.
```

### ⬛ GitHub Copilot / Codex (과제 코드 보조)
```python
# TODO: OSSU 자료구조 과제 - LRU Cache 구현
#   - capacity: int
#   - get(key): O(1)
#   - put(key, value): O(1)
#   - 자료구조: HashMap + Doubly Linked List
#   - 테스트: 10개 케이스 작성
```

## 🔗 5. 관련 레포 · 다음 단계

- **본 레포**: [ossu/computer-science](https://github.com/ossu/computer-science)
- **데이터 사이언스 트랙**: [ossu/data-science](https://github.com/ossu/data-science)
- **머신러닝 트랙**: [ossu/machine-learning](https://github.com/ossu/machine-learning)
- **코딩 인터뷰**: [Coding Interview University 딥다이브](../interview-university/index.md)
- **알고리즘 구현**: [The Algorithms 딥다이브](../algorithms/index.md)
- **시스템 디자인**: [System Design Primer 딥다이브](../system-design/index.md)
- **로드맵 시각화**: [Developer Roadmap 딥다이브](../roadmap/index.md)
- **본 가이드북**: [Part 1 · 개발 기초](../../../part1-foundation/index.md)
