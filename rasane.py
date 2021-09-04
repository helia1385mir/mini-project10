

from pyfiglet import Figlet

from os import read

import pyfiglet


class menu:
  def __init__(self,edit,add,exit):
      print('1-edit clip')
      print('2-add clip')
      print(3-'exit')




vorodi_karbar=int(input('adad entekhabi ra vared konid'))
if vorodi_karbar==1:
    pass
elif vorodi_karbar==2:
    pass
elif vorodi_karbar==3:
    exit()
proudc=[]

open=open('rasane.txt','r')
r=open.read()

split1=r.split('\n')


for i in range(len(split1)):
    split2=split1[i].split(',')
    etelaat={'id':None,'name':None,'Director':None,'imdb score':None,'url':None,'time':None,'casts':None }
    etelaat['id']=split2[0]
    etelaat['name']=split2[1]
    etelaat['Director']=[2]
    etelaat['imdb score']=[3]
    etelaat['url']=[4]
    etelaat['time']=[5]
    etelaat['casts']=[6]
#############




class media:
    def shoro():
       print('wait..') 
       p=pyfiglet.Figlet(font='standard')
       print(p.renderText('khosh amadid'))
    def __init__(self,name,director,imdbscore,url,casts):
        self.name= name
        self.director='director'
        self.imdbscore='imdbscore'
        self.url='url'
        self.duraction='duraction'
        self.casts=[actor]
    def show_info(self):
        pass
    def downlowd(self):
        pass

class serial(media):
    def __init__(self, name):
     def tedad_ghesmat():
        input('tedad ghesmat ha:')

class Film(media):
    def janer():
        input('janer film chis:')
    def __init__(self, name):
          pass
class clip(media):
    def __init__(self, name):
        def mozo():
            print('mozo clip chis')
class Documentary(media):
    def __init__(self, name):
        def duc():
            input('mozo mostanad')
class actor:
    pass



