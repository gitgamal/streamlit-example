import requests
import openai
openai.api_key = "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"
openai.organization = "org-XXX"
def get_web_results(query):
 response = requests.get(f"https://api.google.com/search?q={query}")
 data = response.json()
 results = data["items"]
 return results
def generate_response(prompt):
 completion = openai.ChatCompletion.create(
 model="gpt-3.5-turbo",
 messages=[
 {"role": "user", "content": prompt}
 ]
 )
 message = completion.choices[0].message.content.strip()
 return message
query = input("Enter your search query: ")
results = get_web_results(query)
prompt = f"What do you want to know about {query}? Here are the top web results:\n"
for result in results:
 prompt += f"- {result['title']}: {result['snippet']}\n"
response = generate_response(prompt)
print(response)
