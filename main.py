from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from unidecode import unidecode
import random

TOKEN: Final = '6506340787:AAEwkynZgKaPQ6oIs7pvhALCvA-cK3eki_c'
BOT_USERNAME: Final = '@ghicitori_bot'

ghicitori = [
    {"intrebare": "Ce este mereu înainte, dar nu poate să prindă niciodată?", "raspuns": "Viitorul"},
    {"intrebare": "Ce are mereu chei, dar nu deschide nicio ușă?", "raspuns": "Pianul"},
    {"intrebare": "Ce are ochi, dar nu poate vedea?", "raspuns": "Acul"},
    {"intrebare": "Ce are două mâini, dar nu poate să apuce nimic?", "raspuns": "Ceasul"},
    {"intrebare": "Ce cuvânt este scris incorect în dicționar?", "raspuns": "Incorect"},
    {"intrebare": "Ce culoare are cutia neagra a avioanelor?", "raspuns": "Portocalie"},
    {"intrebare": "O pisică albă urcă în copac. Cum coboară?", "raspuns": "Albă"},
    {"intrebare": "Tata-l Mariei are 5 fete: Ana, Irina, Nina și Alina. Cum o cheamă pe a 5-a?", "raspuns": "Maria"},
    {"intrebare": "Ce s-a terminat in 1919", "raspuns": "1918"},
    {"intrebare": "Ce merge în sus şi în jos, dar nu se mişcă?", "raspuns": "Scara"},
    {"intrebare": "Ce îţi aparţine şi este folosit mai mult de alţii?", "raspuns": "Numele"},
    {"intrebare": "Într-un coş sunt patru mere galbene şi cinci roşii. Câte mere sunt în coş?", "raspuns": "4"},
    {"intrebare": "Un paznic de noapte moare in timpul zilei. Are dreptul la pensie?", "raspuns": "Mortii n-au pensie"},
    {"intrebare": "Sub ce copac se ascunde iepurele cand ploua?", "raspuns": "Ud"},
    {"intrebare": "Care este cea mai mare cifra?", "raspuns": "9"},
    {"intrebare": "Câte zile de naştere are un om de 33 de ani născut în luna februarie?", "raspuns": "1"},
    {"intrebare": "Cati ani ai avea daca te-ai nascut 10 ani in urma?", "raspuns": "10"},
    {"intrebare": "Jupâneasa durdulie\nCu rochița cenușie\nLucrată din pene lucii,\nCaută pe lac papucii.",
     "raspuns": "Gasca"},
    {"intrebare": "Într-un coş sunt patru mere galbene şi cinci roşii. Câte mere sunt în coş?", "raspuns": "4"},
    {"intrebare": "Poare fi un șoricel\nÎnsă are aripioare\nZboară noaptea-n chip și fel\nPurtând numele de floare.",
     "raspuns": "liliacul"},
    {"intrebare": "Are dânsul și picioare\nDar e-obișnuit să zboare;\nCine-i obraznicătura?", "raspuns": "tintarul"},
    {"intrebare": "În cojoc întors pe dos\nMormăind morocănos,\nUmblă pustnic prin pădure\nDupă miere, după mure.",
     "raspuns": "ursul"},
    {"intrebare": "Ce îi spune un perete altui perete?", "raspuns": "Ne intalnim la colt"},
    {"intrebare": "Mergeau soț și soție, frate și soră, cumnat și cumnată. Câți erau, de fapt?", "raspuns": "3"},
    {"intrebare": "Câte luni pe an au 28 de zile?", "raspuns": "Toate"},
    {"intrebare": "Ce nu poate fi mâncat la micul dejun?", "raspuns": "Pranzul si cina"},
    {"intrebare": "Nu-i pasăre şi totuşi zboară dacă-l ţii bine de sfoară.", "raspuns": "zmeul"},
    {"intrebare": "În bărcuțe stau culcați, laolaltă patru frați. Când îi simt în cozonac, mie cel mai mult îmi plac.",
     "raspuns": "Nuca"},
    {"intrebare": "În grădina lui Pandele, e un pom plin de mărgele. La culoare-s roșii toate, cu codițe împerecheate.",
     "raspuns": "Cirese"},
    {"intrebare": "Balon dezumflat, galben colorat, are mustăcioară și se cheamă?", "raspuns": "Para"},
    {"intrebare": "Ciucur verde sau roșcat, pe arac stă agățat. Cine este?", "raspuns": "Strugure"},
    {"intrebare": "Are zeci de ace groase, dar nu țese, nici nu coase. ", "raspuns": "Ariciul"},
    {"intrebare": "Roade oase, stă în cușcă, pe dușmanii săi îi mușcă.", "raspuns": "Cainele"},
    {"intrebare": "Ce obiect se udă în timp ce te usucă?", "raspuns": "prosop"},
    {"intrebare": "Nu-i pisică, nici motan. E dungat și roșcovan.", "raspuns": "Tigrul"},
    {"intrebare": "Și un an de mă privești, tot pe tine te zărești.", "raspuns": "oglinda"},
    {"intrebare": "Are roți, dar nu-i căruță. Are uși, dar nu-i căsuță. Se numește?", "raspuns": "masinuta"},
    {"intrebare": "Apar noaptea, fără să fie chemate, dispar dimineața, fără să fie furate.", "raspuns": "stelele"},
    {"intrebare": "Nu-l întrebi și îți răspunde cauți în jur și nu știi unde-i.", "raspuns": "ecoul"},
    {"intrebare": "Animal cu chip de om țopăie din pom în pom.", "raspuns": "maimuta"},
    {"intrebare": "Ce trece prin apă fără să se ude?", "raspuns": "luna"},
    {"intrebare": "Felinar cu trei culori i-ajută pe trecători.", "raspuns": "semaforul"},
    {"intrebare": "Cât este ziua de mare, se tot uită după soare.", "raspuns": "floarea soarelui"},
    {"intrebare": "N-are roți, n-are picioare mă duce iute la vale. Dar pe deal de voi urca trebuie s-o duc eu pe ea.",
     "raspuns": "Sania"},
    {"intrebare": "N-are gură, dar vorbește și deloc nu obosește. Și în fiecare zi îți spune tot ce se petrece-n lume.",
     "raspuns": "radioul"},
    {"intrebare": "Ce roată nu se mișcă atunci când o mașină virează la dreapta? ", "raspuns": "roata de rezerva"},
    {"intrebare": "Peste tot găsești în lume cinci frați cu același nume.", "raspuns": "Degetele"},
    {"intrebare": "De ce trag clopotele la biserică?", "raspuns": "De funie"},
    {"intrebare": "Cum numești o femeie care știe mereu unde este soțul ei?", "raspuns": "Vaduva"},
    {"intrebare": "Ce se întâmplă dacă o batistă roșie este înmuiată în Marea Neagră?", "raspuns": "Se va uda"},
    {"intrebare": "Un român care trăieşte în București poate fi înmormântat la New York?",
     "raspuns": "Nu, pentru ca traieste"},
    {"intrebare": "Nu e gheață, dar se topește, nu e barcă, dar plutește.", "raspuns": "Salariul"},
    {"intrebare": "Ce fel de pietre nu sunt în mare?", "raspuns": "uscate"},
    {"intrebare": "Ce se afla intre Pamant si Soare", "raspuns": "si"},
]

numar_total_ghicitori = len(ghicitori)
numar_ghicitori_corecte = 0

ghicitoare_curenta = None

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salut, sunt un bot de ghicitori făcut pentru a te pune la încercări 😁🤭')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Aceasta comanda este pentru a te ajuta!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

async def ghicitoare_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global ghicitoare_curenta
    ghicitoare_curenta = random.choice(ghicitori)
    await update.message.reply_text(ghicitoare_curenta["intrebare"])

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global ghicitoare_curenta, numar_ghicitori_corecte

    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    try:
        if "Urmatoarea" in text or "urmatoarea" in text:
            await ghicitoare_aleatoare(update)
        elif ghicitoare_curenta and unidecode(text.lower()) == unidecode(ghicitoare_curenta["raspuns"].casefold()):
            numar_ghicitori_corecte += 1
            await update.message.reply_text("EXCELENT!\nFelicitări, ai raspuns corect la ghicitoare 🎉🎉🎉")
            await ghicitoare_aleatoare(update)
        elif "/raspunsul" in text:
            await raspunsul_command(update)
        else:
            await update.message.reply_text("N-ai ghicit, mai încearcă 🤭")
    except Exception as e:
        print(f'Error handling message: {e}')

async def ghicitoare_aleatoare(update: Update):
    global ghicitoare_curenta
    ghicitoare_curenta = random.choice(ghicitori)
    await update.message.reply_text(ghicitoare_curenta["intrebare"])

async def statistica_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global numar_total_ghicitori, numar_ghicitori_corecte

    mesaj_statistica = (
        f"Statistica ghicitori:\n"
        f"Număr total de ghicitori: {numar_total_ghicitori}\n"
        f"Număr ghicitori corecte: {numar_ghicitori_corecte}"
    )

    await update.message.reply_text(mesaj_statistica)

async def raspunsul_command(update: Update):
    global ghicitoare_curenta

    if ghicitoare_curenta:
        await update.message.reply_text(f'Răspunsul la ghicitoare este: {ghicitoare_curenta["raspuns"]}')
    else:
        await update.message.reply_text('Nu există o ghicitoare în desfășurare momentan.')

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('ghicitoare', ghicitoare_command))
    app.add_handler(CommandHandler('statistica', statistica_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Verifică dacă funcția de tratare a erorilor a fost înregistrată anterior
    if 'error' not in [handler.callback for handler in app.error_handlers]:
        app.add_error_handler(error)

    print('Pooling...')
    app.run_polling(poll_interval=3)
