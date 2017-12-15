from tkinter import *
import time
import datetime
global nextPeriod
root = Tk()

root.overrideredirect(True)
root.attributes("-topmost", True)
root.configure(background='black')
global topmostTest,hide
topmostTest = True
def topmost():
    global topmostTest,hide
    if topmostTest == True:
        hide.config(relief=FLAT,bg='red',activebackground='red')
        root.attributes("-topmost", False)
        topmostTest = False
    else:
        hide.config(relief=FLAT,bg='gray20',activebackground='gray35')
        root.attributes("-topmost", True)
        topmostTest = True
def closeWindow():
    root.quit()
hide = Button(root, bg='gray35',width=1,height=1,relief='flat',overrelief='flat',command=topmost)
#hide.pack(side="left", fill="y")
hide.grid(row=0,column=0,sticky=N)
close = Button(root, bg='red',width=1,height=1,relief='flat',overrelief='flat',text='X',fg='white',command=closeWindow)
#close.pack(side="right", fill="y")
close.grid(row=0,column=2,sticky=N)

def StartMove(event):
    root.x = event.x
    root.y = event.y

def StopMove(event):
    root.x = None
    root.y = None

def OnMotion(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry("+%s+%s" % (x, y))

root.bind("<ButtonPress-1>", StartMove)
root.bind("<ButtonRelease-1>", StopMove)
root.bind("<B1-Motion>", OnMotion)

try:
    clock = Label(root, font=('Segoe UI Light', 15, 'bold'), bg='black', fg='white',width=10)
    #clock.pack(fill=BOTH, expand=1)
    clock.grid(row=0,column=1)
    nextPeriod = Label(root, font=('Segoe UI Light', 10, 'bold'), bg='black', fg='white')
    nextPeriod.grid(row=1,column=1)
    #nextPeriod.pack(fill=BOTH, expand=1)
except:
    clock = Label(root, font=('Helvetica', 15, 'bold'), bg='black', fg='white')
    #clock.pack(fill=BOTH, expand=1)
    nextPeriod = Label(root, font=('Helvetica', 10, 'bold'), bg='black', fg='white')
    #nextPeriod.pack(fill=BOTH, expand=1)
def tick():
    global y
    empty = '00:00:00'
    x = '8:40:01'
    FMT = '%H:%M:%S'
    t2 = datetime.datetime.now().time().strftime('%H:%M:%S')
    timetable = [[datetime.time(8, 40, 0), datetime.time(9, 5, 0), 'Registration'],
                 [datetime.time(9, 5, 1),datetime.time(9, 55, 0), 'Period 1'],
                 [datetime.time(9, 55, 1), datetime.time(10, 45, 0), 'Period 2'],#P2
                 [datetime.time(10, 45, 1),datetime.time(11, 00, 0), 'Break'],#Break
                 [datetime.time(11, 00, 1),datetime.time(11, 55, 0), 'Period 3'],#P3
                 [datetime.time(11, 55, 1),datetime.time(12, 45, 0), 'Period 4'],#P4
                 [datetime.time(12, 45, 1),datetime.time(13, 20, 0), 'Lunch'],#Lunch
                 [datetime.time(13, 20, 1),datetime.time(14, 10, 0), 'Period 5'],#P5
                 [datetime.time(14, 10, 1),datetime.time(15, 00, 0), 'Period 6']]#P6
    if datetime.datetime.now().time() <= timetable[0][0]:#Pre-reg
        t1 = timetable[0][0].strftime('%H:%M:%S')
        td = datetime.datetime.strptime(t1, '%H:%M:%S') - datetime.datetime.strptime(t2, '%H:%M:%S')
        currentPeriod = timetable[0][2]
        nextPeriodText = timetable[0][2]

    elif timetable[0][0] <= datetime.datetime.now().time() <= timetable[0][1]:#Registration
        t1 = timetable[0][1].strftime('%H:%M:%S')
        td = datetime.datetime.strptime(t1, '%H:%M:%S') - datetime.datetime.strptime(t2, '%H:%M:%S')
        currentPeriod = timetable[0][2]
        nextPeriodText = timetable[1][2]

    elif timetable[1][0] <= datetime.datetime.now().time() <= timetable[1][1]:#P1
        t1 = timetable[1][1].strftime('%H:%M:%S')
        td = datetime.datetime.strptime(t1, '%H:%M:%S') - datetime.datetime.strptime(t2, '%H:%M:%S')
        currentPeriod = timetable[1][2]
        nextPeriodText = timetable[2][2]

    elif timetable[2][0] <= datetime.datetime.now().time() <= timetable[2][1]:#P2
        t1 = timetable[2][1].strftime('%H:%M:%S')
        td = datetime.datetime.strptime(t1, '%H:%M:%S') - datetime.datetime.strptime(t2, '%H:%M:%S')
        currentPeriod = timetable[2][2]
        nextPeriodText = timetable[3][2]

    elif timetable[3][0] <= datetime.datetime.now().time() <= timetable[3][1]:#Break
        t1 = timetable[3][1].strftime('%H:%M:%S')
        td = datetime.datetime.strptime(t1, '%H:%M:%S') - datetime.datetime.strptime(t2, '%H:%M:%S')
        currentPeriod = timetable[3][2]
        nextPeriodText = timetable[4][2]

    elif timetable[4][0] <= datetime.datetime.now().time() <= timetable[4][1]:#P3
        t1 = timetable[4][1].strftime('%H:%M:%S')
        td = datetime.datetime.strptime(t1, '%H:%M:%S') - datetime.datetime.strptime(t2, '%H:%M:%S')
        currentPeriod = timetable[4][2]
        nextPeriodText = timetable[5][2]

    elif timetable[5][0] <= datetime.datetime.now().time() <= timetable[5][1]:#P4
        t1 = timetable[5][1].strftime('%H:%M:%S')
        td = datetime.datetime.strptime(t1, '%H:%M:%S') - datetime.datetime.strptime(t2, '%H:%M:%S')
        currentPeriod = timetable[5][2]
        nextPeriodText = timetable[6][2]

    elif timetable[6][0] <= datetime.datetime.now().time() <= timetable[6][1]:#Lunch
        t1 = timetable[6][1].strftime('%H:%M:%S')
        td = datetime.datetime.strptime(t1, '%H:%M:%S') - datetime.datetime.strptime(t2, '%H:%M:%S')
        currentPeriod = timetable[6][2]
        nextPeriodText = timetable[7][2]

    elif timetable[7][0] <= datetime.datetime.now().time() <= timetable[7][1]:#P5
        t1 = timetable[7][1].strftime('%H:%M:%S')
        td = datetime.datetime.strptime(t1, '%H:%M:%S') - datetime.datetime.strptime(t2, '%H:%M:%S')
        currentPeriod = timetable[7][2]
        nextPeriodText = timetable[8][2]

    elif timetable[8][0] <= datetime.datetime.now().time() <= timetable[8][1]:#P6
        t1 = timetable[8][1].strftime('%H:%M:%S')
        td = datetime.datetime.strptime(t1, '%H:%M:%S') - datetime.datetime.strptime(t2, '%H:%M:%S')
        currentPeriod = timetable[8][2]
        nextPeriodText = 'End of teaching day'
    else:
        td = ''
        nextPeriodText = 'End of teaching day'
    clock.config(text=td)
    if nextPeriodText == '':
        text1 = ''
    if nextPeriodText == 'End of teaching day':
        text1 = nextPeriodText
    else:
        text1 = 'Next: '+nextPeriodText
    nextPeriod.config(text=text1)
    # calls itroot every 200 milliseconds
    clock.after(400, tick)
tick()
root.mainloop(  )
