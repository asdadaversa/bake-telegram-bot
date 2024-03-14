from openai import OpenAI
import logging


client = OpenAI(api_key="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")


def generate_openai_tekst(vopros: str):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{vopros}"}
      ]
    )
    return completion.choices[0].message.content


def generate_image(prompt: str, n=1, size="1024x1024") -> str:

    pes = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      n=n,
      size="1024x1024"
    )

    return pes.data[0].url
