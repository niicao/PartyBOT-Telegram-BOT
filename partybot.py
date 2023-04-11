import logging
from datetime import datetime
from pytz import timezone
import datetime
import pytz
from telegram import __version__ as TG_VER
import os


try:

    from telegram import __version_info__

except ImportError:

    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]


from telegram import (

    KeyboardButton,

    KeyboardButtonPollType,

    Poll,

    ReplyKeyboardMarkup,

    ReplyKeyboardRemove,

    Update,

)

from telegram.constants import ParseMode

from telegram.ext import (

    Application,

    CommandHandler,

    ContextTypes,

    MessageHandler,

    PollAnswerHandler,

    PollHandler,

    filters,

)


# Enable logging

logging.basicConfig(

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO

)

logger = logging.getLogger(__name__)



async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE):

    """Sends a predefined poll"""

    questions = ["Sim", "Nao"]
    event_name = " ".join(context.args)
    
    message = await context.bot.send_poll(

        update.effective_chat.id,

        event_name,

        questions,

        is_anonymous=False,

        allows_multiple_answers=False,

    )
    #Checking for old files

    BRT = pytz.timezone('America/Sao_Paulo')
    date1 = (datetime.datetime.strptime(str(message.date), "%Y-%m-%d %X%z"))
    date2 = datetime.datetime.today().strftime("%Y-%m-%d %X")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d %X")


    with open("resources/ID_index", "r+") as file_checker:
        file_checker.seek(0, os.SEEK_END)
        endOfFile = file_checker.tell() <= 1
        print(endOfFile)
        i = 0
        file_checker.seek(0, os.SEEK_SET)
        
        lista_horario_id = file_checker.readlines()
        while i < len(lista_horario_id) and not endOfFile:
            date1 = datetime.datetime.strptime(lista_horario_id[i], "%Y-%m-%d %X\n")
            time_diff = date2 - date1
            if time_diff.days > 30:
                delete_id = lista_horario_id[i + 1]
                delete_id = delete_id.strip()

                os.remove(delete_id)
                updateFile = open("resources/ID_index", "w+")

                for word in lista_horario_id:
                    if word != lista_horario_id[i] and word != lista_horario_id[i+1]:
                        updateFile.write(word)
                updateFile.truncate()
                print("Arquivo removido: "+ delete_id + "\n")
                i += 2

            else:
                i += 2
            updateFile.close()
            file_checker.close()


        




    
    date1 = date1.astimezone(BRT)
    date1 = date1.replace(tzinfo=None)
    date2 = date2.replace(tzinfo=None)

    file = open("resources/" + str(message.id), "w")
    
    file.write(event_name + "\n")

    file.close()

    file_index = open("resources/ID_index", "a")

    date_write = datetime.datetime.strptime(str(update.message.date.replace(tzinfo=None)), "%Y-%m-%d %X")

    file_index.write(str(date_write) + "\n" + str(message.id) + "\n")
    
    file_index.close()

    payload = {

        message.poll.id: {

            "questions": questions,

            "message_id": message.message_id,

            "chat_id": update.effective_chat.id,

            "answers": 0,

        }

    }

    context.bot_data.update(payload)


async def getupdate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text ='Nuh ' + update.message.reply_to_message.from_user.name + ', ai é inside demais')



async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:


    answer = update.poll_answer

    answered_poll = context.bot_data[answer.poll_id]
    

    if 0 in answer.option_ids:

        print(answered_poll.get("message_id"))
        file = open("resources/" + str(answered_poll.get("message_id")), "a")
        file.write(update.effective_user.full_name + " @"+update.effective_user.username + "\n")

        

    try:

        questions = answered_poll["questions"]


    except KeyError:

        return

    selected_options = answer.option_ids

    answer_string = ""

    for question_id in selected_options:

        if question_id != selected_options[0]:

            answer_string += questions[question_id] + " and "

        else:

            answer_string += questions[question_id]

    answered_poll["answers"] += 1

from telegram.ext import CommandHandler, Updater

async def reply_call_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open("resources/" +str(update.message.reply_to_message.message_id), "r")
    text = file.readlines()
    print_message = ""
    for i in range(0, len(text)):
        print_message += text[i].split("@")[0] + "\n"


    await context.bot.send_message(chat_id= update.effective_chat.id, text=print_message)


async def call_everyone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open("resources/" + str(update.message.reply_to_message.message_id), "r")
    list_names = file.readlines()

    for i in range(1, int(len(list_names)/4)):
        # 0*1 + 1  0*2 + 2... 1*4 + 1 1*4 + 2
        await context.bot.send_message(chat_id=update.effective_chat.id,
        text= "@" + list_names[i*4 + 1].partition("@") + "@" + list_names[i*4 + 2].partition("@") + "\n" + "@" + list_names[i*4 + 3].partition("@") + "\n" + "@" + list_names[i*4 + 4].partition("@") + "\n"
        )
    counter_for_last_names = len(list_names)%4 - 1
    msg_str = ""
    for j in range(len(list_names)-1, (len(list_names) - len(list_names)%4), -1):
        msg_str += "@" + list_names[j].partition("@")[-1] + "\n"
    await context.bot.send_message(chat_id=update.effective_chat.id,
        text=msg_str
        )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,

        text="Olá, os comandos do PartyCaller BOT são: \n/poll (ENQUETE) para criar uma enquete de SIM ou NAO\n\n/list ao responder uma mensagem para retornar todos os usuários que votaram SIM na enquete\n\n/inside para dizer que algo era inside demais!\n\n/everyone ao responder uma enquete para pingar todos os usuários que votaram X naquela mensagem, lembrando que o telegram só pinga 4 usuários por mensagem, logo o bot vai mandar múltiplas mensagens!\n\n Qualquer problema, contatar @Niicaoxd"       

        )



def main() -> None:


    application = Application.builder().token("6100414754:AAEHpcO0-wOJRIEro-969LphXCp-qH4oHr8").build()


    application.add_handler(CommandHandler("poll", poll))
    application.add_handler(CommandHandler("list", reply_call_list))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("everyone", call_everyone))
    

    application.add_handler(CommandHandler('inside', getupdate))

    application.add_handler(PollAnswerHandler(receive_poll_answer))
    application.run_polling()



if __name__ == "__main__":

    main()