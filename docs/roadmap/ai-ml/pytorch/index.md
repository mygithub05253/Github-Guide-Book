# 📘 PyTorch 딥다이브 실전 가이드

[![GitHub stars](https://img.shields.io/github/stars/pytorch/pytorch.svg?style=social)](https://github.com/pytorch/pytorch)

!!! info "레포지토리"
    **pytorch/pytorch** · 84k+ ⭐ · BSD-3 · [pytorch.org](https://pytorch.org)

---

## 🧐 1. PyTorch는 정확히 무엇이고, 실무에서 어떻게 쓰이나요?

**한 줄 요약**: PyTorch는 **Meta가 주도하는 Python 기반 딥러닝 프레임워크**입니다. NumPy처럼 직관적인 텐서 연산 + 자동 미분(`autograd`) + GPU 가속을 결합해 연구·산업 양쪽에서 사실상 표준입니다.

### 핵심 특성
- **동적 계산 그래프**: 코드 실행 중 그래프가 만들어짐 → Python의 if/for를 그대로 사용.
- **autograd**: `.backward()` 한 줄로 그래디언트 자동 계산.
- **CUDA 지원**: `.to('cuda')`로 GPU 사용.
- **에코시스템**: torchvision(이미지), torchaudio(오디오), torchtext, Hugging Face 호환.
- **TorchScript / ONNX**: 모델을 production에 배포하기 위한 직렬화.

### 실무 도입 포인트
| 도입 이유 | 효과 |
|---|---|
| **연구 논문 재현 1순위** | 거의 모든 SOTA 논문이 PyTorch 코드 공개 |
| **Hugging Face 통합** | Transformers·Diffusers의 기본 백엔드 |
| **디버깅 쉬움** | 동적 그래프 → `print()`, `pdb` 그대로 사용 |

## 🚀 2. 10분 퀵스타트

```bash
pip install torch torchvision
```

```python
import torch
import torch.nn as nn

# 1) 텐서
x = torch.tensor([[1., 2.], [3., 4.]], requires_grad=True)
y = (x * 2).sum()
y.backward()
print(x.grad)   # tensor([[2., 2.], [2., 2.]])

# 2) 미니 신경망
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
)

# 3) 학습 1 스텝
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

inputs = torch.randn(32, 784)
labels = torch.randint(0, 10, (32,))

logits = model(inputs)
loss = loss_fn(logits, labels)
optimizer.zero_grad()
loss.backward()
optimizer.step()
print("loss:", loss.item())
```

## 🛠️ 3. 코드 해부학

| 모듈 | 역할 |
|---|---|
| `torch` | 텐서, autograd, 옵티마이저 |
| `torch.nn` | 레이어·손실 함수 |
| `torch.utils.data` | Dataset·DataLoader (배치, 셔플, 병렬 로딩) |
| `torch.cuda` | GPU 관리 |
| `torch.distributed` | 멀티 GPU/노드 학습 |

## 🤖 4. AI 200% 활용 프롬프트 팩

### 🟠 Claude
```
/think 다음 PyTorch 학습 루프를 리뷰해 줘:
- optimizer.zero_grad() 위치
- loss 누적·평균 처리
- GPU 전송 누락
- mixed precision 적용 가능성
```

### 🔵 Gemini
```
PyTorch vs TensorFlow vs JAX를 2026년 기준 비교해 줘.
연구, 프로덕션 배포, 모바일, 학습 자원 측면에서.
```

### 🟢 ChatGPT
```
"손글씨 숫자 분류"를 PyTorch로 처음부터 끝까지 구현하는 학습 로드맵을 짜 줘.
MNIST 데이터, CNN 아키텍처, 학습 코드, 평가, 시각화 포함.
```

### ⬛ Copilot
```python
# TODO: ResNet18 기반 이미지 분류 학습 스크립트 (CIFAR-10)
```

## 🔗 5. 관련 레포 · 다음 단계
- [Transformers 딥다이브](../transformers/index.md)
- [PyTorch Lightning](https://github.com/Lightning-AI/pytorch-lightning) (학습 루프 추상화)
- 공식 튜토리얼: [pytorch.org/tutorials](https://pytorch.org/tutorials)
