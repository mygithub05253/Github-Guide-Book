# 📘 Django 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/django/django.svg?style=social)](https://github.com/django/django)

!!! info "레포지토리"
    **django/django** · 80k+ ⭐ · BSD-3 · [djangoproject.com](https://www.djangoproject.com)

---

## 🧐 1. Django는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Django는 **"배터리 포함(batteries-included)" 철학의 Python 풀스택 웹 프레임워크**입니다. ORM, Admin, 인증, 폼, 마이그레이션, 템플릿이 전부 기본 제공됩니다. Instagram, Pinterest, Disqus가 Django로 시작했습니다.

### 핵심 특성
- **Django ORM**: 마이그레이션·관계·쿼리 빌더가 통합된 강력한 ORM.
- **Admin 자동 생성**: 모델 등록 한 줄로 CRUD 관리자 페이지 완성 → 사내 도구 폭발적 생산성.
- **인증·권한**: User 모델·세션·권한·그룹 즉시 사용.
- **DRF (Django REST Framework)**: 별도 패키지로 REST API에 특화.
- **보안 기본 장착**: CSRF, XSS, SQL Injection 방어가 기본.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **MVP 1주 이내 출시** | Admin + Auth가 무료 제공 |
| **데이터 분석가가 백엔드로 확장** | Python·Pandas와 동일 언어 |
| **공공 데이터·연구 프로젝트** | 안정성·보안이 검증됨 |

## 🚀 2. 10분 퀵스타트

```bash
pip install django
django-admin startproject plaf .
python manage.py startapp blog
```

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

`http://localhost:8000/admin` → Post CRUD 즉시 사용 가능.

## 🛠️ 3. 코드 해부학

| 경로 | 역할 |
|---|---|
| `manage.py` | CLI 진입점 |
| `<project>/settings.py` | 전체 설정 (DB, INSTALLED_APPS, MIDDLEWARE) |
| `<project>/urls.py` | 루트 URL 라우팅 |
| `<app>/models.py` | DB 모델 |
| `<app>/views.py` | 요청 처리 (FBV/CBV) |
| `<app>/admin.py` | Admin 등록 |
| `<app>/migrations/` | 마이그레이션 파일 (자동 생성) |

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 다음 Django View를 리뷰해 줘.
- N+1 쿼리 (select_related/prefetch_related 누락)
- 권한 체크 (LoginRequiredMixin/permission_classes)
- 폼 검증 누락
```

### 🔵 Gemini
```
Django vs FastAPI vs Flask를 "신규 Python 백엔드 프로젝트 선택" 관점에서 비교해 줘.
유스케이스별 추천도 포함.
```

### 🟢 ChatGPT
```
"학내 동아리 관리 시스템"을 Django + DRF로 설계해 줘.
모델, ViewSet, 권한, Admin 커스터마이즈 포함.
```

### ⬛ Copilot
```python
# TODO: Post 모델에 좋아요(M:N) 추가 + ViewSet에 like 액션
```

## 🔗 5. 관련 레포 · 다음 단계
- 공식 문서: [docs.djangoproject.com](https://docs.djangoproject.com) · 한국어: [docs.djangoproject.com/ko](https://docs.djangoproject.com/ko/)
- DRF: [django-rest-framework](https://www.django-rest-framework.org)
- Async 작업: [Celery](https://docs.celeryq.dev)
