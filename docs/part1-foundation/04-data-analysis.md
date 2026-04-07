# 1-4. 데이터 분석 & 시각화

> "데이터 분석은 데이터 분석가만 하는 것"이라는 생각은 옛날 얘기입니다.
> 백엔드든 프론트든, 본인 서비스의 데이터를 직접 뜯어볼 줄 알아야 성장이 빨라요.

!!! info "📌 핵심 요약"
    - **Pandas 5개 API**만 알면 80%의 분석이 가능
    - **Matplotlib/Seaborn**으로 차트는 4가지 유형만 익히면 충분
    - **Streamlit**으로 HTML/JS 몰라도 웹 대시보드 제작 가능

---

## 환경 설정 (5분)

### 🚀 15분 퀵스타트

1단계. 가상환경 생성 (프로젝트 격리를 위해)

```bash
# Windows PowerShell
python -m venv data-env
.\data-env\Scripts\Activate.ps1

# macOS/Linux
python -m venv data-env
source data-env/bin/activate
```

2단계. 필수 라이브러리 설치

```bash
pip install jupyter numpy pandas matplotlib seaborn scikit-learn streamlit
```

예상 출력:

```
Successfully installed pandas-2.x.x numpy-1.x.x matplotlib-3.x.x ...
```

3단계. Jupyter Notebook 실행

```bash
jupyter notebook
```

브라우저가 자동으로 열리고 `http://localhost:8888`에 노트북 환경이 뜹니다.

!!! danger "🚨 자주 발생하는 에러"
    **에러**: `ModuleNotFoundError: No module named 'pandas'`
    **원인**: 가상환경 활성화 안 됨 또는 다른 Python을 쓰고 있음
    **해결**:

    ```bash
    # 가상환경 활성화 확인
    where python   # Windows
    which python   # macOS/Linux

    # 경로에 data-env가 포함되어야 함
    ```

---

## Pandas 기초 — 5개 API로 80% 커버

### 📋 필수 5대 API

| API | 용도 | 예시 |
|-----|------|------|
| `read_csv` | CSV 읽기 | `pd.read_csv('data.csv')` |
| `head / info / describe` | 탐색 | `df.describe()` |
| `fillna / dropna` | 결측 처리 | `df.fillna(0)` |
| `groupby` | 그룹 집계 | `df.groupby('category').sum()` |
| `merge` | 데이터 조인 | `pd.merge(a, b, on='id')` |

### 🚀 실전 예제: 매출 데이터 분석

```python
import pandas as pd

# 1. 데이터 로딩
df = pd.read_csv('sales.csv')

# 2. 기본 탐색
print(df.head())           # 상위 5행
print(df.info())           # 컬럼 타입 + 결측치 개수
print(df.describe())       # 수치형 기초 통계

# 3. 데이터 정제
df = df.fillna(df.mean(numeric_only=True))  # 결측 → 평균으로
df = df.drop_duplicates()                   # 중복 제거

# 4. 분석 - 카테고리별 매출 합계
category_sales = df.groupby('category')['sales'].sum()
print(category_sales.sort_values(ascending=False))

# 5. 상관관계 분석
correlation = df.corr(numeric_only=True)
print(correlation)
```

예상 출력:

```
category
Electronics    1250000
Books           890000
Clothing        720000
Name: sales, dtype: int64
```

### 💡 실무 꿀팁

!!! tip "💡 꿀팁: 탐색 단계 3종 세트"
    새로운 데이터를 받으면 항상 **이 3줄을 먼저** 실행하세요.

    ```python
    df.head()       # 어떤 컬럼이 있나
    df.info()       # 타입과 결측은 어떤가
    df.describe()   # 숫자 분포는 어떤가
    ```

    이 3줄이 당신의 시간을 몇 시간씩 아껴줍니다.

!!! warning "⚠️ 자주 하는 실수: 체이닝 중 원본 수정"
    ```python
    # 나쁜 예 (경고 발생)
    df[df['age'] > 20]['salary'] = 1000

    # 좋은 예
    df.loc[df['age'] > 20, 'salary'] = 1000
    ```

---

## 시각화 — Matplotlib + Seaborn

### 🎨 4가지 차트만 익히자

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 분포 (히스토그램)
sns.histplot(df['sales'], bins=30)
plt.title('매출 분포')
plt.show()

# 2. 비교 (박스플롯)
sns.boxplot(x='category', y='sales', data=df)
plt.title('카테고리별 매출 비교')
plt.show()

# 3. 관계 (산점도)
sns.scatterplot(x='price', y='sales', hue='category', data=df)
plt.title('가격-매출 관계')
plt.show()

# 4. 상관관계 (히트맵)
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('상관관계 히트맵')
plt.show()
```

!!! tip "💡 꿀팁: 한글 폰트 깨짐 해결"
    Matplotlib에서 한글이 네모로 나오면 아래 코드를 노트북 맨 위에 추가하세요.

    ```python
    import matplotlib.pyplot as plt
    import platform

    if platform.system() == 'Windows':
        plt.rcParams['font.family'] = 'Malgun Gothic'
    elif platform.system() == 'Darwin':  # macOS
        plt.rcParams['font.family'] = 'AppleGothic'
    plt.rcParams['axes.unicode_minus'] = False
    ```

---

## 머신러닝 기초 — scikit-learn 3단계 파이프라인

대부분의 기초 머신러닝 문제는 **3단계 파이프라인**으로 해결됩니다.

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. 데이터 분할
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. 스케일링
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. 학습 + 예측
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)

print(f"정확도: {accuracy_score(y_test, predictions):.2%}")
```

예상 출력:

```
정확도: 87.50%
```

---

## Streamlit — 파이썬만으로 대시보드 만들기

**Streamlit**은 Python 스크립트 한 개로 웹 대시보드를 만드는 도구입니다. HTML/CSS/JS 몰라도 됩니다.

### 🚀 15분 퀵스타트 — 실전 대시보드

`dashboard.py`

```python
import streamlit as st
import pandas as pd

st.title('매출 대시보드')

# 사이드바: 데이터 업로드
uploaded = st.sidebar.file_uploader('CSV 파일 업로드', type='csv')
if uploaded is None:
    st.info('먼저 CSV 파일을 업로드하세요.')
    st.stop()

df = pd.read_csv(uploaded)

# KPI 4개
col1, col2, col3, col4 = st.columns(4)
col1.metric('총 매출', f"{df['sales'].sum():,}원")
col2.metric('평균 가격', f"{df['price'].mean():,.0f}원")
col3.metric('주문 수', f"{len(df):,}건")
col4.metric('카테고리 수', df['category'].nunique())

# 필터
category = st.selectbox('카테고리 선택', df['category'].unique())
filtered = df[df['category'] == category]

# 시계열 차트
st.subheader(f'{category} 일별 매출')
daily = filtered.groupby('date')['sales'].sum()
st.line_chart(daily)

# 데이터 테이블
st.subheader('원본 데이터')
st.dataframe(filtered)
```

실행:

```bash
streamlit run dashboard.py
```

예상 출력:

```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트: 데이터 탐색"
    > "내 sales.csv(컬럼: date, category, price, sales)를 Pandas로 분석해줘. 결측치 처리 → 일별 매출 추이 → 카테고리별 Top 5 → 가격-매출 상관관계 순서로 코드와 결과 해석을 작성해줘."

!!! example "🤖 Claude Code 프롬프트: 대시보드 생성"
    > "내 CSV 파일(컬럼: date, category, sales)로 Streamlit 대시보드를 만들어줘. KPI 4개 + 시계열 차트 + 카테고리 필터 + 원본 테이블 포함. 한글 폰트 문제도 해결해줘."

!!! example "🤖 Claude Code 프롬프트: 머신러닝 파이프라인"
    > "내 데이터의 'churn' 컬럼을 예측하는 scikit-learn 파이프라인을 만들어줘. 전처리 → 훈련/테스트 분할 → RandomForest → 평가(정확도, F1, Confusion Matrix)까지. 왜 RandomForest를 선택했는지 설명도 해줘."

### 📚 학습 체크리스트

- [ ] Pandas 5대 API 실습 완료
- [ ] 공공 데이터(data.go.kr)로 분석 리포트 1개 작성
- [ ] Seaborn 4가지 차트 그려보기
- [ ] scikit-learn 3단계 파이프라인 실행
- [ ] Streamlit 대시보드 1개 배포 (streamlit.io/cloud 무료)

!!! warning "⚠️ 자주 하는 실수"
    **"분석 결과"만 자랑하고 "해석"을 빠뜨리는 것**.
    면접이나 발표에서는 차트보다 **"그래서 뭐?(So what?)"**가 훨씬 중요합니다.
    항상 "이 차트가 의미하는 비즈니스 인사이트"를 한 줄로 요약하세요.

---

## 추천 무료 데이터셋

| 출처 | 데이터 종류 | 링크 |
|------|------------|------|
| 공공데이터포털 | 한국 정부/공공 | https://data.go.kr |
| Kaggle | 전 세계 실무 | https://kaggle.com/datasets |
| UCI ML Repo | 머신러닝 학습용 | https://archive.ics.uci.edu/ml |
| 서울 열린데이터광장 | 서울시 데이터 | https://data.seoul.go.kr |

---

!!! tip "💡 다음 단계"
    Part 1 기초를 마치셨다면 축하드려요! 🎉
    이제 [Part 2: 프레임워크 / 언어별 학습](../part2-frameworks/index.md)으로 넘어가
    Spring Boot나 React 같은 본격적인 스택을 공부하실 차례입니다.
