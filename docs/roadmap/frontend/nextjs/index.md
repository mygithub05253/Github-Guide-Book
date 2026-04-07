# 📘 Next.js 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/vercel/next.js.svg?style=social)](https://github.com/vercel/next.js)

!!! info "레포지토리"
    **vercel/next.js** · 130k+ ⭐ · MIT License · [nextjs.org](https://nextjs.org)

---

## 🧐 1. Next.js는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Next.js는 **React 기반 풀스택 웹 프레임워크**입니다. SSR(서버 사이드 렌더링), SSG(정적 생성), API Routes, 이미지 최적화, App Router(RSC) 등 production에 필요한 거의 모든 기능을 통합 제공합니다.

### 핵심 특성
- **App Router (Next 13+)**: 파일 시스템 기반 라우팅 + React Server Components(RSC) 표준 지원. 서버에서만 실행되는 컴포넌트로 번들 크기를 극적으로 줄입니다.
- **렌더링 옵션**: SSR / SSG / ISR(Incremental Static Regeneration) / CSR을 페이지별로 선택.
- **풀스택**: Route Handlers (`app/api/*/route.ts`)로 백엔드 API를 동일 프로젝트에서 작성.
- **이미지·폰트 최적화**: `next/image`, `next/font`로 LCP 자동 최적화.
- **Edge Runtime**: Vercel·Cloudflare 엣지에서 실행되는 가벼운 런타임.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **SEO가 중요한 서비스** | SSR/SSG로 메타 태그·OG 이미지가 크롤러에 노출 |
| **빠른 첫 페이지 로딩** | RSC + 스트리밍으로 TTFB·LCP 개선 |
| **풀스택 일체화** | 프론트·BFF를 한 레포에서 관리 |
| **Vercel 무료 배포** | 개인 프로젝트·포트폴리오를 1분 만에 배포 |

## 🚀 2. 10분 퀵스타트

```bash
npx create-next-app@latest my-next-app --typescript --tailwind --app
cd my-next-app
npm run dev
```

브라우저: `http://localhost:3000`

### 첫 Server Component
```tsx
// app/page.tsx
async function getStars() {
  const res = await fetch('https://api.github.com/repos/vercel/next.js', {
    next: { revalidate: 3600 }, // ISR: 1시간마다 재검증
  });
  return (await res.json()).stargazers_count;
}

export default async function Home() {
  const stars = await getStars();
  return <h1>Next.js stars: {stars.toLocaleString()}</h1>;
}
```

서버에서 fetch 실행 → HTML로 직렬화 → 클라이언트는 JS 없이도 보임.

## 🛠️ 3. 코드 해부학

| 경로 | 역할 |
|---|---|
| `app/layout.tsx` | 전역 레이아웃 (`<html>`, `<body>`) |
| `app/page.tsx` | 루트 페이지 (Server Component 기본) |
| `app/api/*/route.ts` | Route Handler (REST API) |
| `next.config.js` | 빌드 설정 (이미지 도메인, redirects 등) |
| `middleware.ts` | 모든 요청 진입점 (인증·A/B 테스트) |

!!! warning "Server vs Client 구분"
    `'use client'` 지시어가 없는 컴포넌트는 모두 **서버 컴포넌트**입니다. `useState`, `onClick` 등을 쓰려면 파일 최상단에 `'use client'`를 명시해야 합니다.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 다음 Next.js App Router 페이지를 RSC 모범 사례에 맞게 리뷰해 줘.
- 'use client' 경계가 최소화되었는가
- fetch 캐싱·재검증 전략이 적절한가
- Suspense·loading.tsx로 스트리밍이 적용되었는가
[코드]
```

### 🔵 Gemini
```
Next.js App Router와 Pages Router의 차이를 비교 표로 정리하고,
2026년 신규 프로젝트가 App Router를 선택해야 하는 이유 5가지를 설명해 줘.
```

### 🟢 ChatGPT
```
Next.js 14 + Supabase + Tailwind로 "대학생 스터디 매칭 서비스"를 만들려고 한다.
폴더 구조, 라우트 목록, DB 스키마, 4주 스프린트를 마크다운으로 기획해 줘.
```

### ⬛ Copilot
```tsx
// TODO: app/api/posts/route.ts - GET(목록), POST(작성)
//   - Zod로 입력 검증, Prisma로 DB 접근
```

## 🔗 5. 관련 레포 · 다음 단계
- [React 딥다이브](../react/index.md) · [Tailwind 딥다이브](../tailwind/index.md)
- 공식 문서: [nextjs.org/docs](https://nextjs.org/docs) · 한국어: [nextjs.org/learn](https://nextjs.org/learn)
- 호스팅: [Vercel](https://vercel.com), [Cloudflare Pages](https://pages.cloudflare.com)
- 본 가이드북: [Part 2-3 · Next.js](../../../part2-frameworks/03-nextjs.md)
