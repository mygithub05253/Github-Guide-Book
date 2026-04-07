# Part 3: 프로젝트 및 공모전 활용

> 실전 프로젝트 경험을 쌓고, 포트폴리오를 만들고, 오픈소스에 기여하는 방법을 다룹니다.

## 학습 목표
- 풀스택 프로젝트 템플릿 활용
- 포트폴리오 구축 전략
- 오픈소스 기여 방법
- 해커톤/공모전 준비

---



## 3-1. 풀스택 프로젝트 템플릿

### 3-1-1. RealWorld (gothinkster/realworld)
**GitHub Stars**: 80K+
**프로젝트 설명**: Medium 클론 애플리케이션 - 모든 주요 프레임워크로 구현된 풀스택 프로젝트
**용도**: 풀스택 개발자 역량 증명용 포트폴리오 프로젝트

#### 개요
RealWorld는 다양한 프레임워크(Spring Boot, React, Django, Node.js 등)로 동일한 애플리케이션을 구현한 메가 레포입니다. 블로그 플랫폼인 "Conduit"을 구현하며, 사용자 인증, 게시물 CRUD, 팔로우 기능, 즐겨찾기 등을 포함합니다.

#### 설치 방법

```bash
# RealWorld 레포 클론
git clone https://github.com/gothinkster/realworld.git
cd realworld

# 원하는 백엔드 구현 선택 (예: Spring Boot)
cd implementations/spring-boot-gradle-jpa

# 의존성 설치
./gradlew build

# 데이터베이스 설정 (application.yml)
# spring.datasource.url: jdbc:h2:mem:testdb
# spring.jpa.hibernate.ddl-auto: create-drop
```

#### 핵심 코드 구조

**User 도메인 (Spring Boot)**
```java
@Entity
@Getter
@Setter
@NoArgsConstructor
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true)
    private String username;

    @Column(unique = true)
    private String email;

    private String password;
    private String bio;
    private String image;

    @OneToMany(mappedBy = "author")
    private List<Article> articles = new ArrayList<>();

    @ManyToMany
    @JoinTable(
        name = "user_followers",
        joinColumns = @JoinColumn(name = "user_id"),
        inverseJoinColumns = @JoinColumn(name = "follower_id")
    )
    private Set<User> followers = new HashSet<>();
}
```

**Article 도메인**
```java
@Entity
@Getter
@Setter
public class Article {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String slug;
    private String title;
    private String description;
    private String body;

    @CreationTimestamp
    private LocalDateTime createdAt;

    @UpdateTimestamp
    private LocalDateTime updatedAt;

    @ManyToOne
    private User author;

    @ManyToMany
    @JoinTable(name = "article_favorites")
    private Set<User> favoritedBy = new HashSet<>();

    @ElementCollection
    private List<String> tagList = new ArrayList<>();
}
```

**Article Service**
```java
@Service
@RequiredArgsConstructor
public class ArticleService {
    private final ArticleRepository articleRepository;
    private final UserRepository userRepository;

    public ArticleResponse createArticle(String username, CreateArticleRequest request) {
        User author = userRepository.findByUsername(username)
            .orElseThrow(() -> new UserNotFoundException("User not found"));

        Article article = new Article();
        article.setTitle(request.getTitle());
        article.setDescription(request.getDescription());
        article.setBody(request.getBody());
        article.setAuthor(author);
        article.setSlug(generateSlug(request.getTitle()));
        article.setTagList(request.getTagList());

        Article saved = articleRepository.save(article);
        return ArticleResponse.fromArticle(saved);
    }

    public Page<ArticleResponse> listArticles(Pageable pageable, String author, String tag) {
        Specification<Article> spec = (root, query, cb) -> cb.conjunction();

        if (author != null) {
            spec = spec.and((root, query, cb) ->
                cb.equal(root.get("author").get("username"), author)
            );
        }

        if (tag != null) {
            spec = spec.and((root, query, cb) ->
                cb.isMember(tag, root.get("tagList"))
            );
        }

        return articleRepository.findAll(spec, pageable)
            .map(ArticleResponse::fromArticle);
    }
}
```

#### 실전 활용 시나리오

**시나리오 1: 본인 기술스택 선택 후 확장**
- Spring Boot 백엔드 + React 프론트엔드 조합으로 시작
- 댓글 기능, 실시간 알림, 고급 검색 추가
- 포트폴리오로 GitHub에 공개

**시나리오 2: 데이터베이스 최적화 연습**
- H2 → PostgreSQL 마이그레이션
- N+1 문제 해결 (Eager Loading vs Lazy Loading)
- 복합 인덱스 추가로 성능 개선

**시나리오 3: 배포 파이프라인 구축**
- Docker 컨테이너화
- GitHub Actions CI/CD
- 클라우드 배포 (AWS EC2, Heroku)

#### Claude Code 연동 팁

```
/think → RealWorld 아키텍처 분석
- Entity 관계 다이어그램 생성
- API 엔드포인트 설계 검토

/review → 코드 품질 검토
- JPA 쿼리 최적화 제안
- 에러 처리 개선 방안

/test → 테스트 케이스 자동 생성
- ArticleService 단위 테스트
- 통합 테스트 시나리오
```

---

### 3-1-2. Full Stack FastAPI Template
**GitHub Stars**: 28K+
**프로젝트 설명**: FastAPI + React + PostgreSQL + Docker 완전한 풀스택 보일러플레이트
**용도**: 빠른 프로젝트 시작, 현대적 스택 학습

#### 개요
tiangolo/full-stack-fastapi-template는 프로덕션 레벨의 풀스택 템플릿입니다. Docker Compose로 모든 서비스를 한 번에 실행하고, JWT 인증, SQLAlchemy ORM, React 상태 관리를 포함합니다.

#### 설치 방법

```bash
# 레포 클론
git clone https://github.com/tiangolo/full-stack-fastapi-template.git
cd full-stack-fastapi-template

# Docker Compose로 전체 스택 실행
docker-compose up -d

# 브라우저에서 확인
# 프론트엔드: http://localhost:3000
# API 문서: http://localhost:8000/docs
```

#### 핵심 코드 구조

**FastAPI User 모델**
```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()

class UserBase(BaseModel):
    email: str
    full_name: str = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

@app.post("/api/v1/users/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user
```

**SQLAlchemy ORM**
```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
```

**JWT 인증**
```python
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from jose import JWTError, jwt
from datetime import timedelta

security = HTTPBearer()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=24)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(credentials: HTTPAuthCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401)
    except JWTError:
        raise HTTPException(status_code=401)

    user = crud.get_user_by_email(db, username)
    return user
```

**React + Axios 프론트엔드**
```typescript
// src/api/users.ts
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

interface User {
  id: number;
  email: string;
  full_name: string;
}

export const createUser = async (email: string, password: string): Promise<User> => {
  const response = await axios.post(`${API_URL}/users/`, {
    email,
    password,
    full_name: '',
  });
  return response.data;
};

export const getUser = async (token: string): Promise<User> => {
  const response = await axios.get(`${API_URL}/users/me`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};
```

#### 실전 활용 시나리오

**시나리오 1: SaaS 애플리케이션 시작**
- 기본 템플릿을 프로덕션 배포
- Stripe 결제 통합
- 사용자 조직 및 권한 관리 추가

**시나리오 2: 마이크로서비스 분할**
- FastAPI 백엔드를 여러 서비스로 분리
- 각 서비스별 독립적 배포
- API Gateway 구성

**시나리오 3: 성능 최적화**
- Redis 캐싱 계층 추가
- 데이터베이스 연결 풀 최적화
- CDN으로 정적 자산 배포

#### Claude Code 연동 팁

```
/plan-eng-review → 아키텍처 리뷰
- 마이크로서비스 분할 계획
- 확장성 제안

/qa → 테스트 자동 생성
- FastAPI 엔드포인트 테스트
- React 컴포넌트 테스트
```

---

### 3-1-3. Redoc: API 문서화 도구
**GitHub Stars**: 24K+
**프로젝트 설명**: OpenAPI 스펙을 아름다운 문서로 변환하는 도구
**용도**: API 문서 자동화, 개발자 경험 향상

#### 개요
Redoc는 OpenAPI 3.0 스펙을 기반으로 인터랙티브한 API 문서를 자동 생성합니다. Swagger UI와 달리 Try It Out은 없지만, 매우 깔끔하고 모바일 친화적인 UI를 제공합니다.

#### 설치 방법

```bash
# npm으로 설치
npm install redoc redoc-cli

# CLI로 정적 HTML 생성
npx redoc-cli build openapi.yaml -o index.html

# 또는 React 컴포넌트로 사용
npm install redoc react
```

#### 핵심 코드 구조

**OpenAPI 스펙 작성 (openapi.yaml)**

RealWorld 스펙은 아래 요소를 중심으로 구성됩니다. 전체 YAML은 레포의 `api/` 폴더에서 바로 확인할 수 있습니다.

- `info`: title, version, description
- `servers`: Production/Staging URL
- `paths`: `/api/articles` (GET/POST), `/api/articles/{slug}`, `/api/users/login` 등
- `components.schemas`: Article, Profile, ArticleCreate (필수 필드: title/description/body)
- `components.securitySchemes`: BearerAuth (JWT)

**React에서 Redoc 렌더링**
```typescript
import React from 'react';
import { ReDocStandalone } from 'redoc';

export const ApiDocumentation = () => {
  return (
    <ReDocStandalone
      specUrl="https://api.realworld.io/openapi.yaml"
      options={{
        scrollYOffset: 50,
        hideDownloadButton: false,
        hideHostname: false,
        hideLoading: false,
        suppressWarnings: false,
        expandResponses: '200,201',
      }}
    />
  );
};
```

**FastAPI에서 자동 OpenAPI 생성**
```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="RealWorld API",
    description="Medium Clone API",
    version="1.0.0",
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="RealWorld API",
        version="1.0.0",
        description="Medium Clone API",
        routes=app.routes,
    )

    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# http://localhost:8000/redoc 에서 문서 자동 렌더링
```

#### 실전 활용 시나리오

**시나리오 1: 자동 API 문서화**
- FastAPI/Spring Boot 코드에서 자동 생성
- CI/CD 파이프라인에 통합
- 배포 시 최신 문서 자동 반영

**시나리오 2: 개발자 포털 구축**
- Redoc + 추가 가이드 페이지
- 인증 토큰 테스트
- 자동화된 SDK 생성

**시나리오 3: 버전 관리**
- 여러 API 버전 문서 병렬 운영
- 마이그레이션 가이드 제공

#### Claude Code 연동 팁

```
/think → OpenAPI 스펙 설계
- 엔드포인트 구조 분석
- 요청/응답 모델 최적화

/document-release → 자동 문서 생성
- OpenAPI YAML 자동 정리
- 배포용 HTML 생성
```

---

## 3-2. 포트폴리오 & 오픈소스 기여

### 3-2-1. First Contributions
**GitHub Stars**: 46K+
**프로젝트 설명**: 오픈소스 첫 기여 가이드 - PR 만드는 법 배우기
**용도**: 깃/GitHub 기초 학습, 오픈소스 기여 시작

#### 개요
first-contributions/first-contributions는 오픈소스 첫 PR을 쉽게 만들 수 있도록 도와주는 튜토리얼입니다. 15개 이상 언어로 작성되었고, 간단한 PR 하나로 오픈소스 기여 경험을 얻을 수 있습니다.

#### 설치 방법

```bash
# 1. 레포 Fork (GitHub 웹사이트에서)
# https://github.com/firstcontributions/first-contributions

# 2. 로컬에 클론
git clone https://github.com/<your-username>/first-contributions.git
cd first-contributions

# 3. upstream 리모트 추가
git remote add upstream https://github.com/firstcontributions/first-contributions.git
```

#### 기본 워크플로우

**Step 1: 브랜치 생성**
```bash
git checkout -b add-<your-name>
```

**Step 2: Contributors 파일에 이름 추가**

`CONTRIBUTORS.md` 파일의 Contributors 섹션에 `- [Your Name](https://github.com/your-username)` 형식으로 한 줄 추가합니다.

**Step 3: 변경 커밋**
```bash
git add CONTRIBUTORS.md
git commit -m "Add <your-name> to Contributors"
```

**Step 4: GitHub에 푸시 및 PR 생성**
```bash
git push origin add-<your-name>
```

#### 실전 활용 시나리오

**시나리오 1: 첫 오픈소스 경험**
- 이 레포에서 첫 PR 완성
- GitHub 프로필에 표시됨
- 오픈소스 문화 이해

**시나리오 2: 오픈소스 기여 스킬 다졌기**
- 더 큰 프로젝트로 진출
- 버그 리포트 → 픽스 → PR
- 포트폴리오 다양화

#### Claude Code 연동 팁

```
/think → Git 워크플로우 정리
- Fork vs Clone 차이
- Upstream sync 방법

/document-release → PR 템플릿 검토
- 설명 명확성 검증
- 커밋 메시지 개선
```

---

### 3-2-2. Awesome for Beginners
**GitHub Stars**: 70K+
**프로젝트 설명**: 초보자 친화 오픈소스 레포 모음
**용도**: 기여할 만한 레포 발견, 실전 기여 경험

#### 개요
MunGell/awesome-for-beginners는 "good first issue" 라벨이 있는 오픈소스 레포들을 한 곳에 모아놨습니다. 각 레포마다 난이도, 언어, 설명이 있어 초보자가 쉽게 기여할 수 있는 프로젝트를 찾을 수 있습니다.

#### 레포지토리 선택 가이드 (Python 초보자용 추천)

- **First Contributions** — 난이도 ⭐, 모든 언어, Git/GitHub 기본 학습
- **Up For Grabs** — 난이도 ⭐⭐, JavaScript/Python/C#, 초보자 태스크 수집 사이트
- **Exercism** — 난이도 ⭐⭐⭐, Python/JavaScript/Ruby 등, 코딩 연습 + 코드 리뷰
- **PySimpleGUI** — 난이도 ⭐⭐, Python, GUI 프로그래밍 입문

#### 기여 전략

**1단계: 좋은 이슈 찾기**
```bash
# GitHub 검색
site:github.com label:"good first issue" language:python

# 또는 awesome-for-beginners에서 추천 레포 선택
```

**2단계: 이슈 분석 체크리스트**

- [ ] 이슈 설명을 완전히 이해했는가
- [ ] 요구 사항이 명확한가
- [ ] 내 스킬 레벨에 맞는가
- [ ] 관련 문서/가이드가 있는가

**3단계: 코드 작성**
```python
# 예: 간단한 버그 픽스
# Before
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item.price  # 버그: 할인 미적용
    return total

# After
def calculate_total(items):
    total = 0
    for item in items:
        total = total + (item.price * (1 - item.discount))
    return total
```

**4단계: PR 작성**

PR 본문에는 아래 항목이 포함되면 리뷰가 빨라집니다.

- 설명: 어떤 이슈(#123)를 해결하는지
- 변경 사항: 핵심 수정 3-5줄 bullet
- 테스트 결과: `pytest -v` 등 실제 실행 결과
- 체크리스트: 테스트/문서/커밋 메시지 확인

#### 실전 활용 시나리오

**시나리오 1: 3개월 도전**
- 매주 1개 레포 기여
- 다양한 프로젝트 경험
- 포트폴리오 빠른 구축

**시나리오 2: 특정 기술 집중**
- Python 데이터 분석 라이브러리 기여
- 관련 기술 깊이 있게 학습
- 해당 분야 전문가 이미지 구축

#### Claude Code 연동 팁

```
/think → 이슈 분석
- 요구사항 분해
- 구현 전략 수립

/review → PR 품질 검증
- 코드 스타일 검토
- 테스트 커버리지 확인

/qa → 자동 테스트 생성
- 엣지 케이스 테스트
- 통합 테스트 작성
```

---

### 3-2-3. GitHub Opensource Guide
**GitHub Stars**: 14K+
**프로젝트 설명**: 오픈소스 프로젝트 운영 가이드
**용도**: 오픈소스 프로젝트 시작, 커뮤니티 관리

#### 개요
github/opensource.guide는 오픈소스 프로젝트를 시작하고 운영하는 방법을 다룹니다. 라이선스, 기여 가이드, 커뮤니티 구성, 지속성 확보 등을 포함합니다.

#### 필수 문서 체크리스트

**1. 기본 설정**: README.md, LICENSE(MIT/Apache 2.0/GPL 등), .gitignore, CONTRIBUTING.md
**2. 코드 구조**: 명확한 폴더 구조, 설치 가이드, 사용 예제, API 문서
**3. 커뮤니티**: CODE_OF_CONDUCT.md, Issue 템플릿, PR 템플릿, Discussions
**4. 자동화**: GitHub Actions CI/CD, 자동 테스트, 문서 배포, 릴리스 자동화

#### 핵심 문서 작성

**README.md 템플릿 구성 요소**

- 프로젝트 타이틀 + Shields.io 배지(Stars, License, Build 등)
- 한 줄 설명(tagline)
- 기능 목록(bullet)
- 설치 명령어 (bash 코드 블록)
- 사용 예제 (주 언어 코드 블록)
- 기여 안내 (CONTRIBUTING.md 링크)
- 라이선스 표기

**CONTRIBUTING.md 구성 요소**

- 개발 환경 설정(clone/install/dev 명령)
- 커밋 메시지 규칙: Conventional Commits (`feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`)
- PR 프로세스: Fork → 브랜치 생성 → 커밋 → PR → 리뷰 → 병합

**CODE_OF_CONDUCT.md 구성 요소**

- 우리의 약속(존중, 건설적 피드백)
- 허용되지 않는 행동(괴롭힘, 차별, 욕설)
- 위반 보고 연락처

> Claude Code 활용 팁
> `> "github/opensource.guide를 참고해서 내 프로젝트(주제: xxx)용 README/CONTRIBUTING/CODE_OF_CONDUCT 초안을 만들어줘"`

#### 실전 활용 시나리오

**시나리오 1: 개인 프로젝트 오픈소스화**
- 실무 프로젝트를 GitHub에 공개
- 가이드 따라 필수 문서 작성
- 첫 기여자 모으기

**시나리오 2: 팀 프로젝트 관리**
- 자동화된 이슈/PR 관리
- 릴리스 프로세스 정립
- 커뮤니티 성장 전략

#### Claude Code 연동 팁

```
/document-release → 문서 자동화
- README 템플릿 생성
- API 문서 자동 추출
- 릴리스 노트 작성

/cso → 보안 및 라이선스 검토
- 라이선스 호환성 확인
- 보안 정책 수립
```

---

## 3-3. 해커톤 & 공모전

### 3-3-1. Hackathon Starter
**GitHub Stars**: 35K+
**프로젝트 설명**: Node.js + Express + MongoDB 해커톤 보일러플레이트
**용도**: 해커톤 빠른 시작, Passport.js 인증 학습

#### 개요
sahat/hackathon-starter는 웹 앱 기초(회원가입, 로그인, 소셜 로그인, API)를 포함한 완성된 스타터 템플릿입니다. 해커톤에서 2-3시간 내에 기본 백엔드를 완성하고 핵심 기능 개발에 집중할 수 있습니다.

#### 설치 및 설정

```bash
# 클론
git clone https://github.com/sahat/hackathon-starter.git
cd hackathon-starter

# 의존성 설치
npm install

# .env 파일 설정
cp .env.example .env

# MongoDB 연결 (로컬 또는 MongoDB Atlas)
# MONGODB_URI=mongodb://localhost/hackathon

# 개발 서버 실행
npm run dev
```

#### 핵심 코드: 인증

**Passport 설정**
- `config/passport.js`에서 `LocalStrategy`로 email/password 인증을 설정하고, `serializeUser`/`deserializeUser`로 세션을 유지합니다.
- 레포의 해당 파일을 그대로 복사해서 쓸 수 있도록 정리되어 있어 해커톤에서 시간 낭비가 없습니다.

**User 모델**
- `models/User.js`에서 Mongoose 스키마로 email/password/profile/provider를 정의합니다.
- `pre('save')` 훅으로 bcrypt 해싱, `comparePassword` 메서드로 로그인 검증.

**라우트 및 컨트롤러**
- `/signup`, `/login`, `/logout`, `/profile` (GET/PUT) 엔드포인트가 `routes/user.js`에 모두 구현돼 있습니다.
- 인증 보호는 `ensureAuthenticated` 미들웨어 하나로 처리.

**소셜 로그인 (Google)**
- `passport-google-oauth20`를 추가하고 `GOOGLE_ID`/`GOOGLE_SECRET` 환경변수만 설정하면 됩니다.
- 콜백 URL은 `/auth/google/callback`으로 고정, 레포에 Facebook/GitHub/Twitter 전략도 함께 들어 있습니다.

> Claude Code 활용 팁
> `> "hackathon-starter의 passport 설정을 내 프로젝트에 맞게 이메일 인증만 쓰는 버전으로 축약해줘"`

#### 실전 활용 시나리오

**시나리오 1: 24시간 해커톤**
- 템플릿으로 1시간 내 기본 앱 완성
- 나머지 23시간 핵심 기능(AI, 데이터 분석 등) 개발
- 우승 가능성 높음

**시나리오 2: API 해커톤**
- 기본 인증 구조 재사용
- 다양한 API 엔드포인트 추가
- 빠른 프로토타입 배포

**시나리오 3: 학습용**
- Node.js + Express 기초 학습
- Passport.js 인증 패턴 이해
- MongoDB 스키마 설계 학습

#### Claude Code 연동 팁

```
/think → 해커톤 빠른 시작
- 필수 기능 분석
- 스케줄링

/plan-eng-review → 아키텍처 최적화
- API 엔드포인트 설계
- 데이터 모델 검증

/qa → 엣지 케이스 테스트
- 인증 플로우 테스트
- 에러 처리 검증
```

---

### 3-3-2. AutoGPT
**GitHub Stars**: 173K+
**프로젝트 설명**: 자율 AI 에이전트 구현 - OpenAI API 활용
**용도**: AI 해커톤, LLM 프로젝트, 자동화 학습

#### 개요
Significant-Gravitas/AutoGPT는 "AI 자신이 목표 달성을 위해 자동으로 작업을 수행"하는 개념의 구현입니다. 사용자가 목표를 주면 AI가 필요한 단계들을 스스로 계획하고 실행합니다. 최근 버전은 프로덕션 안정성을 강화했습니다.

#### 설치

```bash
# 클론
git clone https://github.com/Significant-Gravitas/AutoGPT.git
cd AutoGPT

# Python 환경
python -m venv venv
source venv/bin/activate  # 또는 venv\Scripts\activate (Windows)

# 의존성 설치
pip install -r requirements.txt

# OpenAI API 키 설정
export OPENAI_API_KEY="sk-..."

# 실행
python -m autogpt
```

#### 핵심 아키텍처

**Agent 패턴**
- LangChain의 `initialize_agent`로 LLM + Tools + Memory를 결합한 에이전트를 만듭니다.
- Tool은 `(name, func, description)` 삼총사로 등록합니다. 예: Calculator, Search, FileWrite.
- `agent.run(goal)` 한 줄로 목표를 던지면 에이전트가 스스로 도구를 선택해 실행합니다.

**Task Planning**
- `PromptTemplate` + `LLMChain`으로 "목표 → 단계별 계획" 변환을 구현합니다.
- 결과 텍스트를 줄 단위 파싱해 숫자로 시작하는 줄만 steps 리스트에 담으면 간단합니다.

**Memory System**
- `ConversationBufferMemory`는 최근 대화를 그대로 기억, `ConversationSummaryMemory`는 요약해서 기억합니다.
- AutoGPT는 두 메모리를 함께 써서 긴 세션에서도 맥락을 유지합니다.

> Claude Code 활용 팁
> `> "AutoGPT의 Agent 클래스를 읽고 내 프로젝트(주제 검색 → 마크다운 리포트 생성)에 맞게 최소 버전으로 줄여줘"`

#### 실전 활용 시나리오

**시나리오 1: AI 해커톤 우승**
- AutoGPT 기반 자동화 도구 개발
- 특정 도메인(예: 데이터 분석, 콘텐츠 생성) 최적화
- 사용자 피드백 반영 개선

**시나리오 2: 작업 자동화**
- 일일 리포트 자동 생성
- 이메일 응답 자동화
- 데이터 처리 파이프라인 구축

**시나리오 3: 교육/포트폴리오**
- LLM 기반 프로젝트 경험 제시
- AI 공학 기술 증명
- AI 회사 면접 준비

#### Claude Code 연동 팁

```
/think → 에이전트 설계
- Task planning 흐름
- Memory system 최적화
- Tool integration 전략

/review → 프롬프트 엔지니어링
- Few-shot 예제 추가
- 출력 형식 명확화
- Hallucination 방지

/qa → 테스트 자동화
- 에이전트 응답 검증
- 오류 처리 테스트
- 한국어 처리 검증
```

---

### 3-3-3. LangChain
**GitHub Stars**: 100K+
**프로젝트 설명**: LLM 애플리케이션 프레임워크
**용도**: AI 해커톤, RAG 시스템, LLM 체인 구축

#### 개요
langchain-ai/langchain은 LLM(Large Language Model) 기반 애플리케이션을 빠르게 개발하는 프레임워크입니다. Prompt 관리, 메모리, 검색, 도구 통합을 통합적으로 제공합니다.

#### 설치

```bash
pip install langchain openai python-dotenv
```

#### 기본 사용법

**Simple Chain**
```python
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0)

# 템플릿 정의
prompt = PromptTemplate(
    input_variables=["topic"],
    template="다음 주제에 대해 설명하시오: {topic}"
)

# 체인 생성
chain = LLMChain(llm=llm, prompt=prompt)

# 실행
result = chain.run("머신러닝")
print(result)
```

**Document Processing with RAG**
```python
from langchain.document_loaders import PDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# PDF 로드
loader = PDFLoader("document.pdf")
documents = loader.load()

# 텍스트 분할
text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
docs = text_splitter.split_documents(documents)

# 벡터 임베딩
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)

# RAG 체인 생성
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=db.as_retriever()
)

# 문서 기반 질의응답
answer = qa.run("문서의 주요 내용은?")
print(answer)
```

**Agent with Tools**
```python
from langchain.agents import initialize_agent, Tool
from langchain.tools import DuckDuckGoSearchRun
from langchain.llms import OpenAI

# 도구 정의
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="웹 검색 수행"
    ),
    Tool(
        name="Calculator",
        func=lambda x: eval(x),
        description="수학 계산"
    )
]

# 에이전트 초기화
agent = initialize_agent(
    tools,
    OpenAI(temperature=0),
    agent="zero-shot-react-description",
    verbose=True
)

# 실행
result = agent.run("2024년 한국 GDP 성장률은?")
```

**Memory Management**
```python
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.chains import ConversationChain

# 메모리 설정
memory = ConversationBufferMemory()

# 대화형 체인
conversation = ConversationChain(
    llm=OpenAI(),
    memory=memory,
    verbose=True
)

# 연속 대화
conversation.predict(input="안녕, 나는 데이터 과학자야")
conversation.predict(input="나의 경력을 요약해줄래?")
```

**Custom Chain**
```python
from langchain.schema import BaseMemory
from langchain.chains import Chain

class CustomChain(Chain):
    @property
    def input_keys(self):
        return ["user_input"]

    @property
    def output_keys(self):
        return ["response"]

    def _call(self, inputs):
        user_input = inputs["user_input"]

        # 커스텀 로직
        response = f"사용자가 입력한 내용: {user_input}"

        return {"response": response}

# 사용
chain = CustomChain()
result = chain({"user_input": "안녕하세요"})
```

#### 실전 활용 시나리오

**시나리오 1: 챗봇 개발**
- 컨텍스트 유지 메모리
- 다양한 도구 통합
- 자연스러운 대화 흐름

**시나리오 2: 문서 분석 시스템**
- RAG로 대규모 문서 처리
- 정확한 인용 기능
- 다중 언어 지원

**시나리오 3: 해커톤 프로젝트**
- 빠른 프로토타입 개발
- API 통합 간소화
- 복잡한 워크플로우 체인화

#### Claude Code 연동 팁

```
/think → 아키텍처 설계
- Chain 구성 전략
- Tool selection
- Memory strategy

/review → 프롬프트 최적화
- Temperature 조절
- Few-shot 예제 추가
- 출력 형식 지정

/qa → 통합 테스트
- 체인 정확성 검증
- 도구 호출 검증
```

이어서 카테고리 3를 작성하겠습니다.

---

