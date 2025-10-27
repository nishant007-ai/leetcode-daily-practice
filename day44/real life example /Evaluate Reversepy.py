class Solutin :
  def preIS(self,n):
    s= []

    for m in n:
        if m not in ("+-*/"):
            s.append(int(m))
        else:
            q = s.pop()
            w = s.pop()

            if m = ('+'):
                s.append(w + q )
            elif m = ('-'):
                s.append(w - q )
            elif m = ('*'):
                s.append(w * q )           
            else : # '/'
                s.append(int(w / q )) # correct: truncates toward zero
    return s[-1]    
  


  