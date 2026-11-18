N=(-33,-31,-18,-14,14,18,31,33);B=(-17,-15,15,17);R=(-16,-1,1,16);K=B+R
V=dict(zip('PNBRQKpnbrqk',(100,320,330,500,900,0)*2));I=1e9;Z=dict(N=N,K=K,B=B,R=R,Q=B+R)
S=b"@@@@^^^^JJOTEEJO@EEJ@@EE@@@@@@@@',11,6@@6@EJ;@JJ;@JJ6@EJ16@@',116;;;;@EE;@EJ@EJJ@EJJ@EJJ;@EE6;;;@@@@@@@@;@@@;@@@;@@@;@@@@@EE@@@E6;;;;@@@@@EE@@EE;@EE;@@@;@@@6;;;,11666;@;;@@;;@@;;@@66;@166;,116"
n=0;C=50000;X=TimeoutError;L=[0]*128;T={}
def setup(f):
 global b,t,c,e
 p=f.split();s=''.join('.'*int(h)if h<'A'else h for h in p[0]if h!='/')
 b=[s[i-i//16*8]if i%16<8 else ' 'for i in range(128)]
 t=(p[1]=='w')*2-1;c=p[2].strip('-');q=p[3];e=(8-int(q[1]))*16+ord(q[0])-97 if q!='-' else -1
def A(s,w):
 S=('PNBRQK','pnbrqk')[w<0]
 for d in N+K:
  x=s+d
  if x&0x88<1 and(b[x]==S[1+(d in K)*4]or abs(d)in(15,17)and d*w>0 and b[x]==S[0]):return 1
 for d in B+R:
  x=s+d
  while x&0x88<1:
   p=b[x]
   if p!='.':
    if p in (S[4],S[2+(d in R)]):return 1
    break
   x+=d
 return 0
def G(o=False,J=0):
 m=[];w=t;H=lambda x,r:m.extend((f,x,q)for q in('QRBN'if r%7<1 else['']))
 for f,p in enumerate(b):
  if p<'A'or(p<'a')^(w>0):continue
  u=p.upper()
  if u=='P':
   d=-16*w;v=f+d
   if v&0x88<1 and b[v]<'A' and not o:
    r=v//16;H(v,r)
    if f//16==1+5*(w>0) and b[f+2*d]<'A':m.append((f,f+2*d,''))
   for x in (f+d-1,f+d+1):
    if x&0x88:continue
    q=b[x]
    if q!='.' and (q<'a')==(w<0):
     r=x//16;H(x,r)
    elif x==e:m.append((f,x,''))
  else:
   for d in Z[u]:
    x=f+d
    while x&0x88<1:
     q=b[x]
     if q<'A':
      if not o:m.append((f,x,''))
      if u in 'NK':break
      x+=d;continue
     if (q<'a')==(w<0):m.append((f,x,''))
     break
 if not o:
  for r,ks,rs,ts in(('K',116,119,118),('Q',116,112,114),('k',4,7,6),('q',4,0,2)):
   if r in c and b[rs]=='Rr'[w<0] and set(b[min(ks,rs)+1:max(ks,rs)])=={'.'} and all(not A(x,-w)for x in range(min(ks,ts),max(ks,ts)+1)):m.append((ks,ts,''))
 for v in m[:]:
  u=D(v)
  if A(b.index('Kk'[-t<0]),t):m.remove(v)
  U(u)
 m.sort(key=lambda v:(v==J)*1e3+V.get(b[v[1]],0)*10-V[b[v[0]]],reverse=1)
 return m
def D(m):
 global t,c,e
 f,x,pr=m;p=b[f];u=[f,x,pr,b[x],c,e,0,0];b[x]=p;b[f]='.'
 if p in 'Pp' and x==e:u[6]=x+16*t;u[7]=b[u[6]];b[u[6]]='.'
 if pr:b[x]=(pr,pr.lower())[t<0]
 if p in 'Kk' and abs(x-f)==2:
  g=x+(-1,1)[x<f];h=x+(1,-2)[x<f];u[6]=g;u[7]=b[g];b[g]='Rr'[t<0];b[h]='.'
 for h,ks,rs in zip('KQkq',(116,116,4,4),(119,112,7,0)):
  if f in(ks,rs)or x==rs:c=c.replace(h,'')
 e=(f+x)//2 if p in 'Pp' and abs(x-f)==32 else -1;t=-t;return u
def U(u):
 global t,c,e
 f,x,pr,q,c,e,g,r=u;t=-t;p=b[x];b[f]=p
 if pr:b[f]='Pp'[t<0]
 b[x]=q
 if g:
  if p in 'Kk' and abs(x-f)==2:b[x+(1,-2)[x<f]]='Rr'[t<0]
  b[g]=r
def Y():
 s=0
 for i,p in enumerate(b):
  if p<'A':continue
  r=i//16;j=(7-r,r)[p<'a']*4+min(i%16,7-i%16)
  v=V[p]+S['PNBRQK'.index(p.upper())*32+j]-64-5*(p in'Pp'and b[i+(16,-16)[p<'a']]==p)
  if p in'Rr':q=b[i%16::16];v+=15*(not('P'in q or'p'in q))
  if(p=='P'and r<2)or(p=='p'and r>5):v+=20
  s+=v if p<'a' else -v
 return (s+30*((b.count('B')>1)-(b.count('b')>1)))*t
def F(d,a,be,pl):
 global n
 n+=1;K=0
 if n>C:raise X
 if d<1:
  a=max(a,Y())
  if a>=be:return be
 else:
  K=(tuple(b),t,c,e);z=T.get(K)
  if z and z[0]>=d and z[1]>=be:return be
  if z:L[pl]=z[3]
 k=b.index('Kk'[t<0]);h=A(k,-t)
 if d and h:d+=1
 m=G(d<1 and h<1,L[pl])
 if not m:return h and pl-I or a*(d<1)
 for v in m:
  u=D(v);x=-F(d-1,-be,-a,pl+1);U(u)
  if x>=be:L[pl]=v;T[K]=(d,be,1,v);return be
  if x>a:a=x
 return a
def W():
 global n
 n=best=0
 len(T)>1e5 and T.clear()
 for d in range(6):
  try:
   r=[(lambda u:(-F(d,-I,I,1),U(u),m)[::2])(D(m))for m in G()]
   if r:best=max(r)[1]
  except X:break
 return best
def al(m):
 f,x,pr=m;a=lambda v:chr(97+v%16)+str(8-v//16);return a(f)+a(x)+pr.lower()
import json,os,urllib.request as u
E=os.getenv('MAKEFUN_ENV_URL')
def P(p,b):
 q=u.Request(E+p,json.dumps(b).encode())
 return json.load(u.urlopen(q))
while 1:
 g=P('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  setup(g['fen']);m=W();m=al(m)if m else'';v=g['legal_moves'];g=P('/move',{'game':g['game'],'move':m if m in v else v[0]})
