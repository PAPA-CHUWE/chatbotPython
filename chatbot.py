from chatterbot.conversation import Statement
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer 

chatbot=ChatBot('TERRENCIA')
trainer=ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

print("Hi,My name is : TERRENCIA, what's your name?")
while True:
    ask=input("\nAsk Anything :")
    print(chatbot.get_response(Statement(text=ask,search_text=ask)))