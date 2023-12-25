import random
import subprocess
import time
inpul = ["0"]
inpux = []
inpulx = []
logx = []
pronouns = ['i', 'you', 'he', 'she', 'it', 'we', 'they', 'myself', 'yourself', 'herself', 'himself', 'itself', 'oneself', 'ourselves', 'yourselves', 'themselves', 'each other', 'one another', 'whoever', 'whomever', 'whatsoever', 'whosoever', 'whichever', 'whichever way']
verbs = ['is', 'was', 'run', 'eat', 'think', 'feel', 'become', 'begin', 'bring', 'build', 'buy', 'call', 'carry', 'catch', 'choose', 'come', 'cost', 'cut', 'dance', 'deal', 'depend', 'deserve', 'destroy', 'die', 'dig', 'do', 'draw', 'dream', 'drink', 'drive', 'eat', 'end', 'enter', 'escape', 'expect', 'explain', 'fall', 'feed', 'feel', 'fight', 'find', 'finish', 'fit', 'fly', 'follow', 'forget', 'forgive', 'freeze', 'get', 'give', 'go', 'grow', 'hang', 'have', 'hear', 'help', 'hide', 'hit', 'hold', 'hope', 'hurt', 'include', 'injure', 'intend', 'introduce', 'invite', 'join', 'jump', 'keep', 'kill', 'kiss', 'know', 'laugh', 'learn', 'leave', 'lend', 'lie', 'lift', 'light', 'like', 'listen', 'live', 'lose', 'love', 'make', 'mean', 'meet', 'melt', 'mind', 'miss', 'move', 'murder', 'need', 'offer', 'open', 'operate', 'order', 'organize', 'own', 'pack', 'paint', 'park', 'pay', 'peel', 'pick', 'place', 'plan', 'play', 'please', 'point', 'poison', 'polish', 'possess', 'pour', 'pray', 'prepare', 'press', 'pretend', 'print', 'produce', 'promise', 'protect', 'pull', 'push', 'put', 'question', 'race', 'rain', 'raise', 'reach', 'read', 'realize', 'receive', 'recognize', 'recommend', 'record', 'refuse', 'regret', 'relate', 'relax', 'release', 'rely', 'remain', 'remember', 'remove', 'rent', 'repair', 'repeat', 'replace', 'report', 'represent', 'rescue', 'rest', 'return', 'reveal', 'ride', 'ring', 'rise', 'rob', 'roll', 'run', 'rush', 'sail', 'say', 'scare', 'scratch', 'scream', 'screw', 'scrub', 'search', 'see', 'sell', 'send', 'separate', 'serve', 'set', 'settle', 'sew', 'shake', 'shave', 'shine', 'shoot', 'shop', 'show', 'shrink', 'shut', 'sing', 'sink', 'sit', 'ski', 'sleep', 'slide', 'slip', 'smell', 'smile', 'smoke', 'sneeze', 'soak', 'solve', 'sort', 'sound', 'speak', 'speed', 'spend', 'spill', 'spin', 'spit', 'split', 'spoil', 'spread', 'spring', 'sprinkle', 'squeeze', 'stab', 'stand', 'start', 'stay', 'steal', 'stick', 'stir', 'stop', 'store', 'stretch', 'strike', 'study', 'stuff', 'stumble', 'succeed', 'suck', 'suffer', 'suggest', 'suit', 'supply', 'support', 'surprise', 'swallow', 'sweep', 'swim', 'swing', 'talk', 'taste', 'teach', 'tear', 'tell', 'test', 'thank', 'think', 'throw', 'tie', 'tighten', 'tip', 'touch', 'trade', 'train', 'translate', 'travel', 'treat', 'tremble', 'try', 'turn', 'type', 'understand', 'undress', 'unfold', 'unlock', 'unpack', 'upset', 'use', 'vacuum', 'value', 'visit', 'vote', 'wait', 'wake', 'walk', 'wander', 'want', 'warm', 'wash', 'waste', 'watch', 'water', 'wear', 'weave', 'weep', 'weigh', 'welcome', 'wet', 'wheel', 'whisper', 'whistle', 'win', 'wind', 'wipe', 'wish']
articles = ['the', 'a', 'an']
com = ['clear']
def inpuld(x):
  global inpul
  back = inpul 
  inpul = x
  return back
r = True

def gram(words):
  global pronouns
  global verbs
  global articles
  try:
    pos_t = {
      "NN": lambda w: w.lower()[-3:] == "ist",
      "VB": lambda w: w.lower() in verbs,  
      "JJ": lambda w: w.lower()[-4:] == "iest"
    }
    adjectives = [w for w in words if pos_t["JJ"](w)]
    nouns = [w for w in words if pos_t["NN"](w)]
    words = sorted(words, key=lambda w: (0,1) if pos_t["JJ"](w) else (1,0)) 
    words = sorted(words, key=lambda w: (0,2) if pos_t["NN"](w) else (2,0))
    words = sorted(words, key=lambda w: (0,3) if w.lower() in verbs else (3,0))
    words = sorted(words, key=lambda w: (pronouns.index(w.lower()), w) if w.lower() in pronouns else (4, w))
    words = sorted(words, key=lambda w: (articles.index(w.lower()), w) if w.lower() in articles else (5, w))
    for item in words:
      if item.endswith('?') or item.endswith('!'):
        words.remove(item)
        words.append(item)
    return words
  except: return words

def nerve_in(inpu,log,split,sts,sts2,res,res2,lear,logxb,tll):
  def run(inpu,log):
    global inpul
    global inpux
    global inpulx
    global r
    global pronouns
    global verbs
    global articles
    global logx
    global com
    trm = False
    re = False
    re2 = False
    re3 = False
    re4 = False
    re5 = False
    out = []
    numr = 0
    nume = 0
    st1 = set(str(inpu))
    st2 = set(str(inpulx))
    intersect = st1.intersection(st2)
    uniont = st1.union(st2)
    rpt = len(intersect) / len(uniont)
    rpst = rpt * 100
    try:
      if rpt >= random.randint(sts-10,sts):inpu.append(inpulx)
    except:pass
    s1 = set(str(inpu))
    s2 = set(str(inpux))
    intersec = s1.intersection(s2)
    union = s1.union(s2)
    rp = len(intersec) / len(union)
    rps = rp * 100
    try:inpu = inpu.split(str(split))
    except:pass
    try:
      #Each is different and may require changes
      if inpu[0] == '_':
        inpux.append(inpulx)
        flat = []
        for item in inpux:
          if isinstance(item, list):flat.extend(item)
          else:flat.append(item)
        inpux = flat
        if re == False:inpu.remove('_');re=True
    except:pass
    try:
      if inpu[0] == 'pron_':
        pronouns.append(inpulx)
        flat = []
        for item in pronouns:
          if isinstance(item, list):flat.extend(item)
          else:flat.append(item)
        pronouns = flat
        if re == False:inpu.remove('pron_');re2=True
    except:pass
    try:
      if inpu[0] == 'verb_':
        verbs.append(inpulx)
        flat = []
        for item in verbs:
          if isinstance(item, list):flat.extend(item)
          else:flat.append(item)
        verbs = flat
        if re == False:inpu.remove('verb_');re3=True
    except:pass
    try:
      if inpu[0] == 'arti_':
        articles.append(inpulx)
        flat = []
        for item in articles:
          if isinstance(item, list):flat.extend(item)
          else:flat.append(item)
        articles = flat
        if re == False:inpu.remove('arti_');re4=True
    except:pass
    try:
      if inpu[0] == 'outme_':
        if re == False:inpu.remove('outme_')
        print(inpul)
    except:pass
    try:
      if inpu[0] == 'com_':
        com.append(inpulx)
        flat = []
        for item in com:
          if isinstance(item, list):flat.extend(item)  
          else:flat.append(item)
        com = flat;output = subprocess.check_output(inpulx, shell=True);print(output)
        if re == False:
          inpu.remove('com_');re5=True
    except Exception as e:
      com.append(e)
    if re or re2 or re3 or re4 or re5: rem = True
    else: rem = False
    if rem == False:
      flat = []
      inputw = []
      try:inpu = inpu.split(str(split))
      except:pass
      try:
        for item in inpu:
          if item.endswith("?") or item.endswith("!"):
            inputw.append(item)
            inpu.remove(item)
        inpu.extend(inputw)
      except:pass
      for item in logx:
        if isinstance(item, list):flat.extend(item)
        else:flat.append(item)
      logx = flat
      if logxb == True:inpu.append(logx)
      re=True
    for x in inpu:
      #print(inpul)
        if rps < random.randint(sts2-10,sts2):
          if x in inpu:
            for r in inpul:
              if tll == True:
                try: nld = [i for i, n in enumerate(inpul) if n == r];rs=2
                except:pass
              else:
                try: nl = inpul.index(x)
                except:pass
            try:
              for nl in nld:
                if lear == True:
                  if str(x) in inpul or str(x) in inpulx:
                    inpul.insert(nl,inpu)
                    flat = []
                    for item in inpul:
                      if isinstance(item, list):flat.extend(item)
                      else:flat.append(item)
                    inpul = flat
                    if res2 == True:inpul.append(inpu[inpu.index(x)]);inpul.append(inpu[int(inpu.index(x))-1])
                    else:inpul.append(inpu[inpu.index(x)]);inpul.append(inpu[int(inpu.index(x))+1])
                  numm = 1
                  for n in range(len(inpu)):
                    numm += 1
                    if inpu[inpu.index(x)+n] != None:
                      inpul.append(inpu[int(inpu.index(x))+n])
            except:pass
            try:
              if res2 == True:
                for xn in range(len(inpu)):out.append(inpul[nl - xn])
              else: out.append(inpul[nl + 1]);out.append(inpul[nl + 2])
              if len(out)>1: out.remove(out[0])
            except:pass
          if rps >= random.randint(sts2-10, sts2):
            trm = True
            try:
              for x in inpu:
                if rps >= random.randint(sts2-10, sts2):
                  try:
                    nl = inpux.index(x)
                    for xn in range(len(inpu)):
                      out.append(inpul[nl + xn])
                  except:pass
                  if trm == False:
                    nl = inpul.index(x)
                    for xn in range(len(inpu)):
                      out.append(inpul[nl + xn])
            except:pass
        numr += 1
    try:
      if log == True:print(inpul);print(rps),print(inpux);print(rpt)
    except:pass
    outref = []
    for it in out:
      if it not in outref:
        outref.append(it)
    if r == True:
      try:
        if len(inpu)>=2: inpul.pop(0);inpul.pop(0);r = False
      except:pass
    if res == True:outref.reverse()
    inpulx = outref
    logx = outref
    return outref
  return run(inpu,log)
def nerves_in(inpu,log,split):
  stglo = nerve_in(inpu,log,split,45,60,False,False,True,True,True)
  stlow = nerve_in(inpu,log,split,45,50,False,False,False,False,True)
  sthi = nerve_in(inpu,log,split,60,70,False,False,False,False,True)
  stb = nerve_in(inpu,log,split,45,50,True,True,False,False,True)
  stb2 = nerve_in(inpu,log,split,45,50,False,True,False,False,True)
  stb3 = nerve_in(inpu,log,split,45,50,True,False,False,False,True)
  comb = []
  if random.randint(0,5) == 5:
    for item in stglo:
      nt = random.randint(0,100)
      if nt <= 60:
        if item in stlow or item in sthi or item in stb or item in stb2 or item in stb3:
            comb.append(item)
      if nt <= 70 and nt > 60:
        if item in stlow or item in sthi and item in stb or item in stb2 or item in stb3:
            comb.append(item)
      if nt <= 80 and nt > 70:
        if item in stlow and item in sthi and item in stb or item in stb2 or item in stb3:
            comb.append(item)
      if nt <= 95 and nt > 80:
        if item in stlow and item in sthi and item in stb and item in stb2 or item in stb3:
            comb.append(item)
      if nt <= 100 and nt > 95:
        if item in stlow and item in sthi or item in stb and item in stb2 and item in stb3:
            comb.append(item)
  else:comb.append(stglo)
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
def nul(inpu,log,split):
  le1 = nerves_in(inpu,log,split);le2 = nerves_in(le1,log,split); le3 = nerves_in(le2,log,split)
  inpu = inpu.split(str(split));inpu.append(logx)
  return le3
if __name__ == '__main__':
  while True:
    s=(gram(nerves_in(input("Input:"),False," ")))
    try:s = ' '.join(s);print(s)
    except:pass
