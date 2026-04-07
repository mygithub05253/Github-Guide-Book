# 📘 System Design Primer 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/donnemartin/system-design-primer.svg?style=social)](https://github.com/donnemartin/system-design-primer)

!!! info "레포지토리"
    **donnemartin/system-design-primer** · 280k+ ⭐ · CC BY 4.0 · 한국어 번역 존재

---

## 🧐 1. System Design Primer는 무엇이고, 누구에게 필요한가요?

**한 줄 요약**: System Design Primer는 **"대규모 시스템을 어떻게 설계하는가"를 처음부터 배우고 싶은 개발자를 위한 학습 자료 + 면접 대비 가이드**입니다. 캐시, 로드밸런서, 데이터베이스 샤딩, CAP, 일관성, 확장성 등 시스템 디자인 인터뷰 단골 주제를 모두 다룹니다.

### 핵심 특성
- **이론 + 사례**: 각 개념마다 실제 예제(예: 단축 URL, Twitter, 검색 엔진).
- **시각 자료 풍부**: 다이어그램으로 트레이드오프 설명.
- **면접 답변 가이드**: 단계별 접근법(요구사항 → 추정 → 설계 → 심화).
- **무료**: 모든 콘텐츠가 README에 통합.
- **다국어**: 한국어 번역 README 존재.

### 다루는 주제
| 카테고리 | 예시 |
|---|---|
| 기초 | 성능 vs 확장성, 지연 시간 수치 |
| 아키텍처 | DNS, CDN, 로드 밸런서, 리버스 프록시 |
| 데이터베이스 | RDBMS vs NoSQL, 복제·샤딩, 일관성 모델 |
| 캐시 | 클라이언트·CDN·웹·DB 캐시, 캐시 패턴 |
| 비동기 | 메시지 큐, 백프레셔 |
| 통신 | REST vs RPC vs GraphQL |
| 보안 | 인증, 암호화 |

### 누구에게 필요한가
| 대상 | 활용법 |
|---|---|
| **시니어 면접 준비** | 시스템 디자인 인터뷰 90분 대비 |
| **주니어 → 미들 성장** | "큰 그림"을 익혀 코드 너머를 봄 |
| **아키텍처 결정 참여** | 트레이드오프 설명 능력 |

## 🚀 2. 10분 퀵스타트

```bash
git clone https://github.com/donnemartin/system-design-primer.git
cd system-design-primer
```

또는 GitHub에서 README.md를 바로 읽기 시작.

### 추천 학습 순서
1. **지연 시간 수치** (Latency Numbers) — 모든 결정의 기준
2. **확장성 강의 (Harvard)** — 단일 서버에서 분산까지
3. **CAP 정리** — 분산 시스템의 핵심
4. **샘플 문제: 단축 URL** — end-to-end 설계 연습
5. **샘플 문제: Twitter** — 피드 생성 전략

## 🛠️ 3. 코드 해부학

레포 자체는 마크다운 + 다이어그램 모음입니다.

| 디렉터리 | 내용 |
|---|---|
| `README.md` | 전체 가이드 (메인) |
| `solutions/` | 시스템 디자인 문제 풀이 |
| `solutions/object_oriented_design/` | OOD 면접 문제 |
| `README-ko.md` | 한국어 번역 |

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 시스템 디자인 면접 모의 진행:
"DAU 100만의 단축 URL 서비스를 설계하라" 90분 답변을 생각해 보고
1) 요구사항 명확화 질문
2) 용량·트래픽 추정
3) API 설계
4) 데이터 모델
5) 핵심 컴포넌트 다이어그램
6) 병목·확장 전략
7) 트레이드오프
순서로 답변 초안을 작성해 줘.
```

### 🔵 Gemini
```
System Design Primer가 다루는 "캐시 패턴 5가지"(Cache-aside, Write-through,
Write-back, Refresh-ahead, Read-through)를 비교 표로 정리하고
각 패턴이 적합한 시나리오를 예시와 함께 설명해 줘.
```

### 🟢 ChatGPT
```
나는 백엔드 신입이다. 시스템 디자인 인터뷰 1개월 준비 계획을 짜 줘.
주차별: 학습 주제, 풀 문제, 모의 인터뷰 일정.
System Design Primer 챕터와 매핑해 줘.
```

### ⬛ Copilot
```
// 코드 자동화 외 - 다이어그램 마크업(Mermaid)으로 아키텍처 그릴 때 보조
```

## 🔗 5. 관련 레포 · 다음 단계
- [OSSU 딥다이브](../ossu/index.md), [Coding Interview University 딥다이브](../interview-university/index.md)
- 추천 도서: 알렉스 쉬, 가상 면접 사례로 배우는 대규모 시스템 설계 기초
- 사례 연구: [High Scalability 블로그](http://highscalability.com)
- [Kubernetes 딥다이브](../../devops-cloud/kubernetes/index.md), [Kafka 딥다이브](../../db-data/kafka/index.md)
