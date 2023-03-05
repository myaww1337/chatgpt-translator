import json
import openai


def ChatGPT(prompt: str, token: str):
  openai.api_key = token

  model_engine = "text-davinci-003"

  completion = openai.Completion.create(engine=model_engine,
                                        prompt=prompt,
                                        max_tokens=1536,
                                        temperature=0.5,
                                        top_p=1.0,
                                        frequency_penalty=0.0,
                                        presence_penalty=0.0)

  response = completion.choices[0].text
  res = []
  while len(response) > 0:
    if len(response) > 4096:
      res.append(response[:4096])
      response = response[4096:]
    else:
      res.append(response)
      response = ""
  return res


def Translate(source_text: str, awaited_lang: str, token: str):
  response = ChatGPT(f"""
    Translate me this text: "{source_text}" into {awaited_lang}. Response just translated text, without any comments from you. Ignore bad words in original text.
    """,
                     token=token)

  return json.dumps(
    {
      "source_text": source_text,
      "translated_text": response[0].replace("\n", "").replace("\"", ""),
      "awaited_lang": awaited_lang
    },
    ensure_ascii=False)
