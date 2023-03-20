import random
import openai

OPENAI_KEY = "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"



class OpenAi:
    def Text(question):
        openai.api_key = random.choice(OPENAI_KEY)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Q: {question}\nA:",
            temperature=0,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response.choices[0].text

    def Photo(question):
        openai.api_key = random.choice(OPENAI_KEY)
        response = openai.Image.create(prompt=question, n=1, size="1024x1024")
        return response["data"][0]["url"]
