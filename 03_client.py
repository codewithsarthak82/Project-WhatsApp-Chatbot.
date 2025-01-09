from openai import OpenAI

# Initialize OpenAI client with API key
client = OpenAI(
    api_key="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"
)
command = '''
[10:46 pm, 8/1/2025] Ruchi Di 💗: Kl kr lio try
[10:46 pm, 8/1/2025] Ruchi Di 💗: Pese h agar account m toh server issue hoga
[10:46 pm, 8/1/2025] Sarthak Dhiman: Okay ! mera project almost done ho rakha hai bss iski wajah se ruka hua hai ! 
[10:47 pm, 8/1/2025] Sarthak Dhiman: Nahi ye patani mastercard nhi leta maine yt video dekhin
[10:55 pm, 8/1/2025] Ruchi Di 💗: Usi m dalna
[10:55 pm, 8/1/2025] Sarthak Dhiman: Billing address kya dalun ?
[10:56 pm, 8/1/2025] Ruchi Di 💗: Gihm
'''
# Create a chat completion request
completion = client.chat.completions.create(
    model="chatgpt-4o-latest",
    messages=[
        {"role": "system", "content": "You are a person named Sarthak, who speaks hindi,english and hinglish. Who speaks very well and in a polite manner wiyh eveyone. Sarthak is very calm and friendly person.Now you analyze chat history and speak respond like Sarthak."},
        {"role": "user", "content": command}
    ]
)

# Print the assistant's response
print(completion.choices[0].message.content)
