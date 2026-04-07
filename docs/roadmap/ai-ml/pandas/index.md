# 📘 Pandas 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/pandas-dev/pandas.svg?style=social)](https://github.com/pandas-dev/pandas)

!!! info "레포지토리"
    **pandas-dev/pandas** · 43k+ ⭐ · BSD-3 · [pandas.pydata.org](https://pandas.pydata.org)

---

## 🧐 1. Pandas는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Pandas는 **Python의 데이터 분석·조작 표준 라이브러리**입니다. 핵심 자료구조 `DataFrame`은 엑셀의 시트와 SQL의 테이블을 합친 것 같은 객체로, 수백만 행 데이터를 빠르게 다룰 수 있습니다.

### 핵심 특성
- **DataFrame / Series**: 라벨 인덱스 + 컬럼 기반 2D/1D 데이터 구조.
- **다양한 입출력**: CSV, Excel, JSON, Parquet, SQL DB, HDF5.
- **결측치 처리**: `dropna`, `fillna`, `interpolate`.
- **GroupBy / Pivot / Merge**: SQL의 GROUP BY·JOIN을 Python 코드로.
- **시계열 지원**: 날짜 인덱스, 리샘플링, 윈도우 연산.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **데이터 분석가 1순위 도구** | 채용 공고 필수 |
| **엑셀의 한계 돌파** | 수십만 행도 빠름 |
| **머신러닝 전처리 표준** | scikit-learn·PyTorch와 자연스러운 연결 |

## 🚀 2. 10분 퀵스타트

```bash
pip install pandas
```

```python
import pandas as pd

# 1) DataFrame 생성
df = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie", "David"],
    "major":  ["CS", "Math", "CS", "Stat"],
    "gpa":    [4.1, 3.7, 4.3, 3.9],
})

# 2) 필터링
cs_students = df[df["major"] == "CS"]

# 3) 그룹별 평균
print(df.groupby("major")["gpa"].mean())

# 4) CSV 저장/로드
df.to_csv("students.csv", index=False)
df2 = pd.read_csv("students.csv")
```

## 🛠️ 3. 코드 해부학

| 영역 | 핵심 메서드 |
|---|---|
| 입출력 | `read_csv`, `read_excel`, `read_sql`, `to_parquet` |
| 선택 | `df.loc[]`, `df.iloc[]`, `df.query()` |
| 결측치 | `isna`, `dropna`, `fillna` |
| 변형 | `apply`, `map`, `assign`, `pipe` |
| 집계 | `groupby`, `agg`, `pivot_table` |
| 결합 | `merge`, `concat`, `join` |
| 시계열 | `resample`, `rolling`, `shift` |

!!! tip "성능 팁"
    - 큰 데이터에는 `dtype` 명시(`category`, `int32`)로 메모리 절약.
    - 반복문보다 **벡터 연산**을 우선.
    - 더 큰 데이터셋은 [Polars](https://github.com/pola-rs/polars), [DuckDB](https://duckdb.org)로 확장.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 다음 Pandas 코드를 성능·가독성 관점에서 리팩토링해 줘:
- iterrows() → 벡터 연산
- chained indexing → loc
- 메모리 효율적 dtype
[코드]
```

### 🔵 Gemini
```
Pandas vs Polars vs DuckDB를 "수억 행 데이터셋 분석" 시나리오에서 비교해 줘.
문법, 메모리, 속도, 학습 곡선 기준.
```

### 🟢 ChatGPT
```
"공공 데이터 포털의 미세먼지 데이터"를 Pandas로 분석하는 4주 학습 계획을 짜 줘.
EDA, 시각화, 시계열 분석, 보고서 작성 포함.
```

### ⬛ Copilot
```python
# TODO: 월별 매출 데이터에 7일 이동평균과 전년 동월 대비 증감률 컬럼 추가
```

## 🔗 5. 관련 레포 · 다음 단계
- 시각화: [Matplotlib](https://github.com/matplotlib/matplotlib), [Seaborn](https://github.com/mwaskom/seaborn), [Plotly](https://github.com/plotly/plotly.py)
- 차세대: [Polars](https://github.com/pola-rs/polars), [DuckDB](https://duckdb.org)
- 본 가이드북: [Part 1-4 · 데이터 분석](../../../part1-foundation/04-data-analysis.md)
