import pygame
import random as ran
import math as mt
import pickle
import datetime

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()



font=pygame.font.SysFont('Comic Sans MS',100)
fonts=pygame.font.SysFont('Comic Sans MS',99)
fonthero=pygame.font.SysFont('Comic Sans MS',14)
fontdragon=pygame.font.SysFont('Comic Sans MS',36)
fonthp=pygame.font.SysFont('Comic Sans MS',25)
fontextreme=pygame.font.SysFont('Comic Sans MS',10)
fontmedio=pygame.font.SysFont('Comic Sans MS',50)
fontok=pygame.font.SysFont('Comic Sans MS',18)
fontrank=pygame.font.SysFont('Comic Sans MS',12)
text1=font.render('Play!',True,(255,0,0))
title=fonts.render('Hero Versus Dragon!',True,(102,0,204))
titleb=font.render('Hero Versus Dragon!',True,(255,0,0))
dragonw=fontdragon.render('Dragon',True,(255,0,0))
dead=font.render('R.I.P 2019-2019',True,(0,0,0))
win=font.render('Victory Royale!',True,(0,128,255))
menuback=fontmedio.render('Back To Menu!',True,(0,0,0))
menubackw=fontmedio.render('Back To Menu!',True,(218,165,32))
controlstext=fontmedio.render('Controls',True,(0,0,210))
tipstext=fontmedio.render('Tips!',True,(0,0,255))
leaderbod=fontmedio.render('Leaderboard',True,(0,0,0))
backtext=fontmedio.render('Back',True,(10,10,10))
enter=fontmedio.render('Enter',True,(0,0,0))
namehere=fonts.render('Enter Name or ID',True,(127,127,127))
typehere=fontmedio.render('Type Here',True,(255,255,255))
nameexist=fontmedio.render('Name Already Exist!',True,(211,0,0))
nameempty=fontmedio.render('Name Can Not Be Empty!',True,(211,0,0))
ctrl1=fontdragon.render('W - Up',True,(255,255,255))
ctrl2=fontdragon.render('A - Left',True,(255,255,255))
ctrl3=fontdragon.render('S - Down',True,(255,255,255))
ctrl4=fontdragon.render('D - Right',True,(255,255,255))
ctrl5=fontdragon.render('Q - Shield',True,(255,255,255))
ctrl6=fontdragon.render('Mouse Left - Attack',True,(255,255,255))
ctrl7=fontdragon.render('Space - Skill',True,(255,255,255))
ctrl8=fontdragon.render('Z - Ultimate',True,(255,255,255))
ctrl9=fontdragon.render('Esc - Pause',True,(255,255,255))
scool=fontok.render('Shield',True,(255,255,255))
sacool=fontok.render('Skill',True,(255,255,255))
ucool=fontok.render('Ulti',True,(255,255,255))
cheat=fontok.render('Cheat Mode: On',True,(255,0,0))
tip1=fonthp.render('1) Hero Armor Formula: dmg=(dmg-dmg*((armour/10000)*(90/100)))',True,(255,255,255))
tip2=fonthp.render('2) Dragon Armor Formula: dmg=(dmg-dmg*((armour/4000)*(99/100)))',True,(255,255,255))
tip3=fonthp.render('3) Heal=2500-6000,DamageUp=3000-5000,ArmorUp=500-1250',True,(255,255,255))
tip4=fonthp.render('4) Dragon Hp<=40000,Fires Beam,Armor+++',True,(255,255,255))
tip5=fonthp.render('5) After 3 Minutes=Hell Mode',True,(255,255,255))
tip6=fonthp.render('6) Konami Code',True,(255,255,255))
tip7=fonthp.render('7) Red Color In Leaderboard=Cheater!',True,(255,255,255))
tip8=fonthp.render("8) Don't Touch The Dragon!",True,(255,255,255))
tip9=fonthp.render("9) Nullify The Fireball With Your Own Attacks!",True,(255,255,255))
me=fonthp.render('Me And Me Only',True,(255,255,255))
credito=fontmedio.render('Credits',True,(188,0,188))
settin=fontmedio.render('Settings',True,(24,24,24))
pauseesc=fontmedio.render('[Esc] To Resume!',True,(0,0,0))
paused=fontmedio.render('Paused',True,(0,0,0))
version=fontok.render('Version 1.0.0.2',True,(255,255,255))




swid=1000
shei=800

screen=pygame.display.set_mode((swid,shei))
pygame.display.set_caption("First Game!")

lwall=100
rwall=swid-100
uwall=100
dwall=shei
r=255
g=127
b=0

music1=r'/var/www/html/First Game!/Music/song1.mp3'
music2=r'/var/www/html/First Game!/Music/song2.mp3'
music3=r'/var/www/html/First Game!/Music/song3.mp3'
music4=r'/var/www/html/First Game!/Music/song4.mp3'
music5=r'/var/www/html/First Game!/Music/song5.mp3'
music6=r'/var/www/html/First Game!/Music/song6.mp3'
music7=r'/var/www/html/First Game!/Music/song7.mp3'
music8=r'/var/www/html/First Game!/Music/song8.mp3'
musiclist=[music1,music2,music3,music4,music5,music6,music7,music8]
musicdraw=0
musicdrawed=[]

healsound=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/heal.wav')
hitsoundweak=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/weakhit.wav')
hitsoundmedio=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/hit.wav')
hitsoundstrong=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/stronghit.wav')
burnsound=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/fire.wav')
diesound=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/die.wav')
buffsound=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/buff.wav')
firesound=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/firestorm.wav')
skillsound=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/skill.wav')
ultisound=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/ulti.wav')
boomsound=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/explode.wav')
attacksound=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/shotgun.wav')
startsound=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/opening.wav')
clicksound=pygame.mixer.Sound(r'/var/www/html/First Game!/Sound/click.wav')


pygame.mouse.set_visible(False)
def music():
    global musiclist,musicdraw,musicdrawed
    pygame.mixer.music.set_volume(0.6*(volume1.musiclength/300))
    if not(pygame.mixer.music.get_busy()):
        musicdraw=ran.randint(0,7)
        #checkdraw=[draw for draw,drawnum in enumerate(musicdrawed)if drawnum==musicdraw]
        if not(musicdraw in musicdrawed):
            pygame.mixer.music.load(musiclist[musicdraw])
            pygame.mixer.music.play(1)
            musicdrawed.append(musicdraw)
        if len(musicdrawed)>=8:
            musicdrawed.clear()

dragon=pygame.image.load(r'/var/www/html/First Game!/Sprite/dragon.png').convert_alpha()
dragonf=pygame.transform.flip(dragon,True,False).convert_alpha()

yuusha=pygame.image.load(r'/var/www/html/First Game!/Sprite/yuusha.png').convert_alpha()

yuushaf=pygame.transform.flip(yuusha,True,False).convert_alpha()

bg=pygame.image.load(r'/var/www/html/First Game!/Sprite/background.jpg').convert_alpha()
heaven=pygame.image.load(r'/var/www/html/First Game!/Sprite/heaven.jpg').convert_alpha()
treasure=pygame.image.load(r'/var/www/html/First Game!/Sprite/treasure.jpg').convert_alpha()

aim=pygame.image.load(r'/var/www/html/First Game!/Sprite/aim.png').convert_alpha()


fire=pygame.image.load(r'/var/www/html/First Game!/Sprite/fireball.png').convert_alpha()


tomb=pygame.image.load(r'/var/www/html/First Game!/Sprite/tombstone.png').convert_alpha()

explode=pygame.image.load(r'/var/www/html/First Game!/Sprite/boom.png').convert_alpha()

sword=pygame.image.load(r'/var/www/html/First Game!/Sprite/sword.png').convert_alpha()

shield=pygame.image.load(r'/var/www/html/First Game!/Sprite/shield.png').convert_alpha()

medkit=pygame.image.load(r'/var/www/html/First Game!/Sprite/medkit.png').convert_alpha()

note=pygame.image.load(r'/var/www/html/First Game!/Sprite/note.png').convert_alpha()

speaker=pygame.image.load(r'/var/www/html/First Game!/Sprite/speaker.png').convert_alpha()




bg=pygame.transform.scale(bg,(swid,shei)).convert_alpha()
heaven=pygame.transform.scale(heaven,(swid,shei)).convert_alpha()
treasure=pygame.transform.scale(treasure,(swid,shei)).convert_alpha()
explode=pygame.transform.scale(explode,(80,80)).convert_alpha()
aim=pygame.transform.scale(aim,(30,30)).convert_alpha()
fire=pygame.transform.scale(fire,(65,40)).convert_alpha()
fire=pygame.transform.rotate(fire,-90).convert_alpha()
burn=pygame.transform.scale(fire,(20,32)).convert_alpha()
deadyuusha=pygame.transform.scale(yuushaf,(63,75)).convert_alpha()
deaddragon=pygame.transform.scale(dragon,(108,84)).convert_alpha()
tomb=pygame.transform.scale(tomb,(372,304))
medkit=pygame.transform.scale(medkit,(20,20))
sword=pygame.transform.scale(sword,(20,20))
shield=pygame.transform.scale(shield,(30,30))
note=pygame.transform.scale(note,(80,80))
speaker=pygame.transform.scale(speaker,(80,80))



drect=dragon.get_rect()
yrect=yuusha.get_rect()
brect=explode.get_rect()
arect=aim.get_rect()
frect=fire.get_rect()
bgrect=bg.get_rect()
mrect=medkit.get_rect()
srect=shield.get_rect()
krect=sword.get_rect()

clock=pygame.time.Clock()

class hero():
    
    def __init__(a,x,y,hp,armour):
        a.x=x
        a.y=y
        a.v=0
        a.hp=hp
        a.armour=armour
        a.hpmulti=0
        a.r=255
        a.g=255
        a.stime=0
        a.shield=False
        a.aatk=False
        a.atime=0
        a.atk=[]
        a.av=7
        a.aradius=10
        a.newacolor=(100,255,100)
        a.acolor=(0,0,0)
        a.xlog=0
        a.ylog=0
        a.xlock=[]
        a.ylock=[]
        a.firex=0
        a.firey=0
        a.burnl=[]
        a.burnt=[]
        a.btime=0
        a.fltime=0
        a.burnx=[]
        a.burny=[]
        a.firstb=False
        a.healnum=0
        a.medkit=False
        a.dmgup=False
        a.dmin=1000
        a.dmax=8000
        a.dmgupnum=0
        
        a.shieldnum=0
        a.shieldup=False
        a.popup=[]
        a.satime=0
        a.sctime=0
        a.skill=False
        a.askill=False
        a.sav=9
        a.sactime=0
        a.skilll=[]
        a.ulti=False
        a.uatime=0
        a.uctime=0
        a.aulti=False
        a.secret=False
    def draw(a,screen,pcx,fcx):
        a.fcx=fcx
        a.pcx=pcx
        
        if a.pcx <= a.fcx:
            screen.blit(yuushaf,(a.x,a.y))
        elif a.pcx>=a.fcx:
            screen.blit(yuusha,(a.x,a.y))
        pygame.draw.rect(screen,(0,0,0),(a.x+16,a.y-10,82,6))
        if a.hpmulti != 0:
            a.hpmulti=a.hpmulti-100       
            if a.hpmulti <0:
                a.hp=a.hp-a.hpmulti
                a.hpmulti=0
            a.hp=a.hp-100
        if a.hp <=0:
            a.hp=0
            
        screen.blit(Herow,(a.x-18,a.y-20))
        pygame.draw.rect(screen,(a.r*(abs(a.hp-10000)/10000),a.g*(a.hp/10000),0),(a.x+16,a.y-10,82*(a.hp/10000),6))
        
        for a.pop in a.popup:
            a.pop.draw()
            if a.pop.y <=0:
                a.popup.pop(a.popup.index(a.pop))
        if a.secret:
            if f1.ftimer%100==0:
                a.healnum=a.healnum+1000
                a.popup.append(popups(a.x,a.y+10,1000,2))
    def move(a):
        a.burna=False
        
        if a.x+yrect.centerx>= f1.x+20 and a.x+yrect.centerx<=f1.x+drect.centerx*2-20 and a.y+yrect.centery>=f1.y+32 and a.y+yrect.centery<=f1.y+drect.centery*2-32:
             a.v=2
             a.burna=True
        else:
            a.v=5
        if a.secret:
            a.v=10
        if k[pygame.K_w] and a.y >uwall:
             a.y-=p1.v
        if k[pygame.K_a]and a.x>lwall:
             a.x-=a.v
        if k[pygame.K_s]and a.y+yrect.centery*2<dwall:
             a.y+=a.v
        if k[pygame.K_d]and a.x+yrect.centerx*2<rwall-26:
             a.x+=a.v
    def thirddegreeburn(a):
        a.firex=ran.randint(5,yrect.centerx*2-30)
        a.firey=ran.randint(5,yrect.centery*2-40)
        
        if a.burna:
            burnsound.play()
            a.btime=a.btime+1
            if a.btime==20:
                a.btime=0
                if not(a.secret):
                    a.burndmg=(1000-1000*((a.armour/10000)*(90/100)))
                if a.secret:
                    a.burndmg=(1000-1000*((a.armour/10000)*(99/100)))
                a.hpmulti=a.hpmulti+a.burndmg
                a.burnx.append(a.firex)
                a.burny.append(a.firey)
                a.popup.append(popups(a.x,a.y+10,a.burndmg,1))
                if len(a.burnx)==6 and len(a.burny)==6:
                    a.burnx.pop(0)
                    a.burny.pop(0)
                    
            for a.numx in a.burnx:
                for a.numy in a.burny:
                    
                    screen.blit(burn,(a.x+a.numx,a.y+a.numy))
        else:
            a.burnx.clear()
            a.burny.clear()
    def healget(a,medx,medy):
        a.medx=medx
        a.medy=medy
        
        if a.medx+mrect.centerx >= a.x and a.medx+mrect.centerx <= a.x+yrect.centerx*2 and a.medy+mrect.centery>= a.y and a.medy+mrect.centery<=a.y+yrect.centery*2:
            healsound.play()
            if not(a.secret):
                a.ranheal=ran.randint(2500,6000)
            if a.secret:
                a.ranheal=ran.randint(5000,12000)
            a.healnum=a.healnum+a.ranheal
            a.medkit=True
            a.popup.append(popups(a.x,a.y+10,a.ranheal,2))
            
    def heal(a):
        if a.healnum!=0:
            a.hp=a.hp+75
            a.healnum=a.healnum-75
        if a.healnum <0:
                a.hp=a.hp+a.healnum
                a.healnum=0
        if a.hp>=10000:
            a.hp=10000
        
    def damageupget(a,dmgx,dmgy):
        a.dmgx=dmgx
        a.dmgy=dmgy
        if a.dmgx+krect.centerx >= a.x and a.dmgx+krect.centerx <= a.x+yrect.centerx*2 and a.dmgy+krect.centery>= a.y and a.dmgy+krect.centery<=a.y+yrect.centery*2:
            buffsound.play()
            if not(a.secret):
                a.randmg=ran.randint(3000,5000)
            if a.secret:
                a.randmg=ran.randint(6000,10000)
            a.dmgupnum=a.dmgupnum+a.randmg
            a.dmgup=True
            a.popup.append(popups(a.x,a.y+10,a.randmg,4))
            
    def damageup(a):
        if a.dmgupnum!=0:
            a.dmin=a.dmin+50
            a.dmax=a.dmax+50
            a.dmgupnum=a.dmgupnum-50
        if a.dmgupnum <0:
                a.dmin=a.dmin+a.dmgupnum
                a.dmax=a.dmax+a.dmgupnum
                a.dmgupnum=0
        if a.dmin>=42000:
            a.dmin=42000
        if a.dmax>=50000:
            a.dmax=50000
    def armourupget(a,sx,sy):
        a.sx=sx
        a.sy=sy
        if a.sx+srect.centerx >= a.x and a.sx+srect.centerx <= a.x+yrect.centerx*2 and a.sy+srect.centery>= a.y and a.sy+srect.centery<=a.y+yrect.centery*2:
            buffsound.play()
            if not(a.secret):
                a.ranshield=ran.randint(500,1250)
            if a.secret:
                a.ranshield=ran.randint(1000,2500)
            a.shieldnum=a.shieldnum+a.ranshield
            a.shieldup=True
            a.popup.append(popups(a.x,a.y+10,a.ranshield,3))
        
    def armourup(a):    
        if a.shieldnum!=0:
            a.armour=a.armour+50
            a.shieldnum=a.shieldnum-50
        if a.shieldnum <0:
                
            a.armour=a.armour+a.shieldnum
            a.shieldnum=0

        if a.armour>=10000:
            a.armour=10000

            
    def stats(a):
        a.hstats=fontok.render('Hitpoints: '+str(round(a.hp))+'(Max:10000)',True,(255,255,255))
        screen.blit(a.hstats,(10,50))
        a.dstats=fontok.render('Damage: '+str(a.dmin)+' - '+str(a.dmax)+' (Max:42000 - 50000)',True,(255,255,255))
        screen.blit(a.dstats,(10,80))
        a.sstats=fontok.render('Armor: '+str(a.armour)+'(Max:10000)',True,(255,255,255)) 
        screen.blit(a.sstats,(10,110))
        
        screen.blit(scool,(10,140))
        pygame.draw.rect(screen,(255,0,0),(64,148,100,12),0)
        if a.stime==0 and a.sctime==0:
            pygame.draw.rect(screen,(0,255,0),(64,148,100,12),0)
        if not(a.shield):
            if not(a.secret):
                pygame.draw.rect(screen,(0,255,0),(64,148,100*(a.sctime/160),12),0)
            if a.secret:
                pygame.draw.rect(screen,(0,255,0),(64,148,100*(a.sctime/60),12),0)
        if a.shield:
            pygame.draw.rect(screen,(0,0,255),(64,148,100-100*(a.stime/140),12),0)
        screen.blit(sacool,(10,170))
        pygame.draw.rect(screen,(255,0,0),(64,178,100,12),0)
        if a.satime==0 and a.sactime==0:
            pygame.draw.rect(screen,(0,255,0),(64,178,100,12),0)
        if not(a.skill) :
            if not(a.secret):
                
                pygame.draw.rect(screen,(0,255,0),(64,178,100*(a.sactime/150),12),0)
            if a.secret:
                pygame.draw.rect(screen,(0,255,0),(64,178,100*(a.sactime/100),12),0)
        if a.skill:
            pygame.draw.rect(screen,(0,0,255),(64,178,100-100*(a.satime/100),12),0)
            
        screen.blit(ucool,(10,200))
        pygame.draw.rect(screen,(255,0,0),(64,208,100,12),0)
        if a.uatime==0 and a.uctime==0:
            pygame.draw.rect(screen,(0,255,0),(64,208,100,12),0)
        if not(a.ulti):
            if not (a.secret):
                pygame.draw.rect(screen,(0,255,0),(64,208,100*(a.uctime/971),12),0)
            if a.secret:
                pygame.draw.rect(screen,(0,255,0),(64,208,100*(a.uctime/460),12),0)
        if a.ulti:
            pygame.draw.rect(screen,(0,0,255),(64,208,100-100*(a.uatime/140),12),0)
        if a.secret:
            screen.blit(cheat,(10,230))
    def activation(a,mx,my):
        a.mx=mx
        a.my=my
        a.adamage=ran.randint(a.dmin,a.dmax)
        if k[pygame.K_q] and a.stime==0 :
            a.shield=True
        if a.shield:
            pygame.draw.circle(screen,(0,153,0),(a.x+yrect.centerx,a.y+yrect.centery),60,4)            
            a.stime=a.stime+1
        if a.stime>=140:
            a.shield=False
            a.stime=a.stime+1
            a.sctime=a.sctime+1
        if not(a.secret):
            if a.stime>=300:
                a.stime=0
                a.sctime=0
        if a.secret:
            if a.stime>=200:
                a.stime=0
                a.sctime=0
        if mouse[0]and a.atime==0 and (not(a.skill or a.ulti)):
            attacksound.play()
            
            a.aatk=True
            a.xlog=a.mx-(a.x+yrect.centerx)
            a.ylog=a.my-(a.y+yrect.centery)
            if not(a.secret):
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog,a.ylog,a.av))
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog-50,a.ylog+50,a.av))
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog+50,a.ylog-50,a.av))
            if a.secret:
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog,a.ylog,a.av))
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog-50,a.ylog+50,a.av))
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog+50,a.ylog-50,a.av))
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog-25,a.ylog+25,a.av))
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog+25,a.ylog-25,a.av))
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog-75,a.ylog+75,a.av))
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog+75,a.ylog-75,a.av))
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog-100,a.ylog+100,a.av))
                a.atk.append(projectiles(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),a.aradius,a.adamage,a.xlog+100,a.ylog-100,a.av))
        if a.aatk:
            a.atime=a.atime+1
        if not(a.secret):
            if a.atime>=40:
                a.aatk=False
                a.atime=0
        if a.secret:
            if a.atime>=20:
                a.aatk=False
                a.atime=0
        if k[pygame.K_SPACE] and a.satime==0 and (not(a.ulti)):
            a.skill=True

        if a.skill:
            a.xlog1=a.mx-(a.x+yrect.centerx)
            a.xlog2=a.mx-((a.x+yrect.centerx-50))
            a.xlog3=a.mx-((a.x+yrect.centerx+50))
            a.xlog4=a.mx-((a.x+yrect.centerx-25))
            a.xlog5=a.mx-((a.x+yrect.centerx+25))
            a.ylog1=a.my-(a.y+yrect.centery)
            a.ylog2=a.my-((a.y+yrect.centery-50))
            a.ylog3=a.my-((a.y+yrect.centery+50))
            a.ylog4=a.my-((a.y+yrect.centery-25))
            a.ylog5=a.my-((a.y+yrect.centery+25))
            pygame.draw.line(screen,(255,255,255),(a.x+yrect.centerx,a.y+yrect.centery),(a.mx,a.my),1)
        if a.skill and mouse[0]:
            a.askill=True
        if a.askill:
            a.satime=a.satime+1
        if not(a.secret):
            if a.satime!=0 and a.satime <=100 and a.satime%8==0:
                skillsound.play()
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),round(a.aradius/1.2),a.adamage/10,a.xlog1,a.ylog1,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery-50),round(a.aradius/1.2),a.adamage/10,a.xlog1,a.ylog2,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery+50),round(a.aradius/1.2),a.adamage/10,a.xlog1,a.ylog3,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery-25),round(a.aradius/1.2),a.adamage/10,a.xlog1,a.ylog4,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery+25),round(a.aradius/1.2),a.adamage/10,a.xlog1,a.ylog5,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx-50),round(a.y+yrect.centery),round(a.aradius/1.2),a.adamage/10,a.xlog2,a.ylog1,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx+50),round(a.y+yrect.centery),round(a.aradius/1.2),a.adamage/10,a.xlog3,a.ylog1,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx-25),round(a.y+yrect.centery),round(a.aradius/1.2),a.adamage/10,a.xlog4,a.ylog1,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx+25),round(a.y+yrect.centery),round(a.aradius/1.2),a.adamage/10,a.xlog5,a.ylog1,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx+25),round(a.y+yrect.centery-25),round(a.aradius/1.2),a.adamage/10,a.xlog5,a.ylog4,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx+25),round(a.y+yrect.centery+25),round(a.aradius/1.2),a.adamage/10,a.xlog5,a.ylog5,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx-25),round(a.y+yrect.centery-25),round(a.aradius/1.2),a.adamage/10,a.xlog4,a.ylog4,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx-25),round(a.y+yrect.centery+25),round(a.aradius/1.2),a.adamage/10,a.xlog4,a.ylog5,a.sav,0))
        if a.secret:
            if a.satime!=0 and a.satime <=100 and a.satime%5==0:
                skillsound.play()
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),round(a.aradius/1.2),a.adamage/10,a.xlog1,a.ylog1,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery-50),round(a.aradius/1.2),a.adamage/10,a.xlog1,a.ylog2,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery+50),round(a.aradius/1.2),a.adamage/10,a.xlog1,a.ylog3,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery-25),round(a.aradius/1.2),a.adamage/10,a.xlog1,a.ylog4,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx),round(a.y+yrect.centery+25),round(a.aradius/1.2),a.adamage/10,a.xlog1,a.ylog5,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx-50),round(a.y+yrect.centery),round(a.aradius/1.2),a.adamage/10,a.xlog2,a.ylog1,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx+50),round(a.y+yrect.centery),round(a.aradius/1.2),a.adamage/10,a.xlog3,a.ylog1,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx-25),round(a.y+yrect.centery),round(a.aradius/1.2),a.adamage/10,a.xlog4,a.ylog1,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx+25),round(a.y+yrect.centery),round(a.aradius/1.2),a.adamage/10,a.xlog5,a.ylog1,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx+25),round(a.y+yrect.centery-25),round(a.aradius/1.2),a.adamage/10,a.xlog5,a.ylog4,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx+25),round(a.y+yrect.centery+25),round(a.aradius/1.2),a.adamage/10,a.xlog5,a.ylog5,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx-25),round(a.y+yrect.centery-25),round(a.aradius/1.2),a.adamage/10,a.xlog4,a.ylog4,a.sav,0))
                a.skilll.append(heroskill(screen,a.newacolor,round(a.x+yrect.centerx-25),round(a.y+yrect.centery+25),round(a.aradius/1.2),a.adamage/10,a.xlog4,a.ylog5,a.sav,0))
        


        if a.satime>=100:
            a.satime=a.satime+1
            a.sactime=a.sactime+1
            a.skill=False
            a.askill=False
        if not(a.secret):
            if a.satime>=250:
                a.satime=0
                a.sactime=0
        if a.secret:
            if a.satime>=200:
                a.satime=0
                a.sactime=0
        if k[pygame.K_z] and a.uatime==0 and (not(a.skill)):
            a.ulti=True
        if a.ulti:
            
            pygame.draw.line(screen,(255,255,255),(a.x+yrect.centerx,a.y+yrect.centery),(a.mx,a.my),1)
        if a.ulti and mouse[0] :
            a.aulti=True
        if a.aulti:
            a.uatime=a.uatime+1
        
        if a.uatime!=0 and a.uatime <=140 and a.uatime%1==0:
            ultisound.play()
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx),round(a.y+yrect.centery),round(a.aradius/1.5),a.adamage/10,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx+ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery-ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            a.skilll.append(heroskill(screen,a.acolor,round(a.x+yrect.centerx-ran.randint(-100,100)),round(a.y+yrect.centery+ran.randint(-100,100)),round(a.aradius/2),a.adamage/100,a.xlog1,a.ylog1,a.sav))
            a.xlog1=a.mx-((a.x+yrect.centerx-ran.randint(-100,100)))
            a.ylog1=a.my-((a.y+yrect.centery-ran.randint(-100,100)))
            
            
            
            
            
            
            
            
            
        if a.uatime>140:
            a.uatime=a.uatime+1
            a.uctime=a.uctime+1
            a.ulti=False
            a.aulti=False
        if not(a.secret):
            if a.uatime==1111:
                a.uatime=0
                a.uctime=0
        if a.secret:
            if a.uatime==600:
                a.uatime=0
                a.uctime=0
            
    def ashield(a):
        return a.shield
    
    def hit(a,damage):
        if a.armour>=8000:
            hitsoundweak.play()
        elif a.armour >=4000:
            hitsoundmedio.play()
        elif a.armour <4000:
            hitsoundstrong.play()
            
        if not(f1.nightmaremode):
            a.dmg=damage
            if not(a.secret):
                a.tdmg=(a.dmg-a.dmg*((a.armour/10000)*(90/100)))
            if a.secret:
                a.tdmg=(a.dmg-a.dmg*((a.armour/10000)*(995/1000)))
            a.hpmulti=a.hpmulti+a.tdmg
            a.popup.append(popups(a.x,a.y+10,a.tdmg,1))
        if f1.nightmaremode:
            a.dmg=damage
            if not(a.secret):
                a.tdmg=(a.dmg-a.dmg*((a.armour/10000)*(94/100)))
            if a.secret:
                a.tdmg=(a.dmg-a.dmg*((a.armour/10000)*(995/1000)))
            a.hpmulti=a.hpmulti+a.tdmg
            a.popup.append(popups(a.x,a.y+10,a.tdmg,1))
        
    def die(a):
        return a.hp        
class foe():
    def __init__(a,x,y,hp,armour):
        a.x=x
        a.y=y
        a.r=ran.randint(0,255)
        a.g=ran.randint(0,255)
        a.b=ran.randint(0,255)
        a.hp=hp
        a.armour=armour
        a.hpmulti=0
        a.xmlog=0
        a.ymlog=0
        a.v=1
        a.fradius=16
        a.xlog=0
        a.ylog=0
        a.fcolor=(255,255,255)
        a.fv=6
        a.hfv=4
        a.rfv=5
        a.flist=[]
        a.ftimer=0
        a.nightmaremode=False
        a.px=0
        a.px=0
        a.popup=[]
        a.sflist=[]
        a.bhtheta=0
        
        a.bhspin=0
        a.bhv=5
        a.bhinterval=3
        a.beam=False
        a.beamtime=0
    def move(a):
        a.px=a.x+drect.centerx/3
        a.py=a.y+drect.centery/2
        a.xmlog=(p1.x+yrect.centerx)-(a.x+drect.centerx)
        a.ymlog=(p1.y+yrect.centerx)-(a.y+drect.centery)
        if not(a.nightmaremode):
            if a.ftimer%2==0:
                if a.xmlog>0:
                    a.x=a.x+a.v
                if a.xmlog<0:
                    a.x=a.x-a.v
                if a.ymlog>0:
                    a.y=a.y+a.v
                if a.ymlog<0:
                    a.y=a.y-a.v
        if a.nightmaremode:
            if a.ftimer%1==0:
                if a.xmlog>0:
                    a.x=a.x+a.v
                if a.xmlog<0:
                    a.x=a.x-a.v
                if a.ymlog>0:
                    a.y=a.y+a.v
                if a.ymlog<0:
                    a.y=a.y-a.v

        if a.x<=lwall:
            a.x=lwall+1
        if a.x+drect.centerx*2>=rwall-26:
            a.x=rwall-26-drect.centerx*2-1
        if a.y<=uwall-50:
            a.y=uwall-50+1
    def draw(a,screen,fcx,pcx):
        a.pcx=pcx
        a.fcx=fcx
        
        if a.fcx <= a.pcx:
            screen.blit(dragon,(a.x,a.y))
            a.px=a.px
            a.py=a.py
        else:
            screen.blit(dragonf,(a.x,a.y))
            a.px=a.px-drect.centerx/3+drect.centerx/3*5
            
        a.r=a.r+ran.randint(0,5)
        a.g=a.g+ran.randint(0,5)
        a.b=a.b+ran.randint(0,5)

        if a.r>=255:
            a.r=0
        if a.g>=255:
            a.g=0
        if a.b>=255:
            a.b=0
        if a.hpmulti != 0:
            
            a.hpmulti=a.hpmulti-150
            if a.hpmulti <0:
                
                a.hp=a.hp-a.hpmulti
                a.hpmulti=0
            a.hp=a.hp-150
                        
        pygame.draw.rect(screen,(a.r,a.g,a.b),(133,17,swid-141,26),0)
        pygame.draw.rect(screen,(0,0,0),(135,20,swid-145,20),0)
        if not(a.nightmaremode):
            pygame.draw.rect(screen,(200,100,0),(135,20,(swid-145)*(a.hp/100000),20))
            screen.blit(fonthp.render(str(round(a.hp/1000,2))+'%',True,(255,223,0)),(500,12))
        if a.nightmaremode:
            pygame.draw.rect(screen,(255,0,0),(135,20,(swid-145)*(a.hp/100000),20))
            screen.blit(fonthp.render(str(round(a.hp/1000,2))+'%',True,(255,0,0)),(500,12))
        screen.blit(dragonw,(10,0))
        
        if a.hp <=0:
            a.hp=0
            pygame.draw.rect(screen,(0,0,0),(135,20,(swid-145),20))
        if a.hp>=100000:
            a.hp=100000
        

        if a.nightmaremode:
            if a.ftimer%20==0:
                a.hp=a.hp+100
                a.popup.append(popups(a.x+60,a.y+50,100,2))
        for a.pop in a.popup:
            a.pop.draw()
            if a.pop.y <=0:
                a.popup.pop(a.popup.index(a.pop))
    def hit(a,damage):
        if p1.dmin>=30000 and (not(a.nightmaremode)):
            hitsoundmedio.play()
        elif p1.dmin<30000:
            hitsoundweak.play()
            
        a.damage=damage
        if a.nightmaremode:
            a.tdmg=(a.damage-a.damage*((a.armour/4000)*(998/1000)))
        if a.hp >40000:

            a.tdmg=(a.damage-a.damage*((a.armour/4000)*(99/100)))
        elif a.hp <=40000:
            a.tdmg=(a.damage-a.damage*((a.armour/4000)*(995/1000)))
        a.hpmulti=a.hpmulti+a.tdmg
        a.popup.append(popups(a.x+60,a.y+50,a.tdmg,1))
        
    def fire(a):
        
        if not(a.nightmaremode):
            a.fdamage=ran.randint(800,2500)
            a.hfdamage=ran.randint(1000,3333)
            a.rfdamage=ran.randint(1000,3333)
            a.bdamage=ran.randint(500,2222)
            if a.ftimer==800:
                a.ftimer=0
            a.ftimer=a.ftimer+1
            if a.ftimer%75==0 :
                firesound.play()
                a.xlog=(p1.x+yrect.centerx)-a.px#
                a.ylog=(p1.y+yrect.centery)-a.py#
                
                
                a.flist.append(projectiles(screen,a.fcolor,a.px,a.py,a.fradius,a.fdamage,a.xlog,a.ylog,a.fv))
            if a.ftimer%225==0:
                firesound.play()
                a.xlog=(p1.x+yrect.centerx)-a.px#
                a.ylog=(p1.y+yrect.centery)-a.py#

                a.sflist.append(specialprojectiles(screen,a.px,a.py,a.hfdamage,a.xlog,a.ylog,a.hfv,a.bhtheta,2))
            if a.ftimer%150==0:
                firesound.play()
                a.xlog=(p1.x+yrect.centerx)-a.px#
                a.ylog=(p1.y+yrect.centery)-a.py#

                a.sflist.append(specialprojectiles(screen,a.px,a.py,a.rfdamage,a.xlog,a.ylog,a.rfv,a.bhtheta,1))
            if a.ftimer%500==0:
                firesound.play
                a.sflist.append(specialprojectiles(screen,a.px,a.py,a.rfdamage,a.xlog,a.ylog,a.hfv-3,a.bhtheta,7))
            if a.ftimer%400==0 and a.hp<40000:
                firesound.play()
                a.beam=True
            if a.beam:
                a.xlog=(p1.x+yrect.centerx)-a.px#
                a.ylog=(p1.y+yrect.centery)-a.py#
                if a.ftimer%2==0:
                    a.sflist.append(specialprojectiles(screen,a.px,a.py,a.bdamage,a.xlog,a.ylog,a.fv-2,a.bhtheta,1))
                a.beamtime=a.beamtime+1
                if a.beamtime==90:
                    a.beam=False
                    a.beamtime=0
        if a.nightmaremode:
            a.bhdamage=ran.randint(800,2500)
            a.fdamage=ran.randint(800,2500)
            a.hfdamage=ran.randint(1200,3500)
            a.rfdamage=ran.randint(1000,3333)
            a.bdamage=ran.randint(700,2200)
                
            if a.bhspin>=360:
                a.bhspin=0
            
            if a.bhspin>=270:
                a.bhtheta=a.bhtheta-a.bhinterval
                
                a.bhspin=a.bhspin+a.bhinterval

            elif a.bhspin>=180:
                a.bhtheta=a.bhtheta+a.bhinterval
                
                a.bhspin=a.bhspin+a.bhinterval

            elif a.bhspin>=90:
                a.bhtheta=a.bhtheta-a.bhinterval
                
                a.bhspin=a.bhspin+a.bhinterval

            elif a.bhspin>=0:
                a.bhtheta=a.bhtheta+a.bhinterval
                
                a.bhspin=a.bhspin+a.bhinterval
            if a.ftimer==800:
                a.ftimer=0
            a.ftimer=a.ftimer+1
            if a.ftimer%4==0:
                firesound.play()
                
                a.sflist.append(specialprojectiles(screen,a.px,a.py,a.bhdamage,a.xlog,a.ylog,a.bhv,a.bhtheta,3))
                a.sflist.append(specialprojectiles(screen,a.px,a.py,a.bhdamage,a.xlog,a.ylog,a.bhv,a.bhtheta,4))
                a.sflist.append(specialprojectiles(screen,a.px,a.py,a.bhdamage,a.xlog,a.ylog,a.bhv,90-a.bhtheta,5))
                a.sflist.append(specialprojectiles(screen,a.px,a.py,a.bhdamage,a.xlog,a.ylog,a.bhv,90-a.bhtheta,6))
                
            if a.ftimer%40==0 :
                firesound.play()
                a.xlog=(p1.x+yrect.centerx)-a.px#
                a.ylog=(p1.y+yrect.centery)-a.py#
                
                
                a.flist.append(projectiles(screen,a.fcolor,a.px,a.py,a.fradius,a.fdamage,a.xlog,a.ylog,a.fv))
            if a.ftimer%120==0:
                firesound.play()
                a.xlog=(p1.x+yrect.centerx)-a.px#
                a.ylog=(p1.y+yrect.centery)-a.py#

                a.sflist.append(specialprojectiles(screen,a.px,a.py,a.hfdamage,a.xlog,a.ylog,a.hfv,a.bhtheta,2))
            if a.ftimer%80==0:
                firesound.play()
                a.xlog=(p1.x+yrect.centerx)-a.px#
                a.ylog=(p1.y+yrect.centery)-a.py#

                a.sflist.append(specialprojectiles(screen,a.px,a.py,a.rfdamage,a.xlog,a.ylog,a.rfv,a.bhtheta,1))
            if a.ftimer%400==0:
                firesound.play()
                a.beam=True
            if a.beam:
                a.xlog=(p1.x+yrect.centerx)-a.px#
                a.ylog=(p1.y+yrect.centery)-a.py#
                if a.ftimer%2==0:
                    a.sflist.append(specialprojectiles(screen,a.px,a.py,a.bdamage,a.xlog,a.ylog,a.fv-2,a.bhtheta,1))
                a.beamtime=a.beamtime+1
                if a.beamtime==90:
                    a.beam=False
                    a.beamtime=0
            if a.ftimer%400==0:
                firesound.play()
                a.sflist.append(specialprojectiles(screen,a.px,a.py,a.rfdamage,a.xlog,a.ylog,a.hfv-3,a.bhtheta,7))
                a.sflist.append(specialprojectiles(screen,a.px,a.py,a.rfdamage,a.xlog,a.ylog,a.hfv-3,a.bhtheta,7))
    def die(a):
        return a.hp
class almostuseless():
    def __init__(a,x,y):
        a.x=x
        a.y=y
        a.btimer=0
    def draw(a,elist):
        a.btimer=a.btimer+1
        a.elist=elist
        screen.blit(explode,(a.x-brect.centerx,a.y-brect.centery))
        if a.btimer==12:
            a.btimer=0
            a.elist.pop(a.elist.index(a))
class specialprojectiles():
    def __init__(a,screen,x,y,damage,xlog,ylog,av,theta,identifier):
        a.screen=screen
        a.x=x
        a.y=y
        a.damage=damage
        a.xl=xlog
        a.yl=ylog
        a.av=av
        a.vxl=[]
        a.vyl=[]
        a.radius=f1.fradius
        
        a.gettype=identifier
        a.typelist=[]
        a.typelist.append(a.gettype)
        a.homing=False         #2
        a.reflect=False        #1
        a.bullethell=False     #3
        a.rbullethell=False    #4
        a.lbullethell=False    #5
        a.rlbullethell=False   #6
        a.fireblast=False      #7
        a.reflecttimer=0
        a.notreflect=False
        a.reflecttimes=0

        a.theta=theta
        a.thita=90-a.theta
        a.impact=0

        a.blasttime=0
        for a.type in a.typelist:
            if a.type==1:
                a.reflect=True

            elif a.type==2:
                a.homing=True



            elif a.type==3:
                a.bullethell=True
            elif a.type==4:
                a.rbullethell=True

            elif a.type==5:
                a.lbullethell=True

            elif a.type==6:
                a.rlbullethell=True
            elif a.type==7:
                a.fireblast=True
        if a.bullethell:
            a.vx,a.vy=avaSpecial(a.theta,a.thita,a.av)
            if f1.bhspin<90 or f1.bhspin>=360 :
                a.vx=abs(a.vx)
                a.vy=a.vy*-1

            elif f1.bhspin<180:
                a.vx=abs(a.vx)
                a.vy=abs(a.vy)

            elif f1.bhspin<270:
                a.vx=a.vx*-1
                a.vy=abs(a.vy)

            elif f1.bhspin<360:
                a.vx=a.vx*-1
                a.vy=a.vy*-1
        elif a.rbullethell:
            a.vx,a.vy=avaSpecial(a.theta,a.thita,a.av)
            if f1.bhspin<90 or f1.bhspin>=360 :
                a.vx=a.vx*-1
                a.vy=abs(a.vy)

            elif f1.bhspin<180:
                a.vx=a.vx*-1
                a.vy=a.vy*-1

            elif f1.bhspin<270:
                a.vx=abs(a.vx)
                a.vy=a.vy*-1

            elif f1.bhspin<360:
                a.vx=abs(a.vx)
                a.vy=abs(a.vy)
        elif a.lbullethell:
            a.vx,a.vy=avaSpecial(a.theta,a.thita,a.av)
            if f1.bhspin<90 or f1.bhspin>=360 :
                a.vx=a.vx*-1
                a.vy=a.vy*-1

            elif f1.bhspin<180:
                a.vx=abs(a.vx)
                a.vy=a.vy*-1
                

            elif f1.bhspin<270:
                a.vx=abs(a.vx)
                a.vy=abs(a.vy)
                

            elif f1.bhspin<360:
                a.vx=a.vx*-1
                a.vy=abs(a.vy)
                

        elif a.rlbullethell:
            a.vx,a.vy=avaSpecial(a.theta,a.thita,a.av)
            if f1.bhspin<90 or f1.bhspin>=360 :
                a.vx=abs(a.vx)
                a.vy=abs(a.vy)
                

            elif f1.bhspin<180:
                a.vx=a.vx*-1
                a.vy=abs(a.vy)
                
            elif f1.bhspin<270:
                a.vx=a.vx*-1
                a.vy=a.vy*-1

                

            elif f1.bhspin<360:
                a.vx=abs(a.vx)
                a.vy=a.vy*-1
                
        if not(a.bullethell or a.rbullethell or a.lbullethell or a.rlbullethell):
            a.vx,a.vy=avaRemastered(a.xl,a.yl,a.av)
            a.vxl.append(a.vx)
            a.vyl.append(a.vy)
                
    def draw(a):
        screen.blit(fire,(a.x-frect.centerx,a.y-frect.centery))
        


    def move(a):
        if a.bullethell or a.rbullethell or a.lbullethell or a.rlbullethell:
            a.x=a.x+a.vx
            a.y=a.y+a.vy
            
        elif a.homing:
            a.constxlog=(p1.x+yrect.centerx)-a.x
            a.constylog=(p1.y+yrect.centery)-a.y
            a.vx,a.vy=avaRemastered(a.constxlog,a.constylog,a.av)
            if a.constxlog<=0:
                a.x=a.x-a.vx
            if a.constxlog>=0:
                a.x=a.x+a.vx
            if a.constylog<=0:
                a.y=a.y-a.vy
            if a.constylog>=0:
                a.y=a.y+a.vy
        elif a.reflect:
            for a.vx2 in a.vxl:
                for a.vy2 in a.vyl:
                    if not(a.notreflect):
                        if a.x <=lwall or a.x>=rwall:
                            a.vxl[a.vxl.index(a.vx2)]=a.vxl[a.vxl.index(a.vx2)]*-1
                            a.notreflect=True
                        if a.y<=uwall or a.y>=dwall:
                            a.vyl[a.vyl.index(a.vy2)]=a.vyl[a.vyl.index(a.vy2)]*-1
                            a.notreflect=True
                    if a.notreflect:
                        a.reflecttimer=a.reflecttimer+1
                        if a.reflecttimer==3:
                            a.reflecttimer=0
                            a.reflecttimes=a.reflecttimes+1
                            a.notreflect=False

                        
                    if a.xl<0: 
                                               
                        a.x=a.x-a.vx2
                                                    
                    if a.xl>0:
                                                 
                        a.x=a.x+a.vx2
                                    
                    if a.yl<0:
                        a.y=a.y-a.vy2
                                               
                                                    
                    if a.yl>0:
                        a.y=a.y+a.vy2
                    if a.yl==0:
                        if a.xl>0:
                            a.x=a.x+a.vx2
                    if a.xl<0:
                        a.x=a.x-a.vx2
                    if a.xl==0:
                        if a.yl>0:
                            a.y=a.y+a.vy2
                    if a.yl<0:
                        a.y=a.y-a.vy2
        elif a.fireblast:
            for a.vx2 in a.vxl:
                for a.vy2 in a.vyl:
                    if a.xl<0: 
                                               
                        a.x=a.x-a.vx2
                                                    
                    if a.xl>0:
                                                 
                        a.x=a.x+a.vx2
                                    
                    if a.yl<0:
                        a.y=a.y-a.vy2
                                               
                                                    
                    if a.yl>0:
                        a.y=a.y+a.vy2
                    if a.yl==0:
                        if a.xl>0:
                            a.x=a.x+a.vx2
                    if a.xl<0:
                        a.x=a.x-a.vx2
                    if a.xl==0:
                        if a.yl>0:
                            a.y=a.y+a.vy2
                    if a.yl<0:
                        a.y=a.y-a.vy2
            
                    
        
    
        
    def collide(a,elist):
        if not(a.reflect):
            a.hhx=p1.x+4
            a.hhy=p1.y+4
            a.hhw=p1.x+yrect.centerx*2-4
            a.hhh=p1.y+yrect.centery*2-4
            a.elist=elist
            if a.x <=lwall or a.x>=rwall or a.y<=uwall or a.y>=dwall:
                boomsound.play()
                
                a.elist.append(almostuseless(a.x,a.y))
                                    
                f1.sflist.pop(f1.sflist.index(a))
            elif a.x <=p1.x+yrect.centerx+60 and a.x>=p1.x+yrect.centerx-60 and a.y >= p1.y+yrect.centery-60 and a.y<= p1.y+yrect.centery+60 and p1.ashield():
                boomsound.play()
                a.elist.append(almostuseless(a.x,a.y))            
                f1.sflist.pop(f1.sflist.index(a))
            elif a.x<=a.hhw and a.x>=a.hhx and a.y >=a.hhy and a.y <=a.hhh:
                
                    
                a.elist.append(almostuseless(a.x,a.y))
                    
                p1.hit(a.damage)
                        
                f1.sflist.pop(f1.sflist.index(a)) 
            
                
        if a.reflect:
            
            a.hhx=p1.x+4
            a.hhy=p1.y+4
            a.hhw=p1.x+yrect.centerx*2-4
            a.hhh=p1.y+yrect.centery*2-4
            a.elist=elist
            if a.x <=p1.x+yrect.centerx+60 and a.x>=p1.x+yrect.centerx-60 and a.y >= p1.y+yrect.centery-60 and a.y<= p1.y+yrect.centery+60 and p1.ashield():
                boomsound.play()    
                a.elist.append(almostuseless(a.x,a.y))            
                f1.sflist.pop(f1.sflist.index(a))
            elif a.x<=a.hhw and a.x>=a.hhx and a.y >=a.hhy and a.y <=a.hhh:
                
                a.elist.append(almostuseless(a.x,a.y))
                        
                p1.hit(a.damage)
                            
                f1.sflist.pop(f1.sflist.index(a)) 
            
            if a.reflecttimes==3:
                
                if a.x <=lwall or a.x>=rwall or a.y<=uwall or a.y>=dwall:
                    boomsound.play()
                    
                    a.elist.append(almostuseless(a.x,a.y))
                                        
                    f1.sflist.pop(f1.sflist.index(a))
class newtypeprojectiles():
    def __init__(a,screen,x,y,radius,damage,theta,av,spin,identifier):
        a.screen=screen
        a.x=x
        a.y=y
        a.xcheck=0
        a.ycheck=0
        a.radius=radius
        a.damage=damage
        a.theta=theta
        a.av=av
        a.spin=spin
        a.type=identifier
        a.fireblast=False
        if a.type==1:
            a.fireblast=True
        a.vxl=[]
        a.vyl=[]
        a.vx,a.vy=avaSpecial(a.theta,90-a.theta,a.av)
        a.vxl.append(a.vx)
        a.vyl.append(a.vy)

        a.impact=0
        if a.fireblast:
            if a.spin<90 or a.spin>=360 :
                a.vx=abs(a.vx)
                a.vy=a.vy*-1

            elif a.spin<180:
                a.vx=abs(a.vx)
                a.vy=abs(a.vy)

            elif a.spin<270:
                a.vx=a.vx*-1
                a.vy=abs(a.vy)

            elif a.spin<360:
                a.vx=a.vx*-1
                a.vy=a.vy*-1




                
        a.vxl.append(a.vx)
        a.vyl.append(a.vy)  
    def draw(a):
        screen.blit(fire,(a.x-frect.centerx,a.y-frect.centery))
    def move(a):
        if a.fireblast:
            a.x=a.x+a.vx
            a.y=a.y+a.vy
            a.xcheck=a.xcheck+a.vx
            a.ycheck=a.ycheck+a.vy
        if mt.hypot(abs(a.xcheck),abs(a.ycheck)) >=150:
            try:
                f1.sflist.pop(f1.sflist.index(a))
            except:
                pass
    def collide(a,elist):
        if a.fireblast:
            a.hhx=p1.x+4
            a.hhy=p1.y+4
            a.hhw=p1.x+yrect.centerx*2-4
            a.hhh=p1.y+yrect.centery*2-4
            a.elist=elist
            if a.x <=lwall or a.x>=rwall or a.y<=uwall or a.y>=dwall:
                boomsound.play()
                try:
                    a.elist.append(almostuseless(a.x,a.y))
                                       
                    f1.sflist.pop(f1.sflist.index(a))
                except:
                    pass
            elif a.x <=p1.x+yrect.centerx+60 and a.x>=p1.x+yrect.centerx-60 and a.y >= p1.y+yrect.centery-60 and a.y<= p1.y+yrect.centery+60 and p1.ashield():
                boomsound.play()
                try:
                    a.elist.append(almostuseless(a.x,a.y))            
                    f1.sflist.pop(f1.sflist.index(a))
                except:
                    pass
            elif a.x<=a.hhw and a.x>=a.hhx and a.y >=a.hhy and a.y <=a.hhh:
                
                try:   
                    a.elist.append(almostuseless(a.x,a.y))
                        
                    p1.hit(a.damage)
                            
                    f1.sflist.pop(f1.sflist.index(a))
                except:
                    pass
        
class projectiles():
    def __init__(a,screen,color,x,y,radius,damage,xlog,ylog,av):
        a.screen=screen
        a.color=color
        a.x=x
        a.y=y
        a.radius=radius
        a.av=av
        
        a.damage=damage
        a.vxl=[]
        a.vyl=[]
        a.xl=xlog
        a.yl=ylog
        a.vx,a.vy=avaRemastered(a.xl,a.yl,a.av)
        a.vxl.append(a.vx)
        a.vyl.append(a.vy)
        a.impact=0
        
    def adraw(a):
        pygame.draw.circle(screen,a.color,(a.x,a.y),a.radius,0)
    def fdraw(a):
        screen.blit(fire,(a.x-frect.centerx,a.y-frect.centery))
    def vlock(a):
        pass
    def move(a):        
                  
        for a.vx2 in a.vxl:
            for a.vy2 in a.vyl:
                
                if a.xl<0: 
                                           
                    a.x=a.x-a.vx2
                                                
                if a.xl>0:
                                             
                    a.x=a.x+a.vx2
                                
                if a.yl<0:
                    a.y=a.y-a.vy2
                                           
                                                
                if a.yl>0:
                    a.y=a.y+a.vy2
                if a.yl==0:
                    if a.xl>0:
                        a.x=a.x+a.vx2
                if a.xl<0:
                    a.x=a.x-a.vx2
                if a.xl==0:
                    if a.yl>0:
                        a.y=a.y+a.vy2
                if a.yl<0:
                    a.y=a.y-a.vy2
    def fcollide(a,elist):
        a.hhx=p1.x+4
        a.hhy=p1.y+4
        a.hhw=p1.x+yrect.centerx*2-4
        a.hhh=p1.y+yrect.centery*2-4
        a.elist=elist
        if a.x <=lwall or a.x>=rwall or a.y<=uwall or a.y>=dwall:
            boomsound.play()
            
            a.elist.append(almostuseless(a.x,a.y))
                                
            f1.flist.pop(f1.flist.index(a))
        elif a.x <=p1.x+yrect.centerx+60 and a.x>=p1.x+yrect.centerx-60 and a.y >= p1.y+yrect.centery-60 and a.y<= p1.y+yrect.centery+60 and p1.ashield():
            boomsound.play()
            
            a.elist.append(almostuseless(a.x,a.y))            
            f1.flist.pop(f1.flist.index(a))
        elif a.x<=a.hhw and a.x>=a.hhx and a.y >=a.hhy and a.y <=a.hhh:
            
                
            a.elist.append(almostuseless(a.x,a.y))
                
            p1.hit(a.damage)
                    
            f1.flist.pop(f1.flist.index(a))
        
                        
        
  
    def acollide(a,elist):      
        a.elist=elist
        if a.x <=lwall or a.x>=rwall or a.y<=uwall or a.y>=dwall:
            boomsound.play()
            
                
            a.elist.append(almostuseless(a.x,a.y))
                            
            p1.atk.pop(p1.atk.index(a))
        elif a.x>= f1.x+30 and a.x<=f1.x+drect.centerx*2-30 and a.y>f1.y+50 and a.y<f1.y+drect.centery*2-50:
           
            a.elist.append(almostuseless(a.x,a.y))   
            f1.hit(a.damage)
            p1.atk.pop(p1.atk.index(a))

class heroskill():
    def __init__(a,screen,color,x,y,radius,damage,xlog,ylog,av,identifier=1):
        a.screen=screen
        a.color=color
        a.x=x
        a.y=y
        a.radius=radius
        a.av=av
        
        a.damage=damage
        a.vxl=[]
        a.vyl=[]
        a.xl=xlog
        a.yl=ylog
        a.vx,a.vy=avaRemastered(a.xl,a.yl,a.av)
        a.vxl.append(a.vx)
        a.vyl.append(a.vy)
        a.identifier=identifier
    def draw(a):
        pygame.draw.circle(screen,a.color,(a.x,a.y),a.radius,0)
        if a.identifier==1:
            pygame.draw.circle(screen,(255,0,0),(a.x,a.y),a.radius+1,1)
    def move(a):
        for a.vx2 in a.vxl:
            for a.vy2 in a.vyl:
                
                if a.xl<0: 
                                           
                    a.x=a.x-a.vx2
                                                
                if a.xl>0:
                                             
                    a.x=a.x+a.vx2
                                
                if a.yl<0:
                    a.y=a.y-a.vy2
                                           
                                                
                if a.yl>0:
                    a.y=a.y+a.vy2
                if a.yl==0:
                    if a.xl>0:
                        a.x=a.x+a.vx2
                if a.xl<0:
                    a.x=a.x-a.vx2
                if a.xl==0:
                    if a.yl>0:
                        a.y=a.y+a.vy2
                if a.yl<0:
                    a.y=a.y-a.vy2
    def collide(a,elist):
        a.elist=elist
        if a.x <=lwall or a.x>=rwall or a.y<=uwall or a.y>=dwall:
            boomsound.play()
            
                
            a.elist.append(almostuseless(a.x,a.y))
                            
            p1.skilll.pop(p1.skilll.index(a))
        elif a.x>= f1.x+30 and a.x<=f1.x+drect.centerx*2-30 and a.y>f1.y+50 and a.y<f1.y+drect.centery*2-50:
           
            a.elist.append(almostuseless(a.x,a.y))   
            f1.hit(a.damage)
            p1.skilll.pop(p1.skilll.index(a))
def avaSpecial(theta,thita,av):
    avx=mt.cos(mt.radians(thita))*av
    avy=mt.cos(mt.radians(theta))*av
                     
    return round(avx),round(avy)

    
def avaRemastered(x,y,av):
    z=mt.hypot(x,y)
    x=abs(x)
    y=abs(y)
           
    try:
        theta=mt.degrees(mt.atan(x/y))
        thita=90-theta
        
    except:
        try:
            thita=mt.degrees(mt.atan(y/x))
            theta=90-thita
        except:
            thita=45
            theta=45
            
    avx=mt.cos(mt.radians(thita))*av
    avy=mt.cos(mt.radians(theta))*av
                     
    return round(avx),round(avy)

                
def avaV1(x,y,av):
    z=mt.hypot(x,y)
    x=abs(x)
    y=abs(y)
        
            
    if not(y==0):
        theta=mt.degrees(mt.atan(x/y))
        thita=90-theta
    if not(x==0):
        thita=mt.degrees(mt.atan(y/x))
        theta=90-thita
    if not(x==0 and y==0):
        
        
        if x==0 or y==0:
            if x==0:
                av=av-3
                avx=av*((90-theta)/90)
                avy=av*(theta/90)
                
            if y==0:
                av=av-3
                avx=av*((90-thita)/90)
                avy=av*(thita/90)
        else:
            
            if x>=y:
                if theta>=thita:
                    avx=(theta/90)*av
                    avy=(thita/90)*av
                elif thita>=theta:
                    avx=(thita/90)*av
                    avy=(theta/90)*av
            elif y>=x:
                if theta>=thita:
                    avx=(thita/90)*av
                    avy=(theta/90)*av
                elif thita>=theta:
                    avx=(theta/90)*av
                    avy=(thita/90)*av
                    
        if theta>30 and theta<60:
            avx=avx*1.5
            avy=avy*1.5
        elif (theta>10 and theta <31) or (theta >59 and theta <80):
            avx=avx*1.25
            avy=avy*1.25
        else:
            avx=avx*1.1
            avy=avy*1.1
        
    if x==0 and y==0:
        chance=ran.randint(0,1)
        if chance==1:
            avx=av
            avy=0
        if chance==0:
            avx=0
            avy=av            
            
    return round(avx),round(avy)
def pickups():
    global medkitl,armourl,damagel
    randomchance=ran.randint(1,3)
    x=ran.randint(lwall+yrect.centerx,rwall-yrect.centerx)
    y=ran.randint(uwall+yrect.centery+mrect.centerx,dwall-mrect.centery-yrect.centery)
    
    if timer%120==0:
        
        if randomchance==1:
            medkitl.append(boost(x,y))
        if randomchance==2:
            armourl.append(boost(x,y))
        if randomchance==3:
            damagel.append(boost(x,y))
    for med in medkitl:
        med.medkit()
        if p1.medkit:
            medkitl.pop(medkitl.index(med))
            p1.medkit=False
            
    for atk in damagel:
        atk.damage()
        if p1.dmgup:
            damagel.pop(damagel.index(atk))
            p1.dmgup=False

    for armor in armourl:
        armor.shield()
        if p1.shieldup:
            armourl.pop(armourl.index(armor))
            p1.shieldup=False
    if p1.healnum !=0:    
        p1.heal()
    if p1.dmgupnum!=0:
        p1.damageup()
    if p1.shieldnum!=0:
        p1.armourup()
class boost():
    def __init__(a,x,y):
        a.x=x
        a.y=y
    def medkit(a):
        screen.blit(medkit,(a.x-mrect.centerx,a.y-mrect.centery))
        p1.healget(a.x,a.y)
    def damage(a):
        screen.blit(sword,(a.x-krect.centerx,a.y-krect.centery))
        p1.damageupget(a.x,a.y)
    def shield(a):
        screen.blit(shield,(a.x-srect.centerx,a.y-srect.centery))
        p1.armourupget(a.x,a.y)
def cursor(mx,my):
    screen.blit(aim,(mx-arect.centerx,my-arect.centery))
def atrue():
    global elist
    for at in p1.atk:
        if len(p1.skilll)==0:
            adistance=mt.hypot((at.x-(p1.x+yrect.centerx)),(at.y-(p1.y+yrect.centery)))
            if adistance >=200:
                p1.atk.pop(p1.atk.index(at))

    for sk in p1.skilll:
        sk.move()
        sk.draw()
        sk.collide(elist)
        
    for at in p1.atk:
        at.move()
            
        at.adraw()
        at.acollide(elist)
    for at1 in p1.atk:
        for fi1 in f1.flist:
            if  at1.x+at1.radius>= fi1.x-fi1.radius and at1.x-at1.radius<=fi1.x+fi1.radius and at1.y+at1.radius>=fi1.y-fi1.radius and at1.y-at1.radius<=fi1.y+fi1.radius:
                try:
                    p1.atk.pop(p1.atk.index(at1))
                    fi1.impact=fi1.impact+1
                    elist.append(almostuseless(at1.x,at1.y))
                except:
                    pass
    for at2 in p1.atk:
        for fi2 in f1.sflist:
            if  at2.x+at2.radius>= fi2.x-fi2.radius and at2.x-at2.radius<=fi2.x+fi2.radius and at2.y+at2.radius>=fi2.y-fi2.radius and at2.y-at2.radius<=fi2.y+fi2.radius:
                try:
                    p1.atk.pop(p1.atk.index(at2))
                    fi2.impact=fi2.impact+1
                    elist.append(almostuseless(at2.x,at2.y))
                except:
                    pass
    for skill1 in p1.skilll:
        for fi3 in f1.flist:
            if  skill1.x+skill1.radius>= fi3.x-fi3.radius and skill1.x-skill1.radius<=fi3.x+fi3.radius and skill1.y+skill1.radius>=fi3.y-fi3.radius and skill1.y-skill1.radius<=fi3.y+fi3.radius:
                try:
                    p1.skilll.pop(p1.skilll.index(skill1))
                    fi3.impact=fi3.impact+1
                    elist.append(almostuseless(skill1.x,skill1.y))
                except:
                    pass
    for skill2 in p1.skilll:
        for fi4 in f1.sflist:
            if  skill2.x+skill2.radius>= fi4.x-fi4.radius and skill2.x-skill2.radius<=fi4.x+fi4.radius and skill2.y+skill2.radius>=fi4.y-fi4.radius and skill2.y-skill2.radius<=fi4.y+fi4.radius:
                try:
                    p1.skilll.pop(p1.skilll.index(skill2))
                    fi4.impact=fi4.impact+1
                    elist.append(almostuseless(skill2.x,skill2.y))
                except:
                    pass
    for b in elist:
        b.draw(elist)
class popups():
    def __init__(a,x,y,num,vary):
        a.x=x
        a.y=y
        a.num=round(num)
        a.vary=vary
        a.type=[]
        a.type.append(a.vary)#1,2,3,4=hit,heal,armor,dmg
        a.hittype=False
        a.healtype=False
        a.armortype=False
        a.dmgtype=False
        
        for a.get in a.type:
            if a.get==1:
                a.hittype=True

            elif a.get==2:
                a.healtype=True

            elif a.get==3:
                a.armortype=True

            elif a.get==4:
                a.dmgtype=True
            

    def draw(a):
        
        a.y=a.y-5
        
        if a.hittype:
            screen.blit((fontok.render(str(a.num)+' Oof',True,(255,255,255))),(a.x,a.y))


        if a.armortype:
            screen.blit((fontok.render(str(a.num)+' ArmorUp',True,(90,90,200))),(a.x,a.y))


        if a.healtype:
            screen.blit((fontok.render(str(a.num)+' Healed',True,(60,210,60))),(a.x,a.y))


        if a.dmgtype:
            screen.blit((fontok.render(str(a.num)+' DamageUp',True,(210,60,60))),(a.x,a.y))

class rankshow():
    def __init__(a,num,name,time,hell,x,y,date,identifier):
        a.num=num
        a.name=name
        a.time=time
        a.hell=hell
        a.x=x
        a.y=y-4
        a.date=date
        a.identifier=identifier
    def draw(a):
        if a.identifier==0:
            screen.blit(fontrank.render(str(a.num+1)+') Name: '+str(a.name)+' /Time: '+str(a.time//60)+' Minutes '+ str(a.time%60)+' Seconds '+' /Hell Mode: '+str(a.hell),True,(255,255,255)),(a.x,a.y))
            screen.blit(fontrank.render('Recorded On: '+str(a.date),True,(255,255,255)),(a.x,a.y+12))
        elif a.identifier==1:
            screen.blit(fontrank.render(str(a.num+1)+') Name: '+str(a.name)+' /Time: '+str(a.time//60)+' Minutes '+ str(a.time%60)+' Seconds '+' /Hell Mode: '+str(a.hell),True,(255,0,0)),(a.x,a.y))
            screen.blit(fontrank.render('Recorded On: '+str(a.date),True,(255,0,0)),(a.x,a.y+14))
def ftrue():
    global elist
    
    f1.fire()
    
    
    for f in f1.flist:
        
        f.move()
        f.fdraw()
        f.fcollide(elist)
        if f.impact>=1:
            try:
                f1.flist.pop(f1.flist.index(f))
                elist.append(almostuseless(f.x,f.y))
            except:
                pass
    for s in f1.sflist:
        s.move()
        s.draw()
        s.collide(elist)
        if s.impact>=3:
            try:
                f1.sflist.pop(f1.sflist.index(s))
                elist.append(almostuseless(s.x,s.y))
            except:
                pass
        if s.type==7:
            if f1.ftimer%2==0:
                if not(f1.nightmaremode):
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,0,f1.fv-1,0,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,72,f1.fv-1,72,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,36,f1.fv-1,144,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,36,f1.fv-1,216,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,72,f1.fv-1,288,1))
                if f1.nightmaremode:
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,0,f1.fv-1,0,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,72,f1.fv-1,72,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,36,f1.fv-1,144,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,36,f1.fv-1,216,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,72,f1.fv-1,288,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,0,f1.fv-0,0,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,72,f1.fv-0,72,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,36,f1.fv-0,144,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,36,f1.fv-0,216,1))
                    f1.sflist.append(newtypeprojectiles(screen,s.x,s.y,f1.fradius,f1.fdamage,72,f1.fv-0,288,1))
    for b in elist:
        b.draw(elist)
def Draw():
    
    
    f1.draw(screen,pcx,fcx)
    p1.draw(screen,pcx,fcx)
    p1.thirddegreeburn()
    p1.stats()


class volume():
    def __init__(a,x,y,soundlength=150,musiclength=150):
        a.x=x
        a.y=y
        a.soundlength=soundlength
        a.musiclength=musiclength
        
        a.clicking1=False
        a.clicking2=False
    def draw(a):
        if a.soundlength>=300:
            a.soundlength=300
        if a.musiclength>=300:
            a.musiclength=300
        if a.soundlength<=0:
            a.soundlength=0
        if a.musiclength<=0:
            a.musiclength=0
        pygame.draw.rect(screen,(255,0,0),(a.x,a.y,300,16),0)
        pygame.draw.rect(screen,(0,255,0),(a.x,a.y,a.soundlength,16),0)
        pygame.draw.rect(screen,(44,44,44),(a.x+a.soundlength-6,a.y+16,12,20),0)

        pygame.draw.rect(screen,(255,0,0),(a.x,a.y+120,300,16),0)
        pygame.draw.rect(screen,(0,255,0),(a.x,a.y+120,a.musiclength,16),0)
        pygame.draw.rect(screen,(44,44,44),(a.x+a.musiclength-6,a.y+120+16,12,20),0)

        screen.blit(speaker,(a.x-90,a.y-34))
        screen.blit(note,(a.x-90,a.y+82))

        screen.blit(fonthp.render(str(round(100*(a.soundlength/300),2))+'%',True,(0,0,0)),(a.x+114,a.y-36))
        screen.blit(fonthp.render(str(round(100*(a.musiclength/300),2))+'%',True,(0,0,0)),(a.x+114,a.y-36+120))
        
    def act(a,mx,my):
        a.mx=mx
        a.my=my
        
        if mouse[0]:
            if a.mx>=a.x+a.soundlength-6 and a.mx <= a.x+a.soundlength-6+12 and a.my>= a.y+16 and a.my<=a.y+16+20 and (not(a.clicking2)):
                a.clicking1=True
            if a.mx>=a.x+a.musiclength-6 and a.mx <= a.x+a.musiclength-6+12 and a.my>= a.y+16+120 and a.my<=a.y+16+120+20 and (not(a.clicking1)):
                a.clicking2=True
        if a.clicking1:
            if mouse[0]:   
                a.soundlength=a.mx-a.x
            else:
                a.clicking1=False
        if a.clicking2:
            if mouse[0]:   
                a.musiclength=a.mx-a.x
            else:
                a.clicking2=False

        

    def set(a):
        healsound.set_volume(0.5*(a.soundlength/300))
        hitsoundweak.set_volume(0.6*(a.soundlength/300))
        hitsoundmedio.set_volume(0.6*(a.soundlength/300))
        hitsoundstrong.set_volume(0.6*(a.soundlength/300))
        burnsound.set_volume(0.5*(a.soundlength/300))
        diesound.set_volume(0.6*(a.soundlength/300))
        buffsound.set_volume(0.6*(a.soundlength/300))
        firesound.set_volume(0.5*(a.soundlength/300))
        skillsound.set_volume(0.6*(a.soundlength/300))
        ultisound.set_volume(0.6*(a.soundlength/300))
        boomsound.set_volume(0.6*(a.soundlength/300))
        attacksound.set_volume(0.5*(a.soundlength/300))
        startsound.set_volume(0.6*(a.soundlength/300))
        clicksound.set_volume(0.8*(a.soundlength/300))

        
                
volume1=volume(swid/2-100,shei/2-160,150,150)


def p1moves():
    global firstclick
    if not(firstclick):
        p1.atime=1
            
    p1.activation(mx,my)

    if not(firstclick):
        p1.atime=0
    if mouse[0]:
        firstclick=True
def verysecretsecret():
    global u1,u2,d1,d2,l1,r1,l2,r2,b1,a1,secrettimer
    
    
    if u1 or u2 or d1 or d2 or l1 or r1 or l2 or r2 or b1 or a1:
        secrettimer=secrettimer+1
    
    if k[pygame.K_UP]:
        u1=True
    if k[pygame.K_UP] and u1:
        u2=True
    if k[pygame.K_DOWN] and u1 and u2:
        d1=True
    if k[pygame.K_DOWN] and u1 and u2 and d1:
        d2=True
    if k[pygame.K_LEFT] and u1 and u2 and d1 and d2:
        l1=True
    if k[pygame.K_RIGHT] and u1 and u2 and d1 and d2 and l1:
        r1=True
    if k[pygame.K_LEFT] and u1 and u2  and d1 and d2 and l1 and r1:
        l2=True
    if k[pygame.K_RIGHT] and u1 and u2 and d1 and d2 and l1 and r1 and l2:
        r2=True
    if k[pygame.K_b] and u1 and u2 and d1 and d2 and l1 and r1 and l2 and r2:
        b1=True
    if k[pygame.K_a] and u1 and u2 and d1 and d2 and l1 and r1 and l2 and r2 and b1:
        a1=True
    if u1 and u2 and d1 and d2 and l1 and r1 and l2 and r2 and b1 and a1:
        p1.secret=True
    if secrettimer>=300:
        secrettimer=0
        u1=False
        u2=False
        d1=False
        d2=False
        l1=False
        r1=False
        l2=False
        r2=False
        b1=False
        a1=False
    
        
herox=200
heroy=500

foex=620
foey=120

f1=foe(foex,foey,100000,4000)
p1=hero(herox,heroy,10000,0)

button1=bgrect.centerx-100,bgrect.centery-200,200,100
menurun=True
battlerun=False

loading=True
battle = False
menu=False
run=True
hdeadrun=False
hdead=False
ddead=False
ddeadrun=False
controls=False
controlsrun=False
leaderrun=False
leader=False
getidrun=False
getid=False
tipsrun=False
tips=False
creditrun=False
credit=False
settingsrun=False
settings=False

pause=False
pauseup=False


rans=0
fwid=0
lf=0
timer=0                    
sec=0
minute=0
firstclick=False                        
mx=0
my=0
mouse=()
medkitl=[]
armourl=[]
damagel=[]
elist=[]
getinput=False
usernamelist=[]
username=""
events=None
nameexistshow=False
nameemptyshow=False
namelength=0

hellsec=180
number=0

ranklist=[]
try:
    ranklist=pickle.load(open(r"/var/www/html/First Game!/LeaderboardSave/LeaderboardSave.txt","rb"))
except:
    pass


r=ran.randint(0,255)
g=ran.randint(0,255)
b=ran.randint(0,255)
u1=False
u2=False
d1=False
d2=False
l1=False
r1=False
l2=False
r2=False
b1=False
a1=False
secrettimer=0
metimer=0
melist=[]
class manyme():
    def __init__(a,x,y):
        a.x=x
        a.y=y
    def draw(a):
        screen.blit(me,(a.x,a.y))
    
def areset():
    global run,menurun,battlerun,battle,menu,controls,controlsrun,loading,hdead,hdeadrun,ddead,ddeadrun,leader,leaderrun,getid,getidrun,settings,settingsrun,u1,u2,d1,d2,l1,r1,l2,r2,b1,a1,secrettimer,tipsrun,tips,creditrun,credit,pause
    run=True
    menurun=False
    battlerun=False
    menu=False
    battle=False
    hdead=False
    hdeadrun=False
    ddead=False
    ddeadrun=False
    loading=False
    controls=False
    controlsrun=False
    leaderrun=False
    leader=False
    getid=False
    getidrun=False
    tips=False
    tipsrun=False
    creditrun=False
    credit=False
    settingsrun=False
    settings=False
    u1=False
    u2=False
    d1=False
    d2=False
    l1=False
    r1=False
    l2=False
    r2=False
    b1=False
    a1=False
    secrettimer=0
    pause=False
    
def flipquit():
    global run
    pygame.display.flip()
    
    for event in events:
        if event.type==pygame.QUIT:
            
            areset()
            run=False
def init():
    global mx,my,battle,menu,controls,hdead,ddead,mouse,leader,getid,events,tips,credit,settings
    events=pygame.event.get()
    clock.tick(30)
    mouse=pygame.mouse.get_pressed()
    mx,my=pygame.mouse.get_pos()
    music()
    volume1.set()
    if battlerun:
        battle=True
    else:
        battle=False
    if menurun:
        menu=True
    else:
        menu=False
    if hdeadrun:
        hdead=True
    else:
        hdead=False
    if hdeadrun:
        hdead=True
    else:
        hdead=False
    if ddeadrun:
        ddead=True
    else:
        ddead=False
    if controlsrun:
        controls=True
    else:
        controls=False
    if leaderrun:
        leader=True
    else:
        leader=False
    if getidrun:
        getid=True
    else:
        getid=False
    if tipsrun:
        tips=True
    else:
        tips=False
    if creditrun:
        credit=True
    else:
        credit=False
    if settingsrun:
        settings=True
    else:
        settings=False
def hcolor():
    global r,g,b
    r=r+ran.randint(0,5)
    g=g+ran.randint(0,5)
    b=b+ran.randint(0,5)
    if r >= 255:
        r=0
    if g >= 255:
        g=0
    if b >= 255:
        b=0                        
while run:    
    while loading:
        
        init()
        screen.blit(bg,(0,0))
        pygame.draw.rect(screen,(0,0,0),(0,lf,swid,fwid),0)
        if not(fwid>=swid):
            fwid=fwid+154
        if fwid>=swid:
            lf=lf+154
        if lf>=swid:
            lf=0
            fwid=0
            break
        username=""    
        cursor(mx,my)
        flipquit()    
        
    while menu:                
        init()
        screen.blit(bg,(0,0))
        
        pygame.draw.rect(screen,(200,100,0),(button1),0)
        pygame.draw.rect(screen,(60,60,180),(swid/2-100,shei/2-64,200,50),0)
        pygame.draw.rect(screen,(164,164,0),(swid/2-150,shei/2+26,300,50),0)
        pygame.draw.rect(screen,(0,144,0),(swid/2-60,shei/2+116,120,50),0)
        pygame.draw.rect(screen,(45,45,45),(swid/2-90,shei/2+206,180,50),0)
        pygame.draw.rect(screen,(211,0,211),(swid/2-100,shei/2+296,200,50),0)
        
        screen.blit(titleb,(20,10))
        screen.blit(title,(27,10))
        screen.blit(text1,(bgrect.centerx-101,bgrect.centery-225))
        screen.blit(controlstext,(swid/2-98,shei/2-75))
        screen.blit(leaderbod,(swid/2-148,shei/2+15))
        screen.blit(tipstext,(swid/2-56,shei/2+104))
        screen.blit(credito,(swid/2-86,shei/2+194))
        screen.blit(settin,(swid/2-101,shei/2+282))


        screen.blit(version,(swid-121,shei-22))
        if mouse[0]:
           
            if mx>=bgrect.centerx-100 and mx<=bgrect.centerx-100+200:
                if my>=bgrect.centery-200 and my<=bgrect.centery-200+100:
                    clicksound.play()
                    
                        
                    areset()
                    loading=True
                    #battlerun=True
                    getidrun=True
            if mx>=swid/2-100 and mx <=swid/2-100+200:
                if my >=shei/2-64 and my<=shei/2-64+50:
                    clicksound.play()
                    areset()
                    controlsrun=True
                    loading=True

            if mx>=swid/2-150 and mx <= swid/2-150+300:
                if my >= shei/2+26 and my<=shei/2+26+50:
                    clicksound.play()
                    areset()
                    leaderrun=True
                    loading=True
            if mx>=swid/2-60 and mx <= swid/2-60+120:
                if my>=shei/2+116 and my<=shei/2+116+50:
                    clicksound.play()
                    areset()
                    tipsrun=True
                    loading=True

            if mx>=swid/2-90 and mx <=swid/2-90+180:
                if my>=shei/2+206 and my<= shei/2+206+50:
                    clicksound.play()
                    areset()
                    creditrun=True
                    loading=True
            if mx>=swid/2-100 and mx<=swid/2-100+200:
                if my>=shei/2+296 and my <=shei/2+296+50:
                    clicksound.play()
                    areset()
                    settingsrun=True
                    loading=True
                         
        cursor(mx,my)        
        flipquit()
    while settings:
        init()
        screen.blit(bg,(0,0))
        pygame.draw.rect(screen,(200,0,0),(22,24,132,50),0)
        screen.blit(backtext,(30,12))

        pygame.draw.rect(screen,(200,100,24),(swid/2-296,shei/2-300,600,400),0)
            
        screen.blit(settin,(swid/2-settin.get_width()/2,shei/2-303))
        



        volume1.draw()
        volume1.act(mx,my)



        if mouse[0]:
            if mx>=22 and mx<=22+132:
                if my>=24 and my<=24+50:
                    clicksound.play()
                    areset()
                    menurun=True
                    loading=True





        cursor(mx,my)
        flipquit()
    while controls:
        init()
        screen.blit(bg,(0,0))
        
        pygame.draw.rect(screen,(200,0,0),(22,24,132,50),0)
        screen.blit(backtext,(30,12))
        screen.blit(ctrl1,(100,80))
        screen.blit(ctrl2,(100,130))
        screen.blit(ctrl3,(100,180))
        screen.blit(ctrl4,(100,230))
        screen.blit(ctrl5,(100,280))
        screen.blit(ctrl6,(100,330))
        screen.blit(ctrl7,(100,380))
        screen.blit(ctrl8,(100,430))
        screen.blit(ctrl9,(100,480))


        if mouse[0]:
            if mx>=22 and mx<=22+132:
                if my>=24 and my<=24+50:
                    clicksound.play()
                    areset()
                    menurun=True
                    loading=True






        cursor(mx,my)
        flipquit()

    while leader:
        init()
        screen.blit(bg,(0,0))
        pygame.draw.rect(screen,(200,0,0),(22,24,132,50),0)
        screen.blit(backtext,(30,12))
        
        
        for rank in ranklist:
            rank.draw()
            






        if mouse[0]:
            if mx>=22 and mx<=22+132:
                if my>=24 and my<=24+50:
                    clicksound.play()
                    areset()
                    menurun=True
                    loading=True









        cursor(mx,my)
        flipquit()

    while tips:
        init()
        screen.blit(bg,(0,0))
        
        pygame.draw.rect(screen,(200,0,0),(22,24,132,50),0)
        screen.blit(backtext,(30,12))






        screen.blit(tip1,(100,80))
        screen.blit(tip2,(100,130))
        screen.blit(tip3,(100,180))
        screen.blit(tip4,(100,230))
        screen.blit(tip5,(100,280))
        screen.blit(tip6,(100,330))
        screen.blit(tip7,(100,380))
        screen.blit(tip8,(100,430))
        screen.blit(tip9,(100,480))
        
        if mouse[0]:
            if mx>=22 and mx<=22+132:
                if my>=24 and my<=24+50:
                    clicksound.play()
                    areset()
                    menurun=True
                    loading=True








        cursor(mx,my)

        flipquit()
    while credit:
        init()
        screen.blit(bg,(0,0))
        
        
        metimer=metimer+1
        if metimer%10==0:
            melist.append(manyme(ran.randint(1,swid-me.get_width()),ran.randint(1,shei-me.get_height())))
        if metimer>=10:
            metimer=0
        for menow in melist:
            menow.draw()


        if mouse[0]:
            if mx>=22 and mx<=22+132:
                if my>=24 and my<=24+50:
                    clicksound.play()
                    areset()
                    menurun=True
                    loading=True




                    
        pygame.draw.rect(screen,(200,0,0),(22,24,132,50),0)
        screen.blit(backtext,(30,12))
        cursor(mx,my)
        flipquit()
    while getid:
        init()
        screen.blit(bg,(0,0))
        screen.blit(namehere,(80,25))
        pygame.draw.rect(screen,(0,0,0),(swid/2-275,shei/2-200,550,90),0)
        pygame.draw.rect(screen,(128,128,128),(swid/2-265,shei/2-190,530,70),0)
        screen.blit(typehere,(swid/2-132,shei/2-195))
        pygame.draw.rect(screen,(0,211,0),(swid/2-90,shei/2,180,60),0)
        screen.blit(enter,(swid/2-67,shei/2-8))
        usercheck=list(username.lower())
        userchange=list(username)
        if mouse[0]:
            
            if mx>=swid/2-275 and mx <= swid/2-275+550 and my>=shei/2-200 and my<= shei/2-200+90:
                clicksound.play()
                getinput=True
            if not(getinput):
                if mx>=swid/2-90 and mx<=swid/2-90+180 and my>=shei/2 and my<=shei/2+60 and namelength==0:
                    clicksound.play()
                    nameemptyshow=True
            elif not(mx>=swid/2-275 and mx <= swid/2-275+550 and my>=shei/2-200 and my<= shei/2-200+90):
                
                if mx>=swid/2-90 and mx<=swid/2-90+180 and my>=shei/2 and my<=shei/2+60 and namelength!=0:
                    clicksound.play()
                    if len(usernamelist)!=0:
                        try:
                            checksee=usernamelist.index(username)
                            nameexistshow=True
                                
                        except:
                            startsound.play()
                            usernamelist.append(username)
                            areset()
                            loading=True
                            battlerun=True
                            getinput=False
                    else:
                        startsound.play()
                        usernamelist.append(username)
                        areset()
                        loading=True
                        battlerun=True
                        getinput=False
                elif mx>=swid/2-90 and mx<=swid/2-90+180 and my>=shei/2 and my<=shei/2+60 and namelength==0:
                    clicksound.play()
                    nameemptyshow=True
            
                #if not(mx>=swid/2-90 and mx<=swid/2-90+180 and my>=shei/2 and my<=shei/2+60):
                    #getinput=False
        if getinput:
            pygame.draw.rect(screen,(255,255,255),(swid/2-265,shei/2-190,530,70),0)
            showname=fontmedio.render(str(username),True,(0,0,0))
            screen.blit(showname,(swid/2-255,shei/2-190))
            namelength=len(username)
            if namelength>=15:
                username=username[:-1]
            for event in events:
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        
                        username=username[:-1]
                    elif event.key == pygame.K_RETURN and namelength!=0:
                        clicksound.play()
                        if len(usernamelist)!=0:
                            try:
                                checksee=usernamelist.index(username)
                                nameexistshow=True
                                    
                            except:
                                startsound.play()
                                usernamelist.append(username)
                                areset()
                                loading=True
                                battlerun=True
                                getinput=False
                        else:
                            startsound.play()
                            usernamelist.append(username)
                            areset()
                            loading=True
                            battlerun=True
                            getinput=False   
                    elif event.key == pygame.K_RETURN and namelength==0:
                        clicksound.play()
                        nameemptyshow=True
                    else:
                        nameemptyshow=False
                        nameexistshow=False
                        username=username+event.unicode
                
        if nameexistshow:
            screen.blit(nameexist,(swid/2-240,shei/2-100))
        
        if nameemptyshow:
            screen.blit(nameempty,(swid/2-289,shei/2-100))
        
        fbnumlist=[fbnum for fbnum,fb1 in enumerate(usercheck) if fb1 =="f"]
        unumlist=[unum for unum,u1 in enumerate(usercheck) if u1 =="u"]
        cnumlist=[cnum for cnum,c1 in enumerate(usercheck) if c1 =="c"]
        knumlist=[knum for knum,k1 in enumerate(usercheck) if k1 =="k"]
        snumlist=[snum for snum,s1 in enumerate(usercheck) if s1 =="s"]
        hnumlist=[hnum for hnum,h1 in enumerate(usercheck) if h1 =="h"]
        inumlist=[inum for inum,i1 in enumerate(usercheck) if i1 =="i"]
        tnumlist=[tnum for tnum,t1 in enumerate(usercheck) if t1 =="t"]
        bnumlist=[bnum for bnum,b1 in enumerate(usercheck) if b1 =="b"]
        for b1 in bnumlist:
            for i2 in inumlist:
                for t2 in tnumlist:
                    for c2 in cnumlist:
                        for h2 in hnumlist:
                            if b1+1==i2 and i2+1==t2 and t2+1==c2 and c2+1==h2:
                                userchange[b1]="B"
                                userchange[i2]="E"
                                userchange[t2]="E"
                                userchange[c2]="E"
                                userchange[h2]="B"
                                username=""
                                username=username.join(userchange)
        for s1 in snumlist:
            for h1 in hnumlist:
                for i1 in inumlist:
                    for t1 in tnumlist:
                        if s1+1==h1 and h1+1==i1 and i1+1==t1:
                            userchange[s1]="B"
                            userchange[h1]="E"
                            userchange[i1]="E"
                            userchange[t1]="B"
                            username=""
                            username=username.join(userchange)
                        elif userchange[s1+1]==" " and userchange[s1+2]==userchange[h1] and userchange[h1+1]==" " and userchange[h1+2]==userchange[i1] and userchange[i1+1]==" " and userchange[i1+2]==userchange[t1]:
                            userchange[s1]="B"
                            userchange[h1]="E"
                            userchange[i1]="E"
                            userchange[t1]="B"
                            username=""
                            username=username.join(userchange)



                        elif userchange[s1+1]==" " and (userchange[s1+2]==userchange[h1] or userchange[s1+3]==userchange[h1] or userchange[s1+4]==userchange[h1] or userchange[s1+5] ==userchange[h1] or userchange[s1+6]==userchange[h1] or userchange[s1+7]==userchange[h1]) and (userchange[s1+3]==userchange[t1] or userchange[s1+4]==userchange[t1] or userchange[s1+5]==userchange[t1] or userchange[s1+6]==userchange[t1] or userchange[s1+7]==userchange[t1] or userchange[s1+8]==userchange[t1] or userchange[s1+9]==userchange[t1] or userchange[s1+10]==userchange[t1] or userchange[s1+11]==userchange[t1] or userchange[s1+12]==userchange[t1]):
                            userchange[s1]="B"
                            userchange[h1]="E"
                            userchange[i1]="E"
                            userchange[t1]="B"
                            username=""
                            username=username.join(userchange)
        for fb1 in fbnumlist:
            for u1 in unumlist:
                for c1 in cnumlist:
                    for k1 in knumlist:
                        if fb1+1==u1 and u1+1==c1 and c1+1==k1:
                            userchange[fb1]="B"
                            userchange[u1]="E"
                            userchange[c1]="E"
                            userchange[k1]="B"
                            username=""
                            username=username.join(userchange)
                        elif userchange[fb1+1]==" " and userchange[fb1+2]==userchange[u1] and userchange[u1+1]==" " and userchange[u1+2]==userchange[c1] and userchange[c1+1]==" " and userchange[c1+2]==userchange[k1]:
                            userchange[fb1]="B"
                            userchange[u1]="E"
                            userchange[c1]="E"
                            userchange[k1]="B"
                            username=""
                            username=username.join(userchange)



                        elif userchange[fb1+1]==" " and (userchange[fb1+2]==userchange[u1] or userchange[fb1+3]==userchange[u1] or userchange[fb1+4]==userchange[u1] or userchange[fb1+5] ==userchange[u1] or userchange[fb1+6]==userchange[u1] or userchange[fb1+7]==userchange[u1]) and (userchange[fb1+3]==userchange[k1] or userchange[fb1+4]==userchange[k1] or userchange[fb1+5]==userchange[k1] or userchange[fb1+6]==userchange[k1] or userchange[fb1+7]==userchange[k1] or userchange[fb1+8]==userchange[k1] or userchange[fb1+9]==userchange[k1] or userchange[fb1+10]==userchange[k1] or userchange[fb1+11]==userchange[k1] or userchange[fb1+12]==userchange[k1]):
                            userchange[fb1]="B"
                            userchange[u1]="E"
                            userchange[c1]="E"
                            userchange[k1]="B"
                            username=""
                            username=username.join(userchange)
                            
        cursor(mx,my)
        flipquit()

        
    while battle:
        init()        
        screen.blit(bg,(0,0))
        
        
        k=pygame.key.get_pressed()
        
        timer=timer+1
        if timer%30==0:
            sec=sec+1
            if hellsec!=0:
                hellsec=hellsec-1
        
        hcolor()

        Herow=fonthero.render('Hero',True,(r,g,b))
        
        
        screen.blit(fontdragon.render('Enraged In: '+str(round(hellsec//60))+':'+str(round(hellsec%60)),True,(255,0,0)),(swid-292,34))
        if hellsec==0 and (not(f1.nightmaremode)):
            f1.nightmaremode=True
            
        for event in events:
                if event.type == pygame.KEYDOWN:
                    if k[pygame.K_ESCAPE]:
                        pause=True
        
        while pause:
            init()
            screen.blit(bg,(0,0))
            k=pygame.key.get_pressed()
            pygame.draw.rect(screen,(200,100,24),(swid/2-300,shei/2-300,600,500),0)
            
            screen.blit(paused,(swid/2-paused.get_width()/2,shei/2-303))
            screen.blit(pauseesc,(swid/2-pauseesc.get_width()/2,shei/2+118))



            volume1.draw()
            volume1.act(mx,my)

            
            
            for event in events:
                if event.type == pygame.KEYUP:
                    pauseup=True
            if pauseup:
                if k[pygame.K_ESCAPE]:
                    pause=False
                    pauseup=False






            cursor(mx,my)
            flipquit()
        
        pcx=p1.x+yrect.centerx
        fcx=f1.x+drect.centerx

        #fsize=(f1.x+20,f1.y+20,drect.centerx*2-40,drect.centery*2-40)
            
        pickups()
        verysecretsecret()
        
        if timer==300:
            timer=0
        
        p1.move()
        f1.move()
        

        p1moves()
        Draw()
        
        
        atrue()
        ftrue()
        cursor(mx,my) 
        if f1.die()==0:
            diesound.play()
            
            if not(len(ranklist)>31):
                if f1.nightmaremode:
                    if not(p1.secret): 
                        ranklist.append(rankshow(len(ranklist),usernamelist[0],sec,"Yes",160,24*(len(ranklist)+1),datetime.datetime.now(),0))
                    elif p1.secret:
                        ranklist.append(rankshow(len(ranklist),usernamelist[0],sec,"Yes",160,24*(len(ranklist)+1),datetime.datetime.now(),1))
                    
                elif not(f1.nightmaremode):
                    if not(p1.secret):
                        ranklist.append(rankshow(len(ranklist),usernamelist[0],sec,"No",160,24*(len(ranklist)+1),datetime.datetime.now(),0))
                    elif p1.secret:
                        ranklist.append(rankshow(len(ranklist),usernamelist[0],sec,"No",160,24*(len(ranklist)+1),datetime.datetime.now(),1))
            if len(ranklist)>31:                
                if f1.nightmaremode:
                    if not(p1.secret):
                        ranklist.append(rankshow(len(ranklist),usernamelist[0],sec,"Yes",560,24*(len(ranklist)-32+1),datetime.datetime.now(),0))
                    elif p1.secret:
                        ranklist.append(rankshow(len(ranklist),usernamelist[0],sec,"Yes",560,24*(len(ranklist)-32+1),datetime.datetime.now(),1))

                    
                elif not(f1.nightmaremode):
                    if not(p1.secret):
                        ranklist.append(rankshow(len(ranklist),usernamelist[0],sec,"No",560,24*(len(ranklist)-32+1),datetime.datetime.now(),0))
                    elif p1.secret:
                        ranklist.append(rankshow(len(ranklist),usernamelist[0],sec,"No",560,24*(len(ranklist)-32+1),datetime.datetime.now(),1))
                
            usernamelist.pop()
            del p1
            del f1
            del medkitl[:]
            del armourl[:]
            del damagel[:]
            del elist[:]
            f1=foe(foex,foey,100000,4000)
            p1=hero(herox,heroy,10000,0)
            areset()
            ddeadrun=True
            loading=True

            pickle.dump(ranklist,open(r"/var/www/html/First Game!/LeaderboardSave/LeaderboardSave.txt","wb"))
            
        if p1.die()==0:
            diesound.play()
            
            usernamelist.pop()
            
            del p1
            del f1
            del medkitl[:]
            del armourl[:]
            del damagel[:]
            del elist[:]
            f1=foe(foex,foey,100000,4000)
            p1=hero(herox,heroy,10000,0)
            areset()
            hdeadrun=True
            loading=True
        flipquit()
    while ddead:
        init()
        
        screen.blit(treasure,(0,0))
        screen.blit(win,(140,25))



        screen.blit(tomb,(swid/2-372/2,shei-600))
        screen.blit(deaddragon,(swid/2-111/2,shei-475))
        
        if sec>=60:
            minute=sec//60
            sec=sec%60




        time=fontmedio.render('Time: '+str(minute)+' Minutes '+str(sec)+' Seconds',True,(255,255,255))
        screen.blit(time,(swid/2-320,shei-320))

        

        pygame.draw.rect(screen,(188,154,54),(swid/2-175,shei-205,350,70),0)
        pygame.draw.rect(screen,(255,255,51),(swid/2-170,shei-200,340,60),0)
        screen.blit(menubackw,(swid/2-169,shei-208))








        if mouse[0]:
            if mx>=swid/2-175 and mx<=swid/2+175 and my >=shei-205 and my<=shei-135:
                clicksound.play()
                areset()
                menurun=True
                loading=True
                minute=0
                sec=0
                timer=0
                hellsec=180









        
        cursor(mx,my)
        flipquit()
    while hdead:
        init()        
        screen.blit(heaven,(0,0))
        screen.blit(dead,(120,80))
        mx,my=pygame.mouse.get_pos()
        screen.blit(tomb,(swid/2-372/2,shei-600))
        screen.blit(yuushaf,(swid/2-90/2,shei-475))
        pygame.draw.rect(screen,(0,0,0),(swid/2-175,shei-205,350,70),0)
        pygame.draw.rect(screen,(255,0,0),(swid/2-170,shei-200,340,60),0)
        screen.blit(menuback,(swid/2-169,shei-208))

        
        
        survive=fontmedio.render('Survived: '+str(round(sec//60))+' Minutes '+str(round(sec%60))+' Seconds',True,(0,0,0))
        screen.blit(survive,(swid/2-320,shei-320))
        
        if mouse[0]:
            if mx>=swid/2-175 and mx<=swid/2+175 and my >=shei-205 and my<=shei-135:
                clicksound.play()
                areset()
                menurun=True
                loading=True
                minute=0
                sec=0
                timer=0
                hellsec=180
        
        cursor(mx,my)
        flipquit()


pygame.quit()
    
