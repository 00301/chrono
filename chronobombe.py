import time
import tkinter as tk

def play(h:int=1,m:int=0,s:int=0)->None:
    def play_pressed(list_var)->None:
        list_var[2]=not list_var[2]
        text_boutton_play.set(["play","pause"][list_var[2].real])
        fenetre0.update()
    
    def recommencer_pressed(list_var)->None:
        list_var[3]=time.monotonic()
        list_var[1]=list_var[0]
        list_var[4]=False
        
        s_restant:float=list_var[1]%60
        m_restant:int=int(list_var[1]//60)
        h_restant:int=int(m_restant//60)
        code.set("")
        timer.set(f"{h_restant}:{m_restant%60}:"+str(float(s_restant))[:4])
        fenetre0.update()
    
    def valider_pressed(list_var)->None:
        if code.get()=="582614":
            list_var[4]=True
            
            find:tk.Label=tk.Label(fenetre0,text="trouvé",font=("Helvetica",50),bg="#000000",fg="#FFFFFF")
            find.pack(pady=0)
        fenetre0.update()
    
    all_s:float or int=h*3600+m*60+s
    s_rest:float or int=all_s
    is_play:bool=True
    t0:float=time.monotonic()
    is_find:bool=False
    list_var:list[any]=[all_s,s_rest,is_play,t0,is_find]
    
    fenetre0:tk.Tk=tk.Tk()
    fenetre0.title("chronobombe")
    fenetre0.geometry("1080x720")
    fenetre0.minsize(1080,720)
    fenetre0.config(bg='#000000')
    fenetre0.bind("<Key>",lambda x:fenetre0.destroy()if x.keysym=="Escape"else None)
    
    timer:tk.StringVar=tk.StringVar()
    timer.set(f"{h}:{m}:"+str(float(s))[:4])
    
    titre:tk.Label=tk.Label(fenetre0,textvariable=timer,font=("DS-Digital",30),bg='#000000',fg="#ff0000")
    titre.pack(pady=10,side="top")
    
    code:tk.StringVar=tk.StringVar()
    code.set("")
    
    inp_code:tk.Entry=tk.Entry(fenetre0,textvariable=code,font=("Helvetica",15),bg="#FFFFFF",fg="#000000",width=30)
    inp_code.pack(pady=20)
    
    boutton_valid:tk.Button=tk.Button(fenetre0,text="valider",command=lambda:valider_pressed(list_var))
    boutton_valid.pack(pady=40,side="top")
    
    boutton_quit:tk.Button=tk.Button(fenetre0,text="Quitter",command=fenetre0.destroy)
    boutton_quit.pack(pady=40,side="bottom")
    
    text_boutton_play:tk.StringVar=tk.StringVar()
    text_boutton_play.set("pause")
    
    boutton_play:tk.Button=tk.Button(fenetre0,textvariable=text_boutton_play,command=lambda:play_pressed(list_var))
    boutton_play.pack()
    
    boutton_reco:tk.Button=tk.Button(fenetre0,text="recommencer",command=lambda:recommencer_pressed(list_var))
    boutton_reco.pack(pady=0)
    
    fenetre0.update()
    list_var:list[any]=[all_s,s_rest,is_play,t0,is_find]
    
    while fenetre0._tclCommands!=None:
        if list_var[2]and not list_var[4]and list_var[1]>0:
            t1:float=time.monotonic()
            list_var[1]:float=list_var[0]-t1+list_var[3]
            s_restant:float=list_var[1]%60
            m_restant:int=int(list_var[1]//60)
            h_restant:int=int(m_restant//60)
            timer.set(f"{h_restant}:{m_restant%60}:"+str(float(s_restant))[:4])
        elif not list_var[2]and not list_var[4]and list_var[1]>0:
            t2=time.monotonic()
            list_var[3]+=t2-t1
            t1=t2
        fenetre0.update()
        time.sleep(0.1)

if __name__=="__main__":
    play()
