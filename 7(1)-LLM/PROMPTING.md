
## 1. Prompting 방식별 정확도 비교

| Prompting 방식     | 0-shot | 3-shot | 5-shot |
|-------------------|--------|--------|--------|
| Direct Prompting  | 0.18   | 0.22   | 0.20   |
| CoT Prompting     | 0.74   | 0.60   | 0.66   |
| My Prompting      | 0.76   | 0.70   | 0.72   |

## 2. CoT Prompting 방식이 Direct Prompting보다 좋은 이유
### Direct Prompting은 "문제-정답" 패턴으로 문제에 대한 정답을 곧바로 출력하는 방식이다. 모델이 추론과정을 생략하고 과거 데이터를 기반에만 의존하여 답을 추측하는 경향이 있음.
### CoT Prompting은 "문제-논리-정답" 패턴으로 문제를 단계적으로 사고하고 풀이과정을 서술하게 유도함으로써, 중간 추론을 통해 복잡한 문제에 대한 이해도를 증가시켜, 단순 암기 기반이 아닌 논리적 추론 기반의 답변을 생성함.
### 결과적으로 CoT의 방식은 논리적인 단계를 한 번 더 거치기 때문에 높은 Direct Prompting보다 높은 정확도와 일관된 논리전개를 가능하게 해줌으로 더 나은 성능을 보임.


## 3. My Prompting이 CoT Prompting 보다 좋은 이유
### 기존 CoT 방식의 한계: 기존 CoT 방식은 모델이 문제 해결 과정을 거치긴 하지만, 중간과정에서 발생한 오류를 스스로 점검하거나 하는 한계가 있다.
### 구현한 Prompt는 이러한 한계를 보완하기 위해 CoT Prompting의 문제 해결 과정에 ‘자기검토(self-verification)’ 단계를 포함한 방식임. 전체 구조는 ‘문제 - 논리 - 검토 - 정답’의 형태를 따름.
 ### 따라서 모델이 한 번 문제 해결과정을 거친 이후 자신이 쓴 답변에 대해 ‘Verify’ 및 ‘Double-check’ 과정을 거쳐 정확도 향상, 논리적 일관성을 유지하여 CoT에 비해 좋은 성능을 보임.
 ### 실제로 정확도를 비교해보면 아래와 같은 결과로 CoT에 자기검토를 추가하면 더 좋은 성능을 보이는 것을 알 수 있다. 
### CoT Prompting (0-shot): 0.74 → My Prompting (0-shot): 0.76
### CoT Prompting (3-shot): 0.60 → My Prompting (3-shot): 0.70
### CoT Prompting (5-shot): 0.66 → My Prompting (5-shot): 0.72




