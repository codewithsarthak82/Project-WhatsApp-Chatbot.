from openai import OpenAI

# Initialize OpenAI client with API key
client = OpenAI(
    api_key="""Enter your OpenAI API Key"""
)
command = '''
Enter some samples from your chap from the terminal after running the 01_main_bot.py file.
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
