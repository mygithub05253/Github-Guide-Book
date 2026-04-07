# 📘 OWASP Cheat Sheet Series 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/OWASP/CheatSheetSeries.svg?style=social)](https://github.com/OWASP/CheatSheetSeries)

!!! info "레포지토리"
    **OWASP/CheatSheetSeries** · 30k+ ⭐ · CC BY-SA · [cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org)

---

## 🧐 1. OWASP Cheat Sheet Series는 무엇이고, 누구에게 필요한가요?

**한 줄 요약**: OWASP(Open Web Application Security Project)의 **"개발자가 실무에서 즉시 적용할 수 있는 짧은 보안 가이드 모음"**입니다. 인증, 입력 검증, SQL Injection 방어, XSS 방어 등 80개 이상의 주제를 각 1~3페이지 분량으로 정리한 레퍼런스입니다.

### 핵심 특성
- **주제별 단편**: "Authentication Cheat Sheet", "SQL Injection Prevention" 등 즉시 검색 가능.
- **언어·프레임워크 중립**: 원리 중심 + 예시 코드.
- **실무 즉시 적용**: 코드 리뷰 체크리스트로 사용 가능.
- **OWASP Top 10 보완**: Top 10이 "무엇"이라면 Cheat Sheet는 "어떻게".

### 누구에게 필요한가
| 대상 | 활용법 |
|---|---|
| 신입 백엔드 개발자 | 입력 검증·인증 구현 시 우선 참조 |
| 코드 리뷰어 | PR 체크리스트로 사용 |
| 면접 준비생 | "왜 그렇게 구현해야 하는가" 답변 근거 |
| 보안 담당자 | 사내 가이드라인의 출발점 |

## 🚀 2. 10분 퀵스타트

레포 자체가 마크다운 문서 모음입니다. 설치 없음.

### 1단계: 핵심 시트 5개 즉시 읽기
1. [Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
2. [Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
3. [Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
4. [SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
5. [Cross Site Scripting Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

### 2단계: 본인 프로젝트에 체크리스트 적용
- 회원가입에 OWASP Password Storage가 권장하는 해싱(bcrypt/argon2)을 쓰는가?
- 모든 SQL이 Prepared Statement인가?
- 모든 출력에 escape가 적용되는가?

## 🛠️ 3. 코드 해부학

| 디렉터리 | 내용 |
|---|---|
| `cheatsheets/` | 모든 시트의 마크다운 원본 |
| `Index.md` | 전체 목차 |
| `assets/` | 다이어그램·이미지 |

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 우리 Spring Boot 회원가입/로그인 코드를
OWASP Authentication + Password Storage Cheat Sheet 기준으로 감사해 줘.
- 비밀번호 해싱 알고리즘과 비용
- 계정 잠금 정책
- 토큰 만료·재발급
- 비밀번호 정책
- 에러 메시지가 사용자 존재 여부를 노출하는가
```

### 🔵 Gemini
```
OWASP Top 10 (2021)의 각 항목과 대응되는 Cheat Sheet를 매핑한 표를 만들어 줘.
각 항목에 대해 "무엇이 위험인지 + 어떻게 막는지"를 1줄씩.
```

### 🟢 ChatGPT
```
"학생 포트폴리오용 풀스택 앱"에 적용해야 할 OWASP 권장 사항 체크리스트를
프론트엔드 / 백엔드 / 인프라 카테고리로 나눠서 만들어 줘.
```

### ⬛ Copilot
```java
// TODO: OWASP 권장에 따라 비밀번호 해싱 - argon2id, 메모리 19MB, iterations 2
```

## 🔗 5. 관련 레포 · 다음 단계
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP ZAP](https://github.com/zaproxy/zaproxy) (자동화된 보안 스캐너)
- [Bandit](https://github.com/PyCQA/bandit) (Python 정적 분석)
- [npm audit](https://docs.npmjs.com/cli/v10/commands/npm-audit), [Snyk](https://snyk.io)
