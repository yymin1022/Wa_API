import google.generativeai as genai
import os

genai.configure(api_key = os.environ.get("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel(
    model_name = "gemini-1.5-flash-8b-latest",
    system_instruction = "당신은 대한민국의 초등학생입니다. 한국어 반말을 이용해서 대답을 해주면 됩니다. 하지만 답변의 진실 여부는 절대로 틀리면 안됩니다. 무조건 옳은 답변을 지정된 말투로 말해주세요."
)