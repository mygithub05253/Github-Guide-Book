# 📘 Express 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/expressjs/express.svg?style=social)](https://github.com/expressjs/express)

!!! info "레포지토리"
    **expressjs/express** · 65k+ ⭐ · MIT License · [expressjs.com](https://expressjs.com)

---

## 🧐 1. Express는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Express는 **Node.js 위의 가장 미니멀하고 유연한 웹 프레임워크**입니다. 강제하는 구조가 거의 없어 자유도가 높지만, 그만큼 아키텍처 책임은 개발자에게 있습니다.

### 핵심 특성
- **미니멀 코어**: 라우팅 + 미들웨어 체인이 전부.
- **거대 미들웨어 생태계**: `body-parser`, `cors`, `helmet`, `morgan` 등 npm 표준 패키지.
- **유연성**: 어떤 ORM·템플릿·DB와도 결합 가능.
- **사실상 표준**: NestJS, Next.js API, Strapi 등이 내부적으로 Express 호환.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **빠른 프로토타입** | 10줄로 REST 서버 |
| **마이크로서비스의 작은 조각** | 단일 책임 서비스에 적합 |
| **러닝 자료 압도적** | 거의 모든 Node 튜토리얼이 Express 기반 |

## 🚀 2. 10분 퀵스타트

```bash
mkdir my-express && cd my-express
npm init -y
npm install express
```

```js
// app.js
const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
  res.json({ message: 'Hello PLAF' });
});

app.post('/echo', (req, res) => {
  res.json({ youSent: req.body });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Listening on ${PORT}`));
```

```bash
node app.js
```

## 🛠️ 3. 코드 해부학: 권장 폴더 구조

```
src/
├── app.js              # express() 인스턴스 + 미들웨어
├── routes/             # 라우터 모듈
├── controllers/        # 요청 처리
├── services/           # 비즈니스 로직
├── repositories/       # DB 접근
├── middlewares/        # 인증·로깅·에러
└── config/             # 환경 설정
```

!!! warning "구조를 직접 잡아야 함"
    Express는 강제 구조가 없습니다. 신규 프로젝트라면 처음부터 **Layered Architecture**를 적용하세요. 그렇지 않으면 1000줄짜리 `app.js`가 됩니다.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 이 Express 앱의 미들웨어 순서를 리뷰해 줘.
helmet, cors, rate-limit, body-parser, auth, route, error-handler
순서가 적절한지 보안 관점에서 분석.
```

### 🔵 Gemini
```
Express vs Fastify vs Koa vs NestJS를 비교 표로 정리해 줘.
성능, DX, 생태계, 적합 규모 기준으로.
```

### 🟢 ChatGPT
```
"파일 업로드 API"를 Express + Multer + S3로 설계해 줘.
검증·에러 처리·테스트까지 포함.
```

### ⬛ Copilot
```js
// TODO: errorHandler 미들웨어 - 4xx/5xx 분기, 로깅, JSON 응답
```

## 🔗 5. 관련 레포 · 다음 단계
- 공식 문서: [expressjs.com](https://expressjs.com)
- 차세대 대안: [Fastify](https://fastify.dev), [Koa](https://koajs.com), [Hono](https://hono.dev)
- 구조화된 선택: [NestJS 딥다이브](../nestjs/index.md)
