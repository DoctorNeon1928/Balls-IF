# 1....10000

# числа кратные 3 и 7 одновременно

#for i in range(10000):
#      if i%3 == 0 and i%7 == 0 :
#            print(i)


import tkinter;

okno = tkinter.Tk();
okno.geometry('600x600');

holst = tkinter.Canvas(okno, width = 600, height = 600);
holst.pack();

vadim = holst.create_oval(10,110,
                          70,170,
                          fill='#DDBBAA');

platon = 0;

def igor(event):
      global platon;
      x = 0;
      y = 0;
      if event.keysym == 'Right':
            x = 20;
      elif event.keysym == 'Left':
            x = -20;
      elif event.keysym == 'Up':
            y = -20;
      elif event.keysym == 'Down':
            y = 20;
      holst.move(vadim, x, y)
      
      if ya_ya(vadim, cp1) <30:
            platon = 1;
      if ya_ya(vadim, cp2) <30 and platon == 1:
            platon = 2;
      if ya_ya(vadim, cp3) <30 and platon == 2:
            platon = 0;
            print('ДАААААААААААААААААААААААААААА!!!Я ТУПОЙ!!!');
      #print(event.keysym)

def ya_ya (a, b) :  #Расстояние между точками
      k1 = holst.coords(a)
      k2 = holst.coords(b)
      r = ( (k1[0] - k2[0]) ** 2 + (k1[1] - k2[1]) **2)
      return r

okno.bind('<Key>', igor)

cp1 = holst.create_oval(10,110,
                       70,170,
                       fill='#AAFFDD')

cp2 = holst.create_oval(10,210,
                       70,270,
                       fill='#DDFFAA')

cp3 = holst.create_oval(10,310,
                       70,370,
                       fill='#FFBBAA')
          


























































