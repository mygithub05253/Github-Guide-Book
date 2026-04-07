# 1-1. CS 기초 다지기

> 컴퓨터 과학을 정식으로 배우지 않았어도 괜찮아요. 전 세계 비전공자들이 검증한
> "무료로 대학 수준의 CS를 배우는 길"이 이미 존재합니다. 이 챕터에서 안내해 드릴게요.

!!! info "📌 핵심 요약"
    - **ossu/computer-science** — 4년 대학 커리큘럼을 무료로 압축 제공
    - **developer-roadmap** — 내 진로의 "지도"를 시각적으로 확인
    - **coding-interview-university** — 대기업 면접 준비의 바이블

---

## ossu/computer-science (178K+ Stars)

**링크**: https://github.com/ossu/computer-science

**한 줄 소개**: 전 세계 비전공자 학습자를 위한 완전한 무료 컴퓨터 과학 커리큘럼.
**왜 봐야 하는가**: 대학 4년 커리큘럼에 준하는 과목을 무료로 따라갈 수 있고, Google/Microsoft 엔지니어들이 추천하는 검증된 자료만 모아놨습니다.
**난이도**: ⭐⭐⭐⭐

### 📋 이 레포가 다루는 내용

- 180주 분량의 체계적 학습 경로 (주당 30~40시간 투자 기준)
- Fundamentals → Core → Advanced → Specialization 4단계
- 대부분 영어 강좌이지만 일부는 한국어 자막 제공
- 각 과목마다 **"왜 배워야 하는지"** 이유가 명시되어 있음

### 🚀 15분 퀵스타트

1단계. 레포 클론하고 구조 파악하기

```bash
git clone https://github.com/ossu/computer-science.git
cd computer-science
```

2단계. README에서 "Curriculum" 섹션을 찾아 전체 지도를 확인합니다.

```bash
# Windows (PowerShell/Git Bash)
code README.md
```

예상 출력 (README 내 테이블):

```
| Courses                                               | Duration   | Effort     |
| ----------------------------------------------------- | ---------- | ---------- |
| Introduction to Computer Science and Programming ...  | 9 weeks    | 15 hrs/wk  |
| Mathematics for Computer Science                      | 13 weeks   | 5 hrs/wk   |
```

3단계. 아래 "비전공자 추천 4단계"를 기준으로 내 위치 정하기

| 단계 | 예상 기간 | 핵심 과목 | 학습량 |
|------|---------|---------|-------|
| 1단계: 기초 | 12주 | Programming (Python), Math Foundations | 낮음 |
| 2단계: 핵심 | 24주 | Data Structures, Algorithms, Database | 중간 |
| 3단계: 심화 | 16주 | OS, Networks, Compilers | 높음 |
| 4단계: 전공선택 | 12주 | ML, Security, Distributed Systems 중 1개 | 매우 높음 |

!!! tip "💡 꿀팁: CS50부터 시작하세요"
    OSSU 초반에 나오는 **MIT/Harvard CS50**은 전 세계 1위 인기 강좌입니다.
    "한글 자막 + 과제 자동 채점(check50)"이 지원되어 비전공자에게 최고의 첫걸음입니다.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "OSSU CS 커리큘럼의 README를 읽고, 내가 주당 15시간 투자할 수 있는 비전공자라고 가정할 때 가장 효과적인 6개월 학습 계획을 표로 만들어줘."

!!! example "🤖 Claude Code 프롬프트"
    > "OSSU Core CS 섹션에서 'Data Structures' 과목을 듣고 있어. 각 주차별로 풀어볼 Python 연습 문제 3개씩 만들어줘. 난이도는 LeetCode Easy 수준으로."

!!! example "🤖 Claude Code 프롬프트"
    > "CS50 Week 3 (Algorithms) 강의를 막 봤어. 핵심 개념을 내 말로 설명할 수 있는지 퀴즈 10개를 만들어줘."

### 📚 학습 체크리스트

- [ ] OSSU 레포 클론 및 README 완독
- [ ] 4단계 중 "1단계: 기초" 완료
- [ ] CS50 Problem Set 5개 이상 제출
- [ ] 자료구조(스택/큐/링크드리스트) 직접 구현
- [ ] OSSU Discord 한국어 채널 참여

!!! warning "⚠️ 자주 하는 실수"
    **"모든 과목을 다 들어야 한다"고 생각하는 것.**
    OSSU는 "지도"일 뿐입니다. 목표에 맞는 과목만 골라 들어도 충분합니다.
    풀스택 개발자가 목표라면 Compilers나 OS 심화는 나중에 들어도 돼요.

---

## kamranahmedse/developer-roadmap (310K+ Stars)

**링크**: https://github.com/kamranahmedse/developer-roadmap

**한 줄 소개**: 개발자 진로별 기술 스택을 시각적으로 정리한 "지도".
**왜 봐야 하는가**: "Frontend 개발자가 되려면 뭘 배워야 해?" 같은 막연한 질문에 대한 명확한 답이 그림으로 들어있습니다.
**난이도**: ⭐ (초보 친화)

### 📋 이 레포가 다루는 내용

- Frontend / Backend / DevOps / Full Stack / Android / iOS 등 진로별 로드맵
- 각 항목마다 **"Personal Recommendation(노란색) vs Alternative(회색)"** 구분
- SQL, Git, Docker 등 **스킬별 세부 로드맵**
- 인터랙티브 웹사이트: https://roadmap.sh

### 🚀 15분 퀵스타트

1단계. 웹사이트 방문 → 본인에게 맞는 로드맵 선택

```
https://roadmap.sh/frontend   # 프론트엔드
https://roadmap.sh/backend    # 백엔드
https://roadmap.sh/full-stack # 풀스택
```

2단계. 로드맵을 PDF로 다운로드해서 벽에 붙여놓기 (각 페이지 우측 상단 Download 버튼)

3단계. 현재 내가 아는 것과 모르는 것에 색깔로 체크하기 (웹에서 체크박스 클릭)

!!! tip "💡 꿀팁: 로드맵 활용의 3원칙"
    1. **Essential(필수)만 먼저**: 노란색 네모부터 정복
    2. **주제당 40~60시간 할당**: 주 20시간 기준 2~3주
    3. **체크 후 포기**: 중요도 낮은 건 과감히 Skip

### 📊 Frontend 로드맵 예시

```
Frontend Developer Path
├── 1단계: HTML → CSS → JavaScript 기초 (3주)
├── 2단계: npm, Git, VS Code (1주)
├── 3단계: CSS 프레임워크 (Tailwind) (1주)
├── 4단계: JavaScript 심화 (DOM, Fetch) (2주)
└── 5단계: React 또는 Vue (4주)
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트"
    > "developer-roadmap의 Backend 로드맵을 보고, 내가 Java/Spring Boot 취업 목표라면 어떤 노드를 먼저 공부해야 할지 우선순위 Top 10을 매겨줘."

!!! example "🤖 Claude Code 프롬프트"
    > "나는 HTML/CSS/JS 기초만 알아. Frontend 로드맵에서 '다음으로 배워야 할 것' 3가지를 각각 왜 배워야 하는지와 함께 추천해줘."

!!! example "🤖 Claude Code 프롬프트"
    > "Full Stack 로드맵을 주 20시간 학습 기준 6개월 계획표로 만들어줘. 각 주차마다 구체적인 학습 자료 링크 포함."

### 📚 학습 체크리스트

- [ ] 관심 분야 로드맵 2개 이상 훑어보기
- [ ] Essential 항목 리스트 정리
- [ ] 현재 수준 자가 진단
- [ ] 6개월 학습 계획서 작성
- [ ] roadmap.sh에 계정 생성 후 진행 상황 체크

---

## jwasham/coding-interview-university (310K+ Stars)

**링크**: https://github.com/jwasham/coding-interview-university

**한 줄 소개**: Google 면접에 합격한 저자가 8개월 동안 따라간 학습 자료 모음.
**왜 봐야 하는가**: 막연한 "면접 준비"가 아니라 **구체적인 주제 리스트 + 학습 순서 + 문제 풀이 전략**이 모두 담겨 있습니다.
**난이도**: ⭐⭐⭐⭐

### 📋 이 레포가 다루는 내용

- 자료구조 10일, 알고리즘 20일, 시스템 디자인 5일, 행동 질문 3일 — 총 38일 압축판
- **한국어 번역본 존재**: `translations/README-ko.md`
- 각 주제마다 유튜브 강의, 책, 연습 문제 링크 포함

### 🚀 15분 퀵스타트

1단계. 한국어 README 열기

```bash
git clone https://github.com/jwasham/coding-interview-university.git
cd coding-interview-university
# translations/README-ko.md 파일을 에디터로 열기
```

2단계. 첫 번째 자료구조 "Array" 섹션의 첫 영상 시청 (약 15분)

3단계. Python으로 Two Sum 문제 직접 풀어보기

```python
def two_sum(nums: list, target: int) -> list:
    """주어진 리스트에서 합이 target이 되는 두 수의 인덱스를 반환."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# 테스트
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
print("Two Sum 통과")
```

예상 출력:

```
Two Sum 통과
```

### 📅 8주 압축 준비 스케줄

| 주차 | 집중 주제 | 일일 목표 |
|------|----------|-----------|
| 1주 | Array, LinkedList, Stack, Queue | LeetCode Easy 1문제 |
| 2주 | Tree, Graph, Hash Table | Easy+Medium 1~2문제 |
| 3주 | 정렬/탐색, BFS/DFS | Medium 2문제 |
| 4주 | Dynamic Programming | Medium~Hard 1~2문제 |
| 5주 | 시스템 디자인 기초 | 설계 질문 2~3개 |
| 6주 | 행동 질문 + 이력서 | STAR 기법 모의 답변 |
| 7주 | 회사별 기출 풀이 | 2~3시간/일 |
| 8주 | 모의 면접 + 약점 복습 | 주 1~2회 모의 면접 |

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트: 출제 예상"
    > "coding-interview-university의 Tree 섹션을 보고, 네이버/카카오 백엔드 면접에서 나올 법한 문제 Top 5를 Python 풀이와 함께 뽑아줘."

!!! example "🤖 Claude Code 프롬프트: 복잡도 분석"
    > "내가 작성한 이 코드의 시간/공간 복잡도를 분석하고, 더 효율적으로 개선할 방법이 있으면 Big-O 관점에서 비교해줘."

!!! example "🤖 Claude Code 프롬프트: 모의 면접"
    > "coding-interview-university 8주 스케줄의 4주차 DP 섹션 기반으로 모의 면접을 해줘. 힌트는 내가 요청할 때만 주고, 마지막에 피드백 줘."

### 📚 학습 체크리스트

- [ ] 한국어 README 완독
- [ ] Array/LinkedList/Stack/Queue 직접 구현
- [ ] Two Sum, Valid Parentheses, Reverse Linked List 풀이
- [ ] BFS/DFS 템플릿 암기
- [ ] 시스템 디자인 "URL Shortener" 설계 연습

!!! danger "🚨 자주 발생하는 에러"
    **에러**: "너무 많은 주제를 한 번에 하려다 포기"
    **원인**: 38일 풀코스를 완벽히 소화하려는 욕심
    **해결**: 첫 2주는 Array/String만 파고들기. **한 주제를 완벽히**가 핵심.

---

!!! tip "💡 다음 단계"
    CS 기초의 큰 그림이 잡혔다면, 이제 실제로 손을 움직여볼 차례입니다.
    [1-2. 코딩 입문 - 실전 프로젝트](02-coding-entry.md)에서 첫 프로젝트를 만들어봅시다.
