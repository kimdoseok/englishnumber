import string,math

class EnglishNumber:
  def __init__(self):
    self.lefts = []
    self.rights = ''
    self.english = []
    self.numbers = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',
                    9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',
                    15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
                    20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',
                    80:'eighty',90:'ninety',100:'hundred',}
    self.blocks = ['','thousand','million','billion','trillion','quadrillion','quintillion',
                   'sextillion','septillion','octillion','nonillion','decillion','undecillion',
                   'duodecillion','tredecillion','quattuordecillion','quindecillion',
                   'sexdecillion','septendecillion','octodecillion','novemdecillion',]

  def SetNumber(self,numstr):
    self.lefts = []
    self.rights = ''
    self.english = []
    __nums = numstr.strip().split('.')
    if len(__nums)==1 and __nums[0]:
      __lefts = [int(x) for x in __nums[0] if x in string.digits]
      self.rights = "00"
    elif len(__nums)==2:
      __lefts = [int(x) for x in __nums[0] if x in string.digits]
      self.rights = "".join([x for x in __nums[1] if x in string.digits][:2])
    else:
      return False
    bnum = int(math.ceil(len(__lefts)/3.0))
    for i in range(bnum):
      if i==0:
        threelist = __lefts[-3:]
      else:
        threelist = __lefts[-3*(i+1):-3*i]
      self.english.insert(0,self.blocks[i])

      if len(threelist)==1:
        self.english.insert(0,self.numbers[threelist[0]])
      elif len(threelist)==2:
        if threelist[0]>1:
          self.english.insert(0,self.numbers[threelist[1]])
          self.english.insert(0,self.numbers[threelist[0]*10])
        else:
          self.english.insert(0,self.numbers[threelist[0]*10+threelist[1]])
      elif len(threelist)==3:
        if threelist[1]>1:
          self.english.insert(0,self.numbers[threelist[2]])
          self.english.insert(0,self.numbers[threelist[1]*10])
        else:
          self.english.insert(0,self.numbers[threelist[1]*10+threelist[2]])
        if threelist[0]>0:
          self.english.insert(0,self.numbers[100])
          self.english.insert(0,self.numbers[threelist[0]])
    return True

  def GetNumber(self):
    left = " ".join([x for x in self.english if x]).strip()
    if not left: left='None'
    return ("%s and %s/100 " % (left.title(),self.rights)).strip()

if __name__=='__main__':
  a = ['0.01','1.25','12.34','119.12','1001.34','1211.45','1234567.68']
  en = EnglishNumber()
  x = 0.1
  b = ['1263234212341234046223881.90',]
  for i in b:
    en.SetNumber(i)
    print (i,en.GetNumber())
  for i in range(50):
    x *= 1.9
    en.SetNumber("%0.2f"%x)
    print ("%0.2f"%x,en.GetNumber())
