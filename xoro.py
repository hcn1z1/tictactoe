from colorama import Fore
import random
class XO:
    def __init__(self):
        self.vector = [" "]
        self.winner =  False
        self._pos_o = []
        for x in range(1,10):
            self.vector.append(" ")
    def _solo_(self,diff):
        self.remain = [1,2,3,4,5,6,7,8,9]
        if diff == 1:
            self.ig = random.choice([8,10,12])
        elif diff == 2:
            self.ig = random.choice([4,6,8])
        elif diff == 3:
            self.ig = 2
        for x in range(1,10):
            while True:
                if x%2 == 0:
                    o=self.bot(x)
                    s = "o"
                else:
                    o = input("We are adding X on position:")
                    s = "x"
                if int(o)<10 and int(o)>0 and self.vector[int(o)] == " ":
                    self.remain.remove(int(o))
                    break;
                else:print("place is charged or you number abouve value")
            #adding o on self.vector (Table)
            self.vector[int(o)] = s
            #here we check
            win = self.__checking__()
            if win is True:
                for x in range(3):
                    print(self.vector[x*3+1]+Fore.GREEN+" |"+Fore.RESET,self.vector[x*3+2]+Fore.GREEN+" |"+Fore.RESET,self.vector[x*3+3])
                break;
    def _multi_(self):
        for x in range(1,10):
            while True:
                if x%2 == 0:
                    o = input("We are adding O on position:")
                    s = "o"
                else:
                    o = input("We are adding X on position:")
                    s = "x"
                if int(o)<10 and int(o)>0 and self.vector[int(o)] == " ":
                    break;
                else:print("place is charged or you number abouve value")
            #adding o on self.vector (Table)
            self.vector[int(o)] = s
            #here we check
            win = self.__checking__()
            if win is True:
                for x in range(3):
                    print(self.vector[x*3+1]+Fore.CYAN+" |"+Fore.RESET,self.vector[x*3+2]+Fore.CYAN+" |"+Fore.RESET,self.vector[x*3+3])
                break;
    def __checking__(self):
            for _x_ in range(1,4):
                if self.vector[0+_x_]== self.vector[3+_x_] and self.vector[3+_x_]==self.vector[6+_x_] and self.vector[0+_x_]!=" ":
                    print("winner is ",self.vector[0+_x_])
                    self.winner = True
                    return True;
                else:pass
                if self.vector[1+(_x_-1)*3]== self.vector[2+(_x_-1)*3] and self.vector[2+(_x_-1)*3]==self.vector[3+(_x_-1)*3] and self.vector[1+(_x_-1)*3] != " ": 
                    print("winner is ",self.vector[+(_x_)*3])
                    self.winner = True
                    return True;
                else:pass
            if self.vector[1]==self.vector[5] and self.vector[1]==self.vector[9] and self.vector[1]!=" ":
                print("winner is ", self.vector[1])
                self.winner = True
                return True;
            elif self.vector[3]==self.vector[5] and self.vector[3]==self.vector[7] and self.vector[3]!=" ":
                print("winner is ",self.vector[3])
                self.winner = True
                return True; 
            if self.winner:
                return True;
            if self.winner is True:
                pass
            else:pass
            for x in range(3):
                    print(self.vector[x*3+1]+Fore.CYAN+" |"+Fore.RESET,self.vector[x*3+2]+Fore.CYAN+" |"+Fore.RESET,self.vector[x*3+3])
    def bot(self,x):
        print(x)
        if x<=self.ig:
            s = random.choice(self.remain)
            print("here")
            self._pos_o.append(s)
        else:
            defend_bot = False
            for _x_ in range(1,4):
                if self.vector[0+_x_]== self.vector[3+_x_] and self.vector[6+_x_]==" ":
                    if self.vector[0+_x_] =="o":
                        s = 6+_x_
                        break;
                    elif self.vector[0+_x_] =="x":
                        s = 6+_x_
                        defend_bot = True
                elif self.vector[0+_x_]== self.vector[6+_x_] and self.vector[3+_x_]==" ":
                    if self.vector[0+_x_] =="o":
                        s = 3+_x_
                        break;
                    elif self.vector[0+_x_] =="x":
                        defend_bot = True
                        s = 3+_x_
                elif self.vector[3+_x_]== self.vector[6+_x_] and self.vector[0+_x_]==" ":
                    if self.vector[3+_x_] =="o":
                        s = _x_
                        break;
                    elif self.vector[3+_x_] == "x":
                        s = _x_
                        defend_bot = True
                if self.vector[1+(_x_-1)*3] == self.vector[2+(_x_-1)*3]  and self.vector[3+(_x_-1)*3] == " ": 
                    if self.vector[1+(_x_-1)*3] == "o":
                        s = 3+(_x_-1)*3
                        break;
                    elif self.vector[1+(_x_-1)*3] == "x" :
                        s = 3+(_x_-1)*3
                        defend_bot = True
                elif self.vector[1+(_x_-1)*3] == self.vector[3+(_x_-1)*3]  and self.vector[2+(_x_-1)*3] == " ": 
                    if self.vector[1+(_x_-1)*3] == "o":
                        s = 2+(_x_-1)*3
                        break;
                    elif self.vector[1+(_x_-1)*3] == "x":
                        s = 2+(_x_-1)*3
                        defend_bot =True
                elif self.vector[3+(_x_-1)*3] == self.vector[2+(_x_-1)*3]  and self.vector[1+(_x_-1)*3] == " ": 
                    if self.vector[2+(_x_-1)*3] == "o":
                        s = 1+(_x_-1)*3
                        break;
                    elif self.vector[2+(_x_-1)*3] == "x":
                        s = 1+(_x_-1)*3
                        defend_bot = True
                else:
                    if defend_bot is True:
                        pass
                    else:
                        s= random.choice(self.remain)
            if self.vector[1]==self.vector[5] and self.vector[9]==" ":
                if self.vector[1]=="o" or self.vector[1]=="x":
                    s = 9
            elif self.vector[1]==self.vector[9] and self.vector[5]==" ":
                if self.vector[1]=="o" or self.vector[1]=="x":
                    s = 5
            elif self.vector[9]==self.vector[5] and self.vector[1]==" ":
                if self.vector[9]=="o" or self.vector[9]=="x":
                    s = 1
            elif self.vector[3]==self.vector[5] and self.vector[7]==" ":
                if self.vector[3]=="o" or self.vector[3]=="x":
                    s = 7
            elif self.vector[3]==self.vector[7] and self.vector[5]==" ":
                if self.vector[3]=="o" or self.vector[3]=="x":
                    s = 5
            elif self.vector[9]==self.vector[5] and self.vector[3]==" ":
                if self.vector[9]=="o" or self.vector[9]=="x":
                    s = 3
        return s;
if "__main__"==__name__:
    print("Please Choose a mode")
    print(
""" {0}1{1}- Solo
 {0}2{1}- Multi-Player   
X-O@{0}HCn1{1} $: """.format(Fore.RED,Fore.RESET),end="")
    mod = int(input())
    if mod == 2:
        XO()._multi_()
    else:
        print("""Please choose difficulty level
 {0}1{1}- Easy
 {0}2{1}- Medium
 {0}3{1}- Hard         
X-O@{0}HCn1{1} $: """.format(Fore.RED,Fore.RESET),end="")
        diff = int(input())
        XO()._solo_(diff)
