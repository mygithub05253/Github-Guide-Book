# 부록 A: Claude Code Plan 모드 완전 가이드

> Plan 모드는 Claude Code의 **변경사항을 미리 보여주고 승인받는** 안전 장치입니다. 이 부록은 Part 5-7을 더 깊이 파고듭니다.

---

## 왜 Plan 모드가 필요한가

실제 사례부터 봅시다.

!!! danger "🚨 실제로 있었던 사고"
    "src 폴더 정리해줘"라고 말했더니 Claude가 `src/utils/` 전체를 삭제. 3시간 분량 작업 날림. **Plan 모드를 안 써서 생긴 일**입니다.

Plan 모드는 이런 사고를 **Apply 버튼 직전**에 잡아줍니다.

---

## A-1. 일반 모드 vs Plan 모드

```text
┌─ 일반 모드 (Direct Mode)
│  사용자 요청
│     ↓
│  즉시 파일 수정
│     ↓
│  결과 반영
│
│  장점: 빠름
│  단점: 실수 수정 어려움, 롤백 수동
│
└─ Plan 모드 (Preview Mode)
   사용자 요청
      ↓
   변경 계획 작성
      ↓
   사용자 검토 (Apply / Edit / Cancel)
      ↓
   승인 시 실제 수정

   장점: 안전, 검토 가능, 편집 가능
   단점: 30초~1분 추가
```

---

## A-2. 활성화 방법 4가지

### 1) 키보드 단축키 (가장 빠름)
```text
Shift + Tab  (두 번 연속)
```

### 2) 슬래시 명령어
```text
/plan
```

### 3) 프롬프트에 명시
```text
"이 작업을 Plan 모드로 해줘"
"변경사항을 먼저 미리 보여줘"
```

### 4) 메뉴
Claude Code UI 우측 상단 → Plan Mode 토글

---

## A-3. 언제 켜야 하나 (판단 기준)

!!! info "📌 Plan 모드 추천"
    - 수정 파일 2개 이상
    - 기존 파일 삭제 포함
    - 설정 파일 변경 (`package.json`, `database.yml`, `tsconfig.json`)
    - DB 마이그레이션
    - 처음 쓰는 MCP 조합
    - 프로덕션 배포 관련

!!! info "📌 Direct 모드로 충분"
    - 주석 추가
    - 간단한 오타 수정
    - 단일 함수 리팩토링 (충분히 작음)
    - 로그 파일 읽기 (변경 없음)
    - 실험용 스크래치 코드

!!! tip "💡 꿀팁: '의심되면 Plan'"
    애매하면 Plan 모드. 30초 손해와 하루 손해를 비교하면 답은 명확합니다.

---

## A-4. 단계별 워크플로우 (실전)

### Step 1: Plan 활성화 + 요청

```text
[Shift+Tab x2]

사용자: "src/components/ 안의 모든 클래스형 React 컴포넌트를
        함수형 + Hooks로 마이그레이션해줘. 테스트도 업데이트.
        PropTypes는 유지."
```

### Step 2: Plan 미리보기

```diff
PLAN: React 클래스형 → 함수형 마이그레이션
===========================================

파일 목록 (8개):
├─ src/components/UserCard.jsx         [수정]
├─ src/components/ProductList.jsx      [수정]
├─ src/components/Header.jsx           [수정]
├─ src/components/Footer.jsx           [변경 없음 - 이미 함수형]
├─ src/components/SearchBar.jsx        [수정]
├─ src/components/UserCard.test.jsx    [수정]
├─ src/components/ProductList.test.jsx [수정]
├─ src/components/SearchBar.test.jsx   [수정]

변환 패턴:
+ import { useState, useEffect } from 'react';
- class X extends React.Component { ... }
+ function X({ props }) { ... }

예상 결과:
- 코드 라인: 487 → 362 (-26%)
- 파일 크기: -18%
- 의미적 변경: 없음 (기능 동일)

[Apply] [Edit Plan (Ctrl+G)] [Cancel]
```

### Step 3: 검토

**체크 항목 (최소 30초):**
- [ ] 파일 목록이 내 의도와 일치?
- [ ] 변경 없음 표시된 파일이 맞나? (이미 함수형)
- [ ] 테스트 파일이 포함되어 있나?
- [ ] 의미적 변경(기능 변화)이 없다고 명시되어 있나?

### Step 4: Apply 또는 Edit

- **Apply** → 즉시 수정
- **Ctrl+G Edit** → "4번 파일은 건너뛰어줘" 같이 세부 조정
- **Cancel** → 계획 폐기

---

## A-5. Plan 편집 (Ctrl+G) 실전

```text
원래 Plan:
1. UserCard.jsx 리팩토링
2. UserCard.test.jsx 업데이트
3. ProductList.jsx 리팩토링
4. ProductList.test.jsx 업데이트
5. Header.jsx 리팩토링

편집 명령:
"3번과 4번은 건너뛰어. ProductList는 다음 주에 할게.
 5번 Header는 JSDoc 주석도 함께 추가해줘."

수정된 Plan:
1. UserCard.jsx 리팩토링
2. UserCard.test.jsx 업데이트
5. Header.jsx 리팩토링 + JSDoc 추가
```

---

## A-6. 검토 체크리스트 (템플릿)

```text
Plan 검토 체크리스트
=====================
[ ] 파일 목록: 모두 예상한 파일인가?
[ ] 파일 수: 예상과 비슷한가? (너무 많으면 의심)
[ ] 삭제: 삭제되는 파일/코드가 맞는가?
[ ] 신규: 신규 파일 이름과 위치가 적절한가?
[ ] 테스트: 테스트 파일도 함께 업데이트되는가?
[ ] 설정: package.json, tsconfig 등 설정 변경 있나?
[ ] DB: 마이그레이션 스크립트 포함?
[ ] 환경: .env 변경 있나?
[ ] 의존성: 새 패키지 추가 있나?
[ ] 범위: 요청 범위를 벗어난 "친절한" 추가 변경이 있나?
```

!!! danger "🚨 특히 주의: '친절한 추가 변경'"
    Claude는 종종 요청하지 않은 것까지 "좋을 것 같아서" 수정합니다. 예: "ESLint도 고쳤어요", "타입도 엄격하게 바꿨어요". 범위를 벗어나면 **반드시 Edit으로 제외**하세요.

---

## A-7. Plan 모드 실수 패턴

### 실수 1: Apply 연타
- **증상:** Plan 내용 안 읽고 바로 Apply
- **해결:** "Apply 전 30초 검토" 룰 정하기

### 실수 2: Cancel 후 재시작 안 함
- **증상:** Cancel 후 그대로 Direct 모드로 같은 작업
- **해결:** Cancel = Plan 모드 유지 상태, 다시 요청하면 새 Plan 생성

### 실수 3: 너무 큰 Plan
- **증상:** 30개 파일 Plan이 너무 커서 검토 포기
- **해결:** 작업을 쪼개서 여러 Plan으로 분할

---

## A-8. 고급 팁

### 팁 1: Plan 결과 저장

```text
"현재 Plan을 plan-2026-04-07.md 로 저장해줘.
 승인 전에 팀원에게 보여주고 싶어."
```

### 팁 2: 조건부 Apply

```text
"Plan 중 1-3번만 실행해줘. 4-5번은 다음 세션에서."
```

### 팁 3: Plan 재사용

```text
"이전 세션의 plan-2026-04-07.md 를 읽고,
 비슷한 작업을 src/pages/ 에도 적용하는 새 Plan을 생성해줘."
```

---

## 체크리스트

- [ ] Shift+Tab 두 번을 키보드로 익혔다
- [ ] 파일 2개 이상 수정은 무조건 Plan 모드를 쓴다
- [ ] 검토 체크리스트를 본인 상황에 맞게 커스터마이즈했다
- [ ] Ctrl+G 편집을 최소 1번 사용해봤다
- [ ] '친절한 추가 변경' 함정을 인지하고 있다
