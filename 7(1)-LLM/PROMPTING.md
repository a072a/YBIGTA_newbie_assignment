
## 1. Prompting 방식별 정확도 비교

| Prompting 방식     | 0-shot | 3-shot | 5-shot |
|-------------------|--------|--------|--------|
| Direct Prompting  | 0.18   | 0.22   | 0.20   |
| CoT Prompting     | 0.74   | 0.60   | 0.66   |
| My Prompting      | 0.76   | 0.70   | 0.72   |

## 2. CoT Prompting 방식이 Direct Prompting보다 좋은 이유
Direct Prompting은 "문제-정답" 패턴으로 문제에 대한 정답을 곧바로 출력하는 방식입니다. 모델이 추론과정을 생략하고 과거 데이터를 기반에만 의존하여 답을 추측하는 경향이 있습니다.
CoT Prompting은 "문제-논리-정답" 패턴으로 문제를 단계적으로 사고하고 풀이과정을 서술하게 유도함으로써, 중간 추론을 통해 복잡한 문제에 대한 이해도를 증가시켜, 단순 암기 기반이 아닌 논리적 추론 기반의 답변을 생성합니다.

결과적으로 CoT의 방식은 논리적인 단계를 한 번 더 거치기 때문에 높은 Direct Prompting보다 높은 정확도와 일관된 논리전개를 가능하게 해줌으로 더 나은 성능을 보입니다.


## 3. My Prompting이 CoT Prompting 보다 좋은 이유
기존 CoT 방식의 한계: 기존 CoT 방식은 모델이 문제 해결 과정을 거치긴 하지만, 중간과정에서 발생한 오류를 스스로 점검하지 못하는 한계가 있습니다.
이러한 CoT Prompting의 한계를 극복하기 위해 문제 해결 후 스스로 검토(Self-Verification)하는 절차를 포함한 새로운 프롬프트 방식을 설계했습니다.

**사용된 프롬프트는 다음과 같은 5단계 접근을 모델에게 요구합니다:**

1. **READ CAREFULLY**: 문제를 정확히 읽고 주어진 정보와 요구사항을 파악
2. **PLAN**: 문제를 논리적인 단계로 분해하고 계획 수립
3. **SOLVE**: 각 단계를 체계적으로 해결
4. **VERIFY**: 계산 결과를 다시 문제에 대입하며 검산
5. **DOUBLE-CHECK**: 최종 답변이 논리적으로 타당한지 최종 확인

```python
prompt = """Instruction:
You are an expert mathematician. For each problem, follow this systematic approach:

1. READ CAREFULLY: Identify all given information and what is being asked
2. PLAN: Break down the problem into logical steps
3. SOLVE: Work through each step methodically
4. VERIFY: Check your work by plugging your answer back into the problem
5. DOUBLE-CHECK: Ensure your final answer makes logical sense

Always end with: Final Answer: #### [number]

Remember: If you make a mistake, identify it and correct it before giving the final answer.
"""
```


이러한 방식은 단순히 추론하는 것을 넘어, 모델이 스스로의 논리를 점검하도록 유도함으로써 성능을 향상시켰습니다.
실제로 정확도를 비교해보면 아래와 같은 결과로 CoT에 자기검토를 추가하면 더 좋은 성능을 보이는 것을 알 수 있습니다.
CoT Prompting (0-shot): 0.74 → My Prompting (0-shot): 0.76
CoT Prompting (3-shot): 0.60 → My Prompting (3-shot): 0.70
CoT Prompting (5-shot): 0.66 → My Prompting (5-shot): 0.72

