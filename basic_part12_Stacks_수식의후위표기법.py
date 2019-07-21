(12) 중위표현 수식 --> 후위표현 수식
중위 표기법을 따르는 수식 S 가 인자로 주어질 때, 이 수식을 후위 표기법을 따르는 수식으로 변환하여 
반환하는 함수 solution() 을 완성하세요.
인자로 주어지는 수식 문자열 S 는 영문 대문자 알파벳 한 글자로 이루어지는 변수 A - Z 까지와 4칙연산을 
나타내는 연산자 기호 +, -, *, /, 그리고 여는 괄호와 닫는 괄호 (, ) 로 이루어져 있으며 공백 문자는 
포함하지 않는 것으로 가정합니다. 
또한, 올바르게 구성되지 않은 수식은 인자로 주어지지 않는다고 가정합니다. (수식의 유효성은 검증할 필요가 없습니다.)
문제에서 미리 주어진, 연산자의 우선순위를 표현한 python dict 인 prec 을 활용할 수 있습니다.
또한, 스택의 기초 강의에서 이미 구현한, 배열을 이용한 스택의 추상적 자료 구조 코드가 이미 포함되어 
있으므로 그대로 이용할 수 있습니다.


class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    ans = ''
    for char in S:
        if char not in prec and char is not ')':
            ans += char
        elif char == '(':
            opStack.push(char)
        elif char == ')':
            while opStack.peek() != '(':
                    ans += opStack.pop()
            opStack.pop() # 스택에 있던 '(' 버리기
        else:
            if not opStack.isEmpty(): # 스택이 비어 있을 경우를 고려해야 함.
                if prec[opStack.peek()] >= prec[char]:
                    ans += opStack.pop()
            opStack.push(char)
            
    while not opStack.isEmpty():
        ans += opStack.pop()
        
    return ans
