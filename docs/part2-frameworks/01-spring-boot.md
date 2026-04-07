# 2-1. Spring Boot 생태계

> "Java로 백엔드를 하려면 Spring Boot는 피할 수 없다"는 말, 한 번쯤 들어봤을 거예요.
> 금융권·공기업·대기업 SI·스타트업 할 것 없이 한국에서 가장 많이 쓰이는 백엔드 프레임워크입니다.
> 이번 섹션에서는 **Spring Boot를 "혼자 공부하다 막히지 않도록"** 필수 레포 5개를 실전 매뉴얼처럼 안내할게요.

!!! info "📌 이 페이지의 핵심 요약"
    - `spring-boot` 본체 레포는 **내부 동작 이해용**, 신규 프로젝트는 `start.spring.io`에서 만든다
    - `eugenp/tutorials`는 **"하고 싶은 주제 키워드로 검색"** 하는 레시피북이다
    - `macrozheng/mall`은 **실전 아키텍처**를 엿볼 수 있는 유일한 대형 예제다
    - `java-design-patterns`는 한 패턴당 **30분**이면 학습 완료 가능
    - `realworld`는 스택 비교 학습의 끝판왕이다

---

## 전체 학습 로드맵

```
[1주차] start.spring.io로 Hello World → spring-boot 본체에서 @SpringBootApplication 소스 한 번 구경
   ↓
[2주차] eugenp/tutorials에서 관심 있는 모듈 3개 실행 (예: JWT 로그인)
   ↓
[3주차] java-design-patterns로 singleton/strategy/observer 등 5개 패턴 실행
   ↓
[4주차] macrozheng/mall을 클론해서 mall-portal의 주문 흐름 하나만 정복
   ↓
[5주차] realworld 스펙을 보고 "내 버전 Conduit" 클론 시작 → 포트폴리오로 연결
```

---

## 2-1-1. spring-projects/spring-boot (76K+ Stars)

**한 줄 소개**: Spring Framework 기반의 빠른 애플리케이션 개발 프레임워크 본체.
**왜 봐야 하는가**: "자동 설정이 어떻게 마법처럼 동작하는지" 궁금해질 때, 답은 이 레포 안에 있습니다.
**난이도**: ⭐⭐⭐⭐⭐ (본격 학습용 아님. 내부 구현 탐색용)

### 📋 이 레포에서 배울 수 있는 것
- `@SpringBootApplication`이 사실 3개 어노테이션의 합성임을 소스로 확인
- `spring-boot-autoconfigure`의 조건부 로딩 메커니즘 (`@ConditionalOnClass` 등)
- 공식 starter가 어떻게 구성되는지 (의존성만 있고 코드는 거의 없음)
- 내장 Tomcat이 어떻게 시작되는지
- 공식 예제인 `spring-boot-smoke-tests`로 최소 동작 코드 확인

### 🚀 15분 퀵스타트 (본체 레포가 아니라 start.spring.io 사용)

!!! tip "💡 꿀팁: 본체 레포는 학습용이 아니에요"
    `spring-boot` 본체는 76K Stars이지만, **신규 프로젝트를 만들기엔 너무 큽니다.** Spring 팀도 "실제 프로젝트는 `start.spring.io`에서 생성하세요"라고 안내합니다. 본체 레포는 "궁금할 때 소스를 뒤지는 용도"로만 쓰세요.

**1단계: Java 17+ 설치 확인**
```bash
java -version
```
!!! info "예상 출력"
    ```
    openjdk version "17.0.10" 2024-01-16
    OpenJDK Runtime Environment Temurin-17.0.10+7
    ```
    Java 8이나 11이 나오면 반드시 17 이상으로 업그레이드하세요. Spring Boot 3.x는 Java 17 미만에서는 실행조차 안 됩니다.

**2단계: `start.spring.io`에서 프로젝트 생성**
```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web,data-jpa,h2,lombok \
  -d type=gradle-project \
  -d language=java \
  -d bootVersion=3.2.0 \
  -d javaVersion=17 \
  -d name=demo \
  -o demo.zip

# 압축 풀기 (Windows PowerShell)
Expand-Archive demo.zip -DestinationPath demo
cd demo
```

**3단계: 첫 실행**
```bash
./gradlew bootRun
```
!!! info "예상 출력"
    ```
    Started DemoApplication in 2.345 seconds (process running for 2.678)
    ```
    브라우저에서 `http://localhost:8080`을 열어보세요. 404가 뜨면 정상입니다 (아직 컨트롤러가 없으니까요).

**4단계: Hello World 컨트롤러 추가**
`src/main/java/com/example/demo/HelloController.java`를 만들어 붙여넣으세요.
```java
package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
  @GetMapping("/hello")
  public String hello() {
    return "안녕하세요, Spring Boot!";
  }
}
```

**5단계: 본체 레포 클론해서 내부 구경**
```bash
git clone --depth 1 https://github.com/spring-projects/spring-boot.git
cd spring-boot
```
디렉토리 구조에서 주목할 곳은 다음과 같아요.

- `spring-boot-project/spring-boot` — 코어 모듈, `@SpringBootApplication` 구현
- `spring-boot-project/spring-boot-autoconfigure` — 자동 설정 핵심 로직 (여기가 진짜 재미있음)
- `spring-boot-project/spring-boot-starters` — 스타터 의존성 모음 (코드 거의 없음, pom.xml만 있음)
- `spring-boot-tests/spring-boot-smoke-tests` — 작은 샘플 앱 모음 (학습에 최적)

### 🤖 Claude Code로 200% 활용하기

!!! example "프롬프트 예시 1: 자동 설정 마법 해체"
    > "spring-boot-project/spring-boot-autoconfigure 디렉토리에서 DataSourceAutoConfiguration이 어떻게 @ConditionalOnClass로 조건부 로드되는지 소스를 보고 설명해줘. 초보자도 이해할 수 있게 비유를 곁들여서."

!!! example "프롬프트 예시 2: @SpringBootApplication 해부"
    > "@SpringBootApplication 어노테이션이 내부적으로 어떤 어노테이션 3개를 조합하는지 spring-boot 레포에서 소스를 찾아줘. 각 어노테이션의 역할을 1줄씩 설명해줘."

!!! example "프롬프트 예시 3: 학습 순서 추천"
    > "spring-boot-tests/spring-boot-smoke-tests 중에서 가장 단순한 REST API 예제 3개를 찾아서, 초보자가 순서대로 읽으면 좋을 순서로 정렬하고 이유도 말해줘."

### 🚨 자주 발생하는 에러 Top 3

!!! danger "에러 1: `Unsupported class file major version 61`"
    **에러 메시지**: `java.lang.UnsupportedClassVersionError: ... Unsupported class file major version 61`
    **원인**: Java 17로 빌드한 클래스를 Java 11 이하에서 실행하려 할 때 발생.
    **해결**: `java -version`으로 17 이상인지 확인하고, IntelliJ라면 `File > Project Structure > Project SDK`를 17로 변경하세요.
    **Claude로 디버깅**:
    > "Spring Boot 실행했는데 UnsupportedClassVersionError major version 61 에러가 나. Windows 환경에서 Java 17로 JAVA_HOME을 바꾸는 방법과 IntelliJ 설정을 단계별로 알려줘."

!!! danger "에러 2: `Web server failed to start. Port 8080 was already in use`"
    **에러 메시지**: `Web server failed to start. Port 8080 was already in use.`
    **원인**: 8080 포트를 이미 다른 프로세스가 쓰고 있음 (대개 이전에 실행한 Spring Boot가 안 꺼진 경우).
    **해결**: `application.yml`에 `server.port: 8081`을 넣거나, Windows에서 `netstat -ano | findstr :8080`으로 PID 찾아서 종료.
    **Claude로 디버깅**:
    > "Spring Boot가 Port 8080 already in use 에러로 실행이 안 돼. Windows 환경에서 8080 포트를 점유한 프로세스 찾아서 죽이는 방법을 알려줘."

!!! danger "에러 3: `Failed to configure a DataSource`"
    **에러 메시지**: `Failed to configure a DataSource: 'url' attribute is not specified and no embedded datasource could be configured.`
    **원인**: `spring-boot-starter-data-jpa`를 넣었는데 DB 연결 정보가 없음.
    **해결**: `application.yml`에 H2 설정을 추가하거나, JPA가 필요 없다면 의존성에서 제거하세요.
    **Claude로 디버깅**:
    > "Spring Boot 실행하니까 'Failed to configure a DataSource' 에러가 나. H2 인메모리 DB로 임시로 돌리고 싶어. application.yml에 뭘 넣어야 하는지 알려줘."

### 📚 학습 체크리스트
- [ ] `start.spring.io`에서 프로젝트 생성해서 실행했다
- [ ] Hello World 컨트롤러를 추가해서 브라우저로 확인했다
- [ ] `@SpringBootApplication`의 정의를 IntelliJ에서 타고 들어가 읽어봤다
- [ ] `spring-boot-autoconfigure` 디렉토리에서 `AutoConfiguration`으로 끝나는 파일 1개 이상 열어봤다
- [ ] 위 에러 Top 3 중 최소 1개는 실제로 경험해봤다 (고생한 것도 자산입니다!)

---

## 2-1-2. eugenp/tutorials (37K+ Stars) — Baeldung 예제 창고

**한 줄 소개**: Baeldung 블로그의 모든 Java/Spring 예제 코드가 모듈별로 정리된 학습 보물창고.
**왜 봐야 하는가**: "Spring Security JWT 로그인 예제"를 검색하면 Baeldung이 나오는데, 거기서 소개된 코드가 전부 여기 있습니다.
**난이도**: ⭐⭐ (모듈 단위로 보면 쉬움. 전체는 거대해서 절대 다 보지 마세요)

### 📋 이 레포에서 배울 수 있는 것
- Spring Security JWT / OAuth2 / Session 기반 인증 비교
- Spring Data JPA의 `@Query`, Specification, Querydsl 실전 사용법
- Kafka, RabbitMQ 메시징 연동 최소 예제
- JUnit 5, Mockito, Testcontainers 테스트 작성법
- Reactive(WebFlux) vs 전통 Web MVC 비교

### 🚀 15분 퀵스타트

!!! warning "⚠️ 전체 빌드 금지"
    이 레포는 **Maven 멀티 모듈이 수백 개**입니다. 루트에서 `mvn install`하면 1시간 넘게 걸리고 디스크 10GB를 먹습니다. **반드시 필요한 모듈만** 빌드하세요.

**1단계: Shallow Clone**
```bash
git clone --depth 1 https://github.com/eugenp/tutorials.git
cd tutorials
```
!!! info "예상 출력"
    ```
    Cloning into 'tutorials'...
    remote: Enumerating objects: 30000, done.
    ...
    Updating files: 100% (28000/28000), done.
    ```

**2단계: 원하는 모듈로 바로 이동**
```bash
cd spring-security-modules/spring-security-web-login
```

**3단계: 모듈 단독 빌드**
```bash
mvn clean install -DskipTests
```

**4단계: 실행**
```bash
mvn spring-boot:run
```
!!! info "예상 출력"
    ```
    Started Application in 3.456 seconds
    ```
    브라우저에서 `http://localhost:8080/login`을 열어 로그인 화면을 확인하세요.

**5단계: 관심 키워드로 다른 모듈 찾기**
```bash
# Windows PowerShell에서
Get-ChildItem -Recurse -Directory -Filter "*jwt*"
```

### 초보자가 먼저 봐야 할 모듈 Top 5

| 모듈 경로 | 배울 내용 | 난이도 |
| --- | --- | --- |
| `spring-boot-modules/spring-boot-basic-customization` | Spring Boot 기본 설정 커스터마이징 | ⭐⭐ |
| `spring-security-modules/spring-security-web-login` | 폼 로그인 최소 예제 | ⭐⭐⭐ |
| `persistence-modules/spring-data-jpa-query` | JPA `@Query` 어노테이션 사용법 | ⭐⭐⭐ |
| `testing-modules/testing-assertions` | JUnit 5 + AssertJ 테스트 | ⭐⭐ |
| `spring-boot-modules/spring-boot-runtime` | Actuator, 헬스체크, 메트릭 | ⭐⭐⭐ |

### 🤖 Claude Code로 200% 활용하기

!!! example "프롬프트 예시 1: 모듈 탐색"
    > "eugenp/tutorials 레포의 spring-security-modules 디렉토리를 훑어보고, 'JWT 로그인 구현'에 가장 가까운 모듈 3개를 찾아서 난이도 순으로 정렬해줘. 각 모듈의 README 첫 문단도 요약해줘."

!!! example "프롬프트 예시 2: 코드 비교"
    > "persistence-modules 안에서 Spring Data JPA `@Query` 어노테이션을 네이티브 SQL로 쓰는 예제와 JPQL로 쓰는 예제를 각각 하나씩 찾아서 장단점을 비교해줘."

!!! example "프롬프트 예시 3: 내 프로젝트에 이식"
    > "spring-security-modules/spring-security-web-jwt 모듈의 JwtTokenProvider 클래스를 내 Spring Boot 3.x 프로젝트로 복사해올 때, 버전 차이로 수정해야 할 부분을 알려줘."

### 🚨 자주 발생하는 에러 Top 3

!!! danger "에러 1: 전체 빌드 시 OutOfMemoryError"
    **에러 메시지**: `java.lang.OutOfMemoryError: Java heap space`
    **원인**: 루트에서 `mvn install`을 실행해서 수백 개 모듈을 빌드 중.
    **해결**: **당장 중단**하고, 필요한 모듈 디렉토리로 이동해서 그 안에서만 빌드하세요.

!!! danger "에러 2: `Could not find artifact com.baeldung:parent-xxx`"
    **에러 메시지**: `Could not find artifact com.baeldung:parent-boot-3:pom:1.0.0-SNAPSHOT`
    **원인**: 하위 모듈이 parent pom에 의존하는데 parent가 로컬에 없음.
    **해결**: 루트에서 `mvn install -N -DskipTests`로 parent만 먼저 설치.
    **Claude로 디버깅**:
    > "Maven 멀티 모듈 프로젝트에서 parent pom을 먼저 설치하는 방법을 알려줘. `-N` 옵션의 의미도 설명해줘."

!!! danger "에러 3: Lombok 컴파일 에러"
    **에러 메시지**: `cannot find symbol method getName()` (실제로는 `@Getter`가 만들어줘야 할 메서드)
    **원인**: IntelliJ에서 Lombok 플러그인과 annotation processing이 꺼져 있음.
    **해결**: `Settings > Build > Compiler > Annotation Processors`에서 `Enable annotation processing` 체크.

### 📚 학습 체크리스트
- [ ] 전체 빌드하지 않고 1개 모듈만 빌드하는 데 성공했다
- [ ] JWT 로그인 예제를 실행해봤다
- [ ] JPA `@Query` 예제 1개를 내 프로젝트로 복사해봤다
- [ ] Baeldung 블로그 글과 레포 코드가 어떻게 연결되는지 이해했다

---

## 2-1-3. macrozheng/mall (83K+ Stars) — 실전 전자상거래 시스템

**한 줄 소개**: Spring Boot + MyBatis + ES + Redis + RabbitMQ로 구축된 운영 수준의 쇼핑몰 풀스택 백엔드.
**왜 봐야 하는가**: "튜토리얼 수준 예제 말고, 진짜 실무는 어떤 느낌일까?"에 대한 가장 좋은 답.
**난이도**: ⭐⭐⭐⭐ (실행 환경 세팅이 어려움. 코드 읽기만 해도 가치 있음)

### 📋 이 레포에서 배울 수 있는 것
- 대형 프로젝트의 모듈 분리 (admin/portal/search/demo)
- MyBatis XML 매퍼 실전 활용법
- Redis 캐싱 전략 (어떤 메서드에 캐시를 걸지)
- Elasticsearch 상품 검색 연동
- RabbitMQ를 활용한 주문 타임아웃 처리
- JWT + Spring Security 실전 결합
- Swagger/Knife4j 기반 API 문서화

### 🚀 15분 퀵스타트 (코드 읽기 중심)

!!! tip "💡 꿀팁: 실행은 나중에, 코드부터 읽으세요"
    이 레포를 **제대로 실행하려면** MySQL + Redis + ES + RabbitMQ + MongoDB가 다 필요합니다. Docker Compose로 띄워도 초보자에게는 벅찹니다. **먼저 코드만 읽어서 아키텍처를 파악**하고, 실행은 시간 여유 있을 때 도전하세요.

**1단계: Shallow Clone**
```bash
git clone --depth 1 https://github.com/macrozheng/mall.git
cd mall
```

**2단계: 반드시 먼저 읽어야 할 문서**
```bash
cd document
ls
```
!!! info "예상 출력"
    ```
    architect/  docker/  reference/  sql/  ...
    ```
    - `architect/` — 시스템 아키텍처 다이어그램 (**가장 먼저 읽기**)
    - `sql/` — DB 스키마 SQL (**두 번째로 읽기**)
    - `docker/` — Docker Compose 파일들

**3단계: 모듈 구조 파악**
```bash
cd ..
ls mall-*
```
| 모듈 | 역할 |
| --- | --- |
| `mall-admin` | 관리자 백오피스 API (상품 등록, 주문 관리) |
| `mall-portal` | 사용자 쇼핑몰 API (장바구니, 주문, 결제) |
| `mall-search` | Elasticsearch 기반 상품 검색 |
| `mall-demo` | 부가 기능 데모 |
| `mall-common` | 공통 유틸 |
| `mall-security` | Spring Security 공통 설정 |
| `mall-mbg` | MyBatis Generator (코드 자동 생성) |

**4단계: 주문 흐름 한 줄기 따라가기**
초보자에게 가장 학습 가치가 높은 경로는 **사용자 주문 생성 흐름**입니다.
```bash
cd mall-portal/src/main/java/com/macro/mall/portal
```
- `controller/OmsPortalOrderController.java` — 주문 생성 엔드포인트
- `service/OmsPortalOrderService.java` — 주문 생성 서비스 인터페이스
- `service/impl/OmsPortalOrderServiceImpl.java` — **핵심 비즈니스 로직**

**5단계 (선택): 실행 환경 구축**
```bash
cd document/docker
docker-compose up -d
```
!!! warning "⚠️ 경고"
    이 명령은 MySQL, Redis, ES, RabbitMQ, MongoDB 등을 한꺼번에 띄웁니다. RAM 8GB 이상 필요. 처음이라면 **4단계까지만** 하고 다음 레포로 넘어가는 것을 추천합니다.

### 🤖 Claude Code로 200% 활용하기

!!! example "프롬프트 예시 1: 주문 흐름 추적"
    > "mall-portal 모듈의 OmsPortalOrderServiceImpl.generateOrder() 메서드를 읽고, 주문 생성부터 재고 차감, 쿠폰 사용, DB 저장까지의 전체 흐름을 순서도로 그려줘. 각 단계마다 호출되는 다른 서비스도 명시해줘."

!!! example "프롬프트 예시 2: 캐싱 전략 분석"
    > "mall 프로젝트 전체에서 Redis 캐싱(@Cacheable 또는 RedisTemplate)을 사용한 메서드를 모두 찾아서 '어떤 데이터를 왜 캐싱했는지' 표로 정리해줘."

!!! example "프롬프트 예시 3: DB 스키마 이해"
    > "document/sql 디렉토리의 mall.sql을 읽고 pms_product, pms_sku_stock, oms_order 테이블 간 관계를 설명해줘. 상품/SKU/주문이 어떻게 연결되는지 초보자도 이해할 수 있게."

!!! example "프롬프트 예시 4: 내 프로젝트에 이식"
    > "mall-security 모듈의 JWT 인증 필터 구조를 내 Spring Boot 3.x 프로젝트에 이식하려고 해. 버전 차이로 수정해야 할 부분과, 단순화해도 되는 부분을 알려줘."

### 🚨 자주 발생하는 에러 Top 3

!!! danger "에러 1: Docker Compose 메모리 부족"
    **에러 메시지**: `Container mall-elasticsearch exited with code 137`
    **원인**: Elasticsearch가 메모리 부족으로 강제 종료됨 (code 137 = OOM).
    **해결**: Docker Desktop 설정에서 메모리를 최소 6GB로 늘리거나, ES 힙 사이즈를 낮추세요.
    **Claude로 디버깅**:
    > "Docker로 Elasticsearch 띄우니까 exit code 137로 죽어. Docker Desktop 메모리 설정 방법과 ES_JAVA_OPTS로 힙 제한하는 방법 둘 다 알려줘."

!!! danger "에러 2: MyBatis 매퍼 XML을 못 찾음"
    **에러 메시지**: `Invalid bound statement (not found): com.macro.mall.mapper.XxxMapper.selectByPrimaryKey`
    **원인**: Gradle/Maven이 XML 리소스를 classpath에 포함 안 시킴.
    **해결**: `pom.xml`의 `<build><resources>`에 `**/*.xml`을 추가.

!!! danger "에러 3: Redis 연결 거부"
    **에러 메시지**: `Unable to connect to Redis; nested exception is io.lettuce.core.RedisConnectionException`
    **원인**: Redis가 실행 안 됐거나 `application.yml`의 호스트/포트가 잘못됨.
    **해결**: `docker ps`로 Redis 컨테이너 상태 확인, `application.yml`의 `spring.redis.host`를 `localhost`로.

### 📚 학습 체크리스트
- [ ] `document/architect` 다이어그램을 다 읽었다
- [ ] `document/sql/mall.sql`로 DB 스키마 3개 테이블 관계를 이해했다
- [ ] `OmsPortalOrderServiceImpl.generateOrder()` 코드를 한 줄씩 따라 읽었다
- [ ] Redis 캐싱이 적용된 메서드 3개 이상을 찾았다
- [ ] (선택) Docker Compose로 최소 MySQL + Redis 2개라도 띄워봤다

---

## 2-1-4. iluwatar/java-design-patterns (90K+ Stars)

**한 줄 소개**: GoF + 엔터프라이즈 디자인 패턴 150+개를 Java로 구현한 세계 최대 패턴 모음.
**왜 봐야 하는가**: 기술 면접 단골 질문 "디자인 패턴 써본 적 있어요?"에 답하려면 이 레포가 최단 경로.
**난이도**: ⭐⭐ (패턴 하나당 30분, 초보자 친화적)

### 📋 이 레포에서 배울 수 있는 것
- Creational 패턴: Singleton, Factory, Builder, Prototype
- Structural 패턴: Adapter, Decorator, Facade, Proxy
- Behavioral 패턴: Strategy, Observer, Command, Chain of Responsibility
- 엔터프라이즈 패턴: Repository, DAO, DTO, Service Layer
- 각 패턴의 **UML 다이어그램** (README에 포함)

### 🚀 15분 퀵스타트

**1단계: Shallow Clone**
```bash
git clone --depth 1 https://github.com/iluwatar/java-design-patterns.git
cd java-design-patterns
```

**2단계: 전체 빌드 금지, 패턴별 개별 실행**
```bash
cd singleton
mvn compile exec:java
```
!!! info "예상 출력"
    ```
    ivoryTower1=com.iluwatar.singleton.IvoryTower@...
    ivoryTower2=com.iluwatar.singleton.IvoryTower@...
    (두 주소가 동일해야 Singleton 정상 동작)
    ```

**3단계: README 먼저 읽기**
```bash
cd ../strategy
cat README.md  # Windows PowerShell에서는 `Get-Content README.md`
```
각 패턴 디렉토리의 README에는 **"언제 사용하는가", "장단점", "UML 다이어그램"** 이 포함되어 있습니다.

**4단계: 내 손으로 타이핑해보기**
패턴을 진짜 익히려면 **복사 붙여넣기 말고 타이핑**해보세요. `singleton/src/main/java/com/iluwatar/singleton/IvoryTower.java`를 보지 않고 작성할 수 있을 때까지 반복.

**5단계: 실무 연결 상상**
패턴을 실제 어디에 쓸지 상상해보세요. 예: Strategy 패턴 = 결제 수단 선택 (카드/카카오페이/토스).

### 초보자가 먼저 봐야 할 패턴 Top 10

| 순서 | 패턴 | 실무 예시 |
| --- | --- | --- |
| 1 | `singleton` | Spring Bean 기본 스코프 |
| 2 | `factory` | 객체 생성 추상화 |
| 3 | `builder` | Lombok `@Builder`의 원리 |
| 4 | `strategy` | 결제 수단별 처리 로직 |
| 5 | `observer` | 이벤트 리스너, Spring `ApplicationEvent` |
| 6 | `decorator` | HTTP 요청 래퍼, 로깅 추가 |
| 7 | `adapter` | 외부 API 응답 → 내부 DTO 변환 |
| 8 | `facade` | Service 계층의 본질 |
| 9 | `repository` | Spring Data JPA의 Repository |
| 10 | `chain-of-responsibility` | Spring Security Filter Chain |

### 🤖 Claude Code로 200% 활용하기

!!! example "프롬프트 예시 1: 실무 연결"
    > "java-design-patterns 레포의 strategy 패턴 README와 App.java를 읽고, 실제 결제 시스템(카드/카카오페이/토스 3가지)에 Strategy 패턴을 적용한 코드를 Spring Boot 스타일로 작성해줘."

!!! example "프롬프트 예시 2: 패턴 비교"
    > "decorator 패턴과 chain-of-responsibility 패턴이 비슷해 보이는데, 이 레포의 두 예제를 비교하면서 언제 어느 걸 써야 하는지 알려줘."

!!! example "프롬프트 예시 3: 안티 패턴 경고"
    > "singleton 패턴의 이 레포 구현을 보고, 초보자가 흔히 저지르는 안티 패턴(멀티스레드 문제 등)을 지적해줘. 올바른 구현과 비교해서."

### 🚨 자주 발생하는 에러 Top 3

!!! danger "에러 1: 루트에서 `mvn install` 시도하면 1시간 걸림"
    **원인**: 150개 모듈 전체 빌드 중.
    **해결**: **당장 중단**. 패턴별 디렉토리로 이동해서 개별 빌드.

!!! danger "에러 2: `exec:java` 실행 시 mainClass 찾기 실패"
    **에러 메시지**: `No plugin found for prefix 'exec'`
    **해결**: 해당 패턴의 `pom.xml`에 exec-maven-plugin이 없는 경우가 있습니다. `mvn compile`만 하고 IntelliJ에서 `App.java`를 Run하세요.

!!! danger "에러 3: Java 버전 불일치"
    **에러 메시지**: `Source option 17 is no longer supported. Use 21 or later.`
    **원인**: 최신 커밋은 Java 21 타겟.
    **해결**: Java 21 설치 후 `JAVA_HOME` 재설정, 또는 `git checkout` 으로 조금 이전 태그로 이동.

### 📚 학습 체크리스트
- [ ] `singleton`, `factory`, `builder` 3개 패턴을 직접 실행했다
- [ ] `strategy`, `observer`, `decorator`를 README로 학습했다
- [ ] 내 손으로 `singleton` 패턴을 보지 않고 타이핑했다
- [ ] 패턴 1개를 골라 "Spring Boot에서 어디에 쓰이는지" 예시를 찾았다

---

## 2-1-5. gothinkster/realworld (80K+ Stars)

**한 줄 소개**: "모든 프레임워크로 동일한 스펙의 블로그 앱(Conduit)을 만든다"는 메타 프로젝트.
**왜 봐야 하는가**: 같은 기능을 Spring Boot / Express / Django / Rails로 비교 학습할 수 있는 **유일한 레포**.
**난이도**: ⭐⭐⭐ (API 스펙은 중간 난이도, 구현체 선택에 따라 달라짐)

### 📋 이 레포에서 배울 수 있는 것
- 표준 API 스펙 읽는 법 (https://docs.realworld.show/)
- 동일 기능을 여러 언어/프레임워크로 구현할 때의 차이점
- JWT 인증, CRUD, 팔로우/팔로잉, 좋아요 기능의 표준 구현
- "스택 이식"의 감각 (Spring Boot 코드를 NestJS로 옮겨보기 등)

### 🚀 15분 퀵스타트

**1단계: 메인 레포 클론**
```bash
git clone --depth 1 https://github.com/gothinkster/realworld.git
cd realworld
```
!!! tip "💡 메인 레포에는 코드가 없어요"
    메인 `realworld` 레포는 **스펙과 구현체 링크 모음**입니다. 실제 코드는 구현체 레포에 따로 있어요.

**2단계: API 스펙 문서 열기**
```
https://docs.realworld.show/
```
- Endpoints, Request/Response 형식, 인증 방식이 완벽히 정의되어 있습니다.
- **백엔드 개발자라면 이 문서를 반드시 정독**하세요. 표준 REST API 설계 공부의 교과서입니다.

**3단계: 관심 있는 스택의 구현체 클론**
```bash
# Spring Boot 구현
git clone --depth 1 https://github.com/gothinkster/spring-boot-realworld-example-app.git

# Node.js Express 구현
git clone --depth 1 https://github.com/gothinkster/node-express-realworld-example-app.git
```

**4단계: Spring Boot 구현체 실행**
```bash
cd spring-boot-realworld-example-app
./gradlew bootRun
```
!!! info "예상 출력"
    ```
    Started ApplicationKt in 3.5 seconds
    ```
    이 구현체는 Kotlin + Spring Boot입니다. Java 버전을 원하면 구현체 목록에서 다른 레포를 골라도 돼요.

**5단계: Postman으로 API 호출**
API 스펙의 Register 엔드포인트를 Postman으로 호출해보세요.
```http
POST http://localhost:8080/api/users
Content-Type: application/json

{
  "user": {
    "username": "testuser",
    "email": "test@test.com",
    "password": "password"
  }
}
```

### 🤖 Claude Code로 200% 활용하기

!!! example "프롬프트 예시 1: 스택 비교"
    > "gothinkster/spring-boot-realworld-example-app와 gothinkster/node-express-realworld-example-app에서 Article 생성 API의 비즈니스 로직을 각각 찾아서, 코드량/가독성/구조적 차이를 비교해줘."

!!! example "프롬프트 예시 2: JWT 구현 추출"
    > "spring-boot-realworld-example-app의 JWT 인증 구현 부분만 추려서, 내 Spring Boot 프로젝트에 이식할 수 있는 형태로 정리해줘."

!!! example "프롬프트 예시 3: 내가 직접 만들기"
    > "RealWorld 스펙을 기준으로 내가 Spring Boot 3.x + JPA로 Article CRUD만 먼저 구현하려고 해. User 엔티티 없이 Article만 만드는 최소 구조를 잡아줘."

### 🚨 자주 발생하는 에러 Top 3

!!! danger "에러 1: Gradle Wrapper 권한 에러"
    **에러 메시지**: `permission denied: ./gradlew`
    **원인**: Unix 실행 권한 없음 (Windows Git Bash에서 자주 발생).
    **해결**: `sh gradlew bootRun` 또는 Windows는 `gradlew.bat bootRun` 사용.

!!! danger "에러 2: 구현체가 너무 오래되어 빌드 실패"
    **원인**: 일부 구현체는 수년간 업데이트 안 됨.
    **해결**: RealWorld 공식 사이트에서 "Maintained" 배지가 붙은 구현체를 고르세요.

!!! danger "에러 3: CORS 에러"
    **에러 메시지**: `Access-Control-Allow-Origin' header is present`
    **원인**: 프론트엔드와 백엔드를 따로 실행하면서 CORS 설정 누락.
    **해결**: Spring Boot라면 `@CrossOrigin` 또는 `WebMvcConfigurer`로 처리.

### 📚 학습 체크리스트
- [ ] https://docs.realworld.show/ 스펙 문서를 정독했다
- [ ] Spring Boot 또는 Express 구현체 중 하나를 실행해봤다
- [ ] Postman으로 User Register + Login API를 호출해봤다
- [ ] 두 개의 다른 스택 구현체의 Article 생성 API 코드를 비교해봤다

---

## 이 섹션 마무리

여기까지 왔다면 Spring Boot 생태계의 **전체 지형도**가 머릿속에 그려졌을 거예요. 다음은 React 생태계입니다. 프론트엔드는 백엔드와 사고방식이 꽤 다르니, 마음의 준비를 하고 [02-react.md](02-react.md)로 넘어가세요.

!!! info "📌 한 줄 정리"
    Spring Boot 학습의 왕도는 **"start.spring.io로 작게 시작 → eugenp에서 레시피 검색 → design-patterns로 기초 다지기 → mall로 실전 구경 → realworld로 포트폴리오 연결"** 순서입니다.
