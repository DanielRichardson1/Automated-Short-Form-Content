import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI()


def getImageScript(source_material):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a YouTube short narration generator"
            },
            {
                "role": "user",
                "content":
                    f"For every main idea of this source material, create an prompt that will be given to DALLE-3"
                    f"To create the background images for our YouTube short"
                    f"\n\n{source_material}"
            }
        ]
    )
    return response.choices[0].message.content
