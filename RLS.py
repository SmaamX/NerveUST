
class nel:
  import random
  inpul = ["0"];inpux = [];inpulx = [];logx = [];pronouns = ['i', 'you', 'he', 'she', 'it', 'we', 'they', 'myself', 'yourself', 'herself', 'himself', 'itself', 'oneself', 'ourselves', 'yourselves', 'themselves', 'each other', 'one another', 'whoever', 'whomever', 'whatsoever', 'whosoever', 'whichever', 'whichever way'];verbs = ['is', 'was', 'run', 'eat', 'think', 'feel', 'become', 'begin', 'bring', 'build', 'buy', 'call', 'carry', 'catch', 'choose', 'come', 'cost', 'cut', 'dance', 'deal', 'depend', 'deserve', 'destroy', 'die', 'dig', 'do', 'draw', 'dream', 'drink', 'drive', 'eat', 'end', 'enter', 'escape', 'expect', 'explain', 'fall', 'feed', 'feel', 'fight', 'find', 'finish', 'fit', 'fly', 'follow', 'forget', 'forgive', 'freeze', 'get', 'give', 'go', 'grow', 'hang', 'have', 'hear', 'help', 'hide', 'hit', 'hold', 'hope', 'hurt', 'include', 'injure', 'intend', 'introduce', 'invite', 'join', 'jump', 'keep', 'kill', 'kiss', 'know', 'laugh', 'learn', 'leave', 'lend', 'lie', 'lift', 'light', 'like', 'listen', 'live', 'lose', 'love', 'make', 'mean', 'meet', 'melt', 'mind', 'miss', 'move', 'murder', 'need', 'offer', 'open', 'operate', 'order', 'organize', 'own', 'pack', 'paint', 'park', 'pay', 'peel', 'pick', 'place', 'plan', 'play', 'please', 'point', 'poison', 'polish', 'possess', 'pour', 'pray', 'prepare', 'press', 'pretend', 'print', 'produce', 'promise', 'protect', 'pull', 'push', 'put', 'question', 'race', 'rain', 'raise', 'reach', 'read', 'realize', 'receive', 'recognize', 'recommend', 'record', 'refuse', 'regret', 'relate', 'relax', 'release', 'rely', 'remain', 'remember', 'remove', 'rent', 'repair', 'repeat', 'replace', 'report', 'represent', 'rescue', 'rest', 'return', 'reveal', 'ride', 'ring', 'rise', 'rob', 'roll', 'run', 'rush', 'sail', 'say', 'scare', 'scratch', 'scream', 'screw', 'scrub', 'search', 'see', 'sell', 'send', 'separate', 'serve', 'set', 'settle', 'sew', 'shake', 'shave', 'shine', 'shoot', 'shop', 'show', 'shrink', 'shut', 'sing', 'sink', 'sit', 'ski', 'sleep', 'slide', 'slip', 'smell', 'smile', 'smoke', 'sneeze', 'soak', 'solve', 'sort', 'sound', 'speak', 'speed', 'spend', 'spill', 'spin', 'spit', 'split', 'spoil', 'spread', 'spring', 'sprinkle', 'squeeze', 'stab', 'stand', 'start', 'stay', 'steal', 'stick', 'stir', 'stop', 'store', 'stretch', 'strike', 'study', 'stuff', 'stumble', 'succeed', 'suck', 'suffer', 'suggest', 'suit', 'supply', 'support', 'surprise', 'swallow', 'sweep', 'swim', 'swing', 'talk', 'taste', 'teach', 'tear', 'tell', 'test', 'thank', 'think', 'throw', 'tie', 'tighten', 'tip', 'touch', 'trade', 'train', 'translate', 'travel', 'treat', 'tremble', 'try', 'turn', 'type', 'understand', 'undress', 'unfold', 'unlock', 'unpack', 'upset', 'use', 'vacuum', 'value', 'visit', 'vote', 'wait', 'wake', 'walk', 'wander', 'want', 'warm', 'wash', 'waste', 'watch', 'water', 'wear', 'weave', 'weep', 'weigh', 'welcome', 'wet', 'wheel', 'whisper', 'whistle', 'win', 'wind', 'wipe', 'wish'];articles = ['the', 'a', 'an'];com = ['clear'];rpst=None
  def inpuld(x):
    back = self.inpul 
    self.inpul = x
    return back
  r = True

  def gram(self,words):
    try:
      pos_t = {
        "NN": lambda w: w.lower()[-3:] == "ist",
        "VB": lambda w: w.lower() in self.verbs,  
        "JJ": lambda w: w.lower()[-4:] == "iest"
      }
      self.adjectives = [w for w in words if pos_t["JJ"](w)]
      self.nouns = [w for w in words if pos_t["NN"](w)]
      words = sorted(words, key=lambda w: (0,1) if pos_t["JJ"](w) else (1,0)) 
      words = sorted(words, key=lambda w: (0,2) if pos_t["NN"](w) else (2,0))
      words = sorted(words, key=lambda w: (0,3) if w.lower() in self.verbs else (3,0))
      words = sorted(words, key=lambda w: (self.pronouns.index(w.lower()), w) if w.lower() in self.pronouns else (4, w))
      words = sorted(words, key=lambda w: (self.articles.index(w.lower()), w) if w.lower() in self.articles else (5, w))
      for item in words:
        if item.endswith('?') or item.endswith('!'):
          words.remove(item)
          words.append(item)
      return words
    except: return words
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
        if inpu[0] == 'pron_':
          self.pronouns.append(self.inpulx)
          flat = []
          for item in self.pronouns:
            if isinstance(item, list):flat.extend(item)
            else:flat.append(item)
          self.pronouns = flat
          if re == False:inpu.remove('pron_');re2=True
      except:pass
      try:
        if inpu[0] == 'verb_':
          self.verbs.append(self.inpulx)
          flat = []
          for item in self.verbs:
            if isinstance(item, list):flat.extend(item)
            else:flat.append(item)
          self.verbs = flat
          if re == False:inpu.remove('verb_');re3=True
      except:pass
      try:
        if inpu[0] == 'arti_':
          self.articles.append(self.inpulx)
          flat = []
          for item in self.articles:
            if isinstance(item, list):flat.extend(item)
            else:flat.append(item)
          self.articles = flat
          if re == False:inpu.remove('arti_');re4=True
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
def digN(logd):
  nuls = nel();nuls2 = nel();rls=[];rr=0
  while True:
    inps = input("Input -> ");s=nuls.maj(inps);print("Output ->",s);nuls2.inpul=[0];p=nuls2.nerve_in(rls,True," ",45,50,False,False,True,False,True,True,50);rls.append(float((nuls2.rpst+nuls.rpst)/2));nuls2.inpul.extend(rls);me=sum(nuls2.inpul)/len(nuls2.inpul);nuls2.inpul.append(me)
    if rr == 1:nuls2.inpux[-2]=0.0;nuls2.inpul[-2]=0.0;rr=0
    if inps == "_":nuls2.inpux.append(me);rr=1
    if me >= random.randint(40,100):nuls.maj("_");rr=1;p=nuls2.nerve_in("",True,"",45,50,False,False,True,False,True,True,50);nuls2.inpux.append(me)
    if logd == True:print(nuls2.inpux);print(nuls2.inpul)
digN(True)