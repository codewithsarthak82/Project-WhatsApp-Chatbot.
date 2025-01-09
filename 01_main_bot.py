# MEGAPROJECT 02 : CHATBOT ASSISTANT FOR WHATSAPP !

# Importing all of the important and needed libraries in our project:
import pyautogui
import pyperclip
import time
from openai import OpenAI 

# Client for OpenAI integration in our project:
client = OpenAI(
    api_key="""YOUR API KEY FROM OPENAI"""
)

# Clicking on the WhatsApp icon at (883, 745) on the taskbar:
pyautogui.click(487, 744)
time.sleep(2) 

# Drag from (442, 114) to (1338, 704) to select the text in whatsapp window:
pyautogui.moveTo(504, 165)
pyautogui.dragTo(1347, 696, duration=0.5, button='left')

# Copying the selected text to clipboard (Ctrl+C):
pyautogui.hotkey('ctrl', 'c')
time.sleep(1) 

# Deselcting the text by click at the given coordinate:
pyautogui.click(485,167)

# Retrieve the copied text from the clipboard into a variable names text_copied:
chat_History = pyperclip.paste()

# Printing the copied text from the whatsapp window:
print(chat_History)

# OPENAI WALA KAAM:
# Create a chat completion request

completion = client.chat.completions.create(
    model="chatgpt-4o-latest",
    messages=[
            {"role": "system", "content": "You are a person named Sarthak, who speaks hindi,english and hinglish. Who speaks very well and in a romantic manner. Sarthak is very calm and friendly person.Now you analyze chat history and speak respond like Sarthak.Ouput should be the next chat response(text messages only) as Sarthak.Write short responses."},
            {"role": "user", "content": chat_History}
        ]
        )

# Print the assistant's response and also copying in the variable:
response = completion.choices[0].message.content
pyperclip.copy(response)

# Clicking at the type something(response) bar with given coordinates:
pyautogui.click(625,732)
time.sleep(1)

# Pasting the text (response generated using OpenAI):
pyautogui.hotkey('ctrl','v')
time.sleep(1)

# Pressing Enter:
pyautogui.press('enter')

            