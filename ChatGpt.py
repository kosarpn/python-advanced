from openai import OpenAI

client = OpenAI(api_key=f"{import.meta.env.API_KEY}", base_url="https://api.gpt4-all.xyz/v1")

prompt = input("Enter Prompt:")

response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content":prompt}],
            stream=False,
        )

print(response.choices[0].message.content)