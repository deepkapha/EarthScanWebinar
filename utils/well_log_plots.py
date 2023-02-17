# operation that overlaps with ImageNet-C's test set
def cali(logs, ax, i,patch_height):
    ax.plot(logs.CALI[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(6, 24)
    ax.invert_yaxis()
    ax.axis('off')
	
def GR(logs, ax, i,patch_height):
    ax.plot(logs.GR[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(0, 150)
    ax.invert_yaxis()
    ax.axis('off')
	
def SP(logs, ax, i,patch_height):
    ax.plot(logs.SP[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(-150, 150)
    ax.invert_yaxis()
    ax.axis('off')
	
def SGR(logs, ax, i,patch_height):
    ax.plot(logs.SGR[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(0, 150)
    ax.invert_yaxis()
    ax.axis('off')
	
def RSHA(logs, ax, i,patch_height):
    ax.plot(logs.RSHA[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(2, 200)
    ax.invert_yaxis()
    ax.axis('off')

def RMED(logs, ax, i,patch_height):
    ax.plot(logs.RMED[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(2, 200)
    ax.invert_yaxis()
    ax.axis('off')
	
def RDEP(logs, ax, i,patch_height):	
    ax.semilogx(logs.RDEP[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(2, 200)
    ax.invert_yaxis()
    ax.axis('off')
    
	
def RXO(logs, ax, i,patch_height):		
    ax.semilogx(logs.RXO[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(2, 200)
    ax.invert_yaxis()
    ax.axis('off')
	
def RMIC(logs, ax, i,patch_height):	
    ax.semilogx(logs.RMIC[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(2, 200)
    ax.invert_yaxis()
    ax.axis('off')
	
def NPHI(logs, ax, i,patch_height):
    ax.plot(logs.NPHI[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(-0.15, 1.05)
    ax.invert_xaxis()
    ax.invert_yaxis()
    ax.axis('off')	
	
  

def RHOB(logs, ax, i,patch_height):	
    ax.plot(logs.RHOB[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(0.95, 2.95)
    ax.invert_yaxis()
    ax.invert_xaxis()
    ax.axis('off')

def PEF(logs, ax, i,patch_height):	
    ax.plot(logs.PEF[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(0, 10)
    ax.invert_yaxis()
    ax.axis('off')

def ROP(logs, ax, i,patch_height):	
    ax.plot(logs.ROP[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(0, 50)
    ax.invert_yaxis()
    ax.axis('off')

def ROPA(logs, ax, i,patch_height):	
    ax.plot(logs.ROPA[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(0, 50)
    ax.invert_yaxis()
    ax.axis('off')
	
def DRHO(logs, ax, i,patch_height):	
    ax.plot(logs.DRHO[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(-0.2, 1)
    ax.invert_yaxis()
    ax.axis('off')
	
def DTC(logs, ax, i,patch_height):	
    ax.plot(logs.DTC[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(40, 240)
    ax.invert_yaxis()
    ax.invert_xaxis()
    ax.axis('off')
	
def DTS(logs, ax, i,patch_height):		
    ax.plot(logs.DTS[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(40, 240)
    ax.invert_yaxis()
    ax.invert_xaxis()
    ax.axis('off')

def MUDWEIGHT(logs, ax, i,patch_height):	
    ax.plot(logs.MUDWEIGHT[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(0, 150)
    ax.invert_yaxis()
    ax.axis('off')

def BS(logs, ax, i,patch_height):	
    ax.plot(logs.BS[i:i+patch_height], list(range(i,i+patch_height)), 'b')
    ax.set_xlim(6, 24)
    ax.invert_yaxis()
    ax.axis('off')
	
log_plots = [
    cali, GR, SP, SGR, RSHA, RMED, RDEP, RXO, RMIC, NPHI, RHOB, PEF, ROP, ROPA, DRHO, DTC, DTS, 
    MUDWEIGHT, BS
]

	

	
