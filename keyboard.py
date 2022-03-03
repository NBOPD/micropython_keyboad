class keyboard:
  def __init__(self,lcd,entry=False):
    self.lcd=lcd
    self.zb=[0,0]
    self.title=''
    self.entry=entry
    self.page=0
    self.key2=[('1','2','3'),('4','5','6'),('7','8','9'),('back','0','enter')]
    self.key=[('a','b','c','d','e'),('f','g','h','i','j'),('k','l','m','n','o'),('p','q','r','s','t'),('u','v','w','x','y'),('z','back','enter')]
  def init_num(self):
    self.page=1
    self.lcd.fill(0)
    for xx in range(4):
      for x in range(3):
        self.lcd.rect(x*42,1+(xx*16),40,14,1)
        if xx <=2:
          self.lcd.text(self.key2[xx][x],14+(x*42),4+(xx*16))
        elif x==0:
          self.lcd.text('back',4+(0*42),4+(3*16))
        elif x==2:
          self.lcd.text('ent',8+(2*42),4+(3*16))
        elif x==1:
          self.lcd.text(self.key2[3][1],14+(1*42),4+(3*16))
    self.update_num()
  def update_num(self):
    self.lcd.fill_rect(self.zb[0]*42,1+(self.zb[1]*16),40,14,1)
    if self.zb[0] <= 2 and self.zb[1] <=2:
      self.lcd.text(self.key2[self.zb[1]][self.zb[0]],14+(self.zb[0]*42),4+(self.zb[1]*16),0)
    elif self.zb[0] == 0:
      self.lcd.text('back',4,4+(3*16),0)
    elif self.zb[0] == 1:
      self.lcd.text(self.key2[3][1],14+(1*42),4+(3*16),0)
    elif self.zb[0] == 2:
      self.lcd.text('ent',8+(2*42),4+(3*16),0)
  def clear_num(self):
    self.lcd.fill_rect(self.zb[0]*42,1+(self.zb[1]*16),40,14,0)
    self.lcd.rect(self.zb[0]*42,1+(self.zb[1]*16),40,14,1)
    if self.zb[0] <= 2 and self.zb[1] <=2:
      self.lcd.text(self.key2[self.zb[1]][self.zb[0]],14+(self.zb[0]*42),4+(self.zb[1]*16),1)
    elif self.zb[0] == 0:
      self.lcd.text('back',4,4+(3*16),1)
    elif self.zb[0] == 1:
      self.lcd.text(self.key2[3][1],14+(1*42),4+(3*16),1)
    elif self.zb[0] == 2:
      self.lcd.text('ent',8+(2*42),4+(3*16),1)
  def init(self):
    self.page=0
    self.lcd.fill(0)
    self.zb=[0,0]
    for xx in range(5):
      for x in range(5):
        self.lcd.rect(x*25,1+(xx*10),22,9,1)
        self.lcd.text(self.key[xx][x],6+(x*25),1+(xx*10))
    self.lcd.rect(0,51,22,9,1) #z
    self.lcd.rect(25,51,22,9,1) #back
    self.lcd.rect(50,51,22,9,1) #enter
    self.lcd.text(self.key[5][0],5,51)
    self.lcd.text('en',28,51)
    self.lcd.text('ba',53,51)
    self.lcd.fill_rect(0,1,22,9,1)
    self.lcd.text(self.key[0][0],6,1,0)
    if self.entry:
      self.lcd.hline(75,60,48,1)
  def ent_append(self,char):
    self.title=self.title+char
    if not self.page:
      self.lcd.text(self.title[-5:],78,52)
  def ent_back(self,count):
    self.title=self.title[:-(count)]
    if not self.page:
      self.lcd.fill_rect(75,50,48,12,0)
      self.lcd.hline(75,60,48,1)
      self.lcd.text(self.title[-5:],78,52)
  def ent_clear(self):
    self.title=''
    if not self.page:
      self.lcd.fill_rect(75,50,48,12,0)
      self.lcd.hline(75,60,48,1)
      self.lcd.text(self.title[-5:],78,52)
  def ent_get(self):
    return self.title
  def moveUp(self):
    if not self.page:
      if self.zb[1] != 0:
        self.clear()
        self.zb[1]-=1
        self.update()
    else:
      if self.zb[1] != 0:
        self.clear_num()
        self.zb[1]-=1
        self.update_num()
      elif self.zb[1] == 0:
        self.init()
        self.clear()
        self.zb=[0,5]
        self.update()
  def moveDown(self):
    if not self.page:
      if self.zb[1] != 4 or self.zb[0]==0 or self.zb[0] ==1 or self.zb[0] ==2:
        if (self.zb[0] == 0 or self.zb[0] == 1 or self.zb[0] == 2) and self.zb[1] ==4:
          self.clear()
          self.zb[1]+=1
          self.update()
        elif self.zb[1] <=4:
          self.clear()
          self.zb[1]+=1
          self.update()
        elif self.zb[1] == 5:
          self.zb=[0,0]
          self.init_num()
          self.update_num()
    else:
      if self.zb[1] !=3:
        self.clear_num()
        self.zb[1]+=1
        self.update_num()
  def moveLeft(self):
    if not self.page:
      if self.zb[0] !=0:
        self.clear()
        self.zb[0]-=1
        self.update()
    else:
      if self.zb[0] !=0:
        self.clear_num()
        self.zb[0]-=1
        self.update_num()
  def moveRight(self):
    if not self.page:
      if self.zb[1] != 5 or (self.zb[1] == 5 and self.zb[0] !=2):
        if self.zb[0] !=4:
          self.clear()
          self.zb[0]+=1
          self.update()
    else:
      if self.zb[0] !=2:
        self.clear_num()
        self.zb[0]+=1
        self.update_num()
  def get(self):
    if not self.page:
      r=self.key[self.zb[1]][self.zb[0]]
    else:
      r=self.key2[self.zb[1]][self.zb[0]]
    return r
  def clear(self):
    if self.zb[1] != 5 or (self.zb[0] == 0 and self.zb[1] == 5):
      self.lcd.fill_rect(self.zb[0]*25,1+(self.zb[1]*10),22,9,0)
      self.lcd.rect(self.zb[0]*25,1+(self.zb[1]*10),22,9,1)
      self.lcd.text(self.key[self.zb[1]][self.zb[0]],6+(self.zb[0]*25),1+(self.zb[1]*10))
    elif self.zb[0] == 1:
      self.lcd.fill_rect(25,51,22,9,0)
      self.lcd.rect(25,51,22,9,1)
      self.lcd.text('en',28,51,1)
    elif self.zb[0] == 2:
      self.lcd.fill_rect(50,51,22,9,0)
      self.lcd.rect(50,51,22,9,1)
      self.lcd.text('ba',53,51,1)
  def update(self):
    if self.zb[1] != 5 or (self.zb[0] == 0 and self.zb[1] == 5):
      self.lcd.fill_rect(self.zb[0]*25,1+(self.zb[1]*10),22,9,1)
      self.lcd.text(self.key[self.zb[1]][self.zb[0]],6+(self.zb[0]*25),1+(self.zb[1]*10),0)
    elif self.zb[0] == 1:
      self.lcd.fill_rect(25,51,22,9,1)
      self.lcd.text('en',28,51,0)
    elif self.zb[0] == 2:
      self.lcd.fill_rect(50,51,22,9,1)
      self.lcd.text('ba',53,51,0)
  def goto(self,x,y):
    if not self.page:
      self.clear()
      self.zb=[x,y]
      self.update()
    else:
      self.clear_num()
      self.zb=[x,y]
      self.update_num()