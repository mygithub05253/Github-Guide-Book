# 2-4. 이 파트 학습 체크리스트

> 여기까지 오셨다면 정말 수고 많으셨어요. 이 페이지는 Part 2에서 배운 내용을 **스스로 점검**하는 자리입니다.
> 체크가 많이 빈다고 조급해하지 마세요. 하나씩 돌아가며 채워나가면 됩니다.

---

## 어떻게 사용하나요?

1. 각 항목을 읽고 **솔직하게** 체크하세요. (남이 보는 게 아니에요)
2. 체크 못 한 항목은 "왜 못했는지" 옆에 적어두세요. (예: "Docker 설치가 귀찮아서", "Java 17 설치 미완료")
3. 3일~1주일 간격으로 다시 이 페이지로 돌아와 재점검하세요.

!!! tip "💡 꿀팁: 70% 달성이면 충분"
    모든 항목을 100% 채우려 하지 마세요. **본인의 진로에 직결된 항목 70%**만 체크해도 충분합니다. 예를 들어 백엔드 지망이면 Spring Boot 섹션은 90%, Next.js 섹션은 40%면 OK.

---

## 환경 준비 체크리스트

- [ ] Java 17 이상 설치 및 `java -version`으로 확인
- [ ] Node.js 20 LTS 이상 설치 및 `node -v`로 확인
- [ ] Git 2.40+ 설치 및 `git --version`으로 확인
- [ ] IntelliJ IDEA Community 설치 (Java 개발용)
- [ ] VS Code 설치 + ESLint/Prettier 확장 설치
- [ ] (선택) Docker Desktop 설치
- [ ] Windows의 경우 `JAVA_HOME` 환경 변수가 Java 17을 가리키고 있음

---

## 2-1. Spring Boot 생태계 체크리스트

### 2-1-1. spring-projects/spring-boot
- [ ] `start.spring.io`로 최소 프로젝트를 생성해 실행했다
- [ ] Hello World 컨트롤러를 추가해 브라우저로 확인했다
- [ ] `@SpringBootApplication` 내부 구성 (3개 어노테이션)을 설명할 수 있다
- [ ] `Port 8080 already in use` 에러를 한 번이라도 만나 해결해봤다
- [ ] (선택) spring-boot 본체 레포를 클론해서 디렉토리 구조를 훑어봤다

### 2-1-2. eugenp/tutorials
- [ ] 전체가 아닌 **단일 모듈**만 빌드하는 방법을 안다
- [ ] JWT 로그인 관련 모듈을 1개 실행해봤다
- [ ] Baeldung 블로그 글과 이 레포 코드가 어떻게 연결되는지 이해했다
- [ ] 관심 키워드로 모듈을 검색해봤다 (예: `jwt`, `kafka`)

### 2-1-3. macrozheng/mall
- [ ] `document/architect` 아키텍처 다이어그램을 읽었다
- [ ] `document/sql/mall.sql`의 주요 테이블 관계를 이해했다
- [ ] `OmsPortalOrderServiceImpl.generateOrder()` 코드를 한 줄씩 따라 읽었다
- [ ] Redis 캐싱이 적용된 메서드를 3개 이상 찾아봤다
- [ ] (선택) Docker Compose로 MySQL + Redis를 띄워봤다

### 2-1-4. iluwatar/java-design-patterns
- [ ] `singleton`, `factory`, `builder` 패턴을 직접 실행했다
- [ ] `strategy`, `observer`, `decorator`를 README로 학습했다
- [ ] 패턴 1개를 보지 않고 타이핑할 수 있다
- [ ] 디자인 패턴을 Spring Boot의 어디에 쓰이는지 1개 이상 예시를 들 수 있다
- [ ] `repository` 패턴이 Spring Data JPA와 어떻게 연결되는지 설명할 수 있다

### 2-1-5. gothinkster/realworld
- [ ] https://docs.realworld.show/ 스펙 문서를 정독했다
- [ ] Spring Boot 또는 Express 구현체 중 하나를 실행해봤다
- [ ] Postman으로 User Register + Login API를 호출해봤다
- [ ] 두 개 이상 스택의 구현체를 비교해봤다

---

## 2-2. React 생태계 체크리스트

### 2-2-1. facebook/react
- [ ] Vite로 React + TypeScript 프로젝트를 생성해 실행했다
- [ ] `useState`, `useEffect`를 사용한 컴포넌트를 작성했다
- [ ] react.dev 공식 튜토리얼 "Tic-Tac-Toe"를 절반 이상 따라 했다
- [ ] `Invalid hook call` 또는 `Too many re-renders` 에러를 만나 해결해봤다
- [ ] (선택) facebook/react 본체 레포 `packages/` 구조를 훑어봤다

### 2-2-2. typescript-cheatsheets/react
- [ ] https://react-typescript-cheatsheet.netlify.app/을 즐겨찾기했다
- [ ] Form 예제를 내 프로젝트에서 직접 작성했다
- [ ] `ChangeEvent<HTMLInputElement>` 타입의 의미를 설명할 수 있다
- [ ] Generic 컴포넌트를 1개 만들어봤다
- [ ] `useRef`의 올바른 타입 정의 3가지를 안다

### 2-2-3. alan2207/bulletproof-react
- [ ] `docs/` 디렉토리 문서를 5개 이상 정독했다
- [ ] 예제 앱을 로컬에서 실행해 MSW가 동작하는 것을 확인했다
- [ ] `features/` 기반 구조의 장점 3가지를 말할 수 있다
- [ ] 서버 상태(React Query) vs 클라이언트 상태(Zustand) 분리를 이해했다
- [ ] 내 프로젝트 폴더 구조를 리팩토링해봤다

---

## 2-3. Next.js 생태계 체크리스트

### 2-3-1. vercel/next.js
- [ ] `create-next-app`으로 App Router 프로젝트를 생성했다
- [ ] 파일 생성만으로 새 경로를 추가해봤다
- [ ] Server Component와 Client Component의 차이를 설명할 수 있다
- [ ] `'use client'` 지시자를 언제 써야 하는지 판단할 수 있다
- [ ] `examples/blog-starter`를 클론해 실행해봤다
- [ ] `Hydration failed` 또는 `Module not found: fs` 에러를 만나봤다
- [ ] `NEXT_PUBLIC_` 접두사의 의미를 설명할 수 있다

### 2-3-2. vercel/commerce
- [ ] `app/` 디렉토리 구조를 파악했다
- [ ] `app/product/[handle]/page.tsx`를 정독했다
- [ ] Server Component에서 외부 API를 호출하는 패턴을 이해했다
- [ ] `revalidateTag`가 왜 필요한지 설명할 수 있다

---

## Claude Code 활용 체크리스트

이 파트에서 특히 강조한 것이 **"Claude Code를 과외 선생님처럼 쓰기"** 였죠. 다음 항목들을 체크해보세요.

- [ ] 각 레포에 대해 최소 1개 이상의 **구조 파악 프롬프트**를 던져봤다
- [ ] Claude가 레포 소스를 근거로 답변한 것을 확인했다 (공수표 답변 구분)
- [ ] 에러 메시지를 Claude에게 붙여 넣어 **디버깅 도움**을 받아봤다
- [ ] "내 프로젝트에 이식하려면" 식의 **맞춤형 프롬프트**를 써봤다
- [ ] 하나의 주제에 대해 **후속 질문**을 3회 이상 이어간 적이 있다

!!! example "🤖 Claude Code 프롬프트: 이 파트 전체 복습"
    > "내가 지금 Spring Boot + React + Next.js 생태계를 공부하고 있어. 초보자가 4주 동안 하루 2시간씩 학습한다고 가정하고, 주차별 구체적 학습 계획을 짜줘. 첫 주는 Spring Boot, 둘째 주는 React, 셋째 주는 Next.js, 넷째 주는 RealWorld 스펙으로 작은 풀스택 포트폴리오 만들기. 각 주마다 달성해야 할 목표와 막혔을 때 참고할 레포를 명시해줘."

---

## 자기 진단: 나는 지금 어디쯤?

점수별 해석:

| 달성률 | 상태 | 다음 할 일 |
| --- | --- | --- |
| 0~30% | 환경 준비 단계 | 설치/실행부터. 코드 이해는 나중 |
| 30~60% | 기초 학습 중 | 관심 분야 하나에 집중 |
| 60~80% | 실전 적용 단계 | 작은 포트폴리오 시작 |
| 80%+ | 숙련 단계 | Part 3 (프로젝트/공모전)로 진행 |

!!! warning "⚠️ 완벽주의 경계"
    100%를 찍으려다 지치면 안 됩니다. **80%에서 멈추고 다음 파트로 넘어가는 것**이, 100% 찍고 번아웃 오는 것보다 훨씬 낫습니다. 부족한 부분은 Part 3 프로젝트를 하면서 자연스럽게 채워집니다.

---

## 다음 파트로

수고하셨습니다. 이 체크리스트를 다 채우지 못했어도 괜찮습니다. 선배들도 다 그랬어요. **Part 3: 프로젝트 및 공모전 레포지토리**에서는 여기서 배운 프레임워크를 **실전 포트폴리오**로 연결하는 방법을 다룹니다.

!!! info "📌 다음 파트 예고"
    Part 3에서는 "기술은 배웠는데 뭘 만들지?"라는 고민을 해결합니다. 실전 프로젝트 레포, 공모전 우승작, 해커톤 프로젝트를 분석하며 **포트폴리오 레벨업 전략**을 함께 세워봐요.
