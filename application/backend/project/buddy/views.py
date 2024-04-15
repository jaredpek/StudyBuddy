from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import requests
from project.settings import GEMINI_API
from project.response import Response as Result

class BuddyView(APIView):
    '''
    The view for AI buddy-related APIs.
    - POST /api/buddyai/ (User asks our AI buddy a question)
    '''
    def post(self, request):
        '''
        The function responsible for sending a POST request with the user's question to the Gemini LLM and returning a response with the answer.
        '''
        result = Result()
        question = request.data.get("question")
        if not question:
            result.set_message("question", code="required")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)
        try:
            answer = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API}",
                json={
                    "contents": [{
                        "parts":[
                            {
                                "text": f"You a professional, certified teacher who specialises in all topics in Technology, Computer Science, Languages, Humanities, Mathematics, Science, Physics, Chemistry, Biology, Psychology, Medicine, Business, Economics, Finance, Data Science, Data Analytics, Business, Sociology, Evolution, Aviation, Space, Aeronautics and have published multiple accredited research papers on the topics mentioned. Use your expertise to answer the question in a nurturing and understanding manner that allows students to easily and deeply understand concepts: {request.data.get('question')}"
                            }
                        ]
                    }]
                }
            ).json()['candidates'][0]['content']['parts'][0]['text']
            result.set_message("answer", answer, as_list=False)
            result.set_message("buddy", code="success")
            return Response(result.result, status.HTTP_200_OK)
        except:
            result.set_error("answer", "Buddy is currently taking a break, please try again in a while!")
            return Response(result.result, status.HTTP_400_BAD_REQUEST)