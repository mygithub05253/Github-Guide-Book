# 2-3. Next.js 생태계

> "React는 할 줄 아는데 Next.js는 왜 따로 배워야 해요?" 많이 받는 질문입니다.
> 답: **Next.js는 React에 라우팅, 서버 사이드 렌더링, 서버 컴포넌트, API, 이미지 최적화, 배포 최적화까지 얹은 풀스택 프레임워크**이기 때문입니다.
> 지금 한국의 프론트 현업 채용 공고 80% 이상이 Next.js를 요구합니다. 피할 수 없다면 이번 기회에 제대로 익혀봅시다.

!!! info "📌 이 페이지의 핵심 요약"
    - 신규 프로젝트는 `create-next-app`으로 만들고, **App Router**를 기본으로 선택
    - 본체 레포의 `examples/` 디렉토리가 **진정한 보물창고** (100+ 예제)
    - Server Components와 Client Components의 구분이 가장 중요한 개념
    - `vercel/commerce`는 **프로덕션급 App Router 모범 사례**

---

## 전체 학습 로드맵

```
[1주차] create-next-app으로 App Router 프로젝트 생성 → 페이지 1개 만들기
   ↓
[2주차] Server Component vs Client Component 차이 이해 → 'use client' 지시자 연습
   ↓
[3주차] vercel/next.js의 examples/blog-starter 클론해서 마크다운 블로그 만들기
   ↓
[4주차] examples/with-next-auth로 구글 로그인 붙이기
   ↓
[5주차+] vercel/commerce의 app/ 디렉토리를 읽어 실전 패턴 배우기
```

---

## 2-3-1. vercel/next.js (130K+ Stars)

**한 줄 소개**: React 기반 풀스택 프레임워크. 공식 레포에는 100+ 개의 실전 예제가 있습니다.
**왜 봐야 하는가**: "블로그 만들고 싶다 / 스트라이프 결제 붙이고 싶다 / 인증 추가하고 싶다" — 답이 전부 `examples/` 안에 있습니다.
**난이도**: ⭐⭐⭐ (App Router 개념 숙지 필요)

### 📋 이 레포에서 배울 수 있는 것
- App Router의 파일 기반 라우팅
- Server Components (서버에서 렌더링되는 기본값)
- Client Components (`'use client'` 지시자)
- Server Actions (폼 제출을 함수 호출로)
- 데이터 페칭 + 캐싱 + 재검증(`revalidateTag`)
- Image 최적화, Font 최적화
- 100+ 공식 예제 (`examples/` 디렉토리)

### 🚀 15분 퀵스타트

**1단계: Node.js 20+ 확인**
```bash
node -v
```
!!! info "예상 출력"
    ```
    v20.11.0
    ```
    Next.js 14+는 Node 18.17+ 필수, Node 20 LTS 권장.

**2단계: 프로젝트 생성**
```bash
npx create-next-app@latest my-next-app
```
!!! info "대화형 프롬프트 답변 (권장값)"
    ```
    ✔ Would you like to use TypeScript? … Yes
    ✔ Would you like to use ESLint? … Yes
    ✔ Would you like to use Tailwind CSS? … Yes
    ✔ Would you like to use `src/` directory? … Yes
    ✔ Would you like to use App Router? (recommended) … Yes
    ✔ Would you like to customize the default import alias? … No
    ```
    **App Router는 반드시 Yes**. Pages Router는 레거시입니다.

**3단계: 개발 서버 실행**
```bash
cd my-next-app
npm run dev
```
!!! info "예상 출력"
    ```
    ▲ Next.js 14.2.0
    - Local:        http://localhost:3000
    ✓ Ready in 2.3s
    ```

**4단계: 첫 페이지 수정하기**
`src/app/page.tsx`를 열어 다음으로 교체.
```tsx
export default function HomePage() {
  return (
    <main className="p-10">
      <h1 className="text-3xl font-bold">안녕하세요, Next.js!</h1>
      <p className="mt-4">이 페이지는 Server Component 입니다.</p>
    </main>
  );
}
```
저장하면 즉시 반영됩니다. 브라우저 개발자 도구의 Network 탭에서 보면, HTML에 텍스트가 이미 포함되어 옵니다 (클라이언트 JS 실행 전에).

**5단계: 새 경로 추가하기**
`src/app/about/page.tsx` 파일을 만들어 붙여넣으세요.
```tsx
export default function AboutPage() {
  return <h1>About 페이지</h1>;
}
```
`http://localhost:3000/about`으로 접속하면 바로 동작합니다. **파일 시스템이 곧 라우팅**입니다.

### Next.js 본체 레포에서 주목할 곳

```bash
git clone --depth 1 https://github.com/vercel/next.js.git
cd next.js
```

| 디렉토리 | 용도 |
| --- | --- |
| `examples/` | **100+ 공식 예제** (가장 중요) |
| `packages/next` | 프레임워크 코어 |
| `docs/` | 공식 문서 소스 (오프라인 참고용) |
| `test/` | E2E 테스트 (실전 시나리오 참고) |

### 추천 예제 Top 10 (examples/ 하위)

| 예제 디렉토리 | 학습 포인트 | 난이도 |
| --- | --- | --- |
| `blog-starter` | 마크다운 블로그 (초보자 최적) | ⭐⭐ |
| `with-tailwindcss` | Tailwind CSS 통합 | ⭐ |
| `api-routes-rest` | API Routes 기본 패턴 | ⭐⭐ |
| `with-supabase` | 인증 + DB 풀스택 | ⭐⭐⭐ |
| `with-next-auth` | OAuth 소셜 로그인 | ⭐⭐⭐ |
| `with-stripe-typescript` | 결제 연동 | ⭐⭐⭐⭐ |
| `with-prisma` | Prisma ORM 통합 | ⭐⭐⭐ |
| `with-mongodb` | MongoDB 연동 | ⭐⭐⭐ |
| `i18n-routing` | 다국어 라우팅 | ⭐⭐⭐ |
| `with-socket-io` | 실시간 통신 | ⭐⭐⭐⭐ |

### 🤖 Claude Code로 200% 활용하기

!!! example "프롬프트 예시 1: 예제 골라주기"
    > "내가 만들고 싶은 건 '마크다운 파일로 관리하는 개인 블로그 + 구글 로그인으로 댓글 작성'이야. vercel/next.js의 examples/ 디렉토리에서 참고하면 좋을 예제 3개를 골라주고, 각 예제에서 어떤 부분을 가져올지 알려줘."

!!! example "프롬프트 예시 2: blog-starter 이해"
    > "vercel/next.js 레포의 examples/blog-starter 구조를 설명하고, 내 가이드북 프로젝트에 옮겨올 때 수정해야 할 부분을 알려줘. 특히 _posts 디렉토리 구조와 lib/api.ts 파일을."

!!! example "프롬프트 예시 3: App Router vs Pages Router"
    > "App Router의 layout.tsx 와 Pages Router의 _app.tsx 차이를 vercel/next.js 공식 docs 디렉토리에서 근거를 찾아 비교해줘. 왜 App Router로 옮겨야 하는지 이유도."

!!! example "프롬프트 예시 4: Server Action 실전"
    > "Next.js 14의 Server Action을 써서 폼 제출 → DB 저장 → 리다이렉트까지 하는 최소 예제를 작성해줘. vercel/next.js examples에서 참고할 만한 예제도 같이 알려줘."

!!! example "프롬프트 예시 5: 데이터 페칭 패턴"
    > "Server Component에서 데이터 페칭할 때 fetch, unstable_cache, revalidateTag의 차이와 사용 시점을 vercel/next.js 공식 docs를 근거로 설명해줘."

### 🚨 자주 발생하는 에러 Top 5

!!! danger "에러 1: `You're importing a component that needs useState. It only works in a Client Component`"
    **에러 메시지**: Client Hook을 Server Component에서 사용.
    **원인**: Next.js 13+ App Router는 **기본값이 Server Component**. `useState`, `useEffect`, `onClick` 등은 Client에서만 동작.
    **해결**: 파일 맨 위에 `'use client';` 추가.
    **Claude로 디버깅**:
    > "Next.js App Router에서 `'use client'` 지시자를 언제 써야 하고 언제 쓰면 안 되는지 가이드라인을 알려줘. 과용하면 무슨 문제가 생기는지도."

!!! danger "에러 2: `Hydration failed because the initial UI does not match`"
    **에러 메시지**: 하이드레이션 불일치.
    **원인**: Server에서 렌더된 HTML과 Client에서 렌더된 결과가 다름 (대표적으로 `new Date()`, `Math.random()`, `localStorage` 사용).
    **해결**: 시간/랜덤값 관련 로직을 `useEffect` 안으로 이동하거나, 해당 컴포넌트를 `dynamic import`로 SSR 끄기.

!!! danger "에러 3: `Module not found: Can't resolve 'fs'`"
    **에러 메시지**: Node.js 내장 모듈을 Client Component에서 사용.
    **원인**: `fs`, `path` 같은 Node API는 Server Component에서만 사용 가능.
    **해결**: 파일 시스템 접근 코드를 Server Component 또는 API Route로 이동.

!!! danger "에러 4: 이미지가 안 뜸 (`Invalid src prop`)"
    **에러 메시지**: `next/image`에 외부 URL 넣으면 차단됨.
    **원인**: `next.config.js`에 해당 도메인이 허용 목록에 없음.
    **해결**: `next.config.js`의 `images.remotePatterns`에 도메인 추가.

!!! danger "에러 5: 환경 변수가 undefined"
    **에러 메시지**: `process.env.API_KEY`가 클라이언트에서 undefined.
    **원인**: 서버 전용 환경 변수는 클라이언트에 노출 안 됨. 클라이언트에서 쓰려면 `NEXT_PUBLIC_` 접두사 필수.
    **해결**: `.env.local`에 `NEXT_PUBLIC_API_URL=...` 형식으로 선언.

### 📚 학습 체크리스트
- [ ] `create-next-app`으로 App Router 프로젝트를 생성했다
- [ ] 새 경로를 파일 생성만으로 추가해봤다
- [ ] Server Component와 Client Component의 차이를 설명할 수 있다
- [ ] `'use client'` 지시자를 언제 쓸지 판단할 수 있다
- [ ] `examples/blog-starter`를 클론해서 실행해봤다
- [ ] 위 에러 Top 5 중 최소 2개는 실제로 경험했다

---

## 2-3-2. vercel/commerce (11K+ Stars) — 커머스 스타터

**한 줄 소개**: Next.js App Router + Shopify 기반 프로덕션급 커머스 템플릿.
**왜 봐야 하는가**: "App Router의 진지한 실전 사례"를 보여주는 거의 유일한 공식 레포.
**난이도**: ⭐⭐⭐⭐ (App Router 기초가 있어야 함)

### 📋 이 레포에서 배울 수 있는 것
- App Router의 **라우트 그룹** `(group)/` 사용법
- **병렬 라우트** `@slot/` 패턴
- **인터셉트 라우트** `(.)` 패턴
- Server Actions로 장바구니 조작
- `revalidateTag` 기반 캐싱 무효화
- Server-only 함수로 API 키 보호
- Partial Prerendering 최적화

### 🚀 15분 퀵스타트

**1단계: Shallow Clone**
```bash
git clone --depth 1 https://github.com/vercel/commerce.git
cd commerce
```

**2단계: 코드 읽기 모드로 시작 (실행은 나중에)**
!!! tip "💡 꿀팁: 실행보다 코드 읽기 먼저"
    이 레포는 **실제 Shopify 계정**이 있어야 정상 동작합니다. 초보자라면 실행에 30분씩 고생하지 말고, **코드 구조부터 읽으세요**.

**3단계: app/ 디렉토리 구조 파악**
```bash
cd app
ls
```
!!! info "예상 출력"
    ```
    api/
    [page]/
    layout.tsx
    page.tsx
    product/
    search/
    ```

**4단계: 상품 상세 페이지 흐름 따라가기**
```bash
cd product/[handle]
ls
```
- `page.tsx` — 상품 상세 Server Component (핵심!)
- `opengraph-image.tsx` — OG 이미지 자동 생성

**5단계 (선택): 실제 실행**
```bash
cd ../../..
cp .env.example .env.local
# .env.local에 Shopify API 키 입력
npm install
npm run dev
```
!!! warning "⚠️ Shopify 계정 없으면 Step 5는 생략하세요"

### 주목할 파일 (반드시 한 번씩 열어보기)

| 파일 | 학습 포인트 |
| --- | --- |
| `app/layout.tsx` | 전역 레이아웃, 폰트, 메타데이터 |
| `app/page.tsx` | 홈 페이지 (Server Component) |
| `app/product/[handle]/page.tsx` | 동적 라우트 + Server 페칭 |
| `app/search/[collection]/page.tsx` | 카테고리 페이지 |
| `components/cart/` | Server Action 기반 장바구니 |
| `lib/shopify/index.ts` | Server-only 외부 API 호출 |

### 🤖 Claude Code로 200% 활용하기

!!! example "프롬프트 예시 1: Server 페칭 패턴"
    > "vercel/commerce의 app/product/[handle]/page.tsx가 어떻게 Shopify 데이터를 Server Component에서 페칭하는지 설명해줘. lib/shopify/index.ts의 getProduct 함수와 어떻게 연결되는지도 포함해서."

!!! example "프롬프트 예시 2: 캐싱 전략"
    > "이 레포의 revalidateTag 사용 패턴을 모두 찾아서 '어떤 데이터를 언제 재검증하는지' 표로 정리해줘. 그리고 내 블로그 프로젝트에 어떻게 적용할지 제안해줘."

!!! example "프롬프트 예시 3: 장바구니 Server Action"
    > "components/cart 디렉토리를 보고, Server Action으로 장바구니에 상품을 추가하는 전체 흐름을 설명해줘. 클라이언트 폼 → Server Action → 캐시 무효화 순서로."

!!! example "프롬프트 예시 4: 내 프로젝트에 이식"
    > "vercel/commerce의 Server-only 함수 패턴(lib/shopify/)을 내 Next.js 프로젝트에 적용해서 외부 API 키를 클라이언트에 노출하지 않는 방법을 알려줘."

### 🚨 자주 발생하는 에러 Top 3

!!! danger "에러 1: Shopify API 키 없이 실행 시 빌드 실패"
    **에러 메시지**: `Missing required Shopify environment variables`
    **원인**: `.env.local`에 Shopify 키 없음.
    **해결**: Shopify 개발자 계정을 만들어 Storefront API 토큰을 발급받거나, 실행은 포기하고 **코드 읽기 모드**로 전환.

!!! danger "에러 2: TypeScript 빌드 에러"
    **원인**: 이 레포는 최신 TypeScript 기능을 사용. 로컬 TS 버전이 낮으면 에러.
    **해결**: `npm install typescript@latest --save-dev`.

!!! danger "에러 3: `revalidateTag is not a function`"
    **원인**: Next.js 13.4 미만에서는 해당 API 없음.
    **해결**: `package.json`의 Next 버전 14+ 확인.

### 📚 학습 체크리스트
- [ ] `app/` 디렉토리 구조를 완전히 파악했다
- [ ] `app/product/[handle]/page.tsx`를 정독했다
- [ ] Server Component에서 외부 API를 호출하는 패턴을 이해했다
- [ ] `revalidateTag`가 왜 필요한지 설명할 수 있다
- [ ] (선택) Shopify 계정을 만들어 실제 실행해봤다

---

## 이 섹션 마무리

Next.js는 React 경험이 있다면 **1~2주 안에 기본은 익힐 수 있습니다.** 다만 App Router의 Server/Client Component 구분, 캐싱 전략, Server Actions 등 새로운 개념이 많으니 급하게 서두르지 마세요. 공식 문서 `nextjs.org/docs`를 옆에 띄워 두고 `examples/` 예제를 하나씩 클론해 보는 것이 가장 빠른 길입니다.

마지막으로, 이 파트의 전체 학습을 점검하는 체크리스트 페이지로 넘어가세요. [04-checklist.md](04-checklist.md)

!!! info "📌 한 줄 정리"
    Next.js 학습의 왕도는 **"create-next-app으로 App Router 시작 → Server/Client 구분 익히기 → examples 중 관심 예제 1개 실행 → vercel/commerce로 실전 패턴 학습"** 순서입니다.
