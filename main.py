import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

class Math(App):
	
	def build(self):
		self.layout = FloatLayout()
		demo=Label(text="This is a demo App\n created by me\n hope you injoyed",
		font_size="40sp",
		color=(0, 1, 1, 1),
		size_hint=(None,None),
		size=(150,70),
		pos=(300,900))
		
		dembtn=Button(text="continue",
		size_hint=(None,None),
		font_size="25sp",
		background_color=(0, 1, 1, 1),
		size=(600,80),
		pos=(55,600))
		
		dembtn.bind(on_press=self.menu)
		
		self.layout.add_widget(demo)
		self.layout.add_widget(dembtn)
		return self.layout
	
	def menu(self,instance):
		self.layout.clear_widgets()
				
		math=["subtraction","addition",
		"multiplication","division",
		"subtraction & addition",
		"multiplication & divition","mixed"]
		
		leb=Label(text="Math Work",
		font_size="40sp",
		color=(0, 1, 1, 1),
		size_hint=(None,None),
		size=(150,70),
		pos=(300,1440))
		
		for i in range(1,8):
			btn=Button(text=math[i-1],
			size_hint=(None,None),
			font_size="25sp",
			background_color=(0, 1, 1, 1),
			size=(600,80),
			pos=(55,1350-i*150))
			
			btn.bind(on_press=lambda x, n=i: self.mode(n))
			self.layout.add_widget(btn)
			
		self.layout.add_widget(leb)
		
	def mode(self, mode):
		self.select_mode=mode
		self.show_dif()
						
	def show_dif(self):
		self.layout.clear_widgets()
		
		dif=["easy","medium","hard",
		"extreme"]
		
		leb1=Label(text="Difficulty",
		font_size="40sp",
		color=(0, 1, 1, 1),
		size_hint=(None,None),
		size=(150,70),
		pos=(280,1300))
		
		for s in range(1,5):
			difbtn=Button(text=dif[s-1],
			size_hint=(None,None),
			font_size="25sp",
			background_color=(0, 1, 1, 1),
			size=(600,80),
			pos=(55,1250-s*150))
			
			difbtn.bind(on_press=lambda y, m=s: self.tap(m))
			
			self.layout.add_widget(difbtn)
		
		rebtn=Button(text="<<",
		size_hint=(None,None),
		font_size="25sp",
		background_color=(0, 1, 1, 1),
		size=(80,80),
		pos=(600,1440))
		
		rebtn.bind(on_press=self.menu)
		
		self.layout.add_widget(rebtn)
		self.layout.add_widget(leb1)
		
	def tap(self, tap):
		self.level=tap
		self.show_num()
		
	def show_num(self):
		self.layout.clear_widgets()
		
		self.qn= 0
		
		leb2=Label(text="Number of questions",
		font_size="40sp",
		color=(0, 1, 1, 1),
		size_hint=(None,None),
		size=(200,70),
		pos=(280,1300))
		
		pbtn=Button(text="+",
		size_hint=(None,None),
		font_size="25sp",
		background_color=(0, 1, 1, 1),
		size=(80,80),
		pos=(500,1100))
		
		mbtn=Button(text="-",
		size_hint=(None,None),
		font_size="25sp",
		background_color=(0, 1, 1, 1),
		size=(80,80),
		pos=(150,1100))
		
		okbtn=Button(text="ok",
		size_hint=(None,None),
		font_size="25sp",
		background_color=(0, 1, 1, 1),
		size=(600,80),
		pos=(60,950))
		
		self.nleb=Label(text="0",
		size_hint=(None,None),
		font_size="25sp",
		color=(0, 1, 1, 1),
		size=(80,80),
		pos=(330,1100))
		
		pbtn.bind(on_press=lambda z : self.numf(1))
		mbtn.bind(on_press=lambda z : self.numf(-1))
		okbtn.bind(on_press=self.bridge)
		
		rebtn=Button(text="<<",
		size_hint=(None,None),
		font_size="25sp",
		background_color=(0, 1, 1, 1),
		size=(80,80),
		pos=(600,1440))
		
		rebtn.bind(on_press=self.menu)
		
		self.layout.add_widget(rebtn)
		
		self.layout.add_widget(pbtn)
		self.layout.add_widget(mbtn)
		self.layout.add_widget(okbtn)
		self.layout.add_widget(leb2)
		self.layout.add_widget(self.nleb)
		
	def numf(self, numf):
		if self.qn>0:
			self.qn +=numf
		elif self.qn==0 and numf>0:
			self.qn +=numf
		self.nleb.text=str(self.qn)
		
	def bridge(self,instance):
		if self.qn>0:
			self.cor =0
			self.incor =0
			self.lebmain()
		else:
			self.show_num()
	
	def lebmain(self):
		if self.level==1:
			fom=1
			ren=9
		elif self.level==2:
			fom=10
			ren=99
		elif self.level==3:
			fom=100
			ren=999
		elif self.level==4:
			fom=1000
			ren=9999
		if self.qn>0:
			x=random.randint(fom,ren)
			y=random.randint(fom,ren)
			if self.select_mode==1:
				m=x+y
				self.q=f"{m}  -  {y}"
				self.p=x
			elif self.select_mode==2:
				self.q=f"{x}  +  {y}"
				self.p=x+y
			elif self.select_mode==3:
				self.q=f"{x}  ×  {y}"
				self.p=x*y
			elif self.select_mode==4:
				m=x*y
				self.q=f"{m}  ÷  {x}"
				self.p=y
			elif self.select_mode==5:
				r=random.randint(1,2)
				if r==1:
					m=x+y
					self.q=f"{m}  -  {y}"
					self.p=x
				elif r==2:
					self.q=f"{x} + {y}"
					self.p=x+y
			elif self.select_mode==6:
				r=random.randint(1,2)
				if r==1:
					self.q=f"{x}  ×  {y}"
					self.p=x*y
				elif r==2:
					m=x*y
					self.q=f"{m}  ÷  {x}"
					self.p=y
			elif self.select_mode==7:
				r=random.randint(1,8)
				if r==1 or r==5:
					m=x+y
					self.q=f"{m}  -  {y}"
					self.p=x
				elif r==2 or r==6:
					self.q=f"{x} + {y}"
					self.p=x+y
				elif r==3 or r==7:
					self.q=f"{x}  ×  {y}"
					self.p=x*y
				elif r==4 or r==8:
					m=x*y
					self.q=f"{m}  ÷  {x}"
					self.p=y
			self.main()
		else:
			self.final()	

	def main(self):
		self.layout.clear_widgets()
		
		self.lock=False
		self.a =None

		position=[(270, 150),(40, 600),
		(270, 600),(510,600),(40, 450),
		(270, 450),(510, 450),(40, 300),
		(270, 300),(510, 300)]
		
		self.mleb=Label(text=str(self.q),
		font_size="40sp",
		color=(0, 1, 1, 1),
		size_hint=(None,None),
		size=(200,70),
		pos=(270,1350))
		
		self.aleb=Label(text=" ",
		font_size="40sp",
		color=(0, 1, 1, 1),
		size_hint=(None,None),
		size=(200,70),
		pos=(270,1200),
		opacity=0)
		
		canbtn=Button(text="×",
		size_hint=(None,None),
		font_size="25sp",
		background_color=(0, 1, 1, 1),
		size=(150,90),
		pos=(510,150))
		
		ticbtn=Button(text="=",
		size_hint=(None,None),
		font_size="25sp",
		background_color=(0, 1, 1, 1),
		size=(150,90),
		pos=(40,150))
		
		for t in range(0,10):
			tbtn=Button(text=f"{t}",
			size_hint=(None,None),
			font_size="25sp",
			background_color=(0, 1, 1, 1),
			size=(150,90),
			pos=position[t])						
			tbtn.bind(on_press=lambda y, r=t : self.cal(r))
			self.layout.add_widget(tbtn)
			
		rebtn=Button(text="<<",
		size_hint=(None,None),
		font_size="25sp",
		background_color=(0, 1, 1, 1),
		size=(80,80),
		pos=(600,1440))
		
		rebtn.bind(on_press=self.menu)
		
		self.layout.add_widget(rebtn)
			
		canbtn.bind(on_press=self.can)
		ticbtn.bind(on_press=self.check)
		
		self.layout.add_widget(self.mleb)
		self.layout.add_widget(self.aleb)
		self.layout.add_widget(canbtn)
		self.layout.add_widget(ticbtn)
		
	def cal(self, cal):
		if self.lock:
			return
		if self.a is None:
			self.a =0
		self.a=self.a *10 +cal
		self.aleb.text=str(self.a)
		self.aleb.opacity=1
		
	def can(self,instance):
		if self.lock:
			return
		if self.a is None:
			self.aleb.opacity=0
		elif self.a >9:
			self.a=self.a//10
			self.aleb.text=str(self.a)
		else:
			self.a=None
			self.aleb.opacity=0						
	def check(self,instance):
		if self.lock:
			return
		if self.a is None:
			self.aleb.opacity=0
			return
			
		self.lock=True
		
		if self.a==self.p:
			self.aleb.color=(0, 1, 0, 1)
			self.qn -=1
			self.cor +=1
		elif self.a !=self.p:
			self.aleb.color=(1, 0, 0, 1)
			self.qn -=1
			self.incor +=1
				
		Clock.schedule_once(self.show_label,1)			
		
	def show_label(self, dt):
		self.lock=False
		self.lebmain()					
				
	def final(self):
		self.layout.clear_widgets()						
		correct=Label(text=f"correct = {self.cor}",
		font_size="40sp",
		color=(0, 1, 0, 1),
		size_hint=(None,None),
		size=(200,70),
		pos=(270,1200))
		
		incorrect=Label(text=f"incorrect = {self.incor}",
		font_size="40sp",
		color=(1, 0, 0, 1),
		size_hint=(None,None),
		size=(200,70),
		pos=(270,1000))
		
		self.layout.add_widget(correct)
		self.layout.add_widget(incorrect)
		
		rebtn=Button(text="<<",
		size_hint=(None,None),
		font_size="25sp",
		background_color=(0, 1, 1, 1),
		size=(80,80),
		pos=(600,1440))
		
		rebtn.bind(on_press=self.menu)
		
		self.layout.add_widget(rebtn)																								
Math().run()