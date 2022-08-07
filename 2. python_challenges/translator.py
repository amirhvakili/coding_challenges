from googletrans import Translator

# init the Google API translator
translator = Translator()

with open('./2. python_challenges/translation_text.txt', mode='r') as file:
    data = file.read()
    translation = translator.translate(data)

print(translation)
