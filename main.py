N=(-33,-31,-18,-14,14,18,31,33);K=(-17,-16,-15,-1,1,15,16,17);B=(-17,-15,15,17);R=(-16,-1,1,16)
V=dict(zip('PNBRQKpnbrqk',(100,320,330,500,900,0)*2));I=10**9
Z={'N':N,'K':K,'B':B,'R':R,'Q':B+R}
n=0;C=50000;X=TimeoutError
def setup(f='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -'):
 global b,t,c,e
 p=f.split();s=''.join('.'*int(h)if h.isdigit()else h for h in p[0].replace('/',''))
 b=[s[i//16*8+i%16]if i%16<8 else ' 'for i in range(128)]
 t=(p[1]=='w')*2-1;c=p[2].replace('-','');q=p[3];e=(8-int(q[1]))*16+ord(q[0])-97 if q!='-' else -1
def A(s,w):
 S=('PNBRQK','pnbrqk')[w<0]
 for d in (15,17):
  x=s+d*w
  if not x&0x88 and b[x]==S[0]:return 1
 for d in N+K:
  x=s+d
  if not x&0x88 and ((d in N and b[x]==S[1]) or (d in K and b[x]==S[5])):return 1
 for d in B+R:
  x=s+d
  while not x&0x88:
   p=b[x]
   if p!='.':
    if p in (S[4],S[2+(d in R)]):return 1
    break
   x+=d
 return 0
def G(o=False):
 m=[];w=t;H=lambda x,r:m.extend((f,x,q)for q in('QRBN'if r in(0,7)else['']))
 for f,p in enumerate(b):
  if p<'A' or (p<'a')!=(w==1):continue
  u=p.upper()
  if u=='P':
   d=-16*w;v=f-16*w
   if not v&0x88 and b[v]<'A' and not o:
    r=v//16;H(v,r)
    if f//16==6-(w<0)*5 and b[f+2*d]<'A':m.append((f,f+2*d,''))
   for x in (f+d-1,f+d+1):
    if x&0x88:continue
    q=b[x]
    if q!='.' and (q<'a')!=(w==1):
     r=x//16;H(x,r)
    elif x==e:m.append((f,x,''))
  else:
   for d in Z[u]:
    x=f+d
    while not x&0x88:
     q=b[x]
     if q<'A':
      if not o:m.append((f,x,''))
      if u in 'NK':break
      x+=d;continue
     if (q<'a')!=(w==1):m.append((f,x,''))
     break
 if not o:
  for ks,rs,ts in ((116,119,118),(116,112,114),(4,7,6),(4,0,2)):
   r='KQkq'[(ks==4)*2+(ts<ks)]
   if r in c and b[rs]=='Rr'[w<0] and all(b[x]<'A'for x in range(min(ks,rs)+1,max(ks,rs))) and all(not A(x,-w)for x in range(min(ks,ts),max(ks,ts)+1)):m.append((ks,ts,''))
 for v in m[:]:
  u=D(v)
  if A(b.index('Kk'[-t<0]),t):m.remove(v)
  U(u)
 return m
def D(m):
 global t,c,e
 f,x,pr=m;p=b[f];u=[f,x,pr,b[x],c,e,None,None];b[x]=p;b[f]='.'
 if p in 'Pp' and x==e:u[6]=x+16*t;u[7]=b[u[6]];b[u[6]]='.'
 if pr:b[x]=pr if t==1 else pr.lower()
 if p in 'Kk' and abs(x-f)==2:
  g=x-1 if x>f else x+1;h=x+1 if x>f else x-2;u[6]=g;u[7]=b[g];b[g]='R' if t==1 else 'r';b[h]='.'
 for h,ks,rs in zip('KQkq',(116,116,4,4),(119,112,7,0)):
  if (p.upper()=='K' and f==ks) or f==rs or x==rs:c=c.replace(h,'')
 e=(f+x)//2 if p.upper()=='P' and abs(x-f)==32 else -1;t=-t;return u
def U(u):
 global t,c,e
 f,x,pr,q,c,e,g,r=u;t=-t;p=b[x];b[f]=p
 if pr:b[f]='P' if t==1 else 'p'
 b[x]=q
 if g is not None:
  if p in 'Kk' and abs(x-f)==2:b[x+1 if x>f else x-2]='R' if t==1 else 'r'
  b[g]=r
def F(d,a,be,pl):
 global n
 n+=1
 if n>C:raise X
 if d==0:
  s=0
  for i,p in enumerate(b):
   if p<'A':continue
   v=V[p];r=i//16;f=i%16;z=7-abs(f-3.5)-abs(r-3.5)
   v+=48-8*r if p=='P' else r*8 if p=='p' else 6*z if p in 'NBnb' else 2*z if p in 'Qq' else -int(5*z) if p in 'Kk' else 0
   s+=v if p<'a' else -v
  s*=t;a=max(a,s)
  if s>=be:return be
  m=G(True)
 else:
  m=G()
  if not m:return pl-100000 if A(b.index('Kk'[t<0]),-t) else 0
  m.sort(key=lambda v:V.get(b[v[1]],0)*10-V[b[v[0]]],reverse=True)
 for v in m:
  u=D(v);x=-F(max(d-1,0),-be,-a,pl+1);U(u)
  if x>=be:return be
  if x>a:a=x
 return a
def W(md=6):
 global n
 best=None
 for d in range(1,md+1):
  n=0
  try:
   r=[]
   for m in G():
    u=D(m);r.append((-F(d-1,-I,I,1),m));U(u)
   if r:best=max(r)[1]
  except X:break
 return best
def al(m):
 f,x,pr=m;a=lambda v:chr(97+v%16)+str(8-v//16);return a(f)+a(x)+pr.lower()
import json,os,urllib.request as u
E=os.environ['MAKEFUN_ENV_URL']
def P(p,b):
 q=u.Request(E+p,data=json.dumps(b).encode(),headers={'content-type':'application/json'})
 return json.load(u.urlopen(q))
while 1:
 g=P('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  setup(g['fen']);m=W(3);m=al(m)if m else'';g=P('/move',{'game':g['game'],'move':m if m in g['legal_moves'] else g['legal_moves'][0]})
