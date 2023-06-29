#Импортируем библиотеки
import telebot
from telebot import types
import Token
import cv2

#Чтобы работал код нужно передать токен бота, который находиться в файле под названием "Token"
bot = telebot.TeleBot(Token.APi_token)

#Запуск бота чтобы он ответил на команду "start"
@bot.message_handler(commands=['start'])
def start_message (message):
	file = open('Images/Picture.jpeg', 'rb') #Добавляем фото
	mess = f'Добро пожаловать  {message.from_user.first_name} в магазин "Brands.store.astana"'
	bot.send_photo(message.chat.id, file, caption=mess, reply_markup=markup_menu)

#Добавляем кнопки в меню, чтобы дальше работать с ботом
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
bth_tshirts = types.KeyboardButton('👕Футболки👚')
bth_Korzina = types.KeyboardButton('🛒Корзина🛒')
bth_help = types.KeyboardButton('🆘help🆘')
markup_menu.add(bth_tshirts, bth_Korzina, bth_help)

#Добавляем кнопки в сообщения
markup_inline_menu = types.InlineKeyboardMarkup(row_width=1)
bth_inline_tshir = types.InlineKeyboardButton('👕Футболки👚', callback_data='tshir')
bth_inline_Korzina = types.InlineKeyboardButton('🛒Корзина🛒', callback_data='Korzina')
bth_inline_help = types.InlineKeyboardButton('🆘help🆘', callback_data='help')

markup_inline_menu.add (bth_inline_tshir,bth_inline_Korzina, bth_inline_help)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_tshirts = types.InlineKeyboardMarkup(row_width=1)
bth_inline_man = types.InlineKeyboardButton('👕Мужские👕', callback_data='man')
bth_inline_woman = types.InlineKeyboardButton('👚Женские👚', callback_data='woman')
bth_in_back1 = types.InlineKeyboardButton('🔙Назад🔙', callback_data='back1')

markup_inline_tshirts.add(bth_inline_man, bth_inline_woman, bth_in_back1)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_korzina = types.InlineKeyboardMarkup(row_width=1)
bth_delivery = types.InlineKeyboardButton('🚗Способы доставки🚗', callback_data='delivery')
bth_payment = types.InlineKeyboardButton('💵Способы оплаты💵', callback_data='payment')

markup_inline_korzina.add(bth_delivery, bth_payment)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_help = types.InlineKeyboardMarkup(row_width=1)
bth_inline_help1 = types.InlineKeyboardButton('📞Контакты📞', callback_data='nomer')
bth_inline_help2 = types.InlineKeyboardButton('🔗Ссылка на Инстраграмм🔗', callback_data='inst')
bth_inline_help3 = types.InlineKeyboardButton('❌Сообщить об ошибке❌', callback_data='error')

markup_inline_help.add(bth_inline_help1,bth_inline_help2,bth_inline_help3)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_nomer = types.InlineKeyboardMarkup(row_width=1)
bth_inline_nomer1 = types.InlineKeyboardButton('📞+77476884024', callback_data='nomer1')
bth_inline_nomer2 = types.InlineKeyboardButton('📞+77078456814', callback_data='nomer2')

markup_inline_nomer.add(bth_inline_nomer1, bth_inline_nomer2)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_inst = types.InlineKeyboardMarkup()
bth_inline_inst = types.InlineKeyboardButton('🔗Инстаграм', url='https://instagram.com/brands.store.astana?igshid=YmMyMTA2M2Y=')

markup_inline_inst.add(bth_inline_inst)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_tg = types.InlineKeyboardMarkup()
bth_inline_tg = types.InlineKeyboardButton('🔧Написать техподдержку🔧', url='https://t.me/Estat1c')

markup_inline_tg.add(bth_inline_tg)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_gg = types.InlineKeyboardMarkup()
bth_inline_tshirt = types.InlineKeyboardButton('🔙Вернуться, чтобы посмотреть другие модели🔙', callback_data='tshirt')

markup_inline_gg.add (bth_inline_tshirt)


#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_delivery = types.InlineKeyboardMarkup(row_width=1)
bth_in_courier = types.InlineKeyboardButton('🚕Курьер🚕', callback_data='courier')
bth_in_pickup = types.InlineKeyboardButton('🚗Самовывоз🚗', callback_data='pickup')
bth_in_back2 = types.InlineKeyboardButton('🔙Назад🔙', callback_data='back2')

markup_inline_delivery.add(bth_in_courier, bth_in_pickup, bth_in_back2)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_location = types.InlineKeyboardMarkup()
bth_inline_loc = types.InlineKeyboardButton('🗺Локация🗺', requests_location=True)
bth_inline_back8 = types.InlineKeyboardButton('🔙Назад🔙', callback_data='back8')
markup_inline_location.add(bth_inline_loc, bth_inline_back8)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_payment = types.InlineKeyboardMarkup(row_width=1)
bth_in_cash = types.InlineKeyboardButton('💰Наличные💰', callback_data='cash')
bth_in_kaspi = types.InlineKeyboardButton('💳Kaspi💳', callback_data='kaspi')
bth_in_back3 = types.InlineKeyboardButton('🔙Назад🔙', callback_data='back3')

markup_inline_payment.add(bth_in_cash, bth_in_kaspi, bth_in_back3)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_man = types.InlineKeyboardMarkup(row_width=1)
bth_in_model = types.InlineKeyboardButton('Модели', callback_data='model')
bth_in_back = types.InlineKeyboardButton('🔙Назад🔙', callback_data='back')

markup_inline_man.add(bth_in_model, bth_in_back)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_woman = types.InlineKeyboardMarkup(row_width=1)
bth_ins_models = types.InlineKeyboardButton('Модели', callback_data='models')
bth_ins_backs = types.InlineKeyboardButton('🔙Назад🔙', callback_data='backs')

markup_inline_woman.add(bth_ins_models, bth_ins_backs)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_inModel = types.InlineKeyboardMarkup(row_width=2)
bth_in_model1 = types.InlineKeyboardButton('🟧  Модель 1 ', callback_data='model1')
bth_in_model2 = types.InlineKeyboardButton('⬜  Модель 2 ', callback_data='model2')
bth_in_model3 = types.InlineKeyboardButton('🟦  Модель 3 ', callback_data='model3')
bth_in_model4 = types.InlineKeyboardButton('⬛  Модель 4 ', callback_data='model4')
bth_in_model5 = types.InlineKeyboardButton('⬜  Модель 5 ', callback_data='model5')
bth_in_back6 = types.InlineKeyboardButton('🔙Назад🔙', callback_data='back6')

markup_inline_inModel.add(bth_in_model1, bth_in_model2, bth_in_model3, bth_in_model4, bth_in_model5, bth_in_back6 )

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_m1 = types.InlineKeyboardMarkup(row_width=1)
bth_s = types.InlineKeyboardButton('S-размер', callback_data='S')
bth_M = types.InlineKeyboardButton('M-размер', callback_data='M')
bth_L = types.InlineKeyboardButton('L-размер', callback_data='L')
bth_exit = types.InlineKeyboardButton(" Назад", callback_data='E')

markup_m1.add(bth_L, bth_M, bth_s, bth_exit)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_l1 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plus = types.InlineKeyboardButton('➕', callback_data='pl')
bth_inline_minus = types.InlineKeyboardButton('➖', callback_data='mi')
bth_inline_sum = types.InlineKeyboardButton(f'{counter}', callback_data='su')
bth_inline_back9 = types.InlineKeyboardButton(" Назад", callback_data='ex')

markup_m1_l1.add(bth_inline_minus, bth_inline_sum, bth_inline_plus, bth_inline_back9)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_m1 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_p = types.InlineKeyboardButton('➕', callback_data='pl2')
bth_inline_m = types.InlineKeyboardButton('➖', callback_data='mi2')
bth_inline_s = types.InlineKeyboardButton(f'{counter}', callback_data='su2')
bth_inline_ba = types.InlineKeyboardButton(" Назад", callback_data='ex2')

markup_m1_m1.add(bth_inline_m, bth_inline_s, bth_inline_p, bth_inline_ba)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_s1 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_pl = types.InlineKeyboardButton('➕', callback_data='pl3')
bth_inline_mi = types.InlineKeyboardButton('➖', callback_data='mi3')
bth_inline_su = types.InlineKeyboardButton(f'{counter}', callback_data='su3')
bth_inline_bac = types.InlineKeyboardButton(" Назад", callback_data='ex3')

markup_m1_s1.add(bth_inline_mi, bth_inline_su, bth_inline_pl, bth_inline_bac)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_m2 = types.InlineKeyboardMarkup(row_width=1)
bth_s2 = types.InlineKeyboardButton('S-размер', callback_data='S2')
bth_M2 = types.InlineKeyboardButton('M-размер', callback_data='M2')
bth_L2 = types.InlineKeyboardButton('L-размер', callback_data='L2')
bth_exit2 = types.InlineKeyboardButton(" Назад", callback_data='E2')

markup_m2.add(bth_L2, bth_M2, bth_s2, bth_exit2)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_l2 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plus2 = types.InlineKeyboardButton('➕', callback_data='pl4')
bth_inline_minus2 = types.InlineKeyboardButton('➖', callback_data='mi4')
bth_inline_sum2 = types.InlineKeyboardButton(f'{counter}', callback_data='su4')
bth_inline_back92 = types.InlineKeyboardButton(" Назад", callback_data='ex4')

markup_m1_l2.add(bth_inline_minus2, bth_inline_sum2, bth_inline_plus2,  bth_inline_back92)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_m2 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_p2 = types.InlineKeyboardButton('➕', callback_data='pl5')
bth_inline_m2 = types.InlineKeyboardButton('➖', callback_data='mi5')
bth_inline_s2 = types.InlineKeyboardButton(f'{counter}', callback_data='su5')
bth_inline_ba2 = types.InlineKeyboardButton(" Назад", callback_data='ex5')

markup_m1_m2.add(bth_inline_m2, bth_inline_s2, bth_inline_p2, bth_inline_ba2)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_s2 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_pl2 = types.InlineKeyboardButton('➕', callback_data='pl6')
bth_inline_mi2 = types.InlineKeyboardButton('➖', callback_data='mi6')
bth_inline_su2 = types.InlineKeyboardButton(f'{counter}', callback_data='su6')
bth_inline_bac2 = types.InlineKeyboardButton(" Назад", callback_data='ex6')

markup_m1_s2.add(bth_inline_mi2, bth_inline_su2, bth_inline_pl2, bth_inline_bac2)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_m3 = types.InlineKeyboardMarkup(row_width=1)
bth_s3 = types.InlineKeyboardButton('S-размер', callback_data='S3')
bth_M3 = types.InlineKeyboardButton('M-размер', callback_data='M3')
bth_L3 = types.InlineKeyboardButton('L-размер', callback_data='L3')
bth_exit3 = types.InlineKeyboardButton(" Назад", callback_data='E3')

markup_m3.add(bth_L3, bth_M3, bth_s3, bth_exit3)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_l3 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plus3 = types.InlineKeyboardButton('Нельзя добавить', callback_data='pl7')
bth_inline_minus3 = types.InlineKeyboardButton('➖', callback_data='mi7')
bth_inline_sum3 = types.InlineKeyboardButton(f'{counter}', callback_data='su7')
bth_inline_kor3 = types.InlineKeyboardButton('Нельзя добавить 🛒', callback_data='aadd7')
bth_inline_back93 = types.InlineKeyboardButton(" Назад", callback_data='ex7')

markup_m1_l3.add(bth_inline_minus3, bth_inline_sum3, bth_inline_plus3, bth_inline_kor3, bth_inline_back93)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_m3 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_p3 = types.InlineKeyboardButton('➕', callback_data='pl8')
bth_inline_m3 = types.InlineKeyboardButton('➖', callback_data='mi8')
bth_inline_s3 = types.InlineKeyboardButton(f'{counter}', callback_data='su8')
bth_inline_ba3 = types.InlineKeyboardButton(" Назад", callback_data='ex8')

markup_m1_m3.add(bth_inline_m3, bth_inline_s3, bth_inline_p3, bth_inline_ba3)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_s3 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_pl3 = types.InlineKeyboardButton('➕', callback_data='pl9')
bth_inline_mi3 = types.InlineKeyboardButton('➖', callback_data='mi9')
bth_inline_su3 = types.InlineKeyboardButton(f'{counter}', callback_data='su9')
bth_inline_bac3 = types.InlineKeyboardButton(" Назад", callback_data='ex9')

markup_m1_s3.add(bth_inline_mi3, bth_inline_su3, bth_inline_pl3, bth_inline_bac3)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_m4 = types.InlineKeyboardMarkup(row_width=1)
bth_s4 = types.InlineKeyboardButton('S-размер', callback_data='S4')
bth_M4 = types.InlineKeyboardButton('M-размер', callback_data='M4')
bth_L4 = types.InlineKeyboardButton('L-размер', callback_data='L4')
bth_exit4 = types.InlineKeyboardButton(" Назад", callback_data='E4')

markup_m4.add(bth_L4, bth_M4, bth_s4, bth_exit4)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_l4 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plus4 = types.InlineKeyboardButton('➕', callback_data='pl10')
bth_inline_minus4 = types.InlineKeyboardButton('➖', callback_data='mi10')
bth_inline_sum4 = types.InlineKeyboardButton(f'{counter}', callback_data='su10')
bth_inline_back94 = types.InlineKeyboardButton(" Назад", callback_data='ex10')

markup_m1_l4.add(bth_inline_minus4, bth_inline_sum4, bth_inline_plus4, bth_inline_back94)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_m4 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_p4 = types.InlineKeyboardButton('➕', callback_data='pl11')
bth_inline_m4 = types.InlineKeyboardButton('➖', callback_data='mi11')
bth_inline_s4 = types.InlineKeyboardButton(f'{counter}', callback_data='su11')
bth_inline_ba4 = types.InlineKeyboardButton(" Назад", callback_data='ex11')

markup_m1_m4.add(bth_inline_m4, bth_inline_s4, bth_inline_p4, bth_inline_ba4)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_s4 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_pl4 = types.InlineKeyboardButton('➕', callback_data='pl12')
bth_inline_mi4 = types.InlineKeyboardButton('➖', callback_data='mi12')
bth_inline_su4 = types.InlineKeyboardButton(f'{counter}', callback_data='su12')
bth_inline_bac4 = types.InlineKeyboardButton(" Назад", callback_data='ex12')

markup_m1_s4.add(bth_inline_mi4, bth_inline_su4, bth_inline_pl4, bth_inline_bac4)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_m5 = types.InlineKeyboardMarkup(row_width=1)
bth_s5 = types.InlineKeyboardButton('S-размер', callback_data='S5')
bth_M5 = types.InlineKeyboardButton('M-размер', callback_data='M5')
bth_L5 = types.InlineKeyboardButton('L-размер', callback_data='L5')
bth_exit5 = types.InlineKeyboardButton(" Назад", callback_data='E5')

markup_m5.add(bth_L5, bth_M5, bth_s5, bth_exit5)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_l5 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plus5 = types.InlineKeyboardButton('➕', callback_data='pl13')
bth_inline_minus5 = types.InlineKeyboardButton('➖', callback_data='mi13')
bth_inline_sum5 = types.InlineKeyboardButton(f'{counter}', callback_data='su13')
bth_inline_back95 = types.InlineKeyboardButton(" Назад", callback_data='ex13')

markup_m1_l5.add(bth_inline_minus5, bth_inline_sum5, bth_inline_plus5, bth_inline_back95)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_m5 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_p5 = types.InlineKeyboardButton('➕', callback_data='pl14')
bth_inline_m5 = types.InlineKeyboardButton('➖', callback_data='mi14')
bth_inline_s5 = types.InlineKeyboardButton(f'{counter}', callback_data='su14')
bth_inline_ba5 = types.InlineKeyboardButton(" Назад", callback_data='ex14')

markup_m1_m5.add(bth_inline_m5, bth_inline_s5, bth_inline_p5, bth_inline_ba5)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m1_s5 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_pl5 = types.InlineKeyboardButton('➕', callback_data='pl15')
bth_inline_mi5 = types.InlineKeyboardButton('➖', callback_data='mi15')
bth_inline_su5 = types.InlineKeyboardButton(f'{counter}', callback_data='su15')
bth_inline_bac5 = types.InlineKeyboardButton(" Назад", callback_data='ex15')

markup_m1_s5.add(bth_inline_mi5, bth_inline_su5, bth_inline_pl5, bth_inline_bac5)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_inModels5 = types.InlineKeyboardMarkup(row_width=2)
bth_in_models51 = types.InlineKeyboardButton('🟦  Модель 1 ', callback_data='models51')
bth_in_models52 = types.InlineKeyboardButton('🟪  Модель 2 ', callback_data='models52')
bth_in_models53 = types.InlineKeyboardButton('⬜  Модель 3 ', callback_data='models53')
bth_in_models54 = types.InlineKeyboardButton('⬛  Модель 4 ', callback_data='models54')
bth_in_models55 = types.InlineKeyboardButton('⬜  Модель 5 ', callback_data='models55')
bth_in_back7 = types.InlineKeyboardButton('🔙Назад🔙', callback_data='back7')

markup_inline_inModels5.add(bth_in_models51, bth_in_models52, bth_in_models53, bth_in_models54, bth_in_models55, bth_in_back7 )

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_m6 = types.InlineKeyboardMarkup(row_width=1)
bth_s6 = types.InlineKeyboardButton('S-размер', callback_data='S6')
bth_M6 = types.InlineKeyboardButton('M-размер', callback_data='M6')
bth_L6 = types.InlineKeyboardButton('L-размер', callback_data='L6')
bth_exit6 = types.InlineKeyboardButton(" Назад", callback_data='E6')

markup_m6.add(bth_L6, bth_M6, bth_s6, bth_exit6)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_l1 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plus6 = types.InlineKeyboardButton('Невозможно добавить', callback_data='p16')
bth_inline_minus6 = types.InlineKeyboardButton('➖', callback_data='mi16')
bth_inline_sum6 = types.InlineKeyboardButton(f'{counter}', callback_data='su16')
bth_inline_ko64 = types.InlineKeyboardButton('Нельзя добавить 🛒', callback_data='aadd64')
bth_inline_back96 = types.InlineKeyboardButton(" Назад", callback_data='ex16')

markup_m6_l1.add(bth_inline_minus6, bth_inline_sum6, bth_inline_plus6, bth_inline_ko64,bth_inline_back96)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_m6 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_p6 = types.InlineKeyboardButton('➕', callback_data='pl17')
bth_inline_m6 = types.InlineKeyboardButton('➖', callback_data='mi17')
bth_inline_s6 = types.InlineKeyboardButton(f'{counter}', callback_data='su17')
bth_inline_ba6 = types.InlineKeyboardButton(" Назад", callback_data='ex17')

markup_m6_m6.add(bth_inline_m6, bth_inline_s6, bth_inline_p6, bth_inline_ba6)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_s6 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_pl6 = types.InlineKeyboardButton('➕', callback_data='pl18')
bth_inline_mi6 = types.InlineKeyboardButton('➖', callback_data='mi18')
bth_inline_su6 = types.InlineKeyboardButton(f'{counter}', callback_data='su18')
bth_inline_bac6 = types.InlineKeyboardButton(" Назад", callback_data='ex18')

markup_m6_s6.add(bth_inline_mi6, bth_inline_su6, bth_inline_pl6, bth_inline_bac6)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_m7 = types.InlineKeyboardMarkup(row_width=1)
bth_s7 = types.InlineKeyboardButton('S-размер', callback_data='S7')
bth_M7 = types.InlineKeyboardButton('M-размер', callback_data='M7')
bth_L7 = types.InlineKeyboardButton('L-размер', callback_data='L7')
bth_exit7 = types.InlineKeyboardButton(" Назад", callback_data='E7')

markup_m7.add(bth_L7, bth_M7, bth_s7, bth_exit7)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_l2 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plus7 = types.InlineKeyboardButton('➕', callback_data='pl19')
bth_inline_minus7 = types.InlineKeyboardButton('➖', callback_data='mi19')
bth_inline_sum7 = types.InlineKeyboardButton(f'{counter}', callback_data='su19')
bth_inline_back97 = types.InlineKeyboardButton(" Назад", callback_data='ex19')

markup_m6_l2.add(bth_inline_minus7, bth_inline_sum7, bth_inline_plus7, bth_inline_back97)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_m7 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_p7 = types.InlineKeyboardButton('➕', callback_data='pl20')
bth_inline_m7 = types.InlineKeyboardButton('➖', callback_data='mi20')
bth_inline_s7 = types.InlineKeyboardButton(f'{counter}', callback_data='su20')
bth_inline_ba7 = types.InlineKeyboardButton(" Назад", callback_data='ex20')

markup_m6_m7.add(bth_inline_m7, bth_inline_s7, bth_inline_p7,  bth_inline_ba7)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_s7 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_pl7 = types.InlineKeyboardButton('➕', callback_data='pl21')
bth_inline_mi7 = types.InlineKeyboardButton('➖', callback_data='mi21')
bth_inline_su7 = types.InlineKeyboardButton(f'{counter}', callback_data='su21')
bth_inline_bac7 = types.InlineKeyboardButton(" Назад", callback_data='ex21')

markup_m6_s7.add(bth_inline_mi7, bth_inline_su7, bth_inline_pl7, bth_inline_bac7)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_m8 = types.InlineKeyboardMarkup(row_width=1)
bth_s8 = types.InlineKeyboardButton('S-размер', callback_data='S8')
bth_M8 = types.InlineKeyboardButton('M-размер', callback_data='M8')
bth_L8 = types.InlineKeyboardButton('L-размер', callback_data='L8')
bth_exit8 = types.InlineKeyboardButton(" Назад", callback_data='E8')

markup_m8.add(bth_L8, bth_M8, bth_s8, bth_exit8)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_l3 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plus8 = types.InlineKeyboardButton('➕', callback_data='pl22')
bth_inline_minus8 = types.InlineKeyboardButton('➖', callback_data='mi22')
bth_inline_sum8 = types.InlineKeyboardButton(f'{counter}', callback_data='su22')
bth_inline_back98 = types.InlineKeyboardButton(" Назад", callback_data='ex22')

markup_m6_l3.add(bth_inline_minus8, bth_inline_sum8, bth_inline_plus8, bth_inline_back98)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_m8 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_p8 = types.InlineKeyboardButton('➕', callback_data='pl23')
bth_inline_m8 = types.InlineKeyboardButton('➖', callback_data='mi23')
bth_inline_s8 = types.InlineKeyboardButton(f'{counter}', callback_data='su23')
bth_inline_ba8 = types.InlineKeyboardButton(" Назад", callback_data='ex23')

markup_m6_m8.add(bth_inline_m8, bth_inline_s8, bth_inline_p8, bth_inline_ba8)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_s8 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_pl8 = types.InlineKeyboardButton('➕', callback_data='pl24')
bth_inline_mi8 = types.InlineKeyboardButton('➖', callback_data='mi24')
bth_inline_su8 = types.InlineKeyboardButton(f'{counter}', callback_data='su24')
bth_inline_bac8 = types.InlineKeyboardButton(" Назад", callback_data='ex24')

markup_m6_s8.add(bth_inline_mi8, bth_inline_su8, bth_inline_pl8,  bth_inline_bac8)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_m9 = types.InlineKeyboardMarkup(row_width=1)
bth_s9 = types.InlineKeyboardButton('S-размер', callback_data='S9')
bth_M9 = types.InlineKeyboardButton('M-размер', callback_data='M9')
bth_L9 = types.InlineKeyboardButton('L-размер', callback_data='L9')
bth_exit9 = types.InlineKeyboardButton(" Назад", callback_data='E9')

markup_m9.add(bth_L9, bth_M9, bth_s9, bth_exit9)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_l4 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plus9 = types.InlineKeyboardButton('➕', callback_data='pl25')
bth_inline_minus9 = types.InlineKeyboardButton('➖', callback_data='mi25')
bth_inline_sum9 = types.InlineKeyboardButton(f'{counter}', callback_data='su25')
bth_inline_back99 = types.InlineKeyboardButton(" Назад", callback_data='ex25')

markup_m6_l4.add(bth_inline_minus9, bth_inline_sum9, bth_inline_plus9, bth_inline_back99)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_m9 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_p9 = types.InlineKeyboardButton('➕', callback_data='pl26')
bth_inline_m9 = types.InlineKeyboardButton('➖', callback_data='mi26')
bth_inline_s9 = types.InlineKeyboardButton(f'{counter}+1', callback_data='su26')
bth_inline_ba9 = types.InlineKeyboardButton(" Назад", callback_data='ex26')

markup_m6_m9.add(bth_inline_m9, bth_inline_s9, bth_inline_p9, bth_inline_ba9)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_s9 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_pl9 = types.InlineKeyboardButton('➕', callback_data='pl27')
bth_inline_mi9 = types.InlineKeyboardButton('➖', callback_data='mi27')
bth_inline_su9 = types.InlineKeyboardButton(f'{counter}', callback_data='su27')
bth_inline_bac9 = types.InlineKeyboardButton(" Назад", callback_data='ex27')

markup_m6_s9.add(bth_inline_mi9, bth_inline_su9, bth_inline_pl9, bth_inline_bac9)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_m10 = types.InlineKeyboardMarkup(row_width=1)
bth_s10 = types.InlineKeyboardButton('S-размер', callback_data='S10')
bth_M10 = types.InlineKeyboardButton('M-размер', callback_data='M10')
bth_L10 = types.InlineKeyboardButton('L-размер', callback_data='L10')
bth_exit10 = types.InlineKeyboardButton(" Назад", callback_data='E10')

markup_m10.add(bth_L10, bth_M10, bth_s10, bth_exit10)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_l5 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plus10 = types.InlineKeyboardButton('➕', callback_data='pl28')
bth_inline_minus10 = types.InlineKeyboardButton('➖', callback_data='mi28')
bth_inline_sum10 = types.InlineKeyboardButton(f'{counter}', callback_data='su28')
bth_inline_back910 = types.InlineKeyboardButton(" Назад", callback_data='ex28')

markup_m6_l5.add(bth_inline_minus10, bth_inline_sum10, bth_inline_plus10, bth_inline_back910)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_m10 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_p10 = types.InlineKeyboardButton('➕', callback_data='pl29')
bth_inline_m10 = types.InlineKeyboardButton('➖', callback_data='mi29')
bth_inline_s10 = types.InlineKeyboardButton(f'{counter}', callback_data='su29')
bth_inline_ba10 = types.InlineKeyboardButton(" Назад", callback_data='ex29')

markup_m6_m10.add(bth_inline_m10, bth_inline_s10, bth_inline_p10, bth_inline_ba10)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
counter = 0
markup_m6_s10 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_pl10 = types.InlineKeyboardButton('➕', callback_data='pl30')
bth_inline_mi10 = types.InlineKeyboardButton('➖', callback_data='mi30')
bth_inline_su10 = types.InlineKeyboardButton(f'{counter}', callback_data='su30')
bth_inline_bac10 = types.InlineKeyboardButton(" Назад", callback_data='ex30')

markup_m6_s10.add(bth_inline_mi10, bth_inline_su10, bth_inline_pl10, bth_inline_bac10)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_inline_kaspi2 = types.InlineKeyboardMarkup(row_width=1)
bth_in_kaspi1 = types.InlineKeyboardButton('📸QR-код📸', callback_data='Qr-код')
bth_in_kaspi2 = types.InlineKeyboardButton('🤳Перевод🤳', callback_data='transfer')
bth_in_back8 = types.InlineKeyboardButton('🔙Назад🔙', callback_data='back8')

markup_inline_kaspi2.add(bth_in_kaspi1, bth_in_kaspi2, bth_in_back8)

#################################################################################################################
#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_plus22 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plusq22 = types.InlineKeyboardButton('Невозможно добавить', callback_data='pl33')
bth_inline_minusq22 = types.InlineKeyboardButton('➖', callback_data='miq33')
bth_inline_sumq22 = types.InlineKeyboardButton(f'{counter+1}', callback_data='suq33')
bth_inline_korq22 = types.InlineKeyboardButton('Добавить в корзину', callback_data='aaddq33')
bth_inline_backq22 = types.InlineKeyboardButton(" Назад", callback_data='exq33')

markup_plus22.add(bth_inline_minusq22, bth_inline_sumq22,bth_inline_plusq22,bth_inline_korq22, bth_inline_backq22)

###################################################################
#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_plus228 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plusq228 = types.InlineKeyboardButton('Невозможно добавить', callback_data='pl338')
bth_inline_minusq228 = types.InlineKeyboardButton('➖', callback_data='miq338')
bth_inline_sumq228 = types.InlineKeyboardButton(f'{counter+1}', callback_data='suq338')
bth_inline_korq228 = types.InlineKeyboardButton('Добавить в корзину', callback_data='aaddq338')
bth_inline_backq228 = types.InlineKeyboardButton(" Назад", callback_data='exq338')

markup_plus228.add(bth_inline_minusq228, bth_inline_sumq228,bth_inline_plusq228,bth_inline_korq228, bth_inline_backq228)

################################################################################
#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_plus227 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plusq227 = types.InlineKeyboardButton('Невозможно добавить', callback_data='pl38')
bth_inline_minusq227 = types.InlineKeyboardButton('➖', callback_data='miq38')
bth_inline_sumq227 = types.InlineKeyboardButton(f'{counter+1}', callback_data='suq38')
bth_inline_korq227 = types.InlineKeyboardButton('Добавить в корзину', callback_data='aaddq38')
bth_inline_backq227 = types.InlineKeyboardButton(" Назад", callback_data='exq38')

markup_plus227.add(bth_inline_minusq227, bth_inline_sumq227,bth_inline_plusq227,bth_inline_korq227, bth_inline_backq227)

#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_minus22 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plusq222 = types.InlineKeyboardButton('➕', callback_data='pl33')
bth_inline_minusq222 = types.InlineKeyboardButton('➖', callback_data='miq33')
bth_inline_sumq222 = types.InlineKeyboardButton(f'{counter}', callback_data='suq33')
bth_inline_backq222 = types.InlineKeyboardButton(" Назад", callback_data='exq33')

markup_minus22.add(bth_inline_minusq222, bth_inline_sumq222,bth_inline_plusq222,bth_inline_backq222)

###################################################################
#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_minus228 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plusq229 = types.InlineKeyboardButton('➕', callback_data='pl338')
bth_inline_minusq229 = types.InlineKeyboardButton('➖', callback_data='miq338')
bth_inline_sumq229 = types.InlineKeyboardButton(f'{counter}', callback_data='suq338')
bth_inline_backq229 = types.InlineKeyboardButton(" Назад", callback_data='exq338')

markup_minus228.add(bth_inline_minusq229, bth_inline_sumq229,bth_inline_plusq229, bth_inline_backq229)

################################################################################
#Добавляем кнопки в сообщения, для дальнейшей работы с ботом
markup_minus235 = types.InlineKeyboardMarkup(row_width=3)
bth_inline_plusq235 = types.InlineKeyboardButton('➕', callback_data='pl38')
bth_inline_minusq235 = types.InlineKeyboardButton('➖', callback_data='miq38')
bth_inline_sumq235 = types.InlineKeyboardButton(f'{counter}', callback_data='suq38')
bth_inline_backq235 = types.InlineKeyboardButton(" Назад", callback_data='exq38')

markup_minus235.add(bth_inline_minusq235, bth_inline_sumq235,bth_inline_plusq235, bth_inline_backq235)

#Создаем функцию, чтобы кнопки работали
@bot.message_handler(content_types=['text'])
def message15 (message):
	if message.text == "👕Футболки👚":
		bot.reply_to(message, text="Выберите вид футболок:", reply_markup= markup_inline_tshirts)
	elif message.text == "🛒Корзина🛒":
		bot.reply_to(message, text="Ваша корзина:", reply_markup = markup_inline_korzina)
	elif message.text == "🆘help🆘":
		bot.reply_to(message, text = "Руководство:", reply_markup = markup_inline_help)


#Создаем функцию, чтобы кнопки работали
@bot.callback_query_handler(func=lambda call: True)
def call_back_payment(call):
	if call.data == 'delivery':
		bot.send_message(chat_id=call.message.chat.id,text='Выберите способ доставки', reply_markup=markup_inline_delivery)
	elif call.data == 'payment':
		bot.send_message(chat_id=call.message.chat.id, text= "Выберите способ оплаты", reply_markup=markup_inline_payment)
	elif call.data == 'courier':
		bot.send_message(chat_id=call.message.chat.id, text = "Пожалуйста, напишите адрес дома", reply_markup=markup_inline_location)
	elif call.data == 'pickup':
		bot.send_message(chat_id=call.message.chat.id, text = 'Товар можете забрать по адресу\n"Керей и Жанибек хандар 9"\nтеперь выберем способ оплаты ', reply_markup=markup_inline_payment)
	elif call.data == 'cash':
		bot.send_message(chat_id=call.message.chat.id, text = "Наличный способом можно оплать, только в момент доставки товара", reply_markup=markup_inline_gg)
	elif call.data == 'kaspi':
		bot.send_message(chat_id=call.message.chat.id, text = "Оплатить через kaspi можно qr-кодом или переводом ", reply_markup=markup_inline_kaspi2)
	elif call.data == 'tshirt':
		bot.send_message(chat_id=call.message.chat.id, text = "Выберите вид футболок:", reply_markup=markup_inline_tshirts)
	elif call.data == 'man':
		bot.send_message(chat_id=call.message.chat.id, text = "Выберите Мужские модели:", reply_markup=markup_inline_inModel)
	elif call.data == 'woman':
		bot.send_message(chat_id=call.message.chat.id, text="Выберите Женские модели", reply_markup=markup_inline_inModels5)
	elif call.data == 'model':
		bot.send_message(chat_id=call.message.chat.id, text = "Доступные модели:", reply_markup=markup_inline_inModel)
	elif call.data == 'models':
		bot.send_message(chat_id=call.message.chat.id, text = "Доступные модели:", reply_markup=markup_inline_inModels5)
	elif call.data == 'back':
		bot.send_message(chat_id=call.message.chat.id, text = "Выберите вид футболок:", reply_markup=markup_inline_tshirts)
	elif call.data == 'backs':
		bot.send_message(chat_id=call.message.chat.id, text="Выберите вид футболок:", reply_markup=markup_inline_tshirts)
	elif call.data == 'back1':
		bot.send_message(chat_id=call.message.chat.id, text="Что хотите сделать?", reply_markup=markup_inline_menu)
	elif call.data == 'back2':
		bot.send_message(chat_id=call.message.chat.id, text="Что хотите сделать?", reply_markup=markup_inline_menu)
	elif call.data == 'back3':
		bot.send_message(chat_id=call.message.chat.id, text="Что хотите сделать?", reply_markup=markup_inline_menu)
	elif call.data == 'back6':
		bot.send_message(chat_id=call.message.chat.id, text="Выберите вид футболок", reply_markup=markup_inline_tshirts)
	elif call.data == 'back7':
		bot.send_message(chat_id=call.message.chat.id, text="Выберите вид футболок", reply_markup=markup_inline_tshirts)
	elif call.data == 'back8':
		bot.send_message(chat_id=call.message.chat.id, text="Выбрать другой вид доставки", reply_markup=markup_inline_delivery)
	elif call.data == 'tshir':
		bot.send_message(chat_id=call.message.chat.id, text = "Выберите вид футболок:", reply_markup=markup_inline_tshirts)
	elif call.data == 'Korzina':
		bot.send_message(chat_id=call.message.chat.id, text="Ваша корзина:", reply_markup = markup_inline_korzina)
	elif call.data == 'nomer':
		bot.send_message(chat_id=call.message.chat.id, text="Номера техподдержки", reply_markup= markup_inline_nomer)
	elif call.data == 'inst':
		bot.send_message(chat_id=call.message.chat.id, text="Наш инстаграм", reply_markup= markup_inline_inst)
	elif call.data == 'error':
		bot.send_message(chat_id=call.message.chat.id, text="Техподдрежка", reply_markup= markup_inline_tg)
	elif call.data == 'model1':
		bot.send_photo(call.message.chat.id, open('Images/msg-1686004577-225.jpg', 'rb'), reply_markup=markup_m1)
	elif call.data == 'S':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1",reply_markup=markup_m1_s1)
	elif call.data == 'M':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m1_m1)
	elif call.data == 'L':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m1_l1)
	elif call.data == 'E':
		bot.send_message(chat_id=call.message.chat.id, text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'model2':
		bot.send_photo(call.message.chat.id, open('Images/msg-1686004577-226.jpg', 'rb'), reply_markup=markup_m2)
	elif call.data == 'S2':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1",reply_markup=markup_m1_s2)
	elif call.data == 'M2':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m1_m2)
	elif call.data == 'L2':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m1_l2)
	elif call.data == 'E2':
		bot.send_message(chat_id=call.message.chat.id, text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'model3':
		bot.send_photo(call.message.chat.id, open('Images/msg-1686004577-227.jpg', 'rb'), reply_markup=markup_m3)
	elif call.data == 'S3':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1",reply_markup=markup_m1_s3)
	elif call.data == 'M3':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m1_m3)
	elif call.data == 'L3':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m1_l3)
	elif call.data == 'E3':
		bot.send_message(chat_id=call.message.chat.id, text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'model4':
		bot.send_photo(call.message.chat.id, open('Images/msg-1686004577-228.jpg', 'rb'), reply_markup=markup_m4)
	elif call.data == 'S4':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1",reply_markup=markup_m1_s4)
	elif call.data == 'M4':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m1_m4)
	elif call.data == 'L4':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m1_l4)
	elif call.data == 'E4':
		bot.send_message(chat_id=call.message.chat.id, text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'model5':
		bot.send_photo(call.message.chat.id, open('Images/msg-1686004577-229.jpg', 'rb'), reply_markup=markup_m5)
	elif call.data == 'S5':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m1_s5)
	elif call.data == 'M5':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m1_m5)
	elif call.data == 'L5':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m1_l5)
	elif call.data == 'E5':
		bot.send_message(chat_id=call.message.chat.id, text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'models51':
		bot.send_photo(call.message.chat.id, open('Images/msg-1686004577-230.jpg', 'rb'), reply_markup=markup_m6)
	elif call.data == 'S6':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_s6)
	elif call.data == 'M6':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_m6)
	elif call.data == 'L6':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_l1)
	elif call.data == 'E6':
		bot.send_message(chat_id=call.message.chat.id, text="Посмотреть другую модель", reply_markup=markup_inline_inModels5)
	elif call.data == 'models52':
		bot.send_photo(call.message.chat.id, open('Images/msg-1686004577-231.jpg', 'rb'), reply_markup=markup_m7)
	elif call.data == 'S7':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_s7)
	elif call.data == 'M7':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_m7)
	elif call.data == 'L7':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_l2)
	elif call.data == 'E7':
		bot.send_message(chat_id=call.message.chat.id, text="Посмотреть другую модель", reply_markup=markup_inline_inModels5)
	elif call.data == 'models53':
		bot.send_photo(call.message.chat.id, open('Images/msg-1686004577-232.jpg', 'rb'), reply_markup=markup_m8)
	elif call.data == 'S8':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_s8)
	elif call.data == 'M8':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_m8)
	elif call.data == 'L8':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_l3)
	elif call.data == 'E8':
		bot.send_message(chat_id=call.message.chat.id, text="Посмотреть другую модель", reply_markup=markup_inline_inModels5)
	elif call.data == 'models54':
		bot.send_photo(call.message.chat.id, open('Images/msg-1686004577-233.jpg', 'rb'), reply_markup=markup_m9)
	elif call.data == 'S9':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_s9)
	elif call.data == 'M9':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_m9)
	elif call.data == 'L9':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_l4)
	elif call.data == 'E9':
		bot.send_message(chat_id=call.message.chat.id, text="Посмотреть другую модель", reply_markup=markup_inline_inModels5)
	elif call.data == 'models55':
		bot.send_photo(call.message.chat.id, open('Images/msg-1686004577-234.jpg', 'rb'), reply_markup=markup_m10)
	elif call.data == 'S10':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_s10)
	elif call.data == 'M10':
		bot.send_message(chat_id=call.message.chat.id, text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_m10)
	elif call.data == 'L10':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_m6_l5)
	elif call.data == 'E10':
		bot.send_message(chat_id=call.message.chat.id, text="Посмотреть другую модель", reply_markup=markup_inline_inModels5)
	elif call.data == 'pl3':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus22)
	elif call.data == 'pl6':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus22)
	elif call.data == 'pl9':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus22)
	elif call.data == 'pl12':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus22)
	elif call.data == 'pl15':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus22)
	elif call.data == 'pl18':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus22)
	elif call.data == 'pl21':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus22)
	elif call.data == 'pl24':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus22)
	elif call.data == 'pl27':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus22)
	elif call.data == 'pl30':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus22)
	elif call.data == 'pl2':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus228)
	elif call.data == 'pl5':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus228)
	elif call.data == 'pl8':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus228)
	elif call.data == 'pl11':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus228)
	elif call.data == 'pl14':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus228)
	elif call.data == 'pl17':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus228)
	elif call.data == 'pl20':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus228)
	elif call.data == 'pl23':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus228)
	elif call.data == 'pl26':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus228)
	elif call.data == 'pl29':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus228)
	elif call.data == 'pl':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus227)
	elif call.data == 'pl4':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus227)
	elif call.data == 'pl7':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus227)
	elif call.data == 'pl10':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus227)
	elif call.data == 'pl13':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus227)
	elif call.data == 'pl16':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus227)
	elif call.data == 'pl19':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus227)
	elif call.data == 'pl22':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus227)
	elif call.data == 'pl25':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus227)
	elif call.data == 'pl28':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:Нету в наличии\nк Оплате:13.990", reply_markup=markup_plus227)
	elif call.data == 'miq33':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_minus22)
	elif call.data == 'miq338':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_minus228)
	elif call.data == 'miq38':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_minus235)
	elif call.data == 'pl33':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-S \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_plus22)
	elif call.data == 'pl338':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-M \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_plus228)
	elif call.data == 'pl38':
		bot.send_message(chat_id=call.message.chat.id,text="Цена данной модели размера-L \n составляет 13.990 тг\n Количество товара:1", reply_markup=markup_plus227)
	elif call.data == 'exq33':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'exq338':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'exq38':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex1':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex2':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex3':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex4':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex5':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex6':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex7':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex8':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex9':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex10':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex11':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex12':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex13':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex14':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex15':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex16':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex17':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex18':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex19':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex20':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex21':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex22':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex23':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex24':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex25':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex26':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex27':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex28':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex29':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)
	elif call.data == 'ex30':
		bot.send_message(chat_id=call.message.chat.id,text="Посмотреть другую модель", reply_markup=markup_inline_inModel)










#Для того, чтобы бот работал пишем такую команду
bot.polling(non_stop=True)