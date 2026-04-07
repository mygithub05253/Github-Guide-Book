# 📘 Tailwind CSS 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/tailwindlabs/tailwindcss.svg?style=social)](https://github.com/tailwindlabs/tailwindcss)

!!! info "레포지토리"
    **tailwindlabs/tailwindcss** · 82k+ ⭐ · MIT License · [tailwindcss.com](https://tailwindcss.com)

---

## 🧐 1. Tailwind CSS는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Tailwind CSS는 **유틸리티 우선(utility-first) CSS 프레임워크**입니다. `text-center`, `bg-blue-500`, `p-4`처럼 작은 단위 클래스를 HTML에 직접 조합해 디자인을 만듭니다.

### 핵심 특성
- **유틸리티 클래스**: 색상·간격·타이포·플렉스 등 모든 디자인 토큰이 클래스화됨.
- **JIT 컴파일러**: 사용된 클래스만 빌드 결과에 포함 → CSS 파일 수 KB 수준.
- **반응형 prefix**: `md:flex`, `lg:grid-cols-3`처럼 한 줄로 반응형 표현.
- **다크모드**: `dark:bg-gray-900` prefix로 즉시 지원.
- **디자인 토큰 커스터마이즈**: `tailwind.config.js`에서 색상·폰트·간격을 일관되게 정의.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **클래스 이름 고민 제로** | BEM 네이밍 노이즈 사라짐 |
| **디자인 시스템 일관성** | 토큰화된 색상·간격으로 자동 통일 |
| **shadcn/ui 호환** | 가장 인기 있는 React 컴포넌트 라이브러리의 기반 |
| **CSS-in-JS 대비 빠름** | 런타임 스타일 계산 없음 |

## 🚀 2. 10분 퀵스타트

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```js
// tailwind.config.js
export default {
  content: ['./src/**/*.{html,js,ts,jsx,tsx}'],
  theme: { extend: {} },
  plugins: [],
};
```

```css
/* src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 첫 컴포넌트
```html
<button class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-medium hover:bg-indigo-700 transition">
  PLAF 시작하기
</button>
```

## 🛠️ 3. 코드 해부학

| 경로 | 역할 |
|---|---|
| `tailwind.config.js` | 프로젝트 디자인 토큰 (색·폰트·spacing) |
| `src/**/*.tsx` | 클래스가 사용된 모든 파일 (`content` 스캔 대상) |
| `@layer components` | 반복되는 패턴을 컴포넌트 클래스로 추출 |

!!! tip "초보자 함정"
    클래스가 너무 길어지면 **컴포넌트로 분리**하거나 `@apply`를 활용하세요. 한 줄에 30개 클래스는 리팩토링 신호입니다.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 이 React 컴포넌트의 Tailwind 클래스를 리뷰하고
1) 중복 제거 2) 반응형 누락 3) 다크모드 누락 4) 접근성(focus ring)
관점에서 개선해 줘.
```

### 🔵 Gemini
```
Tailwind v3와 v4의 주요 차이점을 비교하고, v4의 Oxide 엔진과 CSS-first 설정이
실무에 어떤 영향을 주는지 설명해 줘.
```

### 🟢 ChatGPT
```
"학생 포트폴리오 사이트"의 디자인 시스템을 Tailwind config로 만들어 줘.
색상 팔레트(primary, secondary, accent), 폰트, 간격을 포함.
```

### ⬛ Copilot
```html
<!-- TODO: 카드 그리드 - 3열 데스크탑, 2열 태블릿, 1열 모바일, 호버 시 그림자 -->
```

## 🔗 5. 관련 레포 · 다음 단계
- [shadcn/ui](https://ui.shadcn.com) — Tailwind 기반 컴포넌트 라이브러리
- [Headless UI](https://headlessui.com), [Radix UI](https://www.radix-ui.com)
- 공식 문서: [tailwindcss.com/docs](https://tailwindcss.com/docs)
- [React 딥다이브](../react/index.md) · [Next.js 딥다이브](../nextjs/index.md)
