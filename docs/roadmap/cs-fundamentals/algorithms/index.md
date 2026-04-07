# 📘 The Algorithms (Python) 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/TheAlgorithms/Python.svg?style=social)](https://github.com/TheAlgorithms/Python)

!!! info "레포지토리"
    **TheAlgorithms/Python** · 190k+ ⭐ · MIT License · [the-algorithms.com](https://the-algorithms.com)

---

## 🧐 1. The Algorithms (Python)은 무엇이고, 어떻게 쓰이나요?

**한 줄 요약**: The Algorithms는 **모든 주요 알고리즘과 자료구조를 Python(및 다른 언어)으로 구현한 교육용 레퍼런스 모음**입니다. "이 알고리즘의 정석 구현이 어떻게 생겼는지" 한 곳에서 볼 수 있습니다.

### 핵심 특성
- **방대한 범위**: 정렬, 탐색, 그래프, DP, 암호학, 머신러닝, 컴퓨터 비전, 수치 해석.
- **교육 목적**: 표준 라이브러리에 의존하지 않고 알고리즘을 처음부터 구현.
- **타입 힌트·doctest**: 거의 모든 함수에 사용 예시가 포함됨.
- **다언어 자매 레포**: Java, C++, JavaScript, Go, Rust 등.

### 누구에게 필요한가
| 대상 | 활용법 |
|---|---|
| 알고리즘 입문자 | "이 정렬을 코드로 어떻게 구현하지?" 답 |
| 면접 준비생 | 표준 구현을 학습 후 변형 문제에 적용 |
| 강의 자료 제작자 | 예제 코드 그대로 활용 가능 |

## 🚀 2. 10분 퀵스타트

```bash
git clone https://github.com/TheAlgorithms/Python.git
cd Python
```

### 정렬 알고리즘 둘러보기
```bash
python sorts/quick_sort.py
python sorts/merge_sort.py
```

### 테스트
```bash
pip install pytest
pytest sorts/quick_sort.py
```

각 파일이 doctest를 포함하므로 별도 테스트 작성 없이도 검증 가능.

## 🛠️ 3. 코드 해부학

| 디렉터리 | 내용 |
|---|---|
| `sorts/` | 정렬 알고리즘 (quick, merge, heap, radix...) |
| `searches/` | 탐색 (binary, jump, ternary...) |
| `data_structures/` | 자료구조 (트리, 그래프, 힙, 트라이...) |
| `dynamic_programming/` | DP 문제 풀이 |
| `graphs/` | 그래프 알고리즘 (BFS, DFS, Dijkstra...) |
| `machine_learning/` | 기초 ML 구현 (선형회귀, k-means...) |
| `ciphers/` | 암호 알고리즘 |

!!! tip "활용 팁"
    그대로 복붙해서 쓰는 것이 아니라, **읽고 → 직접 다시 짜보고 → 비교**하는 것이 학습 효과가 큽니다.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 다음 quick_sort 구현을 비교해 줘:
1) The Algorithms 레포 버전
2) CLRS 교과서 의사 코드
3) Python sorted() 내부(Timsort)
시간 복잡도, 공간 복잡도, 안정성, 실전 성능을 표로.
[코드 붙여넣기]
```

### 🔵 Gemini
```
The Algorithms (Python) 레포에서 "그래프" 디렉터리의
BFS/DFS/Dijkstra 구현을 비교해 줘.
교과서 정의와 일치하는지, 개선 여지가 있는지.
```

### 🟢 ChatGPT
```
나는 정렬 알고리즘 5종(버블, 삽입, 선택, 병합, 퀵)을 직접 구현했다.
The Algorithms 레포의 구현과 비교해 내 코드의 개선점을 찾아 줘.
[내 코드]
```

### ⬛ Copilot
```python
# TODO: Dijkstra 알고리즘 - 우선순위 큐(heapq) 사용, 음수 가중치 검출
```

## 🔗 5. 관련 레포 · 다음 단계
- 자매 레포: [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java), [TheAlgorithms/C-Plus-Plus](https://github.com/TheAlgorithms/C-Plus-Plus)
- 시각화: [VisuAlgo](https://visualgo.net), [algorithm-visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer)
- [Coding Interview University 딥다이브](../interview-university/index.md)
- 본 가이드북: [Part 1-1 · CS 기초](../../../part1-foundation/01-cs-basics.md)
