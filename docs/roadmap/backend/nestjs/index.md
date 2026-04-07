# 📘 NestJS 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/nestjs/nest.svg?style=social)](https://github.com/nestjs/nest)

!!! info "레포지토리"
    **nestjs/nest** · 67k+ ⭐ · MIT License · [nestjs.com](https://nestjs.com)

---

## 🧐 1. NestJS는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: NestJS는 **Angular에서 영감을 받은 모듈·DI 기반의 Node.js 백엔드 프레임워크**입니다. TypeScript First, Express/Fastify 위에서 동작하며, Spring Boot처럼 구조화된 엔터프라이즈 아키텍처를 Node 생태계에 가져옵니다.

### 핵심 특성
- **모듈 시스템**: `@Module()`로 기능을 캡슐화 → 거대 코드베이스에서도 의존성이 명확.
- **DI 컨테이너**: 생성자 주입 기본. 테스트가 쉬워짐.
- **데코레이터 기반**: `@Controller`, `@Get`, `@Injectable`, `@UseGuards` 등으로 선언적 라우팅.
- **TypeScript First**: 런타임 타입 안전 + 풍부한 IDE 지원.
- **마이크로서비스 지원**: gRPC, NATS, Kafka 트랜스포트 내장.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **Spring 출신 자바 개발자가 친숙함** | 패턴이 거의 동일 |
| **거대 팀에서 일관성 유지** | 신입도 즉시 코드 위치 파악 |
| **GraphQL·WebSocket 통합 우수** | `@nestjs/graphql`, `@nestjs/websockets` |
| **Swagger 자동화** | 데코레이터에서 OpenAPI 생성 |

## 🚀 2. 10분 퀵스타트

```bash
npm i -g @nestjs/cli
nest new my-nest-app
cd my-nest-app
npm run start:dev
```

### 첫 컨트롤러 + 서비스
```ts
// users/users.controller.ts
import { Controller, Get, Param } from '@nestjs/common';
import { UsersService } from './users.service';

@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.usersService.findOne(+id);
  }
}
```

```ts
// users/users.service.ts
import { Injectable } from '@nestjs/common';

@Injectable()
export class UsersService {
  findOne(id: number) {
    return { id, name: 'PLAF User' };
  }
}
```

`http://localhost:3000/users/1` → JSON 응답.

## 🛠️ 3. 코드 해부학

| 빌딩 블록 | 역할 |
|---|---|
| **Module** | 기능 단위 캡슐화 (Controller·Provider 등록) |
| **Controller** | HTTP 라우팅 |
| **Provider/Service** | 비즈니스 로직 (`@Injectable()`) |
| **Guard** | 인증/인가 (`@UseGuards()`) |
| **Interceptor** | 요청/응답 가공, 로깅, 캐싱 |
| **Pipe** | 입력 검증·변환 (class-validator 통합) |
| **Filter** | 예외 처리 |

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 다음 NestJS 모듈을 Clean Architecture 관점에서 리뷰해 줘.
- 도메인 로직이 인프라 계층에 누설되었는가
- DTO·Entity 분리가 적절한가
- Guard·Interceptor 사용이 적절한가
```

### 🔵 Gemini
```
NestJS vs Express vs Spring Boot의 차이를 비교 표로 정리해 줘.
생산성, 성능, 채용 시장, 학습 곡선 기준으로.
```

### 🟢 ChatGPT
```
"실시간 채팅 서비스"를 NestJS + WebSocket Gateway + Redis Pub/Sub로 설계해 줘.
모듈 구조, 게이트웨이 코드, 인증 흐름 포함.
```

### ⬛ Copilot
```ts
// TODO: AuthModule - JWT 전략, 로그인/회원가입 컨트롤러
```

## 🔗 5. 관련 레포 · 다음 단계
- 공식 문서: [docs.nestjs.com](https://docs.nestjs.com)
- ORM: [TypeORM](https://typeorm.io), [Prisma](https://www.prisma.io)
- [Spring Boot 딥다이브](../springboot/index.md) (구조 비교)
- [Express 딥다이브](../express/index.md)
