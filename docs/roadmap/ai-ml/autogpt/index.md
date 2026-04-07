# 📘 AutoGPT 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT.svg?style=social)](https://github.com/Significant-Gravitas/AutoGPT)

!!! info "레포지토리"
    **Significant-Gravitas/AutoGPT** · 170k+ ⭐ · MIT License · [agpt.co](https://agpt.co)

---

## 🧐 1. AutoGPT는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: AutoGPT는 **"목표를 주면 LLM이 스스로 작업을 분해·실행하는" 자율 에이전트 플랫폼**입니다. 단순 챗봇을 넘어 "에이전트가 일을 한다"는 패러다임의 시작점이 된 프로젝트입니다.

### 핵심 특성
- **목표 기반 실행**: "이번 주 경쟁사 제품 동향 정리해서 보고서 만들기" 같은 고수준 목표 입력 → 에이전트가 단계 분해.
- **도구 사용**: 웹 검색, 파일 조작, 코드 실행 등 도구를 자율적으로 호출.
- **장기 메모리**: 벡터 DB로 이전 작업 맥락 유지.
- **AutoGPT Platform**: 최근 버전은 노코드 워크플로우 빌더 형태로 진화.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **반복 리서치 자동화** | 매일 아침 시장 동향 요약 |
| **데이터 수집 + 정제** | 웹 스크래핑 → DB 정리까지 한 번에 |
| **에이전트 패턴 학습 교재** | LLM 에이전트 동작 원리를 코드로 이해 |

!!! warning "주의"
    자율 에이전트는 **비용·시간·실패 가능성**이 큽니다. production보다는 학습·실험·내부 자동화에 적합합니다.

## 🚀 2. 10분 퀵스타트

```bash
git clone https://github.com/Significant-Gravitas/AutoGPT.git
cd AutoGPT
# 최신 버전은 docker-compose 권장
cp .env.example .env
# .env에 OPENAI_API_KEY 입력
docker compose up
```

브라우저에서 안내된 포트(예: `http://localhost:3000`) 접속 → 노드 기반 워크플로우 빌더 진입.

## 🛠️ 3. 코드 해부학

| 디렉터리 | 역할 |
|---|---|
| `autogpt_platform/backend/` | 에이전트 실행 엔진 |
| `autogpt_platform/frontend/` | 워크플로우 빌더 UI |
| `classic/` | 초기 AutoGPT CLI 버전 |
| `docs/` | 사용자·개발자 문서 |

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think AutoGPT 워크플로우 1개를 설계해 줘:
"매주 월요일 GitHub trending repo 10개를 가져와 카테고리별로 분류하고 Notion에 저장"
필요한 노드, 입력/출력, 에러 처리를 단계별로.
```

### 🔵 Gemini
```
AutoGPT vs LangGraph vs CrewAI vs AutoGen을 비교 표로 정리해 줘.
용도, 추상화 레벨, 학습 곡선 기준.
```

### 🟢 ChatGPT
```
대학생 개인 비서 에이전트를 AutoGPT로 만들려고 한다.
가능한 사용 사례 5가지와 각각의 도구 조합, 위험 요소를 정리해 줘.
```

### ⬛ Copilot
```python
# TODO: AutoGPT 커스텀 블록 - get_arxiv_papers(query, days)
```

## 🔗 5. 관련 레포 · 다음 단계
- [LangChain 딥다이브](../langchain/index.md), [LangGraph](https://github.com/langchain-ai/langgraph)
- 경쟁: [CrewAI](https://github.com/joaomdmoura/crewAI), [AutoGen](https://github.com/microsoft/autogen)
- Claude 기반 에이전트: [Part 5 · MCP 생태계](../../../part5-ai-tools/index.md)
