from django.shortcuts import render
from googletrans import Translator
import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

# 곰곰AI 페이지 접속 시
def ai_view(request):
    
    # 질문 받기
    question_ko = request.GET.get('question', '')
    
    # 번역기 객체 선언
    translator = Translator()
    
    # 질문이 있는 경우
    if len(str(question_ko)) >= 1:
        question_en = translator.translate(question_ko, src='ko', dest='en')
        response_en = ask_gpt(str(question_en.text))
        response_ko = translator.translate(response_en, src='en', dest='ko')
        print("답변 완료")
        # 답변이 포함된 페이지로 렌더링 해주기
        return render(request, 'ai_response.html', {'response' : response_ko.text})
    
    # 질문이 없는 경우
    else:
        # 답변이 포함 안된 페이지로 렌더링 해주기
        return render(request, 'ai.html') 
        

# 곰곰AI에게 질문 보내고 답변 받기
def ask_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def home_view(request):
    return render(request, 'home.html')