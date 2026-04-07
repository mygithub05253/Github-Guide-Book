# 3-1. 풀스택 프로젝트 템플릿

> "이력서에 쓸 만한 프로젝트가 없어요..." 라는 고민, 이 세 레포로 끝낼 수 있어요. 모두 **실제 서비스 수준**의 아키텍처를 따르기 때문에, 포트폴리오 레포로도 손색이 없습니다.

---

## 3-1-1. RealWorld (gothinkster/realworld) — 80K+ Stars

**한 줄 소개**: Medium 클론 "Conduit"을 **모든 주요 프레임워크**(Spring Boot, React, Django, Node.js, Rails, Go...)로 구현해놓은 메가 레포.

**왜 봐야 하는가**: 한 가지 스펙(API + 기능)을 기준으로 **내가 아는 언어와 내가 모르는 언어의 구현을 비교**할 수 있어요. "Spring Boot에선 이렇게 짜는데, FastAPI는 어떻게 짤까?"에 대한 **정답지**가 되어줍니다.

**난이도**: ⭐⭐⭐ (중급. JPA/ORM과 REST API 기초는 알고 들어와야 해요)

### 📋 이 레포에서 배울 수 있는 것

- 블로그 플랫폼의 **표준 도메인 설계** (User, Article, Comment, Tag, Follow, Favorite)
- JWT 기반 인증/인가 플로우
- N+1 문제가 실제로 어떻게 발생하는지, 그리고 어떻게 푸는지
- 같은 API 스펙을 **언어별로 어떻게 다르게 표현**하는지
- OpenAPI(Swagger) 스펙 작성 실전 예시

### 🚀 15분 퀵스타트

#### Step 1: 레포 클론 및 원하는 스택 선택

```bash
git clone https://github.com/gothinkster/realworld.git
cd realworld
ls implementations/    # 사용 가능한 구현 목록 확인
```

!!! info "예상 출력"
    ```
    spring-boot-gradle-jpa  django  node-express  rails  go-gin
    react-redux  vue  angular  svelte  ...  (30개 이상)
    ```

#### Step 2: Spring Boot 백엔드 선택 후 빌드

```bash
cd implementations/spring-boot-gradle-jpa
./gradlew build
```

#### Step 3: 실행

```bash
./gradlew bootRun
```

!!! info "예상 출력"
    ```
    Started ApplicationKt in 3.241 seconds (JVM running for 3.578)
    Tomcat started on port(s): 8080 (http)
    ```

#### Step 4: API 테스트

```bash
curl -X POST http://localhost:8080/api/users \
  -H "Content-Type: application/json" \
  -d '{"user":{"username":"kim","email":"kim@test.com","password":"pass1234"}}'
```

!!! info "예상 출력"
    ```json
    {"user":{"email":"kim@test.com","username":"kim","bio":null,"image":null,"token":"eyJhbGc..."}}
    ```

#### Step 5: React 프론트엔드 연결

```bash
cd ../../implementations/react-redux
npm install && npm start
```

브라우저에서 `http://localhost:3000` 접속 → 백엔드와 연결된 Medium 클론을 볼 수 있어요.

### 🏗 핵심 코드 구조 (Spring Boot)

**User 엔티티 — 관계 모델링의 교과서**

```java
@Entity
@Getter @Setter @NoArgsConstructor
public class User {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true) private String username;
    @Column(unique = true) private String email;
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

여기서 주목할 점은 **팔로우 관계를 ManyToMany로 풀었다**는 거예요. 초보자는 "User - Follow - User" 중간 테이블을 `@Entity`로 만들기 쉬운데, 단순한 관계는 `@JoinTable`로 충분합니다.

**Article Service — Specification을 활용한 동적 쿼리**

```java
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
```

!!! tip "💡 꿀팁: Specification 패턴은 면접 단골 질문"
    "동적 쿼리를 어떻게 처리하느냐"는 JPA 면접의 단골 질문이에요. Specification / QueryDSL / JPQL 중 **하나는 반드시** 직접 구현해본 경험이 있어야 합니다. RealWorld 코드는 Specification의 좋은 레퍼런스예요.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 아키텍처 다이어그램"
    ```
    implementations/spring-boot-gradle-jpa의 User, Article, Comment, Tag 엔티티를
    읽고 Mermaid ER 다이어그램을 그려줘. 관계(1:N, N:M)와 cascade 옵션도 표시해줘.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 내 스택으로 포팅"
    ```
    Spring Boot 구현의 Article 도메인을 FastAPI + SQLAlchemy로 옮겨줘.
    pydantic 스키마, CRUD 함수, 라우터까지 포함해서 한 번에 만들어줘.
    ```

!!! example "🤖 Claude Code 프롬프트 3: N+1 문제 찾기"
    ```
    ArticleService.listArticles() 메서드를 실행했을 때 발생할 수 있는
    N+1 쿼리를 전부 찾아주고, @EntityGraph 또는 fetch join으로 해결하는
    PR을 만들어줘. before/after의 SQL 로그도 같이 보여줘.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `Port 8080 already in use`"
    **원인**: 다른 Tomcat/Spring 앱이 이미 실행 중
    **해결**:
    ```bash
    # Windows
    netstat -ano | findstr :8080
    taskkill /PID <PID> /F
    ```
    또는 `application.yml`에서 `server.port: 8081`로 변경

!!! danger "🚨 에러 2: `LazyInitializationException`"
    **원인**: `@OneToMany`가 LAZY인데 트랜잭션 밖에서 접근
    **해결**: Service 메서드에 `@Transactional` 추가, 또는 DTO로 변환해서 반환
    **Claude Code 디버깅 프롬프트**:
    ```
    이 스택트레이스를 보고 어떤 메서드에서 LazyInitializationException이
    터진 건지 찾아주고, DTO 변환 시점을 수정해서 해결해줘.
    ```

!!! danger "🚨 에러 3: `Could not resolve placeholder 'jwt.secret'`"
    **원인**: `application.yml`에 JWT secret 값이 비어있음
    **해결**:
    ```yaml
    jwt:
      secret: my-very-long-secret-key-for-jwt-at-least-32-chars
    ```

### 📚 학습 체크리스트

- [ ] 한 개 스택(예: Spring Boot)으로 레포 로컬 실행 성공
- [ ] `/api/articles` GET 요청을 curl로 날려보고 응답 확인
- [ ] User → Article → Comment 엔티티 관계를 종이에 그려보기
- [ ] `Article.createdAt` 필드가 DB에서 언제 자동 세팅되는지 추적하기
- [ ] 프론트(React) + 백(Spring Boot)을 동시에 띄워서 글 작성/삭제 테스트
- [ ] JWT 토큰을 jwt.io에 붙여넣고 payload 내용 확인
- [ ] 기능 1개 추가 (예: 게시물 조회수 카운터) 후 커밋

---

## 3-1-2. Full Stack FastAPI Template (tiangolo/full-stack-fastapi-template) — 28K+ Stars

**한 줄 소개**: FastAPI + React + PostgreSQL + Docker가 전부 연결된 **프로덕션 레디** 템플릿.

**왜 봐야 하는가**: FastAPI 창시자 tiangolo가 직접 만든 템플릿이에요. "이게 정답이다" 수준의 구조를 보여주고, **Docker Compose 하나로 전체 스택이 즉시 뜬다**는 점이 미쳤습니다.

**난이도**: ⭐⭐⭐ (Docker 기초를 모르면 먼저 Docker 입문부터)

### 📋 이 레포에서 배울 수 있는 것

- FastAPI 프로젝트 **폴더 구조 베스트 프랙티스** (`app/api`, `app/crud`, `app/models`, `app/schemas`)
- SQLAlchemy 2.0 스타일 모델링
- Alembic 마이그레이션
- JWT 기반 인증 + OAuth2 Password flow
- Docker Compose로 백엔드 + 프론트 + DB + Adminer 동시 기동
- React + TypeScript + Chakra UI 연결

### 🚀 15분 퀵스타트

#### Step 1: 클론

```bash
git clone https://github.com/tiangolo/full-stack-fastapi-template.git
cd full-stack-fastapi-template
```

#### Step 2: 환경 변수 설정

```bash
cp .env.example .env
# .env 파일을 열어 SECRET_KEY, POSTGRES_PASSWORD를 변경
```

!!! warning "⚠️ 주의"
    `.env` 파일은 **절대 커밋하지 마세요**. `.gitignore`에 이미 들어있긴 하지만, 포트폴리오용으로 Fork했다면 Secrets가 실수로 공개되지 않았는지 반드시 확인하세요.

#### Step 3: Docker Compose 기동

```bash
docker compose up -d
```

!!! info "예상 출력"
    ```
    [+] Running 5/5
     ✔ Container fs-db-1         Started
     ✔ Container fs-backend-1    Started
     ✔ Container fs-frontend-1   Started
     ✔ Container fs-adminer-1    Started
     ✔ Container fs-proxy-1      Started
    ```

#### Step 4: 서비스 접속

| 서비스 | URL |
|---|---|
| 프론트엔드 | http://localhost:5173 |
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |
| Adminer (DB 관리) | http://localhost:8080 |

#### Step 5: 기본 관리자 계정으로 로그인

`.env`에 있는 `FIRST_SUPERUSER`, `FIRST_SUPERUSER_PASSWORD`를 사용해 `/docs`에서 `POST /api/v1/login/access-token`을 호출해보세요.

### 🏗 핵심 코드 패턴

**Pydantic 스키마 분리 전략**

```python
class UserBase(BaseModel):
    email: str
    full_name: str = None

class UserCreate(UserBase):
    password: str            # 생성 시에만 필요

class UserUpdate(UserBase):
    password: str | None = None

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True   # ORM 객체에서 자동 변환
```

!!! tip "💡 꿀팁: UserCreate와 User를 분리하는 이유"
    **보안**입니다. `User` 응답 스키마에 `password`가 들어있으면 API가 평문 비밀번호를 돌려주는 대참사가 터져요. Create/Read/Update를 항상 분리하는 습관을 들이세요.

**JWT 생성 함수**

```python
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(hours=24))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

**React에서 Axios로 API 호출**

```typescript
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

export const getCurrentUser = async (token: string) => {
  const { data } = await axios.get(`${API_URL}/users/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return data;
};
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 폴더 구조 학습"
    ```
    backend/app/ 하위 폴더 구조를 읽고, 각 폴더(api, core, crud, models, schemas)가
    어떤 역할을 하는지 한 문장씩 요약해줘. 그리고 초보자가 이 구조를 그대로 따라 해야 하는
    이유 3가지도 설명해줘.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 도메인 추가"
    ```
    이 템플릿에 "Todo" 도메인을 추가해줘. models/todo.py, schemas/todo.py,
    crud/todo.py, api/routes/todos.py를 만들고 기존 패턴을 그대로 따르도록 작성해줘.
    Alembic 마이그레이션 파일도 생성해줘.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 프로덕션 체크리스트"
    ```
    이 템플릿을 실제로 배포하기 전에 바꿔야 할 환경변수, 보안 설정, CORS 설정을
    체크리스트로 만들어줘. .env.example과 main.py를 기준으로 분석해줘.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `docker compose up` 에서 `exited with code 1`"
    **원인**: `.env`의 `POSTGRES_PASSWORD`가 비어있거나 특수문자 이스케이프 문제
    **해결**: `POSTGRES_PASSWORD=simplepass123` 처럼 영숫자만 써서 테스트

!!! danger "🚨 에러 2: `CORS policy blocked`"
    **원인**: 프론트 URL이 백엔드 CORS 허용 리스트에 없음
    **해결**: `backend/app/main.py`의 `BACKEND_CORS_ORIGINS`에 `http://localhost:5173` 추가

!!! danger "🚨 에러 3: `alembic upgrade head` 실패"
    **원인**: DB 컨테이너가 아직 준비 전
    **해결**:
    ```bash
    docker compose up -d db
    sleep 5
    docker compose exec backend alembic upgrade head
    ```

### 📚 학습 체크리스트

- [ ] Docker Compose로 전체 스택 기동 성공
- [ ] Swagger UI에서 로그인 → 토큰 발급 → 다른 API 호출까지 수행
- [ ] Adminer로 DB 테이블 구조 직접 확인
- [ ] 새 도메인 1개(예: `Memo`) 추가 및 마이그레이션 생성
- [ ] 프론트엔드에 페이지 1개 추가 후 백엔드 호출 연결
- [ ] `.env.example`의 모든 환경변수 의미 파악하기

---

## 3-1-3. Redoc (Redocly/redoc) — 24K+ Stars

**한 줄 소개**: OpenAPI 스펙을 **세상에서 가장 예쁜 API 문서**로 변환해주는 도구.

**왜 봐야 하는가**: Swagger UI는 실전용, Redoc은 **고객 대면용**이에요. 포트폴리오 API 문서를 Redoc으로 뽑으면 면접관이 먼저 "이 사람 일 좀 하네" 생각합니다.

**난이도**: ⭐⭐ (설정만 하면 끝. OpenAPI YAML만 알면 됨)

### 📋 이 레포에서 배울 수 있는 것

- OpenAPI 3.0 스펙 작성법
- API 문서를 정적 HTML로 뽑아 GitHub Pages에 올리는 법
- FastAPI/Spring Boot가 자동 생성하는 OpenAPI 스펙을 Redoc으로 렌더링하기
- 기업급 API 문서의 구성 요소(info, servers, paths, components, securitySchemes)

### 🚀 15분 퀵스타트

#### Step 1: 설치

```bash
npm install -g @redocly/cli
```

!!! info "예상 출력"
    ```
    added 234 packages in 12s
    ```

#### Step 2: 샘플 OpenAPI 파일 준비

```bash
curl -o openapi.yaml https://raw.githubusercontent.com/Redocly/redoc/main/demo/openapi.yaml
```

#### Step 3: 정적 HTML 생성

```bash
redocly build-docs openapi.yaml -o index.html
```

!!! info "예상 출력"
    ```
    Prerendering docs
    Bundling assets
    ✔ Created a bundle for index.html (2.34 MB)
    ```

#### Step 4: 로컬 서버로 미리보기

```bash
redocly preview-docs openapi.yaml
# http://localhost:8080 에서 확인
```

#### Step 5: GitHub Pages에 배포

`index.html`을 레포의 `docs/` 폴더에 넣고 Settings → Pages → Branch: main / folder: /docs 로 설정하면 끝.

### 🏗 OpenAPI 스펙 최소 예제

```yaml
openapi: 3.0.3
info:
  title: My Portfolio API
  version: 1.0.0
  description: 포트폴리오용 API 문서
servers:
  - url: https://api.example.com/v1
paths:
  /users/{id}:
    get:
      summary: 사용자 조회
      parameters:
        - name: id
          in: path
          required: true
          schema: { type: integer }
      responses:
        '200':
          description: 성공
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
components:
  schemas:
    User:
      type: object
      properties:
        id: { type: integer }
        email: { type: string }
        name: { type: string }
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: FastAPI에서 OpenAPI 추출"
    ```
    내 FastAPI 앱(backend/app/main.py)에서 /openapi.json을 가져와 파일로 저장하고,
    redocly build-docs 명령으로 정적 HTML을 만드는 npm 스크립트를 package.json에
    추가해줘.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 스펙 자동 생성"
    ```
    내 Spring Boot 프로젝트의 Controller를 전부 읽고 OpenAPI 3.0 yaml을 생성해줘.
    경로, 메서드, 요청/응답 DTO, 상태 코드를 다 포함해서 완성형으로 만들어줘.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 문서 품질 리뷰"
    ```
    내 openapi.yaml을 읽고 description이 비어있는 곳, 예제(example)가 없는 곳,
    보안 설정이 빠진 엔드포인트를 전부 찾아서 체크리스트로 만들어줘.
    ```

### 📚 학습 체크리스트

- [ ] Redocly CLI 설치 및 샘플 문서 빌드 성공
- [ ] 내 프로젝트의 OpenAPI 스펙을 Redoc으로 렌더링
- [ ] GitHub Pages에 Redoc 문서 배포
- [ ] `components.schemas`로 공통 스키마 정의 경험
- [ ] `securitySchemes`에 JWT Bearer 설정 추가

---

## 🎯 이 섹션을 마친 당신에게

여기까지 왔다면 **"완성된 풀스택 앱"을 로컬에서 돌릴 수 있는 사람**이 되었어요. 축하합니다. 다음 [3-2. 포트폴리오 & 오픈소스 기여](02-portfolio-opensource.md)에서는 이렇게 만든 프로젝트를 **세상에 내보이는 방법**을 배웁니다.

!!! tip "💡 다음 단계로 가기 전에"
    지금까지 로컬에 띄운 템플릿 중 하나를 GitHub의 본인 레포로 push 해두세요. 3-2에서 README.md를 멋지게 꾸밀 때 바로 써먹을 수 있어요.
