# 📘 Coding Interview University 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/jwasham/coding-interview-university.svg?style=social)](https://github.com/jwasham/coding-interview-university)

!!! info "레포지토리"
    **jwasham/coding-interview-university** · 300k+ ⭐ · CC BY-SA · 한국어 번역 존재

---

## 🧐 1. Coding Interview University는 무엇이고, 누구에게 필요한가요?

**한 줄 요약**: John Washam이 **"Google 입사를 목표로 직접 8개월 동안 따라간 학습 자료 모음"**을 정리한 레포지토리입니다. 자료구조·알고리즘·시스템 디자인·OS·네트워크 등 빅테크 코딩 인터뷰에 필요한 모든 주제의 무료 자료 링크를 한 곳에 모았습니다.

### 핵심 특성
- **체계적 커리큘럼**: "이 순서대로 공부하면 된다"는 길잡이.
- **무료 자료 100%**: YouTube 강의, MIT OCW, 책 PDF, 블로그 글.
- **체크리스트 형식**: GitHub fork 후 본인이 완료한 항목 체크.
- **다국어 번역**: [한국어 README](https://github.com/jwasham/coding-interview-university/blob/main/translations/README-ko.md).

### 다루는 주제
| 카테고리 | 내용 |
|---|---|
| 자료구조 | 배열, 연결리스트, 스택, 큐, 해시테이블, 트리, 그래프, 힙 |
| 알고리즘 | 정렬, 탐색, 동적 계획법, 그리디, 분할정복 |
| CS 핵심 | OS, 네트워크, DB, 컴파일러, 아키텍처 |
| 시스템 디자인 | 확장성, 캐시, 큐, CAP 정리 |
| 면접 기술 | 행동 면접, 코딩 화이트보드 연습 |

### 누구에게 필요한가
| 대상 | 활용법 |
|---|---|
| **글로벌 빅테크 지원** | Google·Meta·Amazon 코딩 인터뷰 대비 |
| **국내 대기업 SW 직군** | 카카오·네이버·라인 코테 + 면접 |
| **비전공자** | "어디까지 공부해야 하나"의 답 |
| **학습 페이스 잡기 어려운 사람** | 체크리스트로 진도 관리 |

## 🚀 2. 10분 퀵스타트

### 1단계: 레포 fork
```bash
# GitHub에서 fork → 본인 계정으로
git clone https://github.com/<your-username>/coding-interview-university.git
cd coding-interview-university
```

### 2단계: 학습 트래커 열기
README.md를 열고 본인이 완료한 항목 앞 `[ ]` → `[x]`로 변경.

### 3단계: 첫 주 목표 설정
```
[ ] Big-O 복잡도 강의 시청 (3개)
[ ] 배열 vs 연결리스트 비교 학습
[ ] LeetCode "Two Sum" 직접 해결
[ ] progress.md에 학습 로그 기록
```

### 4단계: 매일 30분 시간 확보
긴 호흡(8개월~1년)이 핵심. 짧게라도 매일.

## 🛠️ 3. 코드 해부학: 레포 구조

```
coding-interview-university/
├── README.md              # 전체 커리큘럼 (영문)
├── translations/
│   ├── README-ko.md       # 한국어 번역
│   └── ...
├── extras/                # 추가 자료
└── programming-language-resources.md
```

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 나는 비전공 4학년이고 6개월 안에 카카오·네이버 신입 공채를 준비한다.
Coding Interview University 기준으로
- 우선순위 Top 30 항목
- 주차별 학습 계획
- 매주 풀어야 할 LeetCode·백준 문제 수
- 모의 면접 일정
을 포함한 학습 로드맵을 만들어 줘.
```

### 🔵 Gemini
```
Coding Interview University가 추천하는 자료구조 강의 중
한국 학생에게 가장 인기 있는 것 5개를 비교해 줘.
난이도, 예제 언어, 영어 자막 품질 기준.
```

### 🟢 ChatGPT
```
나는 LeetCode Easy 50개 풀었다.
이제 Medium에 도전하려고 한다.
Coding Interview University가 권하는 패턴(슬라이딩 윈도우, 투 포인터, BFS/DFS)
순서로 매주 학습 계획과 추천 문제 5개씩 짜 줘.
```

### ⬛ Copilot
```python
# TODO: 슬라이딩 윈도우로 "최대 K개 다른 문자를 가진 가장 긴 부분 문자열" 풀이
```

## 🔗 5. 관련 레포 · 다음 단계
- [OSSU 딥다이브](../ossu/index.md) — CS 학사 수준
- [The Algorithms 딥다이브](../algorithms/index.md) — 구현체
- [System Design Primer 딥다이브](../system-design/index.md)
- 문제 풀이: [LeetCode](https://leetcode.com), [백준](https://www.acmicpc.net), [프로그래머스](https://programmers.co.kr)
