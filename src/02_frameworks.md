# Part 2: 프레임워크 및 언어별 학습 레포지토리

> 실전 개발에 필요한 주요 프레임워크와 언어별 학습 레포지토리입니다.
> Spring Boot, React, Next.js 등을 체계적으로 학습할 수 있습니다.

## 학습 목표
- 백엔드 프레임워크 (Spring Boot) 활용법 이해
- 프론트엔드 프레임워크 (React, Next.js) 학습 경로 파악
- 각 레포지토리에서 "어디를 먼저 읽어야 하는지" 파악
- Claude Code로 대형 오픈소스 코드베이스를 탐색하는 방법 체득

---

이 파트는 10,000+ Stars를 보유한 주요 웹 개발 프레임워크 레포지토리를 **"어떻게 클론해서, 어디를 보고, 무엇을 배울지"** 중심으로 안내합니다. 전체 코드를 옮겨 적는 대신 **레포 구조 · 핵심 파일 위치 · Claude Code 질문 예시**를 제공합니다.

---

## 2-1. Spring Boot 생태계

### 2-1-1. spring-projects/spring-boot (76K+)

#### 레포지토리 개요
Spring Boot는 Spring Framework 기반의 빠른 애플리케이션 개발(RAD) 프레임워크입니다. 자동 설정(Auto-Configuration)과 내장 서버로 선언적 설정을 최소화하고 프로덕션 환경 배포를 단순화합니다. Java 백엔드 개발의 사실상 표준이며 마이크로서비스 아키텍처의 기반이 됩니다.

- Stars: 76,000+
- Language: Java
- License: Apache 2.0
- 공식 사이트: https://spring.io/projects/spring-boot

#### 클론 및 사전 준비
```bash
# JDK 17+ 설치 확인
java -version

# 레포지토리 클론 (크기가 크므로 shallow clone 권장)
git clone --depth 1 https://github.com/spring-projects/spring-boot.git
cd spring-boot
```

#### 디렉토리 구조에서 주목할 곳
- `spring-boot-project/spring-boot` — 코어 모듈, `@SpringBootApplication` 구현
- `spring-boot-project/spring-boot-autoconfigure` — 자동 설정 핵심 로직
- `spring-boot-project/spring-boot-starters` — 스타터 의존성 모음
- `spring-boot-project/spring-boot-docs` — 공식 레퍼런스 문서 소스
- `spring-boot-tests/spring-boot-smoke-tests` — 작은 샘플 앱 모음(학습에 최적)

#### 학습 루트: 본 레포 대신 start.spring.io 사용
실제 신규 프로젝트는 https://start.spring.io/ 에서 생성하고, spring-boot 레포는 **내부 동작을 이해할 때만** 탐색하는 것이 좋습니다.

```bash
# Spring Initializr CLI (선택)
curl https://start.spring.io/starter.zip \
  -d dependencies=web,data-jpa,h2 \
  -d name=demo -o demo.zip
```

#### Claude Code 연동 팁
대형 레포는 한 번에 읽을 수 없습니다. 다음과 같이 질문하세요.

> "spring-boot-project/spring-boot-autoconfigure 디렉토리에서 DataSourceAutoConfiguration이 어떻게 조건부로 로드되는지 설명해 줘."

> "@SpringBootApplication 이 내부적으로 어떤 어노테이션을 조합하는지 소스에서 찾아 줘."

> "spring-boot-smoke-tests 중 REST API 가장 기본 예제를 하나 골라 구조를 설명해 줘."

---

### 2-1-2. eugenp/tutorials (37K+) — Baeldung 예제 모음

#### 레포지토리 개요
Baeldung 블로그의 모든 예제 코드가 모듈별로 정리된 Java/Spring 학습 보물창고입니다. Spring Security, JPA, Kafka, Reactive, JWT 등 거의 모든 주제의 **작동하는 최소 예제**를 제공합니다.

- Stars: 37,000+
- 구조: Maven 멀티 모듈 (수백 개)
- 공식 블로그: https://www.baeldung.com/

#### 클론 후 필요한 모듈만 빌드
```bash
git clone --depth 1 https://github.com/eugenp/tutorials.git
cd tutorials

# 전체 빌드는 30분 이상 걸립니다. 필요한 모듈만 빌드하세요.
cd spring-security-modules/spring-security-web-login
mvn spring-boot:run
```

#### 학습자가 먼저 봐야 할 모듈
- `spring-boot-modules/` — Spring Boot 기초
- `spring-security-modules/` — 인증/인가 (JWT, OAuth2 포함)
- `persistence-modules/spring-data-jpa-*` — JPA, Query 메서드
- `testing-modules/` — JUnit 5, Mockito, Testcontainers

#### Claude Code 질문 예시
> "spring-security-modules 디렉토리에서 JWT 기반 로그인을 구현한 가장 단순한 모듈을 찾아 README와 주요 설정 파일만 요약해 줘."

> "persistence-modules 안에서 Spring Data JPA `@Query` 어노테이션 사용 예제를 3개 찾아 비교해 줘."

---

### 2-1-3. macrozheng/mall (83K+) — 전자상거래 시스템

#### 레포지토리 개요
실제 운영 수준의 **쇼핑몰 백엔드 풀스택 예제**입니다. Spring Boot + MyBatis + Elasticsearch + Redis + RabbitMQ + MongoDB 조합을 실제 비즈니스 요구사항에 맞게 통합한 대형 프로젝트입니다.

- Stars: 83,000+
- 모듈: mall-admin(관리자), mall-portal(사용자), mall-search(검색), mall-demo

#### 클론 및 실행 준비
```bash
git clone --depth 1 https://github.com/macrozheng/mall.git
cd mall

# 필수 인프라: MySQL 5.7+, Redis, (선택)Elasticsearch/RabbitMQ/MongoDB
# Docker Compose 사용을 강력 권장
# document/docker/ 디렉토리에 구성 파일 있음
```

#### 디렉토리 구조에서 주목할 곳
- `mall-admin/` — 관리자 백오피스 API
- `mall-portal/` — 사용자 쇼핑몰 API (주문, 장바구니, 결제)
- `mall-search/` — Elasticsearch 기반 상품 검색
- `document/` — 아키텍처 다이어그램 · DB 스키마 · API 문서 (**반드시 먼저 읽기**)

#### Claude Code 학습 시나리오
> "mall-portal 모듈에서 주문 생성(Order)부터 결제 완료까지 흐름을 Service 계층 위주로 추적해 줘."

> "mall 프로젝트의 Redis 캐싱 전략이 어떤 Service 메서드에 적용됐는지 목록화해 줘."

> "document 디렉토리의 DB 스키마를 보고 상품-카테고리-SKU 관계를 ER 다이어그램으로 설명해 줘."

---

### 2-1-4. iluwatar/java-design-patterns (90K+)

#### 레포지토리 개요
**GoF 디자인 패턴 + 엔터프라이즈 패턴**을 Java로 구현한 세계 최대 패턴 모음입니다. 각 패턴마다 독립 Maven 모듈, 클래스 다이어그램, README가 준비되어 있어 **한 패턴당 30분**이면 학습할 수 있습니다.

- Stars: 90,000+
- 패턴 수: 150+ (Creational, Structural, Behavioral, Concurrency, Architectural 등)

#### 클론 및 특정 패턴 실행
```bash
git clone --depth 1 https://github.com/iluwatar/java-design-patterns.git
cd java-design-patterns

# 원하는 패턴 디렉토리로 이동 후 실행
cd singleton
mvn compile exec:java
```

#### 초보자가 먼저 봐야 할 패턴
- `singleton/`, `factory/`, `builder/` — Creational 기초
- `strategy/`, `observer/`, `command/` — Behavioral 필수
- `adapter/`, `decorator/`, `facade/` — Structural 필수
- `repository/`, `dao/` — 백엔드 실전에서 자주 쓰임

#### Claude Code 질문 예시
> "이 레포의 strategy 패턴 README와 App.java를 읽고, 실제 결제 시스템(카드/카카오페이/토스)에 어떻게 적용할지 구조만 제안해 줘."

> "decorator 패턴과 chain-of-responsibility 패턴의 차이를 이 레포 예제를 인용해 설명해 줘."

---

### 2-1-5. gothinkster/realworld (80K+)

#### 레포지토리 개요
"모든 프레임워크로 동일한 스펙의 블로그 앱(Conduit)을 구현한다"는 컨셉의 메타 레포지토리입니다. **프론트엔드 · 백엔드 100+ 구현체**가 모두 동일한 API 스펙을 따르므로, 같은 기능을 여러 기술 스택으로 비교 학습할 수 있습니다.

- Stars: 80,000+
- API 스펙: https://docs.realworld.show/

#### 활용 방법
```bash
# 메인 레포 클론 (스펙과 구현체 링크만 있음)
git clone --depth 1 https://github.com/gothinkster/realworld.git

# 원하는 구현체는 별도 레포로 존재합니다. 예: Spring Boot 구현
git clone https://github.com/gothinkster/spring-boot-realworld-example-app.git
```

#### 학습 포인트
- 동일 기능을 React / Vue / Angular / Svelte로 비교
- 동일 API를 Spring Boot / Express / Django / Rails / NestJS로 비교
- 자기 스택의 구현체를 읽고 **다른 스택의 구현체로 포팅**해 보는 연습

#### Claude Code 질문 예시
> "Spring Boot 구현체(gothinkster/spring-boot-realworld-example-app)와 Express 구현체(gothinkster/node-express-realworld-example-app)에서 Article 생성 API 비즈니스 로직을 비교해 줘."

---

## 2-2. React 생태계

### 2-2-1. facebook/react (244K+)

#### 레포지토리 개요
React 자체의 소스 코드 레포지토리입니다. 신규 프로젝트는 이 레포에서 시작하지 않고, **Vite / Next.js / Create React App** 등 도구로 생성합니다. 본 레포는 **React 내부 동작을 이해**하고 싶을 때 탐색합니다.

- Stars: 244,000+
- License: MIT
- 공식 문서: https://react.dev/

#### 신규 프로젝트 생성 (권장 경로)
```bash
# Vite 사용 (가장 빠름)
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install
npm run dev
```

#### 레포에서 주목할 곳
- `packages/react` — 코어 라이브러리, Hooks 구현
- `packages/react-dom` — DOM 렌더러
- `packages/react-reconciler` — Fiber 아키텍처
- `packages/scheduler` — 우선순위 기반 스케줄러

#### Claude Code 질문 예시
> "packages/react/src/ReactHooks.js 를 보고 useState가 내부적으로 어떤 구조로 저장되는지 설명해 줘."

> "Fiber 아키텍처가 왜 도입됐는지 packages/react-reconciler README와 핵심 파일을 근거로 요약해 줘."

---

### 2-2-2. typescript-cheatsheets/react (45K+)

#### 레포지토리 개요
**React + TypeScript** 조합에서 자주 겪는 타입 문제를 커뮤니티가 정리한 치트시트 모음입니다. 실제 코드 레포라기보다는 **문서 레포**에 가깝습니다. 실무에서 타입 에러를 만났을 때 가장 먼저 검색할 곳입니다.

- Stars: 45,000+
- 구성: basic / advanced / migrating / hoc 치트시트

#### 활용 방법
```bash
# 별도 클론 없이 웹에서 바로 읽기 가능
# https://react-typescript-cheatsheet.netlify.app/

git clone --depth 1 https://github.com/typescript-cheatsheets/react.git
```

#### 먼저 읽어야 할 문서
- `README.md` — 전체 인덱스
- `docs/basic/` — Props / State / Event / Forms 타입 정의
- `docs/advanced/` — Generic 컴포넌트, Polymorphic 컴포넌트
- `docs/hoc/` — HOC와 Render Prop의 제네릭

#### Claude Code 질문 예시
> "이 레포 docs/basic 을 기반으로 Input 컴포넌트의 onChange 이벤트 타입을 정의하는 방법 3가지를 비교해 줘."

> "advanced 섹션에서 'Generic Components' 예제를 읽고 내 프로젝트의 List 컴포넌트에 어떻게 적용할지 제안해 줘."

---

### 2-2-3. alan2207/bulletproof-react (29K+)

#### 레포지토리 개요
**"확장 가능한 React 프로젝트 구조"의 모범 답안**으로 자주 언급되는 레포입니다. feature 기반 폴더 구조, 상태 관리 분리, 테스트 전략, 배포 설정까지 실무 베스트 프랙티스를 하나의 앱으로 구현했습니다.

- Stars: 29,000+
- 스택: React + TypeScript + Vite + Zustand + React Query + MSW

#### 클론 및 실행
```bash
git clone --depth 1 https://github.com/alan2207/bulletproof-react.git
cd bulletproof-react/apps/react-vite
npm install
npm run dev
```

#### 디렉토리 구조의 핵심 (필독)
- `docs/` — 프로젝트 철학 문서 (**먼저 읽기**)
- `src/features/` — 기능별 모듈 (auth, comments, discussions, users 등)
- `src/components/` — 공용 UI 컴포넌트
- `src/lib/` — 외부 라이브러리 래퍼 (axios, react-query 설정)
- `src/testing/` — 테스트 유틸 + MSW 핸들러

#### Claude Code 학습 시나리오
> "docs 디렉토리의 project-structure.md 와 application-overview.md 를 읽고 이 프로젝트의 폴더 구조 규칙을 내 프로젝트에 적용할 수 있는 체크리스트로 만들어 줘."

> "src/features/discussions 디렉토리의 api, components, routes, types 가 어떻게 상호작용하는지 추적해 줘."

---

## 2-3. Next.js 생태계

### 2-3-1. vercel/next.js (130K+)

#### 레포지토리 개요
React 기반 풀스택 프레임워크. App Router · Server Components · Server Actions · 이미지 최적화 · 파일 기반 라우팅 등 현대 웹 개발의 사실상 표준 기능을 제공합니다. 신규 프로젝트는 `create-next-app` 으로 생성하고, 본 레포는 **내부 동작 이해와 예제 탐색**에 사용합니다.

- Stars: 130,000+
- 공식 문서: https://nextjs.org/docs

#### 신규 프로젝트 생성
```bash
npx create-next-app@latest my-app --typescript --eslint --tailwind --app
cd my-app
npm run dev
# http://localhost:3000
```

#### Next.js 레포에서 주목할 곳
- `examples/` — **가장 중요**. 100+ 공식 예제(인증, DB, 결제, i18n 등)
- `packages/next` — 프레임워크 코어
- `docs/` — 공식 문서 소스
- `test/` — E2E 테스트 (실전 시나리오의 보고)

#### 추천 예제 디렉토리 (examples/ 하위)
- `with-supabase` — 인증 + DB 풀스택
- `with-stripe-typescript` — 결제 연동
- `blog-starter` — 마크다운 블로그
- `with-next-auth` — 소셜 로그인
- `api-routes-rest` — REST API 패턴

#### Claude Code 질문 예시
> "vercel/next.js 레포의 examples/blog-starter 구조를 설명하고, 내 가이드북 프로젝트에 옮겨올 때 수정해야 할 부분을 알려 줘."

> "examples/with-next-auth 를 읽고 Google OAuth 로그인을 추가하는 최소 수정 단계를 정리해 줘."

> "App Router의 layout.tsx 와 Pages Router의 _app.tsx 차이를 공식 docs 디렉토리에서 근거를 찾아 비교해 줘."

---

### 2-3-2. vercel/commerce (11K+) — 커머스 스타터

#### 레포지토리 개요
Next.js + Shopify 기반 **프로덕션급 커머스 템플릿**입니다. Server Components, Server Actions, 캐싱 전략 등 최신 Next.js 기능의 모범 사례를 담고 있어 **App Router 진지하게 배우고 싶다면 필독** 레포입니다.

#### 활용 방법
```bash
git clone --depth 1 https://github.com/vercel/commerce.git
cd commerce
# README의 Shopify 설정 단계를 따라야 실행 가능
```

#### 주목할 곳
- `app/` — App Router 구조, 라우트 그룹, 병렬/인터셉트 라우트
- `components/` — 공용 UI + cart 컴포넌트
- `lib/shopify/` — 외부 API 연동 패턴 (Server-only 함수)

#### Claude Code 질문 예시
> "vercel/commerce 의 app/product/[handle]/page.tsx 가 어떻게 Shopify 데이터를 Server Component 에서 페칭하는지 설명해 줘."

> "이 레포의 revalidateTag 사용 패턴을 내 블로그 프로젝트에 어떻게 적용할지 제안해 줘."

---

## 2-4. 이 파트 학습 체크리스트

- [ ] Spring Boot: `start.spring.io` 로 최소 프로젝트를 하나 만들어 실행했다
- [ ] eugenp/tutorials 에서 관심 있는 1개 모듈을 골라 README를 정독했다
- [ ] iluwatar/java-design-patterns 에서 3개 패턴을 직접 실행해 봤다
- [ ] Vite + React + TypeScript 프로젝트를 생성해 Hooks 예제를 작성했다
- [ ] bulletproof-react 의 `docs/` 디렉토리를 모두 읽었다
- [ ] `create-next-app` 으로 App Router 프로젝트를 생성해 1개 페이지를 만들었다
- [ ] vercel/next.js 의 `examples/` 에서 관심 있는 예제 1개를 클론해 실행했다
- [ ] 각 레포에 대해 Claude Code 에게 최소 1개 이상의 구조 질문을 해봤다

---

> 다음 파트: **Part 3 — 프로젝트 및 공모전 레포지토리**
> 학습한 프레임워크를 실전 포트폴리오로 연결하는 방법을 다룹니다.
