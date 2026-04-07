# 3-3. 해커톤 & 공모전

> 해커톤의 진짜 적은 "아이디어 부족"이 아니라 **"셋업에 3시간 날려먹는 것"**입니다. 이 섹션의 레포들은 로그인/DB/배포 같은 **기본기에서 시간을 0으로** 만들어줘요. 당신은 핵심 아이디어에만 집중하면 됩니다.

---

## 3-3-1. Hackathon Starter (sahat/hackathon-starter) — 35K+ Stars

**한 줄 소개**: Node.js + Express + MongoDB + Passport.js가 **즉시 동작하는** 해커톤 전용 보일러플레이트.

**왜 봐야 하는가**: 소셜 로그인(Google/GitHub/Facebook)까지 **설정 몇 줄로** 동작하는 템플릿은 드물어요. 24시간 해커톤에서 1시간 만에 기본 앱을 올리고 나머지 23시간을 핵심 기능에 투자할 수 있습니다.

**난이도**: ⭐⭐⭐ (Node.js + Express 기초가 필요)

### 📋 이 레포에서 배울 수 있는 것

- Express.js 프로젝트의 표준 구조
- Passport.js로 Local / Google / GitHub OAuth 인증 구성
- Mongoose 스키마 설계와 bcrypt 비밀번호 해싱
- `.env` 기반 환경변수 관리
- 세션 관리와 `ensureAuthenticated` 미들웨어 패턴

### 🚀 15분 퀵스타트

#### Step 1: 클론 및 설치

```bash
git clone https://github.com/sahat/hackathon-starter.git
cd hackathon-starter
npm install
```

#### Step 2: 환경 변수 설정

```bash
cp .env.example .env
```

`.env` 파일 최소 설정:

```
MONGODB_URI=mongodb://localhost:27017/hackathon
SESSION_SECRET=change-this-random-string
```

#### Step 3: MongoDB 실행

```bash
# macOS
brew services start mongodb-community

# Windows (MongoDB 설치 후)
net start MongoDB

# 또는 Docker로
docker run -d -p 27017:27017 --name mongo mongo
```

!!! warning "⚠️ 초보자 함정"
    MongoDB 설치가 귀찮다면 **MongoDB Atlas 무료 클러스터**(https://www.mongodb.com/atlas)를 쓰세요. 회원가입 → 무료 클러스터 생성 → Connection String 복사 → `.env`의 `MONGODB_URI`에 붙여넣기. 5분이면 끝납니다.

#### Step 4: 개발 서버 실행

```bash
npm run dev
```

!!! info "예상 출력"
    ```
    App is running at http://localhost:8080 in development mode
    MongoDB connection established successfully
    Press CTRL-C to stop
    ```

#### Step 5: 브라우저 확인

http://localhost:8080 접속 → 회원가입 / 로그인 페이지가 바로 보입니다.

### 🏗 핵심 코드 구조

**Passport.js Local Strategy (config/passport.js)**

```javascript
passport.use(new LocalStrategy({ usernameField: 'email' }, (email, password, done) => {
  User.findOne({ email: email.toLowerCase() }, (err, user) => {
    if (err) return done(err);
    if (!user) return done(null, false, { msg: '가입되지 않은 이메일입니다.' });
    user.comparePassword(password, (err, isMatch) => {
      if (isMatch) return done(null, user);
      return done(null, false, { msg: '비밀번호가 일치하지 않습니다.' });
    });
  });
}));
```

**User 모델 (models/User.js) — bcrypt 훅**

```javascript
userSchema.pre('save', function save(next) {
  const user = this;
  if (!user.isModified('password')) return next();
  bcrypt.genSalt(10, (err, salt) => {
    if (err) return next(err);
    bcrypt.hash(user.password, salt, (err, hash) => {
      if (err) return next(err);
      user.password = hash;
      next();
    });
  });
});

userSchema.methods.comparePassword = function comparePassword(candidate, cb) {
  bcrypt.compare(candidate, this.password, (err, isMatch) => cb(err, isMatch));
};
```

!!! tip "💡 꿀팁: 이 두 코드만 이해하면 인증은 끝"
    거의 모든 Node.js 인증 로직은 이 패턴의 변형이에요. **pre('save') 훅에서 해싱 + comparePassword 메서드로 검증**. 외워두면 평생 써먹습니다.

**소셜 로그인 추가 (config/passport.js)**

```javascript
passport.use(new GoogleStrategy({
  clientID: process.env.GOOGLE_ID,
  clientSecret: process.env.GOOGLE_SECRET,
  callbackURL: '/auth/google/callback',
}, (accessToken, refreshToken, profile, done) => {
  User.findOne({ google: profile.id }, (err, existingUser) => {
    if (existingUser) return done(null, existingUser);
    const user = new User({
      email: profile.emails[0].value,
      google: profile.id,
      profile: { name: profile.displayName, picture: profile.photos[0].value },
    });
    user.save((err) => done(err, user));
  });
}));
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 불필요 기능 제거"
    ```
    hackathon-starter에는 트위터/페이스북/인스타그램 API 예제가 들어있어.
    나는 Google OAuth만 쓸 거야. 나머지 전략과 라우트를 전부 제거한 mini 버전으로
    만들어줘. package.json 의존성도 같이 정리해줘.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 내 해커톤 아이디어 반영"
    ```
    이 템플릿 위에 "스터디 모임 매칭 앱"을 만들 거야. 필요한 Mongoose 모델
    (Study, Participant, Message), 라우트, 기본 EJS 뷰를 템플릿의 스타일에
    맞춰 추가해줘. 인증은 기존 Passport를 재사용해.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 배포 스크립트"
    ```
    이 앱을 Render.com에 배포하려고 해. 필요한 Dockerfile, render.yaml,
    MongoDB Atlas 연결 체크리스트를 만들어줘. 환경변수도 전부 나열해줘.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `MongooseServerSelectionError`"
    **원인**: MongoDB 서버가 안 켜져 있거나 URI 잘못됨
    **해결**: `mongosh`로 직접 연결 테스트, Atlas라면 IP Whitelist에 `0.0.0.0/0` 추가

!!! danger "🚨 에러 2: `req.user is undefined`"
    **원인**: 세션 미들웨어 순서 문제
    **해결**: `app.js`에서 `app.use(session(...))` → `app.use(passport.initialize())` → `app.use(passport.session())` 순서 확인

!!! danger "🚨 에러 3: Google OAuth `redirect_uri_mismatch`"
    **원인**: Google Cloud Console에 등록한 리다이렉트 URL과 실제 URL 불일치
    **해결**: `http://localhost:8080/auth/google/callback`을 **정확히 그대로** 등록

### 📚 학습 체크리스트

- [ ] 템플릿 로컬 실행 성공
- [ ] 회원가입 → 로그인 → 마이페이지 플로우 확인
- [ ] Google OAuth 연동 테스트
- [ ] User 모델에 필드 1개 추가 (예: `nickname`)
- [ ] 새로운 라우트 `/dashboard` 추가
- [ ] Render/Railway/Fly.io 중 하나에 배포 성공

---

## 3-3-2. AutoGPT (Significant-Gravitas/AutoGPT) — 173K+ Stars

**한 줄 소개**: "목표만 주면 AI가 스스로 계획을 세우고 실행하는" **자율 에이전트**의 원조 레포.

**왜 봐야 하는가**: AI 해커톤에서 "우리는 AutoGPT 기반으로..."라고만 말해도 심사위원의 이목을 끕니다. 핵심 개념(자율성, Task Planning, Memory)은 **LLM 개발자의 필수 상식**이 되었어요.

**난이도**: ⭐⭐⭐⭐ (Python 중급 + OpenAI API 경험 필요)

### 📋 이 레포에서 배울 수 있는 것

- **Agent 패턴**: LLM + Tools + Memory의 조합
- Task Planning: 자연어 목표를 단계별 작업으로 분해
- Long-term vs Short-term Memory 설계
- Tool Integration: Web Search, File I/O, Code Execution
- Prompt Engineering 실전 패턴

### 🚀 15분 퀵스타트

!!! warning "⚠️ 비용 주의"
    AutoGPT는 OpenAI API를 호출합니다. 목표 하나 실행에 **$0.5 ~ $10** 정도 쓸 수 있어요. 반드시 OpenAI 대시보드에서 **Spending limit**을 $5 정도로 걸어두고 시작하세요.

#### Step 1: 클론 및 가상환경

```bash
git clone https://github.com/Significant-Gravitas/AutoGPT.git
cd AutoGPT
python -m venv venv
source venv/bin/activate      # macOS/Linux
# venv\Scripts\activate        # Windows
```

#### Step 2: 의존성 설치

```bash
pip install -r requirements.txt
```

#### Step 3: API 키 설정

```bash
cp .env.template .env
# .env 편집:
# OPENAI_API_KEY=sk-proj-...
```

#### Step 4: 실행

```bash
python -m autogpt
```

!!! info "예상 출력"
    ```
    Welcome to AutoGPT!
    Enter a name for your AI: ResearchBot
    Enter the role of your AI: Research assistant for market trends
    Enter goals (5 max):
    1. Find top 5 AI startups in 2026
    2. Summarize each one in 3 bullet points
    ...
    ```

#### Step 5: 결과 확인

에이전트가 자동으로 검색 → 요약 → `auto_gpt_workspace/` 폴더에 결과 파일을 생성합니다.

### 🏗 핵심 아키텍처 이해하기

**Agent 패턴 (개념)**

```
[목표]
   ↓
[LLM이 계획 수립] → "1. 검색 2. 읽기 3. 요약 4. 저장"
   ↓
[단계별 실행]
   ├─ Tool 선택 (Search / FileWrite / Code Executor)
   ├─ 실행 결과 → Memory 저장
   └─ 다음 단계 결정
   ↓
[목표 달성 여부 판단] → 아니면 재계획
```

**LangChain 스타일로 축약한 최소 구현**

```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

tools = [
    Tool(name="Search", func=search.run, description="웹 검색"),
    Tool(name="Calculator", func=lambda x: eval(x), description="수학 계산"),
]

agent = initialize_agent(
    tools,
    OpenAI(temperature=0),
    agent="zero-shot-react-description",
    verbose=True,
)

agent.run("2026년 한국 주요 AI 스타트업 상위 5개의 투자 유치 금액을 더해서 평균을 구해.")
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 최소 AutoGPT 클론"
    ```
    AutoGPT의 핵심 개념(Plan → Tool 선택 → Memory 갱신 → 재평가)을 가장 단순한
    형태로 구현한 50줄짜리 Python 스크립트를 만들어줘. OpenAI API와 DuckDuckGo 검색만
    사용하고, 의존성을 최소화해줘.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 특정 도메인 에이전트"
    ```
    AutoGPT 스타일로 "내 GitHub 레포 README를 읽고 개선 제안서를 markdown으로
    작성해주는" 에이전트를 만들어줘. 도구: (1) GitHub API 읽기 (2) 파일 쓰기.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 비용 가드"
    ```
    AutoGPT 실행 중 OpenAI 호출 횟수와 예상 비용을 실시간 로깅하고,
    누적 비용이 $1 넘으면 자동 중단하는 wrapper를 만들어줘.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `RateLimitError`"
    **원인**: OpenAI 무료 티어는 RPM 제한이 매우 낮음
    **해결**: 유료 결제 등록, 또는 `tenacity`로 재시도 + 백오프

!!! danger "🚨 에러 2: `ModuleNotFoundError: No module named 'tiktoken'`"
    **원인**: Python 버전 불일치 (3.11+ 권장)
    **해결**: `python --version` 확인 후 적절한 venv 재생성

!!! danger "🚨 에러 3: 무한 루프 (AI가 같은 작업을 반복)"
    **원인**: 목표가 모호하거나 종료 조건 없음
    **해결**: 목표에 "Stop when X is done and save result to file" 명시

### 📚 학습 체크리스트

- [ ] AutoGPT 로컬 실행 및 목표 1개 완수
- [ ] Spending limit 설정 확인
- [ ] Agent / Tool / Memory 개념을 그림으로 설명 가능
- [ ] LangChain 기반 최소 클론 30줄 작성
- [ ] 비용 로깅 wrapper 적용

---

## 3-3-3. LangChain (langchain-ai/langchain) — 100K+ Stars

**한 줄 소개**: **LLM 애플리케이션 개발의 사실상 표준** 프레임워크. 프롬프트, 체인, 메모리, RAG, 에이전트를 통합 제공.

**왜 봐야 하는가**: AI 해커톤의 90%는 LangChain(또는 LlamaIndex)으로 구현됩니다. 이거 하나만 능숙해져도 **RAG 챗봇, 문서 분석, 에이전트**를 하루 만에 만들 수 있어요.

**난이도**: ⭐⭐⭐ (Python 기초 + OpenAI API 이해)

### 📋 이 레포에서 배울 수 있는 것

- PromptTemplate, LLMChain으로 프롬프트 재사용
- RAG(Retrieval-Augmented Generation) 파이프라인 구축
- 벡터 DB(FAISS, Chroma, Pinecone) 연동
- ConversationMemory로 챗봇 문맥 유지
- Tool을 붙인 Agent 구성

### 🚀 15분 퀵스타트

#### Step 1: 설치

```bash
pip install langchain langchain-openai langchain-community python-dotenv faiss-cpu
```

#### Step 2: API 키 설정

```bash
# .env
OPENAI_API_KEY=sk-proj-...
```

#### Step 3: Hello World Chain

```python
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0)
prompt = PromptTemplate(
    input_variables=["topic"],
    template="다음 주제에 대해 3줄로 설명해줘: {topic}",
)
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("머신러닝"))
```

!!! info "예상 출력"
    ```
    머신러닝은 데이터에서 패턴을 학습하는 인공지능의 한 분야입니다.
    명시적 프로그래밍 없이 경험을 통해 성능을 향상시킵니다.
    지도/비지도/강화 학습 세 가지 주요 패러다임으로 나뉩니다.
    ```

#### Step 4: RAG 챗봇 최소 예제 (PDF에 질문하기)

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# 1. 문서 로드 및 분할
loader = PyPDFLoader("my_document.pdf")
docs = loader.load()
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

# 2. 임베딩 + 벡터 DB
db = FAISS.from_documents(chunks, OpenAIEmbeddings())

# 3. QA 체인
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=db.as_retriever(),
)

# 4. 질문
print(qa.run("이 문서의 핵심 주장 3가지는?"))
```

!!! tip "💡 꿀팁: 해커톤 필승 공식"
    **"특정 도메인 PDF" + "RAG 챗봇"** 조합은 해커톤에서 항상 먹힙니다. 법률/의료/학교 공지사항/회사 내부 문서 등 "검색이 짜증나는 PDF 더미"를 가진 사람이 고객입니다.

#### Step 5: 대화형 메모리 추가

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
chat = ConversationChain(llm=OpenAI(), memory=memory, verbose=False)

print(chat.predict(input="안녕, 나는 데이터 사이언스를 공부하는 대학생이야."))
print(chat.predict(input="내가 방금 뭐라고 소개했지?"))
```

두 번째 호출에서 "데이터 사이언스를 공부하는 대학생"이라고 답하면 성공!

### 🏗 Agent with Tools 패턴

```python
from langchain.agents import initialize_agent, Tool
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

tools = [
    Tool(name="Search", func=search.run, description="최신 정보 검색"),
    Tool(name="Calculator", func=lambda x: eval(x), description="수학 계산"),
]

agent = initialize_agent(
    tools,
    OpenAI(temperature=0),
    agent="zero-shot-react-description",
    verbose=True,
)

print(agent.run("2026년 한국 최저시급을 찾아서 월 209시간 기준 월급을 계산해줘."))
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 해커톤 MVP 설계"
    ```
    우리 팀은 "대학생 학사공지 RAG 챗봇"을 만들 거야. LangChain으로 구현하는
    최소 동작 가능한 MVP의 파일 구조, 핵심 코드, Streamlit UI까지 전부 한 번에
    만들어줘. 벡터 DB는 FAISS, 임베딩은 OpenAI를 쓸게.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 프롬프트 개선"
    ```
    내 PromptTemplate이 이거야: <붙여넣기>. 출력이 자꾸 산만해.
    Few-shot 예제 3개를 추가하고, 출력 형식을 JSON으로 강제하는
    개선 버전을 만들어줘.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 비용 최적화"
    ```
    내 RAG 체인에서 OpenAI 비용이 너무 많이 나와. (1) 무료 임베딩 모델로 전환
    (2) 캐싱 적용 (3) gpt-3.5-turbo로 다운그레이드 세 가지를 적용한 최적화
    버전을 만들어줘.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `ImportError: cannot import name 'OpenAI' from 'langchain'`"
    **원인**: LangChain 0.1.0+ 이후 import 경로가 바뀜
    **해결**: `from langchain_openai import OpenAI`로 변경

!!! danger "🚨 에러 2: `FAISS` 설치 실패 (Windows)"
    **원인**: `faiss-cpu` 윈도우 호환성 문제
    **해결**: `pip install faiss-cpu==1.7.4` (구버전 지정) 또는 Chroma로 교체

!!! danger "🚨 에러 3: `InvalidRequestError: context_length_exceeded`"
    **원인**: 문서 청크가 너무 큼
    **해결**: `chunk_size=500`으로 줄이고, `chain_type="map_reduce"`로 변경

### 📚 학습 체크리스트

- [ ] Hello World LLMChain 실행 성공
- [ ] 내 PDF로 RAG 챗봇 구축
- [ ] ConversationMemory로 문맥 유지 경험
- [ ] Agent + Tool로 외부 검색 연결
- [ ] Streamlit UI를 붙여 웹 앱으로 배포
- [ ] 해커톤 1개 출전 후 회고 작성

---

## 🎯 Part 3를 마치며

축하합니다. 여기까지 왔다면 당신은:

- 풀스택 앱을 **로컬에서 띄울 수 있고**
- 오픈소스에 **PR을 날려본 경험**이 있고
- LLM 기반 앱을 **반나절 만에 MVP로 만들** 수 있는 사람이 되었어요.

다음 [Part 4: 문서 처리 라이브러리](../part4-document-libraries/index.md)에서는 **"이 가이드북 자체를 만들어낸 라이브러리들"**을 소개합니다. 이 파트가 특히 재미있을 거예요.

!!! tip "💡 Part 3 전체 회고 프롬프트"
    ```
    Claude, 내가 Part 3를 다 읽었어. 내가 지금 할 수 있는 것과 못하는 것을
    체크리스트로 정리해줘. 그리고 다음 2주간 매일 30분씩 뭘 해야 하는지
    실천 가능한 일일 계획표를 만들어줘.
    ```
