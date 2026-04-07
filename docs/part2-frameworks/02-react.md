# 2-2. React 생태계

> React를 처음 접하는 분들이 가장 많이 하는 실수는 **"facebook/react 레포를 클론해서 공부하려는 것"** 입니다.
> 결론부터 말씀드릴게요. 그 레포는 학습용이 아닙니다. 이 페이지에서 "어디서 시작해야 할지"를 명확히 알려드릴게요.

!!! info "📌 이 페이지의 핵심 요약"
    - `facebook/react`는 **라이브러리 내부가 궁금할 때**만 탐색
    - 실제 학습은 **Vite로 생성한 빈 프로젝트 + 공식 문서 react.dev**
    - TypeScript 타입 에러는 `typescript-cheatsheets/react`에서 검색
    - 실무 구조는 `bulletproof-react`가 가장 좋은 모범 답안

---

## 전체 학습 로드맵

```
[1주차] Vite로 React + TS 프로젝트 생성 → Hooks 기본 (useState, useEffect) 연습
   ↓
[2주차] react.dev 공식 튜토리얼 "Tic-Tac-Toe" 완주
   ↓
[3주차] typescript-cheatsheets/react의 basic 섹션을 따라 타입 정의 연습
   ↓
[4주차] bulletproof-react의 docs 디렉토리 정독 + 폴더 구조 내 프로젝트에 적용
   ↓
[5주차+] facebook/react 본체에서 useState 소스 한 번 훑어보기 (호기심 차원)
```

---

## 2-2-1. facebook/react (244K+ Stars)

**한 줄 소개**: React 라이브러리 본체 소스 코드 레포.
**왜 봐야 하는가**: "useState가 내부적으로 어떻게 상태를 저장할까?"가 궁금해질 때 답을 찾을 수 있는 유일한 곳.
**난이도**: ⭐⭐⭐⭐⭐ (본격 학습용 아님, 내부 동작 탐색용)

### 📋 이 레포에서 배울 수 있는 것
- Fiber 아키텍처의 작동 원리 (우선순위 기반 렌더링)
- Hooks의 내부 구현 (useState, useEffect 등)
- Reconciler의 diff 알고리즘
- Scheduler의 우선순위 처리
- React 팀의 실제 코드 스타일과 주석

### 🚀 15분 퀵스타트 (본체 대신 Vite로 실전 시작)

!!! tip "💡 꿀팁: 신규 프로젝트는 무조건 Vite"
    예전에는 `create-react-app`이 표준이었지만, 2023년 이후 React 팀도 **Vite / Next.js 사용을 권장**합니다. CRA는 유지보수가 중단되었어요. 무조건 Vite로 시작하세요.

**1단계: Node.js 20 LTS 확인**
```bash
node -v
npm -v
```
!!! info "예상 출력"
    ```
    v20.11.0
    10.2.4
    ```
    Node 18 이하라면 업그레이드하세요. 최신 툴체인이 Node 20 이상을 요구합니다.

**2단계: Vite로 프로젝트 생성**
```bash
npm create vite@latest my-react-app -- --template react-ts
cd my-react-app
npm install
```
!!! info "예상 출력"
    ```
    Scaffolding project in ./my-react-app...
    Done. Now run:
      cd my-react-app
      npm install
      npm run dev
    ```

**3단계: 개발 서버 실행**
```bash
npm run dev
```
!!! info "예상 출력"
    ```
    VITE v5.0.0  ready in 324 ms
    ➜  Local:   http://localhost:5173/
    ```
    브라우저에서 `http://localhost:5173`을 열면 Vite + React 기본 페이지가 나옵니다.

**4단계: 첫 Hook 예제 작성**
`src/App.tsx`를 다음으로 교체하세요.
```tsx
import { useState, useEffect } from "react";

export default function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `카운트: ${count}`;
  }, [count]);

  return (
    <div style={{ padding: 40 }}>
      <h1>안녕하세요, React!</h1>
      <button onClick={() => setCount(count + 1)}>
        클릭: {count}
      </button>
    </div>
  );
}
```
저장하면 Vite가 Hot Reload로 즉시 반영합니다. 버튼을 누르면 브라우저 탭 제목도 바뀝니다.

**5단계: 본체 레포는 선택적으로 클론**
```bash
cd ..
git clone --depth 1 https://github.com/facebook/react.git
cd react
```
주목할 디렉토리는 다음과 같습니다.

- `packages/react` — 코어 라이브러리, Hooks 구현
- `packages/react-dom` — DOM 렌더러
- `packages/react-reconciler` — Fiber 아키텍처 (**가장 흥미로움**)
- `packages/scheduler` — 우선순위 스케줄러

!!! warning "⚠️ 본체 레포의 빌드는 시도하지 마세요"
    React 본체는 자체 빌드 시스템이 복잡합니다. **소스를 읽기만** 하세요. 빌드해서 실행할 필요가 전혀 없습니다.

### 🤖 Claude Code로 200% 활용하기

!!! example "프롬프트 예시 1: useState 내부 들여다보기"
    > "facebook/react 레포의 packages/react/src/ReactHooks.js와 packages/react-reconciler/src/ReactFiberHooks.js를 함께 보고, useState가 내부적으로 어떻게 값을 저장하고 리렌더링을 트리거하는지 초보자가 이해할 수 있게 설명해줘."

!!! example "프롬프트 예시 2: Fiber가 왜 필요한가"
    > "React 15의 Stack Reconciler와 React 16+의 Fiber Reconciler의 차이를, packages/react-reconciler 디렉토리의 README와 주요 파일을 근거로 설명해줘. 왜 Fiber가 필요했는지 배경부터."

!!! example "프롬프트 예시 3: Hook 규칙의 이유"
    > "'Hooks를 조건문 안에서 호출하면 안 된다'는 규칙이 왜 있는지, packages/react-reconciler/src/ReactFiberHooks.js의 구현을 근거로 설명해줘."

!!! example "프롬프트 예시 4: 공식 문서 매핑"
    > "react.dev의 공식 문서 'State as a Snapshot' 개념을 facebook/react 레포의 실제 소스 코드 어느 부분에서 확인할 수 있는지 찾아줘."

### 🚨 자주 발생하는 에러 Top 3

!!! danger "에러 1: `Hooks can only be called inside of the body of a function component`"
    **에러 메시지**: `Error: Invalid hook call. Hooks can only be called inside of the body of a function component.`
    **원인 1**: 클래스 컴포넌트에서 Hook 호출.
    **원인 2**: 한 프로젝트에 React가 두 버전 설치됨 (보통 `npm link` 쓸 때).
    **해결**: `npm ls react`로 중복 확인 후 하나만 남기기.
    **Claude로 디버깅**:
    > "'Invalid hook call' 에러가 나는데 컴포넌트는 함수형이야. `npm ls react` 결과 보여주니까 여러 버전이 있어. 해결 방법 알려줘."

!!! danger "에러 2: `Too many re-renders. React limits the number of renders to prevent an infinite loop`"
    **에러 메시지**: 무한 렌더링.
    **원인**: `useState`의 setter를 컴포넌트 본문에서 바로 호출하고 있음 (예: `setCount(count + 1)` 이 JSX 바깥에 있음).
    **해결**: setter는 이벤트 핸들러나 `useEffect` 안에서만 호출.
    **Claude로 디버깅**:
    > "React Too many re-renders 에러가 났어. 지금 이 컴포넌트 코드 보여줄게. 무한 루프 원인과 수정 방법 알려줘."

!!! danger "에러 3: `Each child in a list should have a unique key prop`"
    **에러 메시지**: 리스트 렌더링 시 경고.
    **원인**: `.map()`으로 리스트 만들 때 `key` prop 누락.
    **해결**: 고유한 값을 `key`로 사용 (배열 index는 차선책).

### 📚 학습 체크리스트
- [ ] Vite로 React + TS 프로젝트를 생성해서 실행했다
- [ ] useState, useEffect를 사용한 컴포넌트를 작성했다
- [ ] react.dev 공식 튜토리얼 "Tic-Tac-Toe"를 절반 이상 따라 했다
- [ ] (호기심) facebook/react의 `packages/react/src/` 디렉토리를 열어 파일명만이라도 훑어봤다

---

## 2-2-2. typescript-cheatsheets/react (45K+ Stars)

**한 줄 소개**: React + TypeScript 조합에서 자주 부딪히는 타입 문제 커뮤니티 치트시트.
**왜 봐야 하는가**: "onChange 이벤트 타입이 뭐더라..." 구글 검색하면 결국 여기가 나옵니다.
**난이도**: ⭐⭐⭐ (TS 기초는 있어야 함)

### 📋 이 레포에서 배울 수 있는 것
- Props / State의 정확한 타입 정의
- 이벤트 핸들러 타입 (`React.ChangeEvent<HTMLInputElement>` 등)
- `useRef`의 타입 (`useRef<HTMLDivElement>(null)`)
- Generic 컴포넌트 만들기
- HOC의 타입 정의
- Polymorphic 컴포넌트 (`as` prop 패턴)

### 🚀 15분 퀵스타트

**1단계: 웹에서 바로 읽기 (권장)**
```
https://react-typescript-cheatsheet.netlify.app/
```
!!! tip "💡 클론 없이 웹사이트로"
    이 레포는 문서 위주라서 **클론할 필요가 거의 없습니다**. 즐겨찾기에 추가해두고 필요할 때마다 검색하세요.

**2단계: 필요하면 클론**
```bash
git clone --depth 1 https://github.com/typescript-cheatsheets/react.git
cd react
```

**3단계: 핵심 문서 파일 열기**
- `README.md` — 전체 인덱스
- `docs/basic/getting-started/` — Props, State, Event 기본 타입
- `docs/advanced/` — Generic, Polymorphic, Conditional 타입
- `docs/hoc/` — HOC의 제네릭 처리

**4단계: 내 프로젝트에서 실습**
Vite로 만든 프로젝트의 `App.tsx`에 다음을 추가해보세요.
```tsx
import { useState, ChangeEvent, FormEvent } from "react";

interface FormData {
  username: string;
  age: number;
}

export default function Form() {
  const [form, setForm] = useState<FormData>({ username: "", age: 0 });

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log(form);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="username" onChange={handleChange} />
      <input name="age" type="number" onChange={handleChange} />
      <button type="submit">제출</button>
    </form>
  );
}
```
이 한 예제에 치트시트의 핵심 패턴이 모두 들어 있습니다.

**5단계: 에러 검색 습관 만들기**
VS Code에서 타입 에러가 뜨면, **에러 메시지를 그대로 치트시트에서 검색**하세요. 90% 이상 해결됩니다.

### 🤖 Claude Code로 200% 활용하기

!!! example "프롬프트 예시 1: 이벤트 타입 정리"
    > "typescript-cheatsheets/react의 basic 섹션을 근거로 Input, TextArea, Select, Form의 onChange/onSubmit 이벤트 타입을 모두 표로 정리해줘. 예제 코드도 함께."

!!! example "프롬프트 예시 2: Generic 컴포넌트"
    > "이 레포의 advanced 섹션 'Generic Components' 부분을 보고, 내 프로젝트의 재사용 가능한 List<T> 컴포넌트를 만드는 방법을 step-by-step으로 알려줘."

!!! example "프롬프트 예시 3: 실전 에러 해결"
    > "내가 지금 이런 타입 에러가 났어: `Type '(e: Event) => void' is not assignable to type 'MouseEventHandler<HTMLButtonElement>'`. typescript-cheatsheets/react를 근거로 올바른 타입을 알려줘."

!!! example "프롬프트 예시 4: useRef 타입"
    > "typescript-cheatsheets/react에서 useRef의 올바른 타입 정의 방법 3가지를 찾아서 각각 언제 쓰는지 알려줘. (DOM 참조, 값 저장, forwardRef)"

### 🚨 자주 발생하는 에러 Top 3

!!! danger "에러 1: `Property 'value' does not exist on type 'EventTarget'`"
    **원인**: `e.target.value`가 타입 추론 안 됨.
    **해결**: 이벤트 타입을 `ChangeEvent<HTMLInputElement>`로 명시.
    ```tsx
    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
      console.log(e.target.value); // 이제 string으로 추론됨
    };
    ```

!!! danger "에러 2: `Type 'null' is not assignable to type 'HTMLDivElement'`"
    **원인**: `useRef<HTMLDivElement>()`를 초기값 없이 선언.
    **해결**: `useRef<HTMLDivElement>(null)`로 초기값 `null` 명시.

!!! danger "에러 3: `Children' does not exist on type`"
    **원인**: 함수형 컴포넌트에서 `children`을 받는데 타입 정의 누락.
    **해결**: `React.PropsWithChildren<YourProps>` 또는 `children: React.ReactNode` 명시.
    **Claude로 디버깅**:
    > "children prop을 받는 React 함수 컴포넌트의 가장 권장되는 TypeScript 타입 정의 방법을 알려줘. React.FC 사용 여부도 포함해서."

### 📚 학습 체크리스트
- [ ] `react-typescript-cheatsheet.netlify.app`을 즐겨찾기했다
- [ ] Form 예제를 Vite 프로젝트에서 직접 작성했다
- [ ] `ChangeEvent<HTMLInputElement>` 타입의 의미를 설명할 수 있다
- [ ] Generic 컴포넌트를 하나 만들어봤다

---

## 2-2-3. alan2207/bulletproof-react (29K+ Stars)

**한 줄 소개**: "확장 가능한 React 프로젝트 구조"의 모범 답안으로 가장 자주 인용되는 레포.
**왜 봐야 하는가**: "내 React 프로젝트 폴더 구조 이게 맞나?" 고민될 때 정답지 역할.
**난이도**: ⭐⭐⭐⭐ (현업자 수준의 구조, 초보자는 docs부터 읽으세요)

### 📋 이 레포에서 배울 수 있는 것
- Feature 기반 폴더 구조 (페이지 기반 대신)
- 상태 관리 분리: 서버 상태(React Query) + 전역 UI 상태(Zustand)
- MSW (Mock Service Worker)로 백엔드 없이 프론트 개발
- React Hook Form + Zod 폼 검증
- 테스트 전략 (Vitest, Testing Library, MSW)
- ESLint + Prettier + Husky로 코드 품질 강제

### 🚀 15분 퀵스타트

**1단계: Shallow Clone**
```bash
git clone --depth 1 https://github.com/alan2207/bulletproof-react.git
cd bulletproof-react
```

**2단계: docs 디렉토리를 먼저 읽기 (가장 중요!)**
```bash
cd docs
ls
```
!!! info "예상 출력"
    ```
    application-overview.md
    project-standards.md
    project-structure.md
    components-and-styling.md
    api-layer.md
    state-management.md
    testing.md
    error-handling.md
    security.md
    deployment.md
    ```

!!! tip "💡 꿀팁: 코드보다 docs가 더 중요해요"
    이 레포의 진짜 가치는 `src/` 코드가 아니라 `docs/` 문서입니다. 저자가 수년간 쌓은 **"왜 이렇게 구조를 잡아야 하는지"** 철학이 담겨 있어요. 이 문서들을 정독하는 것만으로도 시니어 수준의 프로젝트 설계 감각이 생깁니다.

**3단계: 예제 앱 실행**
```bash
cd ../apps/react-vite
npm install
npm run dev
```
!!! info "예상 출력"
    ```
    VITE v5.x  ready in 500 ms
    ➜  Local:   http://localhost:3000/
    ```
    MSW가 자동으로 가상 API 서버를 띄워주므로, 백엔드 없이도 완전한 앱이 동작합니다.

**4단계: `src/` 구조 파악**
```bash
cd src
ls
```
- `app/` — 라우팅 + 루트 프로바이더
- `assets/` — 이미지, 폰트
- `components/` — 공용 UI 컴포넌트
- `config/` — 환경 변수
- `features/` — **핵심!** 기능별 모듈
- `hooks/` — 공용 커스텀 훅
- `lib/` — 외부 라이브러리 래퍼 (axios, react-query 설정)
- `providers/` — 앱 전역 프로바이더
- `stores/` — Zustand 전역 상태
- `testing/` — 테스트 유틸 + MSW 핸들러
- `types/` — 공용 타입
- `utils/` — 공용 유틸 함수

**5단계: features 디렉토리 하나 깊이 보기**
```bash
cd features/discussions
ls
```
!!! info "예상 출력"
    ```
    api/          # React Query 훅
    components/   # 이 feature에서만 쓰는 컴포넌트
    routes/       # 이 feature의 페이지
    types/        # 이 feature의 타입
    index.ts      # 공개 API (export)
    ```
    **이 구조가 이 레포의 핵심입니다.** 각 feature는 독립된 작은 앱처럼 동작합니다.

### 🤖 Claude Code로 200% 활용하기

!!! example "프롬프트 예시 1: 구조 철학 이해"
    > "bulletproof-react의 docs/project-structure.md를 읽고, 왜 'pages/' 대신 'features/' 구조를 쓰는지 3가지 이유로 정리해줘. 각 이유마다 구체적 예시 코드도 함께."

!!! example "프롬프트 예시 2: 내 프로젝트에 적용"
    > "내 프로젝트는 지금 pages 기반 구조인데, bulletproof-react의 features 기반으로 리팩토링하려고 해. 어떤 순서로 옮기면 안전한지 단계별 마이그레이션 계획을 짜줘."

!!! example "프롬프트 예시 3: 상태 관리 분리"
    > "bulletproof-react의 docs/state-management.md를 근거로 '서버 상태'와 '클라이언트 상태'를 어떻게 구분하는지 설명하고, 실제 코드에서 React Query와 Zustand가 각각 어떤 데이터를 관리하는지 예시를 찾아줘."

!!! example "프롬프트 예시 4: API 레이어 이식"
    > "bulletproof-react의 src/lib/api-client.ts 파일을 읽고, 내 프로젝트에 이식할 수 있는 최소 버전으로 간소화해줘. 에러 처리 인터셉터는 유지하되, 불필요한 의존성은 제거해서."

!!! example "프롬프트 예시 5: 테스트 전략"
    > "이 레포의 testing 디렉토리와 docs/testing.md를 보고, MSW + Vitest + Testing Library로 한 컴포넌트를 테스트하는 최소 예제를 작성해줘."

### 🚨 자주 발생하는 에러 Top 3

!!! danger "에러 1: `npm install` 실패"
    **에러 메시지**: `npm ERR! peer dep missing` 또는 React 버전 충돌.
    **원인**: 이 레포는 pnpm workspace를 사용. npm으로 하면 문제 생김.
    **해결**: `npm install -g pnpm` 후 `pnpm install`.
    **Claude로 디버깅**:
    > "bulletproof-react를 npm install 하니까 peer dep 에러가 계속 나. pnpm으로 설치하는 방법과 pnpm을 처음 쓰는 사람을 위한 기본 명령어도 알려줘."

!!! danger "에러 2: MSW 핸들러가 동작 안 함"
    **에러 메시지**: Network 탭에서 실제 서버로 요청이 나감.
    **원인**: MSW 서비스 워커가 등록 안 됨 (`public/mockServiceWorker.js` 누락).
    **해결**: `npx msw init public/` 실행.

!!! danger "에러 3: 환경 변수 `VITE_API_URL` 읽기 실패"
    **에러 메시지**: `process.env.VITE_API_URL is undefined`
    **원인**: Vite는 `import.meta.env.VITE_*` 형식 사용. `process.env` 아님.
    **해결**: `.env.local` 파일 생성 후 `VITE_API_URL=http://localhost:8080` 추가, 코드에서는 `import.meta.env.VITE_API_URL`로 접근.

### 📚 학습 체크리스트
- [ ] `docs/` 디렉토리의 문서를 최소 5개 이상 정독했다
- [ ] 예제 앱을 로컬에서 실행해서 MSW로 동작하는 것을 확인했다
- [ ] `features/` 디렉토리 구조의 장점을 3가지 이상 말할 수 있다
- [ ] 내 프로젝트의 폴더 구조를 이 레포 기준으로 리팩토링해봤다
- [ ] React Query와 Zustand의 역할 분리를 이해했다

---

## 이 섹션 마무리

React 생태계는 "본체를 파는 것"이 아니라 **"도구를 조합하는 법을 익히는 것"** 이 핵심입니다. 여러분이 배워야 할 건 Vite + React + TypeScript + React Query + Zustand의 **조합 감각**입니다. 이 감각은 `bulletproof-react`에서 얻을 수 있어요.

다음은 React의 한 단계 위, **Next.js 생태계**입니다. [03-nextjs.md](03-nextjs.md)로 넘어가세요.

!!! info "📌 한 줄 정리"
    React 학습의 왕도는 **"Vite로 빈 프로젝트 → react.dev 공식 문서 → TS 치트시트로 에러 해결 → bulletproof-react로 구조 배우기"** 순서입니다.
