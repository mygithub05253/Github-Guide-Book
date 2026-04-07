# GitHub 인기 레포지토리 학습 가이드

> **대상:** 대학생 개발자 (Spring Boot, 데이터분석 학습 중 / 풀스택 개발자 / 금융 공기업 취업 희망)
>
> **기준:** GitHub Stars 10,000+ 레포지토리 중심
>
> **작성일:** 2026년 4월 6일

---

## 목차

1. [카테고리 1: 프레임워크 및 언어 학습](#카테고리-1-프레임워크-및-언어-학습)
2. [카테고리 2: 프로젝트 및 공모전 활용](#카테고리-2-프로젝트-및-공모전-활용)
3. [카테고리 3: 문서 관련 작업 라이브러리](#카테고리-3-문서-관련-작업-라이브러리)
4. [카테고리 4: 비전공자를 위한 학습 가이드](#카테고리-4-비전공자를-위한-학습-가이드)
5. [보너스: 금융/공기업 취업에 도움되는 레포지토리](#보너스-금융공기업-취업에-도움되는-레포지토리)

---

## 카테고리 1: 프레임워크 및 언어 학습

### 1-1. Spring Boot (Java 백엔드)

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [spring-projects/spring-boot](https://github.com/spring-projects/spring-boot) | 76K+ | Spring Boot 공식 레포지토리. 소스 코드를 직접 읽으며 내부 동작 원리를 학습할 수 있음 |
| [eugenp/tutorials](https://github.com/eugenp/tutorials) | 37K+ | Baeldung 블로그의 Spring 생태계 전반 예제 코드. Spring Boot 3, Security, JPA 등 실무 패턴 학습에 최적 |
| [macrozheng/mall](https://github.com/macrozheng/mall) | 83K+ | Spring Boot + MyBatis 기반 전자상거래 시스템. 실제 기업 수준의 아키텍처를 학습할 수 있음 |
| [RameshMF/spring-boot-tutorial](https://github.com/RameshMF/spring-boot-tutorial) | 2K+ | 100개 이상의 Spring Boot 튜토리얼과 가이드. 입문자에게 단계별 학습 경로 제공 |
| [in28minutes/spring-boot-examples](https://github.com/in28minutes/spring-boot-examples) | 4K+ | 초급~중급 Spring Boot 예제 모음. REST API, JPA, Security 등 핵심 기능별 예제 |
| [gothinkster/realworld](https://github.com/gothinkster/realworld) | 80K+ | 다양한 프레임워크로 동일한 앱(Medium 클론)을 구현한 프로젝트. Spring Boot 구현체 포함 |
| [spring-projects/spring-security](https://github.com/spring-projects/spring-security) | 9K+ | Spring Security 공식 레포. 인증/인가 패턴 학습 필수 |

**학습 추천 순서:** spring-boot-tutorial(입문) → spring-boot-examples(기초) → tutorials(심화) → mall(실무급 프로젝트) → realworld(아키텍처 비교)

---

### 1-2. React (프론트엔드)

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [facebook/react](https://github.com/facebook/react) | 244K+ | React 공식 레포지토리. 최신 Hooks, Concurrent Mode 등의 변경사항을 직접 확인 가능 |
| [enaqx/awesome-react](https://github.com/enaqx/awesome-react) | 67K+ | React 생태계 전체를 아우르는 큐레이션 목록. 라이브러리, 도구, 튜토리얼 총정리 |
| [brillout/awesome-react-components](https://github.com/brillout/awesome-react-components) | 43K+ | React UI 컴포넌트 모음. 프로젝트에 바로 적용할 수 있는 컴포넌트 탐색 |
| [typescript-cheatsheets/react](https://github.com/typescript-cheatsheets/react) | 45K+ | React + TypeScript 조합 치트시트. 실무에서 가장 많이 쓰이는 패턴 정리 |
| [alan2207/bulletproof-react](https://github.com/alan2207/bulletproof-react) | 29K+ | 프로덕션 레벨 React 애플리케이션 아키텍처 가이드 |

**학습 추천 순서:** React 공식 문서(react.dev) → awesome-react(생태계 파악) → typescript-cheatsheets/react(TS 적용) → bulletproof-react(아키텍처)

---

### 1-3. Next.js (풀스택 React 프레임워크)

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [vercel/next.js](https://github.com/vercel/next.js) | 130K+ | Next.js 공식 레포. SSR, SSG, App Router 등 최신 기능 학습 |
| [vercel/next-learn](https://github.com/vercel/next-learn) | 4K+ | Next.js 공식 학습 코스의 소스 코드 |
| [vercel/commerce](https://github.com/vercel/commerce) | 12K+ | Next.js 기반 이커머스 템플릿. 실제 프로덕션 수준의 코드 참고 가능 |
| [shadcn-ui/taxonomy](https://github.com/shadcn-ui/taxonomy) | 18K+ | Next.js 13 App Router + Auth + DB 통합 예제. 풀스택 앱 구조 학습 |

**학습 추천 순서:** next-learn(입문) → Next.js 공식 문서 → commerce(실무 패턴) → taxonomy(풀스택 구조)

---

### 1-4. Django (Python 백엔드)

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [django/django](https://github.com/django/django) | 82K+ | Django 공식 레포지토리. Python 웹 프레임워크의 대표주자 |
| [cookiecutter/cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) | 12K+ | Django 프로젝트 보일러플레이트. 프로덕션 레벨 설정이 모두 포함된 템플릿 |
| [wsvincent/awesome-django](https://github.com/wsvincent/awesome-django) | 10K+ | Django 관련 라이브러리, 도구, 튜토리얼 큐레이션 목록 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 28K+ | Django REST API 구축을 위한 필수 프레임워크 |

**학습 추천 순서:** Django 공식 튜토리얼 → django-rest-framework(API 개발) → cookiecutter-django(프로젝트 구조) → awesome-django(생태계 확장)

---

### 1-5. Node.js / Express (JavaScript 백엔드)

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [expressjs/express](https://github.com/expressjs/express) | 66K+ | 가장 널리 쓰이는 Node.js 웹 프레임워크. 미들웨어 패턴 학습의 기본 |
| [nestjs/nest](https://github.com/nestjs/nest) | 70K+ | TypeScript 기반 엔터프라이즈급 Node.js 프레임워크. Spring과 유사한 구조로 학습 시너지 |
| [goldbergyoni/nodebestpractices](https://github.com/goldbergyoni/nodebestpractices) | 101K+ | Node.js 모범 사례 총정리. 보안, 성능, 코드 스타일 등 실무 지침 |
| [sindresorhus/awesome-nodejs](https://github.com/sindresorhus/awesome-nodejs) | 59K+ | Node.js 패키지와 리소스 큐레이션 목록 |

**학습 추천 순서:** express(기본) → nodebestpractices(모범 사례) → nest(엔터프라이즈 패턴) → awesome-nodejs(생태계)

---

### 1-6. Python 학습

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 195K+ | 모든 알고리즘의 Python 구현. 코딩 테스트 준비에 매우 유용 |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 230K+ | Python 프레임워크, 라이브러리, 도구 큐레이션 |
| [donnemartin/interactive-coding-challenges](https://github.com/donnemartin/interactive-coding-challenges) | 29K+ | Jupyter Notebook 기반 인터랙티브 코딩 챌린지 |
| [satwikkansal/wtfpython](https://github.com/satwikkansal/wtfpython) | 36K+ | Python의 놀라운 동작들을 통해 언어를 깊이 이해하는 가이드 |
| [realpython/python-guide](https://github.com/realpython/python-guide) | 28K+ | Python 모범 사례, 설치, 설정 가이드 |

---

### 1-7. Java 학습

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java) | 60K+ | 자료구조와 알고리즘의 Java 구현 모음 |
| [iluwatar/java-design-patterns](https://github.com/iluwatar/java-design-patterns) | 90K+ | Java로 구현한 디자인 패턴 총집합. 엔터프라이즈 개발 필수 지식 |
| [kdn251/interviews](https://github.com/kdn251/interviews) | 63K+ | Java 기반 코딩 인터뷰 준비 자료 |
| [winterbe/java8-tutorial](https://github.com/winterbe/java8-tutorial) | 17K+ | Java 8 Lambda, Stream API 등 모던 Java 기능 학습 |
| [doocs/advanced-java](https://github.com/doocs/advanced-java) | 77K+ | Java 고급 주제 - 분산 시스템, 고가용성, 마이크로서비스 등 |

---

### 1-8. JavaScript / TypeScript 학습

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) | 190K+ | JavaScript로 구현한 알고리즘과 자료구조. 설명이 매우 친절 |
| [getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS) | 180K+ | JavaScript 심층 학습서. 클로저, 프로토타입, 비동기 등 핵심 개념 |
| [leonardomso/33-js-concepts](https://github.com/leonardomso/33-js-concepts) | 63K+ | 모든 JS 개발자가 알아야 할 33가지 핵심 개념 |
| [type-challenges/type-challenges](https://github.com/type-challenges/type-challenges) | 44K+ | TypeScript 타입 시스템 도전 과제. TS 실력 향상에 탁월 |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 101K+ | TypeScript 공식 레포지토리 |

---

### 1-9. SQL / 데이터베이스 학습

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [pingcap/awesome-database-learning](https://github.com/pingcap/awesome-database-learning) | 8K+ | 데이터베이스 내부 동작 원리 학습 자료 모음 |
| [s-shemmee/SQL-101](https://github.com/s-shemmee/SQL-101) | 1K+ | SQL 초보자를 위한 단계별 튜토리얼과 연습 문제 |
| [bregman-arie/devops-exercises](https://github.com/bregman-arie/devops-exercises) | 67K+ | SQL, Linux, 네트워킹 등 다양한 주제의 연습 문제 포함 |
| [redis/redis](https://github.com/redis/redis) | 67K+ | Redis 공식 레포. 캐싱, 세션 관리 등 실무 필수 기술 |

---

## 카테고리 2: 프로젝트 및 공모전 활용

### 2-1. 풀스택 프로젝트 템플릿 & 보일러플레이트

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [gothinkster/realworld](https://github.com/gothinkster/realworld) | 80K+ | 다양한 프론트/백엔드 조합으로 동일한 앱을 구현. 기술 비교에 최적 |
| [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | 28K+ | FastAPI + React + PostgreSQL + Docker 풀스택 템플릿 |
| [h5bp/html5-boilerplate](https://github.com/h5bp/html5-boilerplate) | 57K+ | 웹 프로젝트의 기초가 되는 HTML5 보일러플레이트 |
| [react-boilerplate/react-boilerplate](https://github.com/react-boilerplate/react-boilerplate) | 29K+ | 프로덕션 레디 React 보일러플레이트 |
| [tiangolo/fastapi](https://github.com/tiangolo/fastapi) | 80K+ | Python 고성능 API 프레임워크. 공모전에서 빠른 백엔드 구축에 최적 |

---

### 2-2. API 개발 도구

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 419K+ | 무료 공개 API 목록. 프로젝트에 외부 데이터 연동 시 필수 참고 |
| [swagger-api/swagger-ui](https://github.com/swagger-api/swagger-ui) | 27K+ | API 문서 자동 생성 도구. REST API 프로젝트에 필수 |
| [Kong/insomnia](https://github.com/Kong/insomnia) | 35K+ | API 테스트 클라이언트. Postman 대안 오픈소스 |
| [hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch) | 66K+ | 웹 기반 API 테스트 도구. 빠르고 가벼운 API 개발 환경 |

---

### 2-3. 데이터베이스 / ORM 도구

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [prisma/prisma](https://github.com/prisma/prisma) | 40K+ | Node.js/TypeScript용 차세대 ORM. 타입 안전한 DB 접근 |
| [sequelize/sequelize](https://github.com/sequelize/sequelize) | 30K+ | Node.js용 ORM. MySQL, PostgreSQL 등 다양한 DB 지원 |
| [typeorm/typeorm](https://github.com/typeorm/typeorm) | 34K+ | TypeScript ORM. NestJS와 궁합이 좋음 |
| [supabase/supabase](https://github.com/supabase/supabase) | 75K+ | Firebase 대안 오픈소스. PostgreSQL 기반 백엔드 서비스 |

---

### 2-4. 인증 / 보안 라이브러리

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [spring-projects/spring-security](https://github.com/spring-projects/spring-security) | 9K+ | Spring 생태계 인증/인가 프레임워크 |
| [jwtk/jjwt](https://github.com/jwtk/jjwt) | 10K+ | Java JWT 라이브러리. 토큰 기반 인증 구현 필수 |
| [nextauthjs/next-auth](https://github.com/nextauthjs/next-auth) | 25K+ | Next.js용 인증 라이브러리. OAuth, 이메일, 자격 증명 인증 지원 |
| [keycloak/keycloak](https://github.com/keycloak/keycloak) | 24K+ | 오픈소스 IAM 솔루션. SSO, OAuth2 학습에 유용 |

---

### 2-5. UI 컴포넌트 라이브러리

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [mui/material-ui](https://github.com/mui/material-ui) | 94K+ | React용 Material Design 컴포넌트. 가장 널리 쓰이는 UI 라이브러리 |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 76K+ | Radix + Tailwind 기반 모던 React 컴포넌트. 2024-2026 트렌드 |
| [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 84K+ | 유틸리티 퍼스트 CSS 프레임워크. 빠른 UI 개발의 핵심 |
| [saadeghi/daisyui](https://github.com/saadeghi/daisyui) | 35K+ | Tailwind CSS 플러그인. 50+ 즉시 사용 가능한 컴포넌트 |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | 93K+ | 엔터프라이즈급 React UI 라이브러리. 관리자 페이지 구축에 최적 |

---

### 2-6. DevOps / CI-CD 도구

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [docker/compose](https://github.com/docker/compose) | 34K+ | Docker 멀티 컨테이너 관리. 프로젝트 배포 필수 도구 |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 112K+ | 컨테이너 오케스트레이션 플랫폼. 대규모 서비스 배포 학습 |
| [nektos/act](https://github.com/nektos/act) | 56K+ | GitHub Actions를 로컬에서 실행. CI/CD 파이프라인 테스트 |
| [argoproj/argo-cd](https://github.com/argoproj/argo-cd) | 18K+ | GitOps 기반 Kubernetes 배포 도구 |

---

### 2-7. 테스트 프레임워크

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [jestjs/jest](https://github.com/jestjs/jest) | 44K+ | JavaScript 테스트 프레임워크. React 테스트의 표준 |
| [testing-library/react-testing-library](https://github.com/testing-library/react-testing-library) | 19K+ | React 컴포넌트 테스트 유틸리티. 사용자 관점의 테스트 작성 |
| [pytest-dev/pytest](https://github.com/pytest-dev/pytest) | 12K+ | Python 테스트 프레임워크. 간결하고 강력한 테스트 작성 |
| [cypress-io/cypress](https://github.com/cypress-io/cypress) | 47K+ | E2E 테스트 도구. 브라우저 기반 통합 테스트에 최적 |

---

### 2-8. 데이터 시각화 라이브러리

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [d3/d3](https://github.com/d3/d3) | 109K+ | 데이터 기반 문서 조작 JavaScript 라이브러리. 커스텀 차트의 표준 |
| [apache/echarts](https://github.com/apache/echarts) | 62K+ | 강력한 인터랙티브 차트 라이브러리. 대시보드 구축에 적합 |
| [recharts/recharts](https://github.com/recharts/recharts) | 24K+ | React 기반 차트 라이브러리. React 프로젝트에 쉽게 통합 |
| [plotly/plotly.js](https://github.com/plotly/plotly.js) | 17K+ | 40+ 차트 유형 지원. 과학/금융 데이터 시각화에 강점 |

---

### 2-9. 머신러닝 / AI 도구

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 187K+ | Google의 ML 플랫폼. 프로덕션 레벨 ML 모델 구축 |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | 86K+ | 연구 및 프로덕션용 ML 라이브러리. 학계에서 가장 인기 |
| [scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn) | 61K+ | Python ML 라이브러리. 데이터 분석 입문에 필수 |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 140K+ | NLP/AI 모델 허브. 최신 AI 모델 활용에 필수 |
| [streamlit/streamlit](https://github.com/streamlit/streamlit) | 37K+ | Python 데이터 앱 빌더. ML 모델 데모/프로토타입에 최적 |

---

## 카테고리 3: 문서 관련 작업 라이브러리

### 3-1. Python 문서 라이브러리

| 레포지토리 | 대상 파일 | 설명 |
|---|---|---|
| [python-openxml/python-docx](https://github.com/python-openxml/python-docx) | .docx | Word 문서 생성 및 수정. 보고서 자동 생성에 활용 |
| [openpyxl/openpyxl](https://github.com/openpyxl/openpyxl) | .xlsx | Excel 파일 읽기/쓰기. 데이터 분석 결과 엑셀 출력 |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | .csv/.xlsx | 데이터 분석 핵심 라이브러리. CSV, Excel 입출력 지원 |
| [py-pdf/pypdf](https://github.com/py-pdf/pypdf) | .pdf | PDF 분할, 병합, 텍스트 추출 |
| [reportlab](https://github.com/MrBitBucket/reportlab-mirror) | .pdf | PDF 생성 라이브러리. 차트, 표가 포함된 PDF 보고서 작성 |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 다양한 형식 | Office 문서를 Markdown으로 변환. 문서 변환 자동화 |
| [python-pptx/python-pptx](https://github.com/python-pptx/python-pptx) | .pptx | PowerPoint 파일 생성 및 수정 |
| [hancomhwp/pyhwp](https://github.com/mete0r/pyhwp) | .hwp | HWP(한글) 파일 처리. 한국 공공기관 문서 작업에 필수 |

**활용 팁:** pandas로 데이터를 분석한 후, openpyxl로 서식이 있는 Excel을, python-docx로 Word 보고서를, python-pptx로 발표 자료를 자동 생성하는 파이프라인을 구축할 수 있습니다.

---

### 3-2. Java 문서 라이브러리

| 레포지토리 | 대상 파일 | 설명 |
|---|---|---|
| [apache/poi](https://github.com/apache/poi) | .docx/.xlsx/.pptx | Java에서 Microsoft Office 문서 처리의 표준. Excel, Word, PowerPoint 모두 지원 |
| [itext/itext-java](https://github.com/itext/itext-java) | .pdf | PDF 생성 및 조작. 금융권 보고서, 증명서 등 PDF 출력에 활용 |
| [documents4j/documents4j](https://github.com/documents4j/documents4j) | 다양한 형식 | Java 문서 변환 라이브러리. Word-PDF 변환 등 |
| [jxlss/jxls](https://github.com/jxlss/jxls) | .xlsx | Java 기반 Excel 보고서 엔진. 템플릿 기반 Excel 생성 |

**활용 팁:** Spring Boot 프로젝트에서 Apache POI로 Excel 데이터를 읽어 DB에 저장하거나, 조회 결과를 Excel/PDF로 다운로드하는 기능은 금융권 시스템에서 매우 흔한 패턴입니다.

---

### 3-3. JavaScript / Node.js 문서 라이브러리

| 레포지토리 | 대상 파일 | 설명 |
|---|---|---|
| [SheetJS/sheetjs](https://github.com/SheetJS/sheetjs) | .xlsx/.csv | JavaScript Excel 처리의 표준. 브라우저/Node.js 모두 지원 |
| [adaltas/node-csv](https://github.com/adaltas/node-csv) | .csv | Node.js CSV 파싱/생성. 대용량 CSV 스트리밍 처리 가능 |
| [bpampuch/pdfmake](https://github.com/bpampuch/pdfmake) | .pdf | 클라이언트/서버 사이드 PDF 생성. 인보이스, 보고서 출력에 활용 |
| [foliojs/pdfkit](https://github.com/foliojs/pdfkit) | .pdf | Node.js PDF 생성 라이브러리. 복잡한 레이아웃의 PDF 제작 |
| [dolanmiu/docx](https://github.com/dolanmiu/docx) | .docx | Node.js에서 Word 문서 생성. 서버 사이드 문서 자동화 |

---

### 3-4. SQL / 데이터 내보내기 도구

| 레포지토리 | 설명 |
|---|---|
| [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core) | 데이터 변환 도구. SQL 기반 ELT 파이프라인 구축 |
| [knex/knex](https://github.com/knex/knex) | Node.js SQL 쿼리 빌더. MySQL, PostgreSQL 등 다중 DB 지원 |
| [metabase/metabase](https://github.com/metabase/metabase) | 오픈소스 BI 도구. SQL 쿼리 결과를 차트/대시보드로 시각화 및 내보내기 |
| [apache/superset](https://github.com/apache/superset) | 데이터 탐색 및 시각화 플랫폼. SQL 결과를 다양한 형식으로 내보내기 가능 |

---

## 카테고리 4: 비전공자를 위한 학습 가이드

### 4-1. 컴퓨터 과학 기초

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | 340K+ | 비전공자가 소프트웨어 엔지니어가 되기 위한 완전한 CS 학습 계획. 한국어 번역 있음 |
| [ossu/computer-science](https://github.com/ossu/computer-science) | 175K+ | 무료 온라인 CS 학위 커리큘럼. 비전공자를 위한 체계적 학습 경로 |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 442K+ | 무료 코딩 교육 플랫폼. 웹 개발, 데이터 분석, ML 커리큘럼 제공 |
| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 486K+ | 직접 만들어보며 배우는 프로그래밍. Git, Docker, DB 등을 처음부터 구현 |
| [florinpop17/app-ideas](https://github.com/florinpop17/app-ideas) | 80K+ | 난이도별 프로젝트 아이디어 모음. 초보자~고급자 단계별 프로젝트 |

---

### 4-2. 코딩 인터뷰 / 알고리즘 준비

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) | 190K+ | 알고리즘과 자료구조 학습의 바이블. 시각적 설명이 탁월 |
| [kdn251/interviews](https://github.com/kdn251/interviews) | 63K+ | 코딩 인터뷰 준비 종합 가이드 |
| [yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 120K+ | 기술 면접 종합 핸드북. 이력서 작성부터 알고리즘, 시스템 설계까지 |
| [ashishps1/awesome-leetcode-resources](https://github.com/ashishps1/awesome-leetcode-resources) | 10K+ | LeetCode 문제 풀이 전략과 패턴별 분류 |

---

### 4-3. 시스템 설계

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | 342K+ | 대규모 시스템 설계 학습의 교과서. Anki 플래시카드 포함 |
| [ByteByteGoHq/system-design-101](https://github.com/ByteByteGoHq/system-design-101) | 66K+ | 시각적 다이어그램으로 배우는 시스템 설계. 초보자에게 매우 친절 |
| [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | 18K+ | 시스템 설계 학습 자료 큐레이션 |

---

### 4-4. 개발자 로드맵

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | 352K+ | 프론트엔드, 백엔드, DevOps, DBA 등 분야별 인터랙티브 로드맵 |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 385K+ | 무료 프로그래밍 도서 목록. 한국어 자료도 포함 |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 452K+ | 모든 분야의 Awesome 리스트 모음. 관심 분야 탐색의 출발점 |
| [mtdvio/every-programmer-should-know](https://github.com/mtdvio/every-programmer-should-know) | 85K+ | 모든 프로그래머가 알아야 할 기술 지식 모음 |

---

## 보너스: 금융/공기업 취업에 도움되는 레포지토리

### 엔터프라이즈 시스템 & 금융 관련

| 레포지토리 | Stars | 설명 |
|---|---|---|
| [macrozheng/mall](https://github.com/macrozheng/mall) | 83K+ | Spring Boot 기반 이커머스 시스템. 금융권 시스템과 유사한 아키텍처 학습 |
| [prometheus/prometheus](https://github.com/prometheus/prometheus) | 56K+ | 모니터링 시스템. 대규모 서비스 운영 필수 도구 |
| [grafana/grafana](https://github.com/grafana/grafana) | 66K+ | 대시보드 및 시각화 플랫폼. 실시간 모니터링 구축 |
| [apache/kafka](https://github.com/apache/kafka) | 29K+ | 분산 스트리밍 플랫폼. 금융 실시간 데이터 처리의 핵심 |
| [elastic/elasticsearch](https://github.com/elastic/elasticsearch) | 71K+ | 분산 검색 엔진. 대용량 로그 분석, 전문 검색에 활용 |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | 53K+ | Python 웹 크롤링 프레임워크. 금융 데이터 수집 자동화 |
| [moov-io/awesome-fintech](https://github.com/moov-io/awesome-fintech) | 1K+ | 핀테크 관련 오픈소스 라이브러리 큐레이션 |

---

## Claude Code 활용 팁

위 레포지토리들을 학습할 때 Claude Code를 활용하면 효율을 극대화할 수 있습니다.

**코드 분석:** 레포지토리를 클론한 후 Claude Code에게 코드 구조 분석을 요청하면, 프로젝트의 전체 아키텍처와 핵심 패턴을 빠르게 파악할 수 있습니다.

**문서 작업 자동화:** 카테고리 3의 라이브러리를 사용해 코드를 작성할 때, Claude Code가 boilerplate 코드를 생성해주므로 핵심 로직에 집중할 수 있습니다.

**학습 노트 정리:** 학습 내용을 Markdown으로 정리하면서 Claude Code에게 코드 예제 생성이나 개념 설명을 요청하면 효과적입니다.

**프로젝트 스캐폴딩:** 공모전이나 사이드 프로젝트 시작 시, 카테고리 2의 보일러플레이트를 기반으로 Claude Code에게 프로젝트 초기 설정을 맡기면 빠르게 개발을 시작할 수 있습니다.

---

> **마지막 조언:** 모든 레포지토리를 한꺼번에 학습하려 하지 마세요. 먼저 developer-roadmap으로 자신의 학습 경로를 설정하고, 각 단계에 맞는 레포지토리를 하나씩 깊이 있게 학습하는 것이 가장 효과적입니다.
