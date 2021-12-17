import os
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pylab
params = {'mathtext.default': 'regular' }          
plt.rcParams.update(params)

M=[i for i in range(-1000,1050,50)] # masses

fii=open("/home/tejas/fractiondata.txt", "w")
fiche=open("/home/tejas/fractiondata_chargino_neutralino.txt", "w")
ri=open("/home/tejas/r_data.txt", "w")
rii=open("/home/tejas/r_data_chargino_neutralino.txt", "w")

print('#mu', '#M2', 'th prediction', 's', 'fraction', file=fii)
print('mC2', 'mN1', 'th prediction', 's', 'fraction', file=fiche)
print('#mu', '#M2', 'r_max', file=ri)
print('#mC2', '#mN1', 'r_max', file=rii)


X=[]    #mu masses
Y=[]    #M2 masses
Z=[]    #fraction values
Zr=[]   #r_max values
X1=[]   #chargino2 masses
Y1=[]   #neutralino1 masses
Y2=[]   #neutralino2 masses
X2=[]   #chargino1 masses
diff2=[]    #chargino1-neutralino1
diff1=[]    #neutralino2-neutralino1

for j in range(len(M)):
    for k in range(len(M)):
        if abs(M[j])<M[k] and M[j]!=0:
            fi=open('/home/tejas/spectrum/ewinos_mu_'+str(M[j])+'_M2_'+str(M[k])+'_M1_'+str(2*M[k])+'.slha', 'r')
            lines=fi.readlines()
            fi.close()
            t=0
            for line in lines:              #cross section of neutralino3 and chargino2^+ production
                if "XSECTION" and "1000025 1000037 # " in line:
                    for i in range(len(lines)):
                        if lines[i]==line:
                            t=i
                        else:
                            pass
            s1=''                      
            u=lines[t+1]
            for w in range(22,37,1):
                s1=s1+u[w]
            if s1=='t. Phys. Commun':
                s1=0
            else:
                s1=s1              
            m=0            
            for line3 in lines:
                if "XSECTION" and "-1000037 1000025 # " in line3: #cross section of neutralino3 and chargino2^- production
                    for i3 in range(len(lines)):
                        if lines[i3]==line3:
                            m=i3
                        else:
                            pass
            s2=''
            v=lines[m+1]
            for q in range(22,37,1):    
                s2=s2+v[q]    
            if s2=='t. Phys. Commun':
                s2=0
            else:
                s2=s2                 
            n=0
            for line1 in lines:
                if "XSECTION" and "-1000037 1000037 # " in line1:#cross section of chargino2^+ and chargino2^- production
                    for i2 in range(len(lines)):
                        if lines[i2]==line1:
                            n=i2
                        else:
                            pass
            s3=''
            w=lines[n+1]
            for p in range(22,37,1):
                s3=s3+w[p]     
            if s3=='t. Phys. Commun':
                s3=0
            else:
                s3=s3                      
            y2=0
            for line4 in lines:
                if "XSECTION" and "1000025 1000025 # " in line4:  #cross section of neutralino3 and neutralino3 production
                    for i4 in range(len(lines)):
                        if lines[i4]==line4:
                            y2=i4
                        else:
                            pass
            s4=''
            w1=lines[y2+1]
            for t2 in range(22,37,1):
                s4=s4+w1[t2] 
            if s4=='t. Phys. Commun':
                s4=0
            else:
                s4=s4                          
            s=float(s1)+float(s2)+float(s3)+float(s4)
            fiii=open('/home/tejas/results/ewinos_mu_'+str(M[j])+'_M2_'+str(M[k])+'_M1_'+str(2*M[k])+'.slha.log', 'r')
            lines2=fiii.readlines()
            fiii.close()
            r=[]
            p=[]
            for line8 in lines2:
                if "Theory prediction:" in line8:
                    pred=''
                    for l in range(19,28,1):
                        pred=pred+line8[l]
                    p.append(float(pred))
                if "Observed r-value:" in line8:
                    rr=''
                    for m in range(18,len(line8),1):
                        rr=rr+line8[m]
                    r.append(float(rr))
            
            if len(r)>0:
                for h2 in range(len(r)):
                    if max(r)<=1 and r[h2]==max(r):
                        thpred=p[h2]
                    else:
                        pass
                fraction=thpred/s
                X.append(M[j])
                Y.append(M[k])
                Z.append(fraction)
                Zr.append(max(r))
                fich=open('/home/tejas/spectrum/ewinos_mu_'+str(M[j])+'_M2_'+str(M[k])+'_M1_'+str(2*M[k])+'.slha', 'r')
                lines3=fich.readlines()
                fich.close()
                mc2=''
                mn1=''
                mc1=''
                mn2=''
                for lin in lines3:
                    if "1000037" and "# ~chargino(2)" in lin:
                        for a1 in range(15,31,1):
                            mc2=mc2+lin[a1]
                for lin in lines3:
                    if "1000022" and "# ~neutralino(1)" in lin:
                        for a2 in range(15,31,1):
                            mn1=mn1+lin[a2]
                for lin in lines3:
                    if "1000023" and "# ~neutralino(2)" in lin:
                        for a3 in range(15,31,1):
                            mn2=mn2+lin[a3]
                for lin in lines3:
                    if "1000024" and "# ~chargino(1)" in lin:
                        for a4 in range(15,31,1):
                            mc1=mc1+lin[a4]
                mn2=abs(float(mn2))                
                mc1=abs(float(mc1))
                mc2=abs(float(mc2))
                mn1=abs(float(mn1))
                dif1=abs(mn2-mn1)
                dif2=abs(mc1-mn1)
                Y2.append(mn2)
                X2.append(mc1)                
                diff1.append(dif1)
                diff2.append(dif2)
                Y1.append(mn1)
                X1.append(mc2)                          
                print(M[j], M[k], thpred, s, fraction, file=fii)
                print(mc2, mn1, thpred, s, fraction, file=fiche)
                print(M[j], M[k], max(r), file=ri)
                print(mc2, mn1, max(r), file=rii)
                                
                       
        else:
            pass

plt.scatter(Y, X, s=50, c=Z, cmap="gist_rainbow")    #plot fraction of production cross section as a function of mu and M2
plt.grid()
cbar = plt.colorbar(orientation="vertical")
plt.clim(0,max(Z))
plt.ylim([-600,600])
plt.xlim([0,610])
cbar.set_label(label="fraction", size=14)
plt.ylabel('mu (GeV)')
plt.xlabel('M2 (GeV)')
plt.title('Plot of fraction of production cross section as a function of mu and M2(for TChiWZ and minmassgap5GeV)')
#plt.savefig('Plot of fraction as a function of mu and M2(TCHiWH and minmassgap5GeV)', dpi=300, bbox_inches='tight')
plt.show()
 
plt.scatter(X1, Y1, s=50, c=Z, cmap="gist_rainbow")    #plot fraction of production cross section as a function of neutralino1 and chargino2 masses
plt.grid()
cbar = plt.colorbar(orientation="vertical")
plt.clim(0,max(Z))
plt.xlim([0,max(X1)+20])
plt.ylim([0,max(Y1)+20])
cbar.set_label(label="fraction", size=14)
plt.xlabel('mass of chargino2 (GeV)')
plt.ylabel('mass of neutralino1 (GeV)')
plt.title('Plot of fraction of production cross section as a function of neutralino1 and chargino2 masses(for TChiWZ and minmassgap 5GeV)')
#plt.savefig('Plot of fraction as a function of neutralino1 and chargino2 masses (TCHiWH and minmassgap5GeV)', dpi=300, bbox_inches='tight')
plt.show()

plt.scatter(Y, X, s=50, c=Zr, cmap="gist_rainbow")    #plot r_max as a function of mu and M2
plt.grid()
cbar = plt.colorbar(orientation="vertical")
plt.clim(0,1.0)
plt.ylim([-600,600])
plt.xlim([0,610])
cbar.set_label(label="r_max", size=14)
plt.ylabel('mu (GeV)')
plt.xlabel('M2 (GeV)')
plt.title('Plot of r_max as a function of mu and M2 for TChiWZ(minmassgap5GeV)')
#plt.savefig('Plot rmax as a function of mu and M2(TCHiWH and minmassgap5GeV)', dpi=300, bbox_inches='tight')
plt.show()

plt.scatter(X1, Y1, s=50, c=Zr, cmap="gist_rainbow")    #plot r_max as a function of neutralino1 and chargino2 masses
plt.grid()
cbar = plt.colorbar(orientation="vertical")
plt.clim(0,1.0)
plt.xlim([0,max(X1)+20])
plt.ylim([0,max(Y1)+20])
cbar.set_label(label="r_max", size=14)
plt.xlabel('mass of chargino2 (GeV)')
plt.ylabel('mass of neutralino1 (GeV)')
plt.title('Plot of r_max as a function of neutralino1 and chargino2 masses for TChiWZ(minmassgap5GeV)')
#plt.savefig('Plot of rmax as a function of neutralino1 and chargino2 masses (TCHiWH and minmassgap5GeV)', dpi=300, bbox_inches='tight')
plt.show()

          
            
