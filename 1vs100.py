# -*- encoding: utf-8 -*-
# ----------------------------------------------------------------------------
# 1 vs. 100
# Copyright © 2021 Sergey Chernov aka Gamer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------
import tkinter as tk
import tkinter.ttk
import codecs
from PIL import Image, ImageTk, ImageDraw, ImageFont
from enum import Enum
from tkinter import messagebox as mb
from random import randint, uniform

root=tk.Tk()
root.geometry("1024x768")
panels = []
playerz = []
images = []
ask_v = []
tysk = []
odpowiedzi = []
help = [True, True, True]
cost = [1000, 1000, 1000, 2000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
costq = None
diff = [0.0, 2.0, 3.5]
#font = ImageFont.truetype("font/2380.ttf", size = 26)
currentq = 0
number_inbase = None
vyluchenyi = None
hero_answer = None
muyt = 0
ar_atsakymas_yra_teisingas = None
error_count = 0
money_count = 0
prachy = 0
error_show = None
money_show = None
left_wrong = 0
number = 0
log = codecs.open('log.txt', 'a', "utf_8_sig")
#
_1vs = Image.open("img/1vs_.png")
_1vs.thumbnail((100, 150), Image.ANTIALIAS)
#draw_text = ImageDraw.Draw(_1vs)
kiek_priesu = ImageTk.PhotoImage(_1vs)
_1_vs_howmany = tk.Label(image = kiek_priesu)
#draw_text.text((100, 40), '111', font=font, fill="#CCCCCC")

# def Vienas_pries(b):
#     global draw_text, font, _1vs
#     draw_text = ImageDraw.Draw(_1vs)
#     draw_text.text((100, 40), '88', font=font, fill="#FFFF7F")

vylet = Image.open("img/vylet.png")
vylet.thumbnail((200, 40), Image.ANTIALIAS)
howmany_wrong = ImageTk.PhotoImage(vylet)
klaidingai_atsake_zaidejai = tk.Label(image = howmany_wrong)


#Vienas_pries(89)


class PlayerState(Enum):
    blue = 0
    yellow = 1
    red = 2
    black = 3

class q_stage(Enum):
    default = 0
    poll = 1
    ask = 2
    trust = 3
    accepted = 4

stadiya = q_stage.default
#s = tkinter.ttk.Style()
#s.configure('TFrame', background = "#ff7fff")
pl = tkinter.ttk.Style()
pl.configure('asj.TFrame', background = "#ffffff")
#
# def fac(i):
#     if i==0:
#         return 1
#     return fac(i-1)*i
# po = Image.open("img/yellow.png")
# po.thumbnail((25, 50), Image.ANTIALIAS)
# lm = ImageTk.PhotoImage(po)

def doSomething():
    if tk.messagebox.askyesno("Exit", "Do you want to quit the application?"):
        log.close()
        root.destroy()

STANDARD = Image.open("img/blue.png")
STANDARD.thumbnail((25, 50), Image.ANTIALIAS)
blue = ImageTk.PhotoImage(STANDARD)

LIFELINE = Image.open("img/yellow.png")
LIFELINE.thumbnail((25, 50), Image.ANTIALIAS)
yellow = ImageTk.PhotoImage(LIFELINE)

WRONG = Image.open("img/red.png")
WRONG.thumbnail((25, 50), Image.ANTIALIAS)
red = ImageTk.PhotoImage(WRONG)

ELIM = Image.open("img/black.png")
ELIM.thumbnail((25, 50), Image.ANTIALIAS)
black = ImageTk.PhotoImage(ELIM)

#domanda_text = tk.Label

place = [0, 10, 22, 36, 52, 68, 84, 100]
nachalo = [4, 3, 2, 1, 1, 1, 1]
#
# def UJ(event, k):
#     root.title(str(k))
#     if panels[k]['style'] == "TFrame":
#         panels[k]['style'] = "asj.TFrame"
#     elif panels[k]['style'] == "asj.TFrame":
#         panels[k]['style'] = "TFrame"
def ask_a_player(pol_igroka, uver):
    if uver==0:
        if pol_igroka == "M":
            return "Я уверен в правильности ответа "
        else:
            return "Я уверена в правильности ответа "
    elif uver==1:
        if pol_igroka == "M":
            return "Я сомневался, но ответил "
        else:
            return "Я сомневалась, но ответила "
    else:
        if pol_igroka == "M":
            return "Я не знаю ответа и наугад выбрал вариант "
        else:
            return "Я не знаю ответа и наугад выбрала вариант "

def igroki(event, k):
    global playerz, yellow, red, blue, black, stadiya, pl, OPV, PlayerState, help, otv, count
    count = 0
    if (stadiya ==q_stage.poll) and (pl[k]['PlayerState'] == PlayerState.yellow):
        stadiya = q_stage.default
        help[0] = False
        life_show()
        mb.showinfo(pl[k]['Name'], ask_a_player(pl[k]["Sex"], pl[k]["WhatWillSay"])+buchstabe(pl[k]["Answer"]))
        for a in range(OPV):
            if(pl[a]["Active"]):
                playerz[a]["image"]=blue
                pl[a]['PlayerState'] = PlayerState.blue
        acc_rev()
    elif (stadiya==q_stage.ask) and (pl[k]['PlayerState'] == PlayerState.yellow):
        count = 0
        mb.showinfo(pl[k]['Name'], ask_a_player(pl[k]["Sex"], pl[k]["WhatWillSay"])+buchstabe(pl[k]["Answer"]))
        pl[k]['PlayerState'] = PlayerState.blue
        playerz[k]['image'] = blue
        for a in range(OPV):
            if pl[a]['PlayerState'] == PlayerState.yellow:
                count+=1
        if (count==0):
            stadiya = q_stage.default
            life_show()
            acc_rev()

    # if(pl[k]["PlayerState"] == PlayerState.yellow):
    #     print(k+1)
    #     pl[k]["PlayerState"] = PlayerState.blue
    #     playerz[k]["image"] = blue

from random import randint
TOTAL = 50
subj = ["Математика", "Общественные науки", "Естественные науки", "Гуманитарные", "Филологические"]
l = [0, 1, 2, 3, 4]
um = [0] * 5

# for a in range (5):
#     while True:
#         i = randint(0, 4)
#         if i in l:
#             break
#     b = l.index(i)
#     while True:
#         pg = randint (1, 20)
#         if ((a<4) and (TOTAL-pg>=(4-a))) or ((a==4) and (TOTAL-pg>=0)):
#             break
#     um[i] = pg
#     TOTAL -=pg
#     l.pop(b)
#
# print(sum(um))
# print(um)

OPV = 100
skolko = 0
pl = []
mnames = []
fnames = []
masc = codecs.open ('mn.txt', 'r', "utf_8_sig")
for line in masc:
    HUH = line.rstrip("\n")
    mnames.append(HUH)
masc.close()
fem = codecs.open ('wn.txt', 'r', "utf_8_sig")
for line in fem:
    HUH = line.rstrip("\n")
    fnames.append(HUH)
fem.close()



for a in range (OPV):
    x = {}
    o = randint(0, 1)
    if (o==0):
        x["Sex"] = "M"
        x["Name"] = mnames[randint(0, len(mnames)-1)]
    else:
        x["Sex"] = "F"
        x["Name"] = fnames[randint(0, len(fnames)-1)]
    TOTAL = 50
    subj = ["Math", "Social", "Natural", "Humanitarian", "Philology"]
    disciplines = [0] * len(subj)
    indices = []
    for aux in range(len(subj)):
        indices.append(aux)
    um = [0] * len(subj)
    for aq in range(len(subj)):
        while True:
            i = randint(0, len(subj)-1)
            if i in indices:
                break
        b = indices.index(i)
        while True:
            p = randint(1, 20)
            if ((aq < len(subj)-1) and (TOTAL - p >= (len(subj)-1 - aq))) or ((aq == len(subj)-1) and (TOTAL - p >= 0)):
                break
        um[i] = p
        TOTAL -= p
        indices.pop(b)
    x["Knowledge"] = um
    mana = randint(0, 20)
    x["Luck"] = mana
    x["Answer"] = 0
    x["Sure"] = 0
    x["WhatWillSay"] = 0
    x["Active"] = True
    x["PlayerState"] = PlayerState.blue
    pl.append(x)

# for a in range (6):
#     global a1
#     l = tkinter.ttk.Frame(root, width=60, height = 40, style="TFrame")
#     panels.append(l)
#     panels[a].place(x=50, y = 110*a)
#     panels[a].bind("<Button-1>", lambda event, a1=a: UJ(event, a1))


for a in range(OPV):

    images.append(blue)



    mj = tk.Label(image = images[a])
    playerz.append(mj)
    klo = -1
    while True:
        klo+=1
        if (a<place[klo]):
            break
    if (klo==1):
        playerz[a].place(x=20+33*(a+4), y=400-60*(klo-1))
    else:
        playerz[a].place(x=20+33*(nachalo[klo-1]+(a-place[klo-1])), y = 400-60*(klo-1))
    #playerz[a].place(x=15+30*, y=25)
    playerz[a].bind("<Button-1>", lambda event, h=a: igroki(event, h))



# q_b = open("baza2.txt", "r")
# baza = []
q_b = codecs.open("baza2.txt", "r", "utf_8_sig")
baza = []
i = {}
for line in q_b:
    i = {}
    teh_answrs = ""
    u = []
    i["Cathegory"] = line.rstrip('\n')
    i['Cathegory'] = int(i['Cathegory'])
    i["Level"] = q_b.readline()
    i["Level"]= i["Level"].rstrip('\n')
    i['Level'] = int(i['Level'])
    i["Difficulty"] = q_b.readline()
    i["Difficulty"]= i["Difficulty"].rstrip('\n')
    i['Difficulty'] = float(i['Difficulty'])
    o = q_b.readline()
    o = o.rstrip('\n')
    if int(o) == 0:
        i['Trick'] = False
    else:
        i['Trick'] = True
    i["Question"] = q_b.readline()
    i["Question"]= i["Question"].rstrip('\n')
    for sa in range (3):
        h = q_b.readline()
        h = h.rstrip('\n')
        u.append(h)
    i["Variants"] = u
    i["Correct"] = q_b.readline()
    i["Correct"] = i["Correct"].rstrip('\n')
    i["Correct"] = int (i["Correct"])-1
    baza.append(i)
    # i["Cathegory"] = int(u[0])
    # i["Level"] = (u[1])
    # i["Difficulty"] = u[2]
    # if u[3]==0:
    #     i["Trick"] = False
    # else:
    #     i["Trick"] = True
    # i["var"] = []
    # i["Question"] = line.rstrip('\n')
    # for g in range(3):
    #     teh_answrs = line.rstrip('\n')
    #     i["var"].append(teh_answrs)
    # i["corr"] = int(line)

    # i = {}
#print (baza)
q_b.close()

# for line in q_b:
#     i = {}
#     teh_answrs = ""
#     i["Cathegory"] = int(q_b.readline())
#     i["Difficulty"] = float(q_b.readline())
#     l = int(q_b.readline())
#     if (l == 0):
#         i["Trick"] = False
#     else:
#         i["Trick"] = True
#     i["Question"] = q_b.readline()
#     i["Question"] = i["Question"].rstrip("\n")
#     i["Variants"] = []
#     for a in range (3):
#         teh_answrs = q_b.readline()
#         teh_answrs = teh_answrs.rstrip("\n")
#         i["Variants"].append(teh_answrs)
#     i["Correct"] = int(q_b.readline())-1
#     baza.append(i)
# i = None
# q_b.close()
def life_hide():
    global poll_the_mob, ask_the_mob, trust_the_mob
    poll_the_mob.place_forget()
    ask_the_mob.place_forget()
    trust_the_mob.place_forget()

def life_show():
    global poll_the_mob, ask_the_mob, trust_the_mob
    poll_the_mob.place(x=900, y=400)
    ask_the_mob.place(x=900, y=445)
    trust_the_mob.place(x=900, y=490)

def poll():#версия одного, написать
    global stadiya
    stadiya = q_stage.poll
    mb.showinfo("Выберите ответ")
    poll_the_mob["state"] = "disabled"
    life_hide()
    #acc()


def ask():#версия двух, написать
    global stadiya, number, otv, baza, number_inbase, pl, ask_v, tysk, odpowiedzi, yg, ask_the_mob, vyluchenyi, help
    if (stadiya == q_stage.default):
        ask_the_mob["state"] = 'disabled'
        life_hide()
        number = 0
        for k in range(OPV):
            if pl[k]["Active"]:
                number+=1
        if (otv[baza[number_inbase]["Correct"]] in [0, number]):
            mb.showinfo("Недоступно", "Мы не можем предоставить вам Версию двух, поскольку все игроки единого мнения."+"\n"+"Но один неверный ответ уберём")
            while True:
                yg = randint(0, 2)
                if yg != (baza[number_inbase]["Correct"]):
                    break
            tysk[yg].place_forget()
            odpowiedzi[yg].place_forget()
            vyluchenyi = yg
        else:
            stadiya = q_stage.ask
            while True:
                lp = randint(1, OPV)
                if (pl[lp-1]["Answer"]) == (baza[number_inbase]["Correct"]) and (pl[lp-1]["Active"]):
                    break
            pl[lp-1]["PlayerState"] = PlayerState.yellow
            playerz[lp-1]["image"] = yellow
            ask_v.append(pl[lp-1]["Answer"])
            while True:
                lp = randint(1, OPV)
                if (pl[lp-1]["Answer"]) != (baza[number_inbase]["Correct"]) and (pl[lp-1]["Active"]):
                    break
            pl[lp-1]["PlayerState"] = PlayerState.yellow
            playerz[lp-1]["image"] = yellow
            ask_v.append(pl[lp - 1]["Answer"])
            while True:
                yg = randint(0, 2)
                if (yg not in ask_v):
                    break
            tysk[yg].place_forget()
            odpowiedzi[yg].place_forget()
            vyluchenyi = yg
        log.write('Игрок берёт Версию двух. Исключается вариант '+buchstabe(yg)+'\n')
        help[1]=False
        life_show()

def acc():
    global tysk, odpowiedzi
    for a in range(3):
        tysk[a]["state"] = "disabled"

def acc_rev():
    for a in range(3):
        tysk[a]["state"] = "normal"

def money_or_mob(o):
    if (o % 10 == 1) and (o!=11):
        return "игрок"
    elif (o % 10 in [2, 3, 4]) and not(o in [12, 13, 14]):
        return "игрока"
    else:
        return "игроков"


def raspil():
    global error_count, money_count, playerz, muyt, left_wrong, pl, baza, number_inbase, costq, number, currentq, temp_string, razd, OPV
    number = 0
    for a in range(OPV):
        if pl[a]["Active"]:
            number += 1
    temp_string = ""
    razd = ""
    if (number % 10 == 1) and (number!=11):
        temp_string = "игрок"
        razd = "разделит"
    elif (number % 10 in [2, 3, 4]) and not(number in [12, 13, 14]):
        temp_string = "игрока"
        razd = "разделят"
    else:
        temp_string = "игроков"
        razd = "разделят"
    log.write("Неправильно ответили: "+str(muyt)+' из '+str(number+muyt)+'\n')
    if (prachy > 0):
        if (number == 0):
            mb.showinfo("Ноль", "Ни Герой, ни сотня ничего не получат")
            log.write("Итог игры: ни Герой, ни сотня ничего не получили" + '\n')
        elif (number == 1):
            mb.showinfo("Поражение", "1 игрок получит "+str(prachy))
            log.write("Итог игры: 1 игрок получит "+str(prachy)+ '\n')
        else:
            mb.showinfo("Поражение", str(number)+' '+temp_string+' '+razd+ ' '+str(prachy)+'.'+'\n'+"Каждый получит по "+str(prachy//number))
            log.write("Итог игры: "+ str(number)+' '+temp_string+' '+razd+ ' '+str(prachy)+".Каждый получит по "+str(prachy//number) + '\n')
    else:
        mb.showinfo("Ноль", "Сотня победила, но раз у Героя на счёте был 0, никто ничего не получит")
        log.write("Итог игры: Сотня победила, но раз у Героя на счёте был 0, никто ничего не получит" + '\n')


def afteranswerright():
    global number, OPV, currentq, prachy, costq, cost
    number = 0
    for k in range(OPV):
        if pl[k]["Active"]:
            number += 1
    if (number>0):
        log.write("Cчёт игрока: "+str(prachy)+'\n')
    if (currentq >= 3) and (number > 0):
        if mb.askyesno("Деньги или игра?", "У вас " + str(prachy) + ", и " + str(number) + ' ' + money_or_mob(
                number) + " в сотне. Будете ли вы играть дальше?"):
            currentq += 1
            if (currentq < (len(cost))):
                costq = cost[currentq - 1]
            else:
                costq = cost[-1]
            #print(prachy)
            mb.showinfo("Следующий вопрос",
                        "Стоимость вопроса - " + str(costq) + " рублей за каждого неверно ответившего игрока.")
            show_no_of_foes()
            hide_error()
            load_question(currentq)
            sh_q_variants()
            mob_answers()
        else:
            mb.showinfo("Поздравляем", "Ваш выигрыш - "+str(prachy))
            log.write("Игрок забирает деньги." + '\n')
            log.write("Выигрыш: "+ str(prachy) + '\n')
            log.close()
            root.destroy()
    elif (number == 0):
        prachy = 1000000
        mb.showinfo("ДЖЕКПОТ!", "Поздравляем, вы миллионер!")
        log.write("Выигрыш: 1000000"+'\n')
        log.close()
        root.destroy()
    else:
        currentq += 1
        if (currentq < (len(cost))):
            costq = cost[currentq - 1]
        else:
            costq = cost[-1]
        #print(prachy)
        mb.showinfo("Следующий вопрос",
                    "Стоимость вопроса - " + str(costq) + " рублей за каждого неверно ответившего игрока.")
        show_no_of_foes()
        hide_error()
        load_question(currentq)
        sh_q_variants()
        mob_answers()

def chyby(f):
    global error_count, money_count, playerz, muyt, left_wrong, pl, baza, number_inbase, costq, number, currentq, OPV, ar_atsakymas_yra_teisingas, prachy
    root.after_cancel(root.count_wrong)
    if (f==0):
        mb.showinfo("Никто не ошибся", "Все игроки ответили правильно")
        if (ar_atsakymas_yra_teisingas == False):
            raspil()
        else:
            log.write("В сотне нет неправильно ответивших"+'\n')
            baza.pop(number_inbase)
            afteranswerright()
    elif(left_wrong>0):
        left_wrong-=1
        while True:
            j = randint(0, OPV-1)
            if (pl[j]["Answer"]!=baza[number_inbase]["Correct"]) and (pl[j]["PlayerState"]==PlayerState.blue):
                break
        pl[j]["PlayerState"] = PlayerState.red
        playerz[j]["image"] = red
        error_count+=1
        money_count = error_count*costq
        upd_error()
        root.count_wrong = root.after(randint(300, 1000), lambda ja=muyt: chyby(ja))
    elif (left_wrong == 0):
        for a in range(OPV):
            if (pl[a]["PlayerState"] == PlayerState.red):
                pl[a]["PlayerState"] = PlayerState.black
                playerz[a]["image"] = black
                pl[a]["Active"] = False
        if (ar_atsakymas_yra_teisingas == False):
            raspil()
        else:
            log.write('Неверно ответивших: '+str(muyt)+' из '+str(number)+ ' ('+str(muyt)+'x'+str(costq)+'='+str(muyt*costq)+')'+'\n')
            prachy += muyt * costq
            baza.pop(number_inbase)
            afteranswerright()




def hide_error():
    global error_count, money_count, error_show, money_show, klaidingai_atsake_zaidejai
    error_show.place_forget()
    money_show.place_forget()
    klaidingai_atsake_zaidejai.place_forget()

def upd_error():
    global error_count, money_count, error_show, money_show
    error_show["text"] = str(error_count)
    money_show["text"] = str(money_count)


def vylet_start(k):
    global klaidingai_atsake_zaidejai, prachy, error_count, money_count, muyt, yko, _1_vs_howmany, error_show, money_show, left_wrong
    root.after_cancel(root.before_count_wrong)
    if (k):
        mb.showinfo("Кто вылетает?", "Сколько игроков вы выбили?")
    else:
        mb.showinfo("Кто вылетает?", "Сколько игроков вместе с вами покидают игру?")
    klaidingai_atsake_zaidejai.place(x=300, y=620)
    yko.place_forget()
    _1_vs_howmany.place_forget()
    error_count = 0
    money_count = 0
    error_show.place(x=310, y=630)
    money_show.place(x=420, y=630)
    upd_error()
    left_wrong = muyt
    root.count_wrong = root.after(randint(300, 1000), lambda ja = muyt: chyby(ja))



def perevirka(kito_kumi):
    global baza, number_inbase, odpowiedzi, tysk, pytanie, muyt, pl, ar_atsakymas_yra_teisingas
    root.after_cancel(root.check)
    odpowiedzi[baza[number_inbase]["Correct"]]["bg"]="#7FFF7F"
    if (kito_kumi==baza[number_inbase]["Correct"]):
        mb.showinfo("Браво!", "Это правильный ответ!")
        ar_atsakymas_yra_teisingas = True
    else:
        mb.showinfo("Ошибка!", "Вы ошиблись!")
        ar_atsakymas_yra_teisingas = False
    for a in range(3):
        tysk[a].place_forget()
        odpowiedzi[a].place_forget()
    log.write("Правильный ответ:" + buchstabe(baza[number_inbase]["Correct"])+'\n')
    pytanie.place_forget()
    muyt = 0
    for a in range(OPV):
        if (pl[a]["Active"]) and (pl[a]["Answer"]!=baza[number_inbase]["Correct"]):
            muyt+=1
    root.before_count_wrong = root.after(1000, lambda k = ar_atsakymas_yra_teisingas: vylet_start(k))


def trust():#версия всех, написать
    global stadiya, number, otv, baza, number_inbase, pl, ask_v, tysk, odpowiedzi, yg, hgt, vyluchenyi, trust_the_mob, hero_answer
    if (stadiya == q_stage.default):
        yg = max(otv)
        hgt = 0
        for a in range(len(otv)):
            if (otv[a]==yg):
                hgt +=1
        if (hgt>1) or ((vyluchenyi is not None) and (otv[vyluchenyi] == yg)):
            mb.showinfo("Недоступно", "Сейчас вы не можете воспользоваться Версией всех")
        else:
            log.write("Игрок берёт Версию всех."+'\n')
            b = otv.index(max(otv))
            mb.showinfo("Ответ "+buchstabe(b), baza[number_inbase]["Variants"][b])
            trust_the_mob["state"] = "disabled"
            help[2] = False
            life_hide()
            odpowiedzi[b]["bg"] = "#FFFF7F"
            stadiya = q_stage.accepted
            hero_answer = b
            log.write('Ответ игрока:'+buchstabe(b)+'\n')
            acc()
            root.check = root.after(2500, lambda lok = b: perevirka(lok))


def diff(spam):
    if (spam<2.0):
        return 1
    elif (spam<3.5):
        return 2
    else:
        return 3


def buchstabe(uh):
    if (uh==0):
        return "А"
    elif (uh==1):
        return "Б"
    else:
        return "В"

def accepted(ipconfig):
    global stadiya, OPV, pl, tysk, playerz, otv, buchstabe, hero_answer
    if (stadiya == q_stage.poll) and(help[0]):
        if (otv[ipconfig]>0):
            for ssu in range(OPV):
                if (pl[ssu]["Answer"]==ipconfig) and (pl[ssu]["Active"]):
                    pl[ssu]["PlayerState"] = PlayerState.yellow
                    playerz[ssu]["image"] = yellow
        else:
            mb.showinfo("0", "Ответ "+buchstabe(ipconfig)+ " не выбрал никто!")
            stadiya = q_stage.default
        help[0] = False
        life_show()
        log.write('Игрок берёт Версию одного по варианту '+buchstabe(ipconfig)+'. Игроков, выбравших данный ответ: '+str(otv[ipconfig])+'\n')
    elif (stadiya == q_stage.default):
        mb.showinfo("Ответ "+buchstabe(ipconfig), baza[number_inbase]["Variants"][ipconfig])
        log.write('Ответ игрока:' + buchstabe(ipconfig) + '\n')
        life_hide()
        odpowiedzi[ipconfig]["bg"] = "#FFFF7F"
        stadiya = q_stage.accepted
        hero_answer = ipconfig
        acc()
        root.check = root.after(2500, lambda lok=ipconfig: perevirka(lok))

    pass #здесь будут действия при окончательном ответе


def mob_answers():
    global otv, temptation, baza, number_inbase, OPV, pl
    otv = [0, 0, 0]
    temptation = None
    if (baza[number_inbase]["Trick"] is True):
        while True:
            temptation = randint(0, 2)
            if (temptation!=baza[number_inbase]["Correct"]):
                break
    #mi = 0 #debug
    mi = uniform(baza[number_inbase]["Difficulty"]*3, baza[number_inbase]["Difficulty"]*5) #так должно быть
    for test in range(OPV):
        if (pl[test]["Active"]):
            if (pl[test]["Knowledge"][baza[number_inbase]["Cathegory"]]>=mi):
                pl[test]["Answer"] = baza[number_inbase]["Correct"]
                pl[test]["Sure"] = 0 #точно уверен
            elif (pl[test]["Knowledge"][baza[number_inbase]["Cathegory"]]+pl[test]["Luck"]>=mi):
                pl[a]["Luck"] -= (mi-pl[test]["Knowledge"][baza[number_inbase]["Cathegory"]])
                if (baza[number_inbase]["Trick"] is True):
                    pl[test]["Answer"] = temptation
                else:
                    pl[test]["Answer"] = baza[number_inbase]["Correct"]
                pl[test]["Sure"] = 1  # я сомневаюсь
            else:
                pl[test]["Luck"] = 0
                pl[test]["Answer"] = randint(0, 2)
                pl[test]["Sure"] = 2  # я ответил наугад
            otv[pl[test]["Answer"]]+=1
            mja = randint(1, 3)
            if (mja>1):
                pl[test]["WhatWillSay"] = pl[test]["Sure"]
            else:
                while True:
                    pl[test]["WhatWillSay"] = randint(0, 2)
                    if (pl[test]["WhatWillSay"]!=pl[test]["Sure"]):
                        break
        else:
            pl[test]["Answer"] = 0
    #print(otv)





def sh_q_variants():
    global pytanie, odpowiedzi, kola_ratunkowe, number_inbase, ya, vin, poll_the_mob, ask_the_mob, trust_the_mob, help, tysk, vyluchenyi, ar_atsakymas_yra_teisingas, log, currentq, costq, number
    pytanie = tk.Label(root, justify=tkinter.CENTER, bg = "#FFFFFF", wraplength=600)
    pytanie.place(x=200, y=580, width = 580, height = 50)
    pytanie["text"] = baza[number_inbase]["Question"]
    pytanie["justify"] = tkinter.CENTER
    pytanie["bg"] = "#ffffcf"
    pytanie["wraplength"] = 600
    tysk = []
    odpowiedzi = []
    log.write('Вопрос ' + str(currentq) + ' (' + str(costq) + ' руб.)'+'\n')
    log.write('1 против '+str(number)+'. '+baza[number_inbase]["Question"]+'\n')
    for bar in range(3):
        #ya = tk.Label(text=(baza[number_inbase]["Variants"][bar])*3, bg="#FFFFFF")
        ya = tk.Label(text = baza[number_inbase]["Variants"][bar], bg = "#FFFFFF") #так должно быть
        vin = tk.Button(root, text = buchstabe(bar), width=4, height=1, command = lambda i=bar: accepted(i))
        tysk.append(vin)
        odpowiedzi.append(ya)
        tysk[bar].place(x=260+200*bar, y = 635)
        odpowiedzi[bar].place(x=200+200*bar, y=660, width=180, height=70)
        odpowiedzi[bar]["wraplength"] = 170
        log.write(buchstabe(bar)+': '+baza[number_inbase]["Variants"][bar]+'\n')
    if(help[0]):
        poll_the_mob["state"] = "normal"
    else:
        poll_the_mob["state"] = "disabled"
    if(help[1]):
        ask_the_mob["state"] = "normal"
    else:
        ask_the_mob["state"] = "disabled"
    if(help[2]):
        trust_the_mob["state"] = "normal"
    else:
        trust_the_mob["state"] = "disabled"
    poll_the_mob.place(x=900, y=400)
    ask_the_mob.place(x=900, y=445)
    trust_the_mob.place(x=900, y=490)
    vyluchenyi = None
    ar_atsakymas_yra_teisingas = None


def load_question(qq):
    global stadiya
    if (qq<=5):
        schwerig = 1
    elif (qq<=9):
        schwerig = 2
    else:
        schwerig = 3
    global number_inbase
    while True:
        number_inbase = randint(0, len(baza)-1)
        if diff(baza[number_inbase]["Difficulty"]) == schwerig:
            break
    stadiya = q_stage.default
    #print(baza[number_inbase])




def show_no_of_foes():
    global yko, number, _1_vs_howmany, skolko
    yko = tk.Label(root, width=3, height=1, fg="#00FF7F", bg="#0000FF", font = ('Arial', 15))
    number = 0
    for k in range(OPV):
        if pl[k]["Active"]:
            number+=1
    yko["text"] = str(number)
    yko.place(x=722, y=140)
    _1_vs_howmany.place(x=660, y=130)

def pradeti():
    global yellow, red, blue, black, playerz, pl, PlayerState, yko, number, currentq, costq, cost, error_show, money_show
    START.place_forget()
    error_show = tk.Label(root, width=3, height=1, fg="#00FF7F", bg="#00BAFF", font = ('Arial', 12))
    money_show = tk.Label(root, width=7, height=1, fg="#00FF7F", bg="#00BAFF", font=('Arial', 12))
    #draw_text = ImageDraw.Draw(_1vs)
    #draw_text.text((100, 40), '111', font=font, fill="#CCCCCC")

    currentq+=1
    if (currentq<(len(cost))):
        costq = cost[currentq-1]
    else:
        costq = cost[-1]
    mb.showinfo("Следующий вопрос", "Стоимость вопроса - "+str(costq)+" рублей за каждого неверно ответившего игрока.")

    show_no_of_foes()

    load_question(currentq)
    sh_q_variants()
    mob_answers()

    #yko["text"] = '90'
    #Vienas_pries(67)


    # po = Image.open("img/yellow.png")
    # po.thumbnail((25, 50), Image.ANTIALIAS)
    # lm = ImageTk.PhotoImage(po)
    #playerz[45].configure(image=red)
    #playerz[45].place_forget()
        # for ji in [68-1, 58-1, 33-1, 5-1]:
        #     playerz[ji]["image"] = yellow
        #     pl[ji]["PlayerState"] = PlayerState.yellow
    pass #дописать начало игры

START = tk.Button(root, text = "Начать игру", command = pradeti, width = 28, height=14)
START.place(x=400, y=500)
poll_the_mob = tk.Button(root, state="normal", text="Версия одного", height=1, width=9, command=poll)
ask_the_mob = tk.Button(root, state="normal", text="Версия двух", height=1, width=9, command=ask)
trust_the_mob = tk.Button(root, state="normal", text="Версия всех", height=1, width=9, command=trust)
root.protocol('WM_DELETE_WINDOW', doSomething)
root.mainloop()