# 📘 Hugging Face Transformers 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/huggingface/transformers.svg?style=social)](https://github.com/huggingface/transformers)

!!! info "레포지토리"
    **huggingface/transformers** · 130k+ ⭐ · Apache 2.0 · [huggingface.co](https://huggingface.co)

---

## 🧐 1. Transformers는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: Hugging Face Transformers는 **수십만 개의 사전학습 모델(NLP·비전·오디오·멀티모달)을 일관된 API로 사용·학습·배포할 수 있게 하는 라이브러리**입니다. AI 분야의 npm·PyPI 같은 존재.

### 핵심 특성
- **Model Hub**: BERT, GPT-2, LLaMA, Whisper, Stable Diffusion 등 50만+ 모델.
- **AutoClass**: `AutoModel.from_pretrained("bert-base-uncased")` 한 줄로 로딩.
- **Pipeline API**: `pipeline("sentiment-analysis")(text)` 3줄로 추론.
- **Trainer**: 학습 루프 추상화 (분산·mixed precision 자동).
- **PyTorch / TensorFlow / JAX 동시 지원**.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **0샷 데모 즉시 가능** | 이미 학습된 모델로 시연 |
| **파인튜닝 표준** | LoRA, QLoRA, PEFT 통합 |
| **멀티모달 지원** | 이미지·음성·텍스트 모두 |

## 🚀 2. 10분 퀵스타트

```bash
pip install transformers torch
```

```python
from transformers import pipeline

# 감정 분석
clf = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
print(clf("I love PLAF guidebook!"))
# [{'label': 'POSITIVE', 'score': 0.999}]

# 한국어 → 영어 번역
ko2en = pipeline("translation", model="Helsinki-NLP/opus-mt-ko-en")
print(ko2en("안녕하세요, 반갑습니다."))
```

### 모델 직접 로딩
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

name = "bert-base-uncased"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForSequenceClassification.from_pretrained(name, num_labels=2)

inputs = tok("Hello PLAF", return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits
print(logits)
```

## 🛠️ 3. 코드 해부학

| 모듈 | 역할 |
|---|---|
| `transformers/models/` | 각 모델 아키텍처 (BERT, GPT, LLaMA 등) |
| `transformers/pipelines/` | 고수준 추론 API |
| `transformers/trainer.py` | 학습 루프 추상화 |
| `tokenizers` (별도 패키지) | Rust 기반 빠른 토크나이저 |

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think LLaMA 3 8B를 LoRA로 한국어 인스트럭션 데이터셋에 파인튜닝하려고 한다.
PEFT·bitsandbytes 4bit·Trainer 설정을 단계별로 작성해 줘.
GPU 메모리 24GB 가정.
```

### 🔵 Gemini
```
Hugging Face Hub에서 한국어 NLP 모델을 선택할 때 고려할 기준
(라이선스, 모델 크기, 벤치마크, 한국어 토크나이저)을 정리해 줘.
```

### 🟢 ChatGPT
```
"학내 공지사항 자동 분류" 프로젝트를 Transformers로 만들려고 한다.
데이터 수집·라벨링, 베이스라인 모델, 파인튜닝, 평가, 배포까지 4주 계획을 짜 줘.
```

### ⬛ Copilot
```python
# TODO: 한국어 텍스트 요약 파이프라인 - paust/pko-t5-base 사용
```

## 🔗 5. 관련 레포 · 다음 단계
- [PyTorch 딥다이브](../pytorch/index.md) (백엔드)
- [Diffusers](https://github.com/huggingface/diffusers) (이미지 생성)
- [PEFT](https://github.com/huggingface/peft) (파라미터 효율적 파인튜닝)
- [Datasets](https://github.com/huggingface/datasets)
