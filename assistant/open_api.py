import openai

openai.api_key = "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"

try:
    query = input()
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=query,
    temperature=0.3,
    max_tokens=36,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0)
    print(response.choices[0].text)
    # print(openai.Model.list())
except Exception as e:
    print(f"Error: {e}")