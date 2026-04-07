# 📘 LangChain 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langchain.svg?style=social)](https://github.com/langchain-ai/langchain)

!!! info "레포지토리"
    **langchain-ai/langchain** · 95k+ ⭐ · MIT License · [python.langchain.com](https://python.langchain.com)

---

## 🧐 1. LangChain은 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: LangChain은 **LLM을 외부 데이터·도구·메모리와 연결해 "단순 챗봇"을 넘어서는 애플리케이션을 만들기 위한 프레임워크**입니다. 핵심 개념은 "체인(chain)"과 "에이전트(agent)"입니다.

### 핵심 특성

- **모델 추상화**: OpenAI, Anthropic Claude, Google Gemini, 로컬 Ollama 등을 동일한 인터페이스(`ChatModel`)로 사용 → 모델을 갈아끼우기 쉬움.
- **LCEL (LangChain Expression Language)**: `prompt | model | parser`처럼 파이프 연산자로 체인을 선언적으로 구성.
- **Retrieval-Augmented Generation (RAG)**: 벡터 DB(Pinecone, Chroma, FAISS) + 임베딩 모델을 결합해 "내 회사 문서에 기반해 답변하는 챗봇"을 만드는 표준 패턴.
- **도구 호출 (Tool Calling)**: LLM이 함수를 호출하도록 만들어 "검색 → 계산 → DB 조회" 같은 다단계 작업을 자동화.
- **메모리**: 대화 이력을 요약·저장해 긴 대화에서도 맥락 유지.

### 실무 도입 포인트

| 도입 이유 | 구체적 효과 |
|---|---|
| **RAG 표준화** | "사내 문서 챗봇"의 시작 코드를 100줄로 줄여줌 |
| **모델 락인 회피** | 한 번 작성한 체인을 OpenAI → Claude로 1줄 수정으로 갈아끼움 |
| **에이전트 패턴** | 검색·계산기·DB 같은 도구를 LLM이 자율적으로 선택해 호출 |
| **LangSmith 통합** | 디버깅·트레이싱·평가를 한 곳에서 → 프롬프트 회귀 테스트 가능 |

### 기존 방식 vs LangChain

```
[직접 OpenAI API 호출]
대화 이력 관리, 토큰 카운팅, 벡터 검색, 함수 호출 파싱을 모두 직접 구현 → 1000줄+

[LangChain]
RetrievalQA.from_chain_type(llm, retriever, ...) 한 줄로 RAG 챗봇 완성
```

## 🚀 2. 10분 퀵스타트

### 환경 준비

```bash
python -V       # 3.10+ 권장
pip install langchain langchain-openai langchain-community
```

### 환경변수 설정

```bash
export OPENAI_API_KEY="sk-..."
# Windows PowerShell: $env:OPENAI_API_KEY="sk-..."
```

### LCEL로 만든 첫 체인

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1) 모델
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# 2) 프롬프트 템플릿
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 한국어 기술 멘토입니다."),
    ("human", "{topic}을(를) 비전공 대학생도 이해할 수 있게 3문단으로 설명해 주세요."),
])

# 3) 파이프로 체인 구성
chain = prompt | llm | StrOutputParser()

# 4) 실행
print(chain.invoke({"topic": "벡터 임베딩"}))
```

### 검증 (예상 출력)

```
벡터 임베딩이란, 단어나 문장을 컴퓨터가 이해할 수 있는 숫자의 배열로 바꾼 것입니다 ...
... (3문단의 한국어 설명) ...
```

### RAG 미니 예제 (in-memory)

```python
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

docs = [
    "PLAF는 GitHub 인기 레포 가이드북 프로젝트입니다.",
    "Part 4는 문서 처리 라이브러리를 다룹니다.",
    "빌드는 python scripts/build_guidebook.py 명령으로 실행합니다.",
]
vs = FAISS.from_texts(docs, embedding=OpenAIEmbeddings())
retriever = vs.as_retriever()
print(retriever.invoke("어떻게 빌드하나요?"))
```

## 🛠️ 3. 코드 해부학: 핵심 모듈

| 모듈 | 역할 | 학습 포인트 |
|---|---|---|
| `langchain_core/prompts/` | 프롬프트 템플릿, 메시지 포맷 | 변수 치환, few-shot 패턴 |
| `langchain_core/runnables/` | LCEL 핵심 (`Runnable`, `|` 연산자) | 모든 체인이 `Runnable` 인터페이스 구현 |
| `langchain_core/output_parsers/` | LLM 응답 파싱 (`StrOutputParser`, `PydanticOutputParser`) | 구조화된 출력의 시작점 |
| `langchain/chains/` | RetrievalQA, ConversationalRetrievalChain 등 | RAG의 표준 구현체 |
| `langchain_community/vectorstores/` | FAISS, Chroma, Pinecone 어댑터 | 벡터 DB 추상화 계층 |
| `langchain/agents/` | Tool-calling 에이전트, ReAct 에이전트 | 도구 사용 자동화 |

!!! tip "초보자 추천"
    먼저 **LCEL 기반 단순 체인**(prompt | model | parser)을 5개 만들어 보세요. 그 다음 **벡터 검색을 추가한 RAG**, 마지막으로 **에이전트(Tool Calling)** 순서로 학습하면 막힘이 적습니다.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude (RAG 파이프라인 설계)
```
/think 사내 PDF 문서 500개로 RAG 챗봇을 만들려고 한다.
다음을 LangChain 코드로 설계해 줘:
1) 청킹 전략 (chunk_size, overlap)
2) 임베딩 모델 선택 기준
3) 벡터 DB 비교 (Chroma vs Pinecone vs Postgres+pgvector)
4) Re-ranking 단계 추가 여부
각 결정의 이유를 함께 설명해 줘.
```

### 🔵 Gemini (LangChain vs 경쟁 프레임워크)
```
LangChain, LlamaIndex, Haystack의 차이점을 비교 표로 정리해 줘.
RAG, 에이전트, 평가 도구 측면에서 강점과 약점을 명확히 구분하고,
"내 회사 문서로 챗봇 만들기" 시나리오에서 어느 것을 추천하는지 결론을 내려 줘.
```

### 🟢 ChatGPT (프로젝트 기획)
```
대학생이 4주 만에 만들 수 있는 LangChain 기반 미니 프로젝트 5개를 추천해 줘.
각 프로젝트는: 목표, 사용 모델, 사용 라이브러리, 주차별 마일스톤,
포트폴리오에 어필할 포인트를 포함해야 한다.
```

### ⬛ GitHub Copilot / Codex (IDE 실시간 보조)
```python
# TODO: PDF 폴더를 받아 RAG 체인을 만드는 함수
#   - 입력: pdf_dir (str), llm_model (str)
#   - 처리: PyPDFLoader → RecursiveCharacterTextSplitter → FAISS
#   - 반환: RetrievalQA chain
```

## 🔗 5. 관련 레포 · 다음 단계

- **공식 문서**: [python.langchain.com](https://python.langchain.com)
- **LangSmith** (트레이싱·평가): [smith.langchain.com](https://smith.langchain.com)
- **LangGraph** (상태 기반 에이전트): [github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
- **경쟁/보완**: [LlamaIndex](https://github.com/run-llama/llama_index), [Haystack](https://github.com/deepset-ai/haystack)
- **Anthropic SDK 직접 사용**: 단순한 케이스에는 LangChain 없이 [Claude API](../../../part5-ai-tools/01-mcp-core.md)를 직접 호출하는 것이 더 깔끔할 수도 있습니다.
