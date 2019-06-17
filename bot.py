from chatterbot import ChatBot

bot = ChatBot(
    "mybot",

    storage_adapter="chatterbot.storage.SQLStorageAdapter",

    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",

        },
        
    ],
    
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database="./myBot"

)

while True:
    your_input = input("Usuario: ")
    bot_output = bot.get_response(your_input)
    print(bot_output)

    