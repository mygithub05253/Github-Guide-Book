# 📘 Spring Boot 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/spring-projects/spring-boot.svg?style=social)](https://github.com/spring-projects/spring-boot)

!!! info "레포지토리"
    **spring-projects/spring-boot** · 75k+ ⭐ · Apache 2.0 · [spring.io/projects/spring-boot](https://spring.io/projects/spring-boot)

---

## 🧐 1. Spring Boot는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Spring Boot는 **"설정 지옥" 없이 production-grade Spring 애플리케이션을 빠르게 만들 수 있도록 하는 자바 백엔드 프레임워크**입니다. Convention over Configuration(관례가 설정을 대체) 원칙을 따릅니다.

### 핵심 특성

- **Auto-configuration**: classpath에 추가된 라이브러리를 보고 필요한 Bean을 자동으로 구성. `spring-boot-starter-data-jpa`만 추가하면 DataSource·EntityManager·TransactionManager가 자동 세팅됩니다.
- **Starter 의존성**: `spring-boot-starter-web`, `-security`, `-data-jpa` 같은 묶음 의존성이 호환 버전을 한 번에 가져옴 → 버전 충돌 지옥 해결.
- **Embedded Server**: Tomcat/Jetty/Undertow가 jar에 내장 → `java -jar app.jar` 한 줄로 실행. 별도 WAS 설치 불필요.
- **Production-ready**: Actuator(헬스체크·메트릭), Micrometer(모니터링), 환경별 프로파일(`application-prod.yml`) 등 운영 기능이 기본 제공.

### 실무 도입 포인트

| 도입 이유 | 구체적 효과 |
|---|---|
| **국내 채용 시장 1위 백엔드** | 금융권·공기업·SI 거의 모든 자바 백엔드 채용 공고가 Spring Boot 요구 |
| **JPA/Hibernate 통합** | RDB 작업을 객체지향으로 표현 → 보일러플레이트 SQL 제거 |
| **Spring Security** | 인증/인가 산업 표준. OAuth2, JWT, RBAC 모두 지원 |
| **거대한 생태계** | Spring Cloud(MSA), Spring Batch(배치), Spring Integration(EAI) 등 확장이 쉽다 |

### 기존 방식 vs Spring Boot

```
[기존 Spring Framework (XML 시대)]
applicationContext.xml 수백 줄, web.xml, Tomcat 설치 → 환경 세팅에만 며칠

[Spring Boot]
@SpringBootApplication 1줄 + application.yml 10줄 = 실행 가능한 서버
```

## 🚀 2. 10분 퀵스타트

### 환경 준비

```bash
java -version    # Java 17+ (LTS) 권장
./gradlew -v     # Gradle wrapper (없으면 프로젝트 생성 시 자동 포함)
```

### Spring Initializr로 프로젝트 생성

가장 쉬운 방법: **[start.spring.io](https://start.spring.io)** 접속 →

1. Project: **Gradle - Groovy**
2. Language: **Java**
3. Spring Boot: **3.x**
4. Dependencies: **Spring Web**, **Spring Data JPA**, **H2 Database**, **Lombok**
5. **Generate** 클릭 → zip 다운로드

또는 CLI:

```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web,data-jpa,h2,lombok \
  -d type=gradle-project -d language=java -d bootVersion=3.3.0 \
  -d javaVersion=17 -o demo.zip
unzip demo.zip -d demo && cd demo
```

### 첫 REST 컨트롤러

```java
// src/main/java/com/example/demo/HelloController.java
package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello(@RequestParam(defaultValue = "World") String name) {
        return "Hello, " + name + "!";
    }
}
```

### 실행 및 검증

```bash
./gradlew bootRun
```

예상 출력:

```
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 :: Spring Boot ::                (v3.3.0)

... Tomcat started on port 8080 ...
... Started DemoApplication in 1.234 seconds ...
```

브라우저: `http://localhost:8080/hello?name=PLAF` → `Hello, PLAF!`

## 🛠️ 3. 코드 해부학: Layered Architecture

표준 패키지 구조 (실무 컨벤션):

```
src/main/java/com/example/demo/
├── DemoApplication.java          # @SpringBootApplication (진입점)
├── controller/                   # HTTP 요청 진입점 (REST API)
│   └── UserController.java
├── service/                      # 비즈니스 로직 + @Transactional
│   └── UserService.java
├── repository/                   # DB 접근 (JPA Repository)
│   └── UserRepository.java
├── domain/                       # JPA Entity (= 테이블)
│   └── User.java
├── dto/                          # Request/Response 객체
│   └── UserDto.java
└── config/                       # @Configuration Bean 정의
    └── SecurityConfig.java
```

| 계층 | 책임 | 호출 방향 |
|---|---|---|
| Controller | HTTP 요청/응답 변환, 입력 검증 | → Service |
| Service | 트랜잭션, 비즈니스 규칙 | → Repository |
| Repository | DB CRUD | DB |
| Domain (Entity) | 테이블 매핑 + 비즈니스 메서드 | — |
| DTO | 계층 간 데이터 전달 (Entity 직접 노출 금지) | — |

!!! warning "초보자 실수 포인트"
    - Entity를 그대로 Controller에서 반환하지 마세요. 순환 참조·N+1 쿼리·민감 정보 노출의 원인이 됩니다. **반드시 DTO로 변환**.
    - `@Transactional`은 **Service 계층**에 붙입니다. Repository에 붙이면 트랜잭션 경계가 너무 작아져 의미가 없어집니다.

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude (아키텍처 리뷰)
```
/think 다음 Spring Boot 컨트롤러를 리뷰해 줘.
- Layered Architecture 위반 사항
- N+1 쿼리 가능성
- 트랜잭션 경계 적절성
- Security 관점 입력 검증 누락
순서대로 지적하고 수정 코드를 제시해 줘.

[코드 붙여넣기]
```

### 🔵 Gemini (Spring 버전 마이그레이션)
```
Spring Boot 2.7에서 3.3으로 마이그레이션할 때 발생하는
주요 Breaking Change 5가지를 정리해 줘.
특히 javax → jakarta 패키지 변경, Spring Security 6 변경점,
Hibernate 6 마이그레이션 포인트를 코드 비교로 보여 줘.
```

### 🟢 ChatGPT (도메인 모델링)
```
"중고 책 거래 플랫폼"의 Spring Boot 백엔드를 설계하려고 한다.
- 핵심 도메인: User, Book, Listing, Order, Review
- JPA Entity 클래스의 필드, 연관관계(@OneToMany 등), 인덱스 전략
- REST API 엔드포인트 목록(메서드, 경로, 요청/응답 DTO)
을 마크다운 표로 기획해 줘.
```

### ⬛ GitHub Copilot / Codex (IDE 실시간 보조)
```java
// TODO: UserService에 회원 가입 메서드를 작성한다.
//   - 입력: SignupDto(email, password, nickname)
//   - 검증: email 중복 체크, 비밀번호 BCrypt 해싱
//   - 트랜잭션 적용
//   - 중복 시 DuplicateEmailException 발생
```

## 🔗 5. 관련 레포 · 다음 단계

- **공식 가이드**: [spring.io/guides](https://spring.io/guides) (수십 개의 5분 튜토리얼)
- **Spring Initializr**: [start.spring.io](https://start.spring.io)
- **JPA 학습**: 김영한, 자바 ORM 표준 JPA 프로그래밍
- **다음 단계**: Spring Security → Spring Cloud(MSA) → Spring Batch
- **Part 2-1**: 본 가이드북의 [Spring Boot 학습 챕터](../../../part2-frameworks/01-spring-boot.md)
