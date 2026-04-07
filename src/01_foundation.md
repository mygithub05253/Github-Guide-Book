# Part 1: 개발 기초 다지기

> 이 파트는 프로그래밍을 처음 시작하는 분들을 위한 기초 가이드입니다.
> CS 기초부터 코딩 입문, 데이터 분석까지 단계별로 학습할 수 있습니다.

## 학습 목표
- 컴퓨터 과학 기본 개념 이해
- 프로그래밍 언어 기초 습득
- 개발 환경 설정 및 Git 사용법
- 데이터 분석 기초

---

# 카테고리 4: 비전공자를 위한 학습 가이드

개발자 지망생 중 컴퓨터 과학을 전공하지 않은 사람들을 위한 체계적인 학습 경로입니다.
이 카테고리는 기초부터 실전까지 단계적으로 성장할 수 있도록 구성했습니다.

---

## 4-1. CS 기초 다지기

### ossu/computer-science (178K+ Stars)
**링크**: https://github.com/ossu/computer-science

전 세계 비전공자 학습자를 위한 완전한 컴퓨터 과학 커리큘럼입니다. 무료이며 대학 수준의 교육을 제공합니다.

#### 📋 개요
- **제공 형식**: 온라인 강좌 모음 + 프로젝트 목록
- **총 소요 시간**: 180주 (주당 30-40시간 투자 기준)
- **커버 범위**: Fundamentals → Core → Advanced → Specialization
- **언어**: 대부분 영어 강좌 (한국어 자막 일부)

#### 🚀 시작하기

1. **Repository 구조 이해**
```bash
# OSSU/CS 저장소 클론
git clone https://github.com/ossu/computer-science.git
cd computer-science

# README.md에서 커리큘럼 전체 구조 확인
cat README.md | head -100
```

2. **추천 학습 단계** (비전공자 기준)

| 단계 | 예상 기간 | 핵심 과목 | 학습량 |
|------|---------|---------|-------|
| **1단계: 기초** | 12주 | Programming (Python), Math Foundations | 낮음 |
| **2단계: 핵심** | 24주 | Data Structures, Algorithms, Database | 중간 |
| **3단계: 심화** | 16주 | OS, Networks, Compilers | 높음 |
| **4단계: 전공선택** | 12주 | ML, Security, Distributed Systems 중 선택 | 매우높음 |

#### 💻 실전 학습법

**Step 1: 프로그래밍 기초 (MIT CS50)**
- CS50x Weeks 6-8에서 Python 문법, 함수, 리스트/딕셔너리 등 기본기를 다집니다.
- 과제 제출 플랫폼(check50)으로 즉시 피드백을 받을 수 있어 독학에 적합합니다.

**Step 2: 자료구조 이해 (스택, 큐, 링크드리스트)**
- UC San Diego의 Data Structures 강좌에서 개념을 잡고, OSSU 리포의 과제 링크를 따라 직접 구현합니다.
- 개념 이해가 먼저입니다. 종이에 그려본 뒤 Python `list`, `collections.deque`로 구현하세요.

**Step 3: 알고리즘 기초 (정렬/탐색)**
- Princeton Algorithms Part I에서 버블/병합/퀵 정렬, 이진 탐색 등을 학습합니다.
- 구현은 이미 레포 안 `coursework/` 폴더에 연습 문제로 포함되어 있습니다.

> Claude Code 활용 팁
> `> "OSSU CS 커리큘럼에서 비전공자에게 가장 중요한 3개 강좌만 골라서 학습 계획을 짜줘"`
> `> "이 레포의 Core CS 섹션을 읽고 내 수준(Python 기초만 앎)에 맞는 시작점을 추천해줘"`

#### ⏱️ 권장 학습 일정

**주 1-4: Python 기초 (MIT CS50)**
- 강좌: CS50x Weeks 6-8 (Python)
- 시간: 주 8-10시간
- 프로젝트: Hello World, 간단한 계산기, To-do list 프로그램

**주 5-8: 자료구조 (UC San Diego DSA)**
- 강좌: Algorithms and Data Structures
- 시간: 주 12-15시간
- 프로젝트: Stack/Queue 구현, LinkedList 만들기

**주 9-12: 알고리즘 (Princeton Algorithms)**
- 강좌: Algorithms Part I & II
- 시간: 주 15-20시간
- 프로젝트: 정렬 알고리즘 성능 비교, 탐색 알고리즘 구현

#### 💡 비전공자 특화 팁

1. **코드 작성 전 개념 이해**: 강좌 영상을 처음부터 끝까지 보고 난 후 코드 작성
2. **손으로 그려보기**: 자료구조는 반드시 종이에 그리면서 학습
3. **작은 프로젝트부터**: 완벽하지 않아도 작동하는 코드부터 시작
4. **온라인 커뮤니티**: OSSU Discord 서버에 한국어 채널 있음

---

### kamranahmedse/developer-roadmap (310K+ Stars)
**링크**: https://github.com/kamranahmedse/developer-roadmap

개발자 진로를 시각화한 로드맵 모음. 각 단계별로 어떤 기술을 배워야 하는지 명확하게 보여줍니다.

#### 📊 로드맵 종류

```
roadmap/
├── Frontend Developer Roadmap
│   ├── 1단계: HTML, CSS, JavaScript 기초
│   ├── 2단계: 패키지 매니저 (npm), 버전 관리 (git)
│   ├── 3단계: CSS 프레임워크 (Tailwind, Bootstrap)
│   ├── 4단계: JavaScript 심화 (DOM, AJAX)
│   └── 5단계: 프론트엔드 프레임워크 (React, Vue, Angular)
├── Backend Developer Roadmap
│   ├── 1단계: 언어 선택 (Node.js, Python, Java)
│   ├── 2단계: 웹 프레임워크 (Express, Django, Spring)
│   ├── 3단계: 데이터베이스 (SQL, NoSQL)
│   ├── 4단계: API 설계 (REST, GraphQL)
│   └── 5단계: 배포 & 확장 (Docker, Kubernetes)
├── DevOps Roadmap
│   ├── Linux 기초
│   ├── 컨테이너 (Docker)
│   ├── 오케스트레이션 (Kubernetes)
│   ├── CI/CD (GitHub Actions, Jenkins)
│   └── 모니터링 (Prometheus, ELK)
└── Full Stack Developer Roadmap
    └── Frontend + Backend + DevOps 통합
```

#### 🎯 로드맵 활용법

**1단계: 현재 수준 파악**
```
당신의 수준이 어디인가요?
- 초급 (0-6개월 경력): Beginner roadmap 선택
- 중급 (6-18개월 경력): Intermediate roadmap 선택
- 고급 (18개월 이상): Advanced roadmap 선택
```

**2단계: 우선순위 정하기**
```
Frontend 개발자가 되고 싶다면:
Essential (필수): HTML → CSS → JavaScript → React
Good to Have (선택): TypeScript → Testing → Performance
Advanced (심화): Custom Build Tools → Web Performance → PWA
```

**3단계: 시간 할당 전략**
- 비전공자는 주제당 40-60시간을 잡습니다. 주 20시간 기준 주제 하나에 2-3주가 적당합니다.
- Frontend 로드맵 예: HTML → CSS → JavaScript → DOM → React → Hooks → State Management 순으로 각 3주.
- 로드맵의 각 노드는 "Personal Recommendation / Alternative Option"으로 구분되어 있어 우선순위를 바로 볼 수 있습니다.

> Claude Code 활용 팁
> `> "developer-roadmap 레포의 Frontend 로드맵을 보고 주 20시간 학습 기준 6개월 계획표를 만들어줘"`

#### 🔗 연관 리소스 링크

각 로드맵의 항목마다 실제 학습 자료 링크가 포함되어 있습니다:
- FreeCodeCamp 튜토리얼
- Udemy 강좌
- MDN 문서
- 공식 문서

---

### jwasham/coding-interview-university (310K+ Stars)
**링크**: https://github.com/jwasham/coding-interview-university

Google과 같은 대기업에 합격하기 위한 완벽한 인터뷰 준비 가이드입니다.

#### 📚 커버 범위

```
Interview Prep Curriculum
├── 자료구조 (10일)
│   ├── Array
│   ├── LinkedList
│   ├── Stack
│   ├── Queue
│   ├── Hash Table
│   ├── Binary Search Tree
│   ├── Heap
│   └── Graph
├── 알고리즘 (20일)
│   ├── DFS (Depth First Search)
│   ├── BFS (Breadth First Search)
│   ├── Dynamic Programming
│   ├── Bit Manipulation
│   └── Combinatorics
├── 시스템 디자인 (5일)
│   ├── Scalability
│   ├── Database Design
│   ├── Caching
│   └── Load Balancing
└── 행동 질문 (3일)
    ├── STAR 기법
    ├── 프로젝트 설명
    └── 성과 이야기
```

#### 💻 알고리즘 인터뷰 대비 코드

**LeetCode Easy: Two Sum 문제**
```python
def two_sum(nums: list, target: int) -> list:
    """
    주어진 리스트에서 합이 target이 되는 두 수의 인덱스를 반환

    예: nums = [2, 7, 11, 15], target = 9
    반환: [0, 1] (2 + 7 = 9)
    """
    # 방법 1: Brute Force (O(n²))
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # 방법 2: Hash Map (O(n)) - 권장
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
print("✓ Two Sum 통과")
```

**LeetCode Medium: Binary Search Tree Validate**
```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    주어진 이진 트리가 유효한 이진 탐색 트리인지 확인

    이진 탐색 트리 규칙:
    - 왼쪽 서브트리의 모든 값 < 노드값
    - 오른쪽 서브트리의 모든 값 > 노드값
    """
    def validate(node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root)

# 테스트 케이스
#     2
#    / \
#   1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
assert is_valid_bst(root) == True
print("✓ Valid BST 확인")

# 잘못된 트리
#     5
#    / \
#   1   4
#      / \
#     3   6
bad_root = TreeNode(5)
bad_root.left = TreeNode(1)
bad_root.right = TreeNode(4)
bad_root.right.left = TreeNode(3)
bad_root.right.right = TreeNode(6)
assert is_valid_bst(bad_root) == False
print("✓ Invalid BST 확인")
```

**LeetCode Hard: Median of Two Sorted Arrays**
```python
def find_median_sorted_arrays(nums1: list, nums2: list) -> float:
    """
    두 정렬된 배열의 중앙값 찾기 (O(log(min(m,n))) 필수)
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1

        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]

        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        if maxLeft1 <= minRight1 and maxLeft2 <= minRight2:
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            right = partition1 - 1
        else:
            left = partition1 + 1

    return -1

# 테스트
assert find_median_sorted_arrays([1, 3], [2]) == 2.0
assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
print("✓ Median of Two Sorted Arrays 통과")
```

#### 📅 8주 준비 스케줄

```
1주: 자료구조 심화 (Array, LinkedList, Stack, Queue)
   - 매일 1개 문제 풀기 (LeetCode Easy)
   - 시간: 1-2시간

2주: 자료구조 심화 (Tree, Graph, Hash Table)
   - 매일 1-2개 문제 (Easy + Medium)
   - 시간: 2-3시간

3주: 정렬/탐색 알고리즘
   - 병합 정렬, 퀵 정렬 구현
   - BFS, DFS 마스터
   - 매일 2개 문제 (Medium)

4주: 동적 프로그래밍
   - DP 개념 정리
   - 클래식 DP 문제 풀이
   - 매일 1-2개 문제 (Medium-Hard)

5주: 시스템 디자인 기초
   - Scalability 개념
   - Database 설계
   - 주당 2-3개 설계 질문 준비

6주: 행동 질문 준비
   - STAR 기법 연습
   - 이력서 정리
   - 모의 면접 1회

7주: 실제 기출 문제 연습
   - 회사별 기출 문제 60문제
   - 매일 2-3시간 문제 풀기

8주: 최종 점검 및 모의 면접
   - 주당 1-2회 모의 면접
   - 약한 부분 집중 복습
```

#### 🎤 인터뷰 팁

**기술 면접 Checklist**
```python
def technical_interview_checklist():
    checklist = {
        "소통": [
            "문제를 충분히 이해했는지 확인",
            "접근 방법을 설명하기",
            "트레이드오프 논의하기"
        ],
        "코딩": [
            "오류 처리 고려",
            "엣지 케이스 처리",
            "코드 정리하기"
        ],
        "최적화": [
            "시간복잡도 분석",
            "공간복잡도 분석",
            "더 나은 솔루션 제시"
        ],
        "테스트": [
            "샘플 입력으로 테스트",
            "엣지 케이스 테스트",
            "성능 검증"
        ]
    }

    for category, items in checklist.items():
        print(f"\n[{category}]")
        for item in items:
            print(f"  ☐ {item}")

technical_interview_checklist()
```

---

## 4-2. 코딩 입문 - 실전 프로젝트

### freeCodeCamp/freeCodeCamp (410K+ Stars)
**링크**: https://github.com/freeCodeCamp/freeCodeCamp

수백 시간의 무료 코딩 교육. 초급부터 고급까지 단계별로 학습할 수 있습니다.

#### 🎓 커리큘럼 구조

```
freeCodeCamp Curriculum
├── Responsive Web Design (300시간)
│   ├── HTML & CSS 기초
│   ├── Flexbox & Grid
│   └── 5개 프로젝트 (Portfolio, Survey, Landing Page 등)
├── JavaScript Algorithms and Data Structures (300시간)
│   ├── JavaScript 기초
│   ├── ES6+ 문법
│   ├── 자료구조 & 알고리즘
│   └── 5개 프로젝트
├── Front End Development Libraries (300시간)
│   ├── Bootstrap
│   ├── jQuery
│   ├── React
│   ├── Redux
│   └── 5개 프로젝트
├── Data Visualization (300시간)
│   ├── D3.js
│   ├── API & Fetch
│   └── 4개 프로젝트
└── Back End Development and APIs (300시간)
    ├── Node.js & Express
    ├── MongoDB
    ├── User Authentication
    └── 5개 프로젝트
```

#### 💻 시작 가이드

**Step 1: 개발 환경 설정**
```bash
# Node.js 설치 확인
node --version
npm --version

# VS Code 설치
# https://code.visualstudio.com/

# 권장 확장 프로그램
# - Live Server
# - Thunder Client (API 테스트)
# - Code Runner
# - Prettier (자동 포맷팅)
```

**Step 2: 첫 번째 프로젝트 - Personal Portfolio**
- freeCodeCamp Responsive Web Design 섹션에서 HTML/CSS Flexbox·Grid를 배운 뒤 포트폴리오 페이지를 만듭니다.
- 필요한 섹션: Navbar, Hero, About, Projects Grid, Contact. 반응형(@media 768px 기준)은 필수.
- Smooth scroll, sticky navbar 등 JS 상호작용은 작은 스니펫만 추가하면 충분합니다.

> Claude Code 활용 팁
> `> "freeCodeCamp 커리큘럼의 Responsive Web Design 프로젝트 5개를 단계별로 어떻게 풀어가는지 알려줘"`
> `> "내가 만든 index.html/style.css를 리뷰하고 접근성(a11y)·반응형 관점에서 개선점을 알려줘"`

---

### TheOdinProject/curriculum (10K+ Stars)
**링크**: https://github.com/TheOdinProject/curriculum

완전한 오픈소스 풀스택 웹개발 커리큘럼. HTML부터 배포까지 모든 것을 배웁니다.

#### 🛣️ 학습 경로

```
The Odin Project Path
├── Foundations (10-20주)
│   ├── Installing Tools
│   ├── How This Course Will Work
│   ├── How the Web Works
│   ├── JavaScript Basics
│   ├── HTML Basics
│   ├── CSS Basics
│   ├── Flexbox
│   ├── Grid
│   └── 10개 프로젝트
├── Intermediate HTML and CSS (4-8주)
│   ├── Intermediate HTML Concepts
│   ├── Intermediate CSS Concepts
│   ├── 2개 프로젝트
├── JavaScript (12-20주)
│   ├── Fundamentals
│   ├── DOM Manipulation
│   ├── OOP
│   ├── Async JavaScript
│   └── 10개 프로젝트
├── Getting Hired (진행 중 진행)
│   ├── Portfolio Project
│   ├── Preparing for Interviews
│   ├── Getting Hired
└── Paths (경로 선택)
    ├── Foundations → React (Front-end)
    │   ├── React Basics
    │   ├── Advanced React
    │   ├── 5개 프로젝트
    │   └── Capstone Project
    └── Foundations → Rails (Full Stack)
        ├── Ruby Basics
        ├── Ruby on Rails
        ├── Databases
        ├── 5개 프로젝트
        └── Capstone Project
```

#### 📌 주요 프로젝트

**1. 가위바위보 게임**
- The Odin Project Foundations 과정의 첫 JavaScript 프로젝트. 3개 버튼 + 랜덤 선택 + 승패 로직만으로 완성됩니다.
- 학습 포인트: `Math.random()`, 조건문, DOM 이벤트 핸들러, 상태 관리.

**2. 계산기 프로젝트 (고급)**
- ES6 Class 문법, 상태 관리(`currentOperand`, `previousOperand`), 데이터 속성(`[data-number]`) 활용을 배웁니다.
- 단순히 만들지 말고 "소수점 2번 입력 방지", "0으로 나누기 예외" 같은 엣지 케이스도 직접 처리하면 실력이 붙습니다.

> Claude Code 활용 팁
> `> "The Odin Project의 Calculator 프로젝트 요구사항을 보고 내가 놓친 기능이 있는지 체크해줘"`

---

### codecrafters-io/build-your-own-x (330K+ Stars)
**링크**: https://github.com/codecrafters-io/build-your-own-x

유명한 도구들을 처음부터 만들어보는 프로젝트 모음입니다.

#### 🏗️ 구성 요소별 학습

```
Build Your Own X
├── Build Your Own Git (Rust)
│   ├── 1. Read Objects
│   ├── 2. Reading Commits
│   ├── 3. Read Tree Objects
│   ├── 4. Writing Objects
│   └── 5. Creating Commits
├── Build Your Own Docker (Go)
│   ├── 1. Container Basics
│   ├── 2. Namespaces
│   ├── 3. Cgroups
│   └── 4. Docker CLI
├── Build Your Own Redis (Python/Ruby/Go)
│   ├── 1. TCP Server
│   ├── 2. RESP Protocol
│   ├── 3. Expiration
│   └── 4. Replication
└── Build Your Own Language (Go/Python)
    ├── 1. Lexer
    ├── 2. Parser
    ├── 3. Evaluator
    └── 4. Advanced Features
```

#### 💾 예시: Redis 만들기 (Python)

- 레포 안 `Build Your Own Redis` 튜토리얼이 단계별 학습 과제를 제공합니다.
- 핵심 학습 순서: TCP 소켓 서버 → RESP 프로토콜 파싱 → SET/GET/DEL 명령어 → 만료(EX 옵션) → 복제.
- Python `socket`, `threading`, `datetime` 세 개 모듈만으로 최소 구현이 가능합니다.

> Claude Code 활용 팁
> `> "build-your-own-x 레포에서 Build Your Own Redis 챕터를 읽고, 비전공자가 1주차에 구현해볼 수 있는 가장 작은 서브셋을 골라줘"`

#### 📚 학습 로드맵

```
초급 (1개월)
- Git 기본 개념 이해
- 간단한 TCP 서버 만들기
- 기본 프로토콜 파싱

중급 (2-3개월)
- Redis 서버 전체 구현
- Docker 컨테이너 기초
- 동시성 처리

고급 (3-6개월)
- 분산 시스템 개념
- 프로그래밍 언어 만들기
- 성능 최적화
```

---

## 4-3. 면접 준비

### yangshun/tech-interview-handbook (122K+ Stars)
**링크**: https://github.com/yangshun/tech-interview-handbook

개발자 면접을 위한 종합 가이드. 구성, 질문, 답변 전략까지 담고 있습니다.

#### 📋 면접 유형별 전략

**1. 코딩 면접 (Coding Interview)**
```python
# 면접 전 체크리스트
interview_checklist = {
    "인터뷰 전": [
        "회사 기술 스택 조사",
        "최근 프로젝트 복습",
        "인터뷰어 LinkedIn 확인",
        "자주 묻는 문제 3-5개 준비"
    ],
    "인터뷰 중": [
        "질문 명확히 이해하기",
        "접근 방법 설명하기",
        "엣지 케이스 고려하기",
        "시간복잡도 분석하기",
        "트레이드오프 논의하기"
    ],
    "코딩 후": [
        "코드 리뷰하기",
        "테스트 케이스 작성하기",
        "성능 개선 제시하기",
        "결과 검증하기"
    ]
}

for phase, items in interview_checklist.items():
    print(f"\n📌 {phase}")
    for item in items:
        print(f"  ☐ {item}")
```

**2. 시스템 디자인 면접**
```
면접 프레임워크:

1. 요구사항 명확히 하기 (5분)
   - 함수형 요구사항 (FRs)
   - 비함수형 요구사항 (NFRs)
   - Scale, QPS, Data volume

2. API 설계 (5분)
   - Endpoints 정의
   - Request/Response 형식
   - Rate limiting

3. 데이터 모델 설계 (5분)
   - Database schema
   - Indexing
   - Sharding strategy

4. 높은 수준의 설계 (10분)
   - Components
   - Data flow
   - Caching layer
   - Message queue

5. 상세 설계 (10분)
   - Core components 심화
   - Bottleneck 분석
   - Optimization

6. 마무리 (5분)
   - Monitoring
   - Logging
   - Future improvements
```

**실제 시스템 디자인 예: URL Shortener**
```
1단계: 요구사항
- 함수형: 긴 URL → 짧은 URL 변환, 리다이렉트
- 비함수형:
  * 초당 쓰기: 500 writes/sec
  * 초당 읽기: 100,000 reads/sec
  * 가용성: 99.9%
  * Latency: < 200ms

2단계: 용량 산정
- 5년 데이터: 500 * 86400 * 365 * 5 = 78.8 billion URLs
- 저장 공간: 78.8B * 100 bytes = 7.88 TB

3단계: API 설계
POST /api/shorten
{
    "long_url": "https://example.com/very/long/url"
}
응답:
{
    "short_url": "https://short.url/abc123"
}

GET /api/{short_code}
응답: 301 Redirect to original URL

4단계: 데이터 모델
Table: URLMapping
- id (PK): bigint
- short_code: varchar(10) UNIQUE
- long_url: varchar(2048)
- created_at: timestamp
- expiration: timestamp

5단계: 높은 수준의 설계
Client → Load Balancer → API Servers
                          ↓
                      Cache (Redis)
                          ↓
                    Database (MySQL)
                          ↓
                    Message Queue (Kafka)
                          ↓
                    Analytics Service

6단계: 상세 설계
- Short code 생성: Base62 encoding (0-9, a-z, A-Z)
- Collision 처리: Retry with increment
- Caching 전략: LRU cache in Redis
- Load 분산: Consistent hashing
```

---

### donnemartin/system-design-primer (290K+ Stars)
**링크**: https://github.com/donnemartin/system-design-primer

확장 가능한 시스템 설계를 위한 종합 리소스입니다.

#### 🏗️ 핵심 개념

**1. Scalability (확장성)**
```
Vertical Scaling (수직 확장)
- CPU 업그레이드
- 메모리 추가
- 한계: 단일 기계의 물리적 제약

Horizontal Scaling (수평 확장)
- 더 많은 서버 추가
- Load balancer로 트래픽 분산
- 권장: 대부분의 경우 수평 확장이 더 효율적

예시: 100 QPS → 1000 QPS로 확장
Before (단일 서버):
  [Application] → [Database] → Bottleneck!

After (수평 확장):
  Load Balancer
      ↓
  App1  App2  App3
      ↓   ↓   ↓
    Cache (Redis)
      ↓
    Database (Master-Slave)
      ↓
  Slave1  Slave2
```

**2. 데이터베이스 설계**
```
SQL vs NoSQL 선택

SQL (관계형 데이터베이스)
장점:
- ACID 보장
- 복잡한 쿼리 가능
- 데이터 무결성
단점:
- 수평 확장 어려움
- 고정된 스키마

예: MySQL, PostgreSQL

NoSQL (비관계형 데이터베이스)
장점:
- 수평 확장 용이
- 빠른 읽기/쓰기
- 유연한 스키마
단점:
- ACID 보장 안 함
- 쿼리 능력 제한
- Consistency 문제

예: MongoDB, Cassandra, DynamoDB
```

**3. 캐싱 전략**
- LRU(Least Recently Used), LFU(Least Frequently Used), Write-Through/Write-Back 등 전략별 차이를 이해합니다.
- Python에서는 `collections.OrderedDict` 또는 `functools.lru_cache` 데코레이터로 쉽게 실험할 수 있습니다.
- system-design-primer는 실제 프로덕션 시스템(Memcached, Redis, CDN)에서 각 전략이 어떻게 쓰이는지 사례와 함께 설명합니다.

---

### kdn251/interviews (63K+ Stars)
**링크**: https://github.com/kdn251/interviews

Java 기반 면접 준비용 알고리즘 및 자료구조 구현.

#### 🎯 Java 기반 면접 준비

- 이 레포는 LeetCode/HackerRank 빈출 문제의 Java 풀이를 카테고리별(Array, String, Tree, DP 등)로 정리해두었습니다.
- 활용법: 문제를 먼저 직접 풀어본 뒤, 이 레포의 풀이와 시간/공간 복잡도를 비교하는 식으로 학습합니다.
- Two Sum, Valid Palindrome, Reverse Integer 같은 Easy 문제로 시작해서 점차 Medium/Hard로 올라가세요.

> Claude Code 활용 팁
> `> "kdn251/interviews 레포의 Array 섹션에서 대기업 면접 빈출 Top 10을 골라줘"`

---

## 4-4. 데이터 분석 & 시각화

### Python 데이터 분석 기초

#### 설치 및 환경 설정
```bash
# 가상 환경 생성
python -m venv data-env
source data-env/bin/activate  # Linux/Mac
data-env\Scripts\activate  # Windows

# 필수 라이브러리 설치
pip install jupyter numpy pandas matplotlib seaborn scikit-learn streamlit
```

#### 📊 Pandas를 이용한 데이터 분석

핵심 API 5가지만 알면 80%의 분석이 가능합니다.

```python
import pandas as pd

df = pd.read_csv('data.csv')
df.head(); df.info(); df.describe()           # 탐색
df.fillna(df.mean(numeric_only=True))         # 결측 처리
df.drop_duplicates()                          # 중복 제거
df.groupby('category')['sales'].sum()         # 그룹 집계
df.corr(numeric_only=True)                    # 상관관계
```

시각화는 `matplotlib`/`seaborn` 기본 차트(hist, boxplot, scatter, heatmap)로 충분하고,
머신러닝은 `scikit-learn`의 `train_test_split` → `StandardScaler` → `RandomForestClassifier`
3단계 파이프라인을 먼저 익히세요.

#### 📊 Streamlit으로 대시보드 만들기

- Streamlit은 Python 스크립트 한 개로 웹 대시보드를 만드는 도구입니다. HTML/CSS/JS 몰라도 됩니다.
- 핵심 API: `st.title`, `st.sidebar`, `st.metric`, `st.line_chart`, `st.bar_chart`, `st.dataframe`, `@st.cache_data`.
- 실행: `streamlit run dashboard.py`로 로컬 서버가 뜹니다.

> Claude Code 활용 팁
> `> "내 CSV 파일(컬럼: date, category, sales)로 Streamlit 대시보드 초안을 만들어줘. KPI 4개 + 시계열 차트 + 카테고리 필터 포함해서."`

```bash
# Streamlit 실행
streamlit run dashboard.py
```

---

