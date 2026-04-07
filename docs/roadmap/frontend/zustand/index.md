# 📘 Zustand 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/pmndrs/zustand.svg?style=social)](https://github.com/pmndrs/zustand)

!!! info "레포지토리"
    **pmndrs/zustand** · 47k+ ⭐ · MIT License

---

## 🧐 1. Zustand는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Zustand("주스탄트", 독일어로 "상태")는 **React를 위한 초경량(1KB) 상태 관리 라이브러리**입니다. Redux의 보일러플레이트 없이, Context API의 성능 문제 없이 글로벌 상태를 관리합니다.

### 핵심 특성
- **Boilerplate 0**: action·reducer·dispatcher 없이 함수 호출로 상태 변경.
- **React 외부 사용 가능**: 컴포넌트 트리 밖(이벤트 핸들러, 워커)에서도 store 접근.
- **선택자(Selector)로 리렌더 최소화**: 필요한 필드만 구독.
- **미들웨어**: persist(LocalStorage), devtools(Redux DevTools), immer, subscribeWithSelector.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **Redux보다 학습 곡선 낮음** | 30분이면 익힘 |
| **Context보다 빠름** | 컴포넌트 단위 구독 → 불필요한 리렌더 없음 |
| **TypeScript 친화** | 제네릭으로 완벽한 타입 추론 |

## 🚀 2. 10분 퀵스타트

```bash
npm install zustand
```

```ts
// store/useCounter.ts
import { create } from 'zustand';

interface CounterState {
  count: number;
  increment: () => void;
  reset: () => void;
}

export const useCounter = create<CounterState>((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  reset: () => set({ count: 0 }),
}));
```

```tsx
function Counter() {
  const count = useCounter((s) => s.count);
  const increment = useCounter((s) => s.increment);
  return <button onClick={increment}>Count: {count}</button>;
}
```

## 🛠️ 3. 코드 해부학

| 패턴 | 권장 사용 |
|---|---|
| **Slice 패턴** | 거대 store를 도메인별로 분리 |
| **persist 미들웨어** | 새로고침해도 유지되는 상태(테마, 로그인) |
| **devtools 미들웨어** | Redux DevTools에서 추적 |
| **shallow 비교** | 객체·배열을 한 selector로 가져올 때 |

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think Redux Toolkit으로 작성된 다음 store를 Zustand로 마이그레이션하고,
slice 패턴 + persist 미들웨어 + TypeScript 타입을 적용해 줘.
```

### 🔵 Gemini
```
Zustand vs Redux Toolkit vs Jotai vs Recoil을 비교 표로 정리해 줘.
번들 크기, 학습 곡선, DevTools 지원, 적합한 프로젝트 규모 기준으로.
```

### 🟢 ChatGPT
```
"장바구니 + 사용자 인증 + 다크모드"를 가진 e-commerce 앱의
Zustand store 구조를 slice 패턴으로 설계해 줘.
```

### ⬛ Copilot
```ts
// TODO: useAuthStore - user, token, login(), logout(), persist 미들웨어 적용
```

## 🔗 5. 관련 레포 · 다음 단계
- pmndrs 생태계: [Jotai](https://github.com/pmndrs/jotai), [Valtio](https://github.com/pmndrs/valtio)
- 공식 문서: [zustand.docs.pmnd.rs](https://zustand.docs.pmnd.rs)
- [React 딥다이브](../react/index.md)
