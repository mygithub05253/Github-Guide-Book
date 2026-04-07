# 📘 React 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/facebook/react.svg?style=social)](https://github.com/facebook/react)

!!! info "레포지토리"
    **facebook/react** · 230k+ ⭐ · MIT License · [react.dev](https://react.dev)

---

## 🧐 1. React는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: React는 **사용자 인터페이스를 만들기 위한 JavaScript 라이브러리**입니다. "프레임워크"가 아니라 "라이브러리"라는 점이 중요합니다 — 라우팅·상태관리·데이터 패칭은 별도 도구를 조합합니다.

### 공식 README 기반 핵심 특성

- **선언형 (Declarative)**: 각 상태(state)에 대한 단순한 뷰를 설계하면, React가 데이터 변경 시 필요한 컴포넌트만 효율적으로 업데이트·렌더링합니다. → 코드가 예측 가능하고 디버깅이 쉬워집니다.
- **컴포넌트 기반 (Component-Based)**: 자체 상태를 관리하는 캡슐화된 컴포넌트를 만들고, 이들을 조합해 복잡한 UI를 구성합니다. 템플릿이 아닌 JavaScript로 로직을 작성하므로 풍부한 데이터를 자유롭게 전달할 수 있습니다.
- **Learn Once, Write Anywhere**: React 자체는 기술 스택에 대한 가정이 없습니다. Node로 SSR, [React Native](https://reactnative.dev/)로 모바일 앱까지 동일한 모델로 개발 가능.

### 실무 도입 포인트

| 도입 이유 | 구체적 효과 |
|---|---|
| **거대한 생태계** | 채용 시장 1위, 라이브러리·도구가 가장 많음 → 막힐 때 검색 답이 가장 빠르게 나옴 |
| **컴포넌트 재사용** | 디자인 시스템(shadcn/ui, Material UI 등)을 그대로 가져와 조립 가능 |
| **점진적 도입** | 기존 jQuery/서버 렌더 페이지의 일부에만 React를 끼워넣을 수도 있음 |
| **메타 프레임워크** | Next.js, Remix 등 풀스택 프레임워크의 기반 → 한 번 배우면 확장 경로가 명확함 |

### 기존 방식 vs React

```
[기존 jQuery/Vanilla JS]
DOM을 직접 조작 → 상태와 UI가 분리됨 → 화면이 복잡해질수록 버그 폭증

[React]
"상태를 바꾸면 UI는 알아서 다시 그려진다" → 개발자는 "지금 이 시점의 화면이 어떻게 생겼는가"만 선언
```

## 🚀 2. 10분 퀵스타트

!!! tip "공식 권장 경로 (2026 기준)"
    React 단독 설치보다 **메타 프레임워크(Next.js, Remix, Vite + React)**로 시작하는 것이 공식 권장 사항입니다. 학습용으로는 Vite가 가장 빠릅니다.

### 환경 준비

```bash
node -v    # v20+ 권장
npm -v
```

### Vite로 React 프로젝트 생성

```bash
npm create vite@latest my-react-app -- --template react-ts
cd my-react-app
npm install
npm run dev
```

### 검증 (예상 출력)

```
  VITE v5.x.x  ready in 312 ms
  ➜  Local:   http://localhost:5173/
```

브라우저에서 `http://localhost:5173` 접속 시 React 로고 화면이 보이면 성공.

### 첫 컴포넌트 (공식 README 예제)

```jsx
import { createRoot } from 'react-dom/client';

function HelloMessage({ name }) {
  return <div>Hello {name}</div>;
}

const root = createRoot(document.getElementById('container'));
root.render(<HelloMessage name="Taylor" />);
```

JSX는 HTML과 비슷해 보이지만 실제로는 JavaScript 함수 호출(`React.createElement`)로 변환됩니다.

## 🛠️ 3. 코드 해부학: 어디부터 열어볼 것인가

학습용으로 `facebook/react` 모노레포를 클론했다면 다음 순서로 탐색하세요.

| 경로 | 역할 | 학습 포인트 |
|---|---|---|
| `packages/react/src/React.js` | Public API 진입점 | `useState`, `useEffect` 등이 어디서 export되는지 확인 |
| `packages/react-dom/src/client/ReactDOMRoot.js` | `createRoot` 구현 | "DOM에 React를 어떻게 마운트하는가" |
| `packages/react-reconciler/` | **Fiber 재조정자(reconciler)** | React의 핵심 — 어떤 컴포넌트를 다시 그릴지 결정하는 알고리즘 |
| `packages/scheduler/` | 작업 우선순위 스케줄러 | Concurrent Mode의 기반 |

!!! tip "초보자 추천"
    소스코드는 매우 방대합니다. 처음에는 **`react.dev/learn`의 튜토리얼**을 끝까지 따라 한 뒤, "Hooks가 내부적으로 어떻게 동작하지?" 같은 호기심이 생겼을 때 `react-reconciler`를 열어보세요.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude (복잡한 컴포넌트 리팩토링)
```
/think 다음 React 컴포넌트는 props가 12개이고 useEffect가 4개 있다.
재사용성과 테스트 가능성을 높이도록 커스텀 Hook으로 분리하고,
각 Hook의 책임을 한 줄 주석으로 설명해 줘.

[코드 붙여넣기]
```

### 🔵 Gemini (최신 변경사항 요약)
```
React 19와 React 18의 주요 차이점을 비전공 대학생도 이해할 수 있게 설명해 줘.
특히 Server Components, use() Hook, Actions 3가지를 실제 코드 예시로 비교해 줘.
```

### 🟢 ChatGPT (학습 로드맵 기획)
```
나는 HTML/CSS/JS 기초만 아는 비전공 대학생이다.
React를 4주 안에 "포트폴리오에 올릴 수 있는 Todo 앱" 수준까지 학습하려고 한다.
주차별 학습 내용·과제·검증 기준을 마크다운 표로 만들어 줘.
```

### ⬛ GitHub Copilot / Codex (IDE 실시간 보조)
```jsx
// TODO: useReducer로 폼 상태 관리
//   - 필드: name, email, message
//   - 액션: UPDATE_FIELD, RESET, SUBMIT_START, SUBMIT_SUCCESS, SUBMIT_ERROR
//   - 검증: email 형식, message 최소 10자
```

## 🔗 5. 관련 레포 · 다음 단계

- **메타 프레임워크**: [Next.js 딥다이브](../nextjs/index.md)
- **상태관리**: [Zustand 딥다이브](../zustand/index.md)
- **스타일링**: [Tailwind CSS 딥다이브](../tailwind/index.md)
- **공식 학습 사이트**: [react.dev](https://react.dev) · 한국어: [ko.react.dev](https://ko.react.dev)
- **컴포넌트 라이브러리**: [shadcn/ui](https://ui.shadcn.com), [Radix UI](https://www.radix-ui.com)
