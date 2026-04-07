# 📘 FastAPI 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/tiangolo/fastapi.svg?style=social)](https://github.com/tiangolo/fastapi)

!!! info "레포지토리"
    **tiangolo/fastapi** · 78k+ ⭐ · MIT License · [fastapi.tiangolo.com](https://fastapi.tiangolo.com)

---

## 🧐 1. FastAPI는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: FastAPI는 **Python 3.8+의 타입 힌트를 기반으로 한 초고속 비동기 웹 프레임워크**입니다. Starlette(웹) + Pydantic(검증) 위에 구축되어 Node.js·Go급 성능을 냅니다.

### 핵심 특성
- **타입 힌트 기반 자동 검증**: 함수 시그니처에 타입만 적으면 입력 검증·문서화가 자동.
- **자동 OpenAPI 문서**: `/docs` (Swagger UI), `/redoc` 무료 제공.
- **비동기 우선**: `async def` 핸들러로 동시성 처리.
- **DI 컨테이너 내장**: `Depends()`로 의존성 주입.
- **Starlette 호환**: WebSocket, 백그라운드 태스크, 미들웨어 그대로 사용.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **AI/ML 모델 서빙 표준** | Hugging Face·LangChain 앱의 기본 백엔드 |
| **Django/Flask 대비 빠름** | TechEmpower 벤치마크 상위권 |
| **자동 문서화** | API 명세 작성 시간 0 |
| **Pydantic v2** | Rust 기반 검증으로 매우 빠름 |

## 🚀 2. 10분 퀵스타트

```bash
pip install "fastapi[standard]"
```

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PLAF Demo API")

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.get("/")
def root():
    return {"message": "Hello PLAF"}

@app.post("/items")
def create_item(item: Item):
    return {"received": item, "total": item.price * 1.1}
```

```bash
fastapi dev main.py
```

브라우저: `http://localhost:8000/docs` → 자동 생성된 Swagger UI에서 API 테스트.

## 🛠️ 3. 코드 해부학: 권장 프로젝트 구조

```
app/
├── main.py              # FastAPI() 인스턴스 + 라우터 등록
├── api/v1/              # 엔드포인트 (라우터)
│   └── users.py
├── schemas/             # Pydantic 모델 (요청/응답)
├── services/            # 비즈니스 로직
├── repositories/        # DB 접근 (SQLAlchemy)
├── models/              # ORM 모델
├── deps.py              # Depends() 함수 모음
└── core/config.py       # 환경 설정
```

| 계층 | 책임 |
|---|---|
| Router | 경로·HTTP 메서드·입력 검증 |
| Service | 트랜잭션·비즈니스 규칙 |
| Repository | DB CRUD |
| Schema | 외부 통신용 DTO (ORM 모델과 분리!) |

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 다음 FastAPI 엔드포인트를 리뷰해 줘:
- async/sync 혼용 문제
- N+1 쿼리 가능성
- Pydantic 응답 모델 누락
- 인증·인가 데코레이터 누락
순서로 지적하고 수정 코드 제시.
```

### 🔵 Gemini
```
FastAPI vs Django REST Framework vs Flask의 차이를
성능, 학습 곡선, 생태계, 적합한 프로젝트 규모 기준으로 비교 표로.
```

### 🟢 ChatGPT
```
"AI 이미지 분류 API"를 FastAPI로 만들려고 한다.
모델 로딩, 파일 업로드, 결과 캐싱, Docker 배포까지의
전체 구조와 핵심 코드를 설계해 줘.
```

### ⬛ Copilot
```python
# TODO: POST /users - SignupSchema 받아 User 생성
#   - 이메일 중복 검사, bcrypt 해싱, JWT 발급
```

## 🔗 5. 관련 레포 · 다음 단계
- 공식 문서: [fastapi.tiangolo.com](https://fastapi.tiangolo.com) (한국어 번역 우수)
- ORM: [SQLAlchemy 2.0](https://www.sqlalchemy.org), [SQLModel](https://sqlmodel.tiangolo.com)
- 마이그레이션: [Alembic](https://alembic.sqlalchemy.org)
- ASGI 서버: [Uvicorn](https://www.uvicorn.org), [Hypercorn](https://hypercorn.readthedocs.io)
- [LangChain 딥다이브](../../ai-ml/langchain/index.md) — FastAPI로 LangChain 앱 서빙
