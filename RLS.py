class nel:
  import random
  inpul = ["0"];inpux = [];inpulx = [];logx = [];com = ['clear'];rpst=None
  def inpuld(x):
    back = self.inpul 
    self.inpul = x
    return back
  r = True

  def gram(self,text):
    try:
      from nltk import word_tokenize, pos_tag
      text = " ".join(text)
      tagged = pos_tag(word_tokenize(text))
      nouns = [word for word, pos in tagged if pos == 'NN'] 
      verbs = [word for word, pos in tagged if pos == 'VB']
      words = sorted(word_tokenize(text),
      key=lambda word: (0,1) if word in nouns else (1,0))
      for item in words:
        if item.endswith('?') or item.endswith('!'):
          words.remove(item)
          words.append(item)
      return words
    except:
      sy=input("F Error try for install nltk , punkt , averaged_perceptron_tagger ? (y/n) ->")
      if "y" in sy:
        import os
        os.system("python -m pip install nltk")
        try:import nltk
        except:os.system("py -m pip install nltk")
        try:nltk.download('punkt');nltk.download('averaged_perceptron_tagger');print("[OK]");return []
        except:print("[FL]");return []
      else:return []
  def nerve_in(self,inpu,log,split,sts,sts2,res,res2,lear,logxb,tll,clea,rv):
    def run(inpu,log):
      trm = False;re = False;re2 = False;re3 = False;re4 = False;re5 = False;out = []
      numr = 0
      nume = 0
      st1 = set(str(inpu))
      st2 = set(str(self.inpulx))
      intersect = st1.intersection(st2)
      uniont = st1.union(st2)
      rpt = len(intersect) / len(uniont)
      self.rpst = rpt * 100
      
      try:
        if rpt >= self.random.randint(sts-10,sts):inpu.append(self.inpulx)
      except:pass
      s1 = set(str(inpu))
      s2 = set(str(self.inpux))
      intersec = s1.intersection(s2)
      union = s1.union(s2)
      rp = len(intersec) / len(union)
      rps = rp * 100
      try:inpu = inpu.split(str(split))
      except:pass
      try:
        #Each is different and may require changes
        if inpu[0] == '_':
          self.inpux.append(self.inpulx)
          flat = []
          for item in self.inpux:
            if isinstance(item, list):flat.extend(item)
            else:flat.append(item)
          self.inpux = flat
          if re == False:inpu.remove('_');re=True
      except:pass
      try:
        if inpu[0] == 'outme_':
          if re == False:inpu.remove('outme_')
          print(self.inpul)
      except:pass
      try:
        if inpu[0] == 'com_':
          com.append(self.inpulx)
          flat = []
          for item in self.com:
            if isinstance(item, list):flat.extend(item)  
            else:flat.append(item)
          com = flat;output = subprocess.check_output(self.inpulx, shell=True);print(output)
          if re == False:
            inpu.remove('com_');re5=True
      except Exception as e:
        self.com.append(e)
      if re or re2 or re3 or re4 or re5: rem = True
      else: rem = False
      if rem == False:
        flat = [];inputw = []
        try:inpu = inpu.split(str(split))
        except:pass
        try:
          for item in inpu:
            if item.endswith("?") or item.endswith("!"):
              self.inputw.append(item)
              inpu.remove(item)
          inpu.extend(inputw)
        except:pass
        for item in self.logx:
          if isinstance(item, list):flat.extend(item)
          else:flat.append(item)
        self.logx = flat
        if logxb == True:inpu.append(self.logx)
        re=True
      for x in inpu:
        #print(inpul)
          if rps < self.random.randint(sts2-10,sts2):
            if x in inpu:
              for r in self.inpul:
                if tll == True:
                  try: nld = [i for i, n in enumerate(self.inpul) if n == r];rs=2
                  except:pass
                else:
                  try: nl = self.inpul.index(x)
                  except:pass
              try:
                for nl in nld:
                  if lear == True:
                    if str(x) in self.inpul or str(x) in self.inpulx:
                      self.inpul.insert(nl,inpu)
                      flat = []
                      for item in self.inpul:
                        if isinstance(item, list):flat.extend(item)
                        else:flat.append(item)
                      self.inpul = flat
                      if res2 == True:self.inpul.append(inpu[inpu.index(x)]);self.inpul.append(inpu[int(inpu.index(x))-1])
                      else:self.inpul.append(inpu[inpu.index(x)]);self.inpul.append(inpu[int(inpu.index(x))+1])
                    numm = 1
                    for n in range(len(inpu)):
                      numm += 1
                      if inpu[inpu.index(x)+n] != None:
                        self.inpul.append(inpu[int(inpu.index(x))+n])
                    if clea == True:self.inpul = list(set([''.join(item) for item in self.inpul]))
              except:pass
              try:
                if res2 == True:
                  for xn in range(len(inpu)):out.append(self.inpul[nl - xn])
                else: out.append(self.inpul[nl + 1]);out.append(self.inpul[nl + 2])
                if len(out)>1: self.out.remove(out[0])
              except:pass
            if rps >= self.random.randint(sts2-10, sts2):
              trm = True
              try:
                for x in inpu:
                  if rps >= self.random.randint(sts2-10, sts2):
                    try:
                      nl = self.inpux.index(x)
                      for xn in range(len(inpu)):
                        out.append(self.inpul[nl + xn])
                    except:pass
                    if trm == False:
                      nl = self.inpul.index(x)
                      for xn in range(len(inpu)):
                        out.append(self.inpul[nl + xn])
              except:pass
            #IQ 9000000000000
            try:
              if self.random.randint(0,rv)==0:out = list(set([''.join(item) for item in out]))
            except:pass
            try:
              if self.random.randint(0,rv*3)==0:self.inpul = list(set([''.join(item) for item in self.inpul]))
            except:pass
          numr += 1
      try:
        if log == True:print(self.inpul);print(rps),print(self.inpux);print(rpt)
      except:pass
      outref = []
      for it in out:
        if it not in outref:
          outref.append(it)
      if self.r == True:
        try:
          if len(inpu)>=2: self.inpul.pop(0);self.inpul.pop(0);r = False
        except:pass
      if res == True:outref.reverse()
      self.inpulx = outref;logx = outref
      return outref
    return run(inpu,log)
  def nerves_in(self,inpu,log,split):
    stglo = self.nerve_in(inpu,log,split,45,60,True,True,True,True,True,True if self.random.randint(0,90)==0 else False,20)
    comb = stglo
    flat = []
    for item in comb:
      if isinstance(item, list):flat.extend(item)
      else:flat.append(item)
    comb = flat
    try:sp = ', '.join(comb)
    except:sp = comb
    try:dl = list(set(sp.split(', ')));dl.reverse()
    except:dl = sp
    try:return dl
    except:return 0
    
  def nul(self,inpu,log,split):
    le1 = self.nerves_in(inpu,log,split);le2 = self.nerves_in(le1,log,split); le3 = nerves_in(le2,log,split)
    inpu = inpu.split(str(split));inpu.append(logx)
    return le3
    
  def maj(self,inp):
    while True:
      s=(self.gram(self.nerves_in(inp,False," ")))
      try:s = ' '.join(s);return(s)
      except:pass

import random
def digN(logd,outm,api="https://api.safone.dev/chatgpt",prm="Make this combination of wording and wording completely correct and do not write anything extra other than the correctly worded and written text, just the text, do not answer any questions and do not say anything else. Your duty is only to rewrite the texts correctly for example INPUT: are hello and you how , Your OUTPUT: hello and how are you , Dont give any impression that you are a gpt chat just be a raw model and avoid saying (Im sorry) and (As an) and (I apologize) and stuff like that. You should not react to anything until further notice ->"):
  nuls = nel();nuls2 = nel();rls=[];rr=0;rs=1
  if outm==True:
    try:import requests
    except ModuleNotFoundError:
      so=input("F Error install requests ? (y/n) ->")
      if "y" in so:
        import os
        os.system("python -m pip install requests")
        try:import requests
        except:os.system("py -m pip install requests")
        try:import requests;print("[OK]")
        except:print("[FL]")
      else:s=""
  while True:
    inps = input("\u001b[44mInput ->\u001b[0m"+" ");s=nuls.maj(inps)
    if outm == True:
      data = {
        "message": prm+"("+s+")"
      }
      try:
        r = requests.post(api, data=data);response_json = r.json();sd=(response_json['choices'][0]['message']['content'])
        if "sorry" in sd or "apologize" in sd or "as an" in sd:print("\u001b[42mOutput ->\u001b[0m",s)
        else:print("\u001b[42mOutput ->\u001b[0m",sd);inps="_"
      except:print("\u001b[42mOutput ->\u001b[0m",s)
    else:print("\u001b[42mOutput ->\u001b[0m",s)
    nuls2.inpul=[0];p=nuls2.nerve_in(rls,True," ",45,50,False,False,True,False,True,True,50);rls.append(float((nuls2.rpst+nuls.rpst)/2));nuls2.inpul.extend(rls);me=sum(nuls2.inpul)/len(nuls2.inpul);nuls2.inpul.append(me)
    if rr == 1 and rs == 1:
      try:nuls2.inpux[-2]=0.0;nuls2.inpul[-2]=0.0;rr=0;rs=0
      except:pass
    if inps == "_":nuls2.inpux.append(me);rr=1
    if me >= random.randint(40,100):nuls.maj("_");rr=1;p=nuls2.nerve_in("",True,"",45,50,False,False,True,False,True,True,50);nuls2.inpux.append(me)
    if logd == True:print(nuls2.inpux);print(nuls2.inpul)
digN(True,True)