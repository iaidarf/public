import schedule
import telebot
import time, datetime
import xlrd
import os, random


token='...'
bot = telebot.TeleBot(token)
chat_id='...'


print("I'm working...")

def job():
    #открываем файл со списком имен и дат
    rb = xlrd.open_workbook('/mnt/hgfs/BD/dr.xls',formatting_info=True)
    #выбираем активный лист
    sheet = rb.sheet_by_index(0)
    #получаем список значений из всех записей
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    #массив для сохранения выбранных имен
    sp=[]
    #получаем текущий день и месяц
    dt_now = datetime.datetime.now().strftime("%d.%m")
    
    #выбор случайной картинки
    img_folder = "/mnt/hgfs/BD/images/"
    random_image = os.path.join(img_folder, random.choice(os.listdir(img_folder))) 
    
    for i in vals:
    	for j in i:
    	   if j == dt_now:
    	       sp.append(i[1])
    if len(sp) != 0:
    	print("C днем рождения!")
    	print(*sp, sep = ", ")
    	print(random_image)
    	sp_str = ', '.join(sp)
    	bot.send_message(chat_id, "C днем рождения, "+sp_str+"!")
    	bot.send_photo(chat_id, photo=open(random_image, 'rb'))
        
#schedule.every(5).seconds.do(job)
schedule.every().day.at("10:00").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

#запускаем бота
bot.polling()
