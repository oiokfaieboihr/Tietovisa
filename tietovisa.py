# Yksinkertainen Tietovisa peli tkinterillä
# Eliah San ja Pauli Eteläniemi 29.11.2023

# Lisätään tkinter moduulit
from tkinter import *
from tkinter import messagebox as mb

# Json moduuli kysymysten käsittelyyn
import json

# Randomisointi moduuli
import random

# Itse tietovisa luokka(Ikkuna tässä tapauksessa)
class Quiz(Menu):
	# Alustus funktio, joka nollaa ja sitten käynnistää eri aliohjelmat järjestyksessä
	def __init__(self):

		# Siivotaan vanha ikkuna(kanvas) ja luodaan uusi
		Menu.clear(self)
		frame2.pack_forget()
		self.frame1 = Frame(gui)
		self.frame1.pack(side="top", expand=True, fill="both")

		# Nollataan muuttujat
		self.q_no=0
		self.end=0

		# Kutsutaan funktiota, joka alustaa ja generoi satunnaistaulukon kysymyksiä varten
		self.random_generator()

		# Kutsutaan funktioita. Toinen luo otsikon ja toinen kysymyksen
		self.display_title()
		self.display_question()
		
		# Valitun valintapainikkeen muuttuja on kokonaislukumuuttuja
		self.opt_selected=IntVar()
		
		# Valinta painikkeiden luonti varten
		self.opts=self.radio_buttons()
		
		# Kutsutaan funktiota, joka luo valinnat
		self.display_options()
		
		# Kutsutaan funktiota, joka luo poistumis- ja seuraavapainikkeen
		self.buttons()
		
		# Määritetään kysymysten määrä, jotta tiedetään milloin kysymyksen on käyty läpi
		self.data_size=Menu.amount
		
		# Alustetaan muuttuja oikeiden vastausten laskemiseen
		self.correct=0

	# Funktio, joka tyhjentää "ikkunan"(kanvaksen)vekottimet(widgets)
	def clear(self):
		for widgets in self.frame1.winfo_children():
			widgets.destroy()

	# Funktio alustaa taulukon johon se laittaa numeroita tiedyltä etäisyydeltä.
	# Sekoittaa taulukon ja siten satunnaistaulukko on valmis
	# Kysymyksiä kaapataan iteraatio muuttujan mukaan satunnaistaulukosta
	def random_generator(self):
		self.random_list = []
		
		self.inputNumbers = range(Menu.startpos, Menu.range)

		self.random_list = random.sample(self.inputNumbers, Menu.amount)

		self.q_no = self.random_list[self.end]


	# Funktio luo pikkuikkunan, jossa lukee tulokset
	def display_result(self):
		# Laskee väärin menneet
		wrong_count = self.data_size - self.correct
		correct = f"Oikein: {self.correct}"
		wrong = f"Väärin: {wrong_count}"
		
		# Laskee prosentuaalisesti pisteet
		score = int(self.correct / self.data_size * 100)
		result = f"Pisteet(%): {score}%"
		
		# Luo pikku ikkunan, jossa näyttää tulokset
		mb.showinfo("Tulokset", f"{result}\n{correct}\n{wrong}")


	# Tarkastaa onko oikea vastaus
	def check_ans(self, q_no):
		
		# Jos valittu painike vastaa oikeata vastausta, ohjelma palauttaa "Totta"
		if self.opt_selected.get() == answer[q_no]:
			# Palauttaa "Totta"
			return True

	# Funktio kutsuu vastauksen tarkastus funktiota.
	# Jos vastaus on oikein, inkrementoi muuttujaa eli lisää +1.
	# Inkrementoi myös kysymys muuttuujaa, jotta voidaan mennä seuraavaan kysymykseen.
	# Tarkastaa lopussa, että onko kaikki kysymykset käyty, jos käyty kutsuu tulos funktiota ja tyhjentää ikkunan takaisin paluuta varten
	# Jos kaikkia kysymyksiä ei ole käyty läpi, menee seuravaan.
	def next_btn(self):
		
		# Jos vastaus "Totta", inkrementoi
		if self.check_ans(self.q_no):
			self.correct += 1
		
		# Siirtyy seuraavaan kysymykseen
		self.end+=1
		
		# Jos kysymysten määrä ja inkrementoitu muuttuja vastaa toisia
		# kaikki kysymykset on käyty
		if self.end==self.data_size:
			
			# Tulostaa tulokset pikkuikkunalle
			self.display_result()
			
			# Tyhjentää "ikkunan"
			self.clear()
			self.frame1.pack_forget()
			
			# Avaa tekstitiedoston, johon syötetään tulokset
			file = open("results.txt","a")
			print( f"{self.correct} / {self.data_size}", file=file)
			Menu.remove_line("results.txt",1)
			file.close()

			# Aloitetaan alusta ohjelma
			Menu()
		else:
			# Vaihtaa kysymystä seuraavaan
			self.q_no = self.random_list[self.end]
			# Tulostaa uuden kysymyksen
			self.display_question()
			self.display_options()


	# Funktio luo Seuraava- ja Sammutapainikkeen
	def buttons(self):
		
		# Luo Seuraavapainikkeen
		# Painettaessa kutsuu kysymysfunktiota, joka siirtää seuraavaan kysymykseen
		next_button = Button(self.frame1, text="Seuraava",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		next_button.place(x=350,y=380)
		
		# Luo Sammutapainikkeen
		# Painettaessa tuhoaa koko ohjelman
		quit_button = Button(self.frame1, text="Sammuta", command=gui.destroy,
		width=8,bg="black", fg="white",font=("ariel",16," bold"))
		quit_button.place(x=725,y=50)


	# Nollaa valinnan ja luo vaihtoehdot silmukan avulla
	def display_options(self):
		val=0
		
		# Nollaa valinnan
		self.opt_selected.set(0)
		
		# Silmukka tulostaa vaihtoehdot
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1
			

	# Tulostaa kysymyksen
	def display_question(self):
		q_no = Label(self.frame1, text=question[self.q_no], width=60,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		q_no.place(x=70, y=100)


	# Tulostaa otsikon
	def display_title(self):
		title = Label(self.frame1, text="Tietovisa",
		width=50, bg="blue",fg="white", font=("ariel", 20, "bold"))
		title.place(x=0, y=2)


	# Tulostaa valintapainikkeet
	def radio_buttons(self):
		
		# Alustaa taulukon
		q_list = []
		
		# Ensimmäisen valintapainikkeen sijainti
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4:
			
			# Painikkeen määritys
			radio_btn = Radiobutton(self.frame1,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			
			# Painike lisätään listaan
			q_list.append(radio_btn)
			
			# Valitaan painikkeen paikka
			radio_btn.place(x = 100, y = y_pos)
			
			# Inkrementoidaan Y-askelia, jotta painikkeet menevät tasaisesti paikoilleen
			y_pos += 40
		
		# Palautetaan lista, jossa painikkeiden määritys sekä sijainti
		return q_list
	



# Valikon luokka/ikkuna
class Menu:
	# Alustus funktio
	def __init__(self):
		# Luo kanvaksen valikolle
		frame2.pack(side="top", expand=True, fill="both")

		# Tulostaa baarin/sliderin, jolla voi valita kysymysten määrän
		self.display_scale()
		# Tulostaa aikaisemman tuloksen
		self.display_recent()
		# Tulostaa otsikon
		self.display_title()
		# Tulostaa "ohjeistuksen"
		self.display_guide()
		# Tulostaa painikkeet
		self.display_buttons()
	

	# Tuhoaa widgetit
	def clear(self):
		for widgets in frame2.winfo_children():
			widgets.destroy()
	

	# Avaa results.txt ja pistää sisällön muuttujaan tarkastelua ja tulostusta varten
	def read_file_from_start(file_path):
		try:
			with open(file_path, 'r') as file:
				content = file.readlines()
			return content
		except FileNotFoundError:
			return []
	
	# Tarkastelee results.txt, kääntää rivien järjestyksen
	# kiinnittää eri rivit yhdeksi stringiksi, jotta sitä voi paremmin tulostaa
	def display_lines_in_label(file_path, self):
		lines_from_start = Menu.read_file_from_start(file_path)
		lines_from_start.reverse()
		self.lines_text = "".join(lines_from_start)

	# Poistaa ensimmäisen rivin results.txt tiedosta, jotta 10 riviä vain tallentuu
	def remove_line(results,lineToSkip):
		with open(results,'r') as read_file:
			lines = read_file.readlines()
		currentLine = 1
		with open(results,'w') as write_file:

			for line in lines:
				if currentLine == lineToSkip:
					pass
				else:
					write_file.write(line)
				currentLine += 1

	# Tulostaa aikaisemmat tulokset
	def display_recent(self):
		file_path = "results.txt"

		if file_path:
			Menu.display_lines_in_label(file_path, self)

		leaderboard_title = Label(frame2, text="Viimeisin:\n",
		width=9, font=("ariel", 16, "bold"))
		leaderboard_title.place(x=0, y=100)

		# Tulostaa kaikki 10 riviä
		leaderboard = Label(frame2, text=self.lines_text,
		width=10, justify='left', font=("ariel", 14, "bold"))
		leaderboard.place(x=0, y=130)

	# Tulostaa sliderin ja päivittää ainakun siihen koskettaa
	def display_scale(self):
		scale = Scale(frame2, from_=1, to=15, command=Menu.on_scale_changed,
		font=("ariel",16,"bold"))
		scale.pack()
		scale.set('0')
		scale.place(x=270,y=113)

	# Tulostaa otsikon
	def display_title(self):
		title = Label(frame2, text="Tietovisa",
		width=50, bg="blue",fg="white", font=("ariel", 20, "bold"))
		title.place(x=0, y=2)

	# Tulostaa opastavat tekstit
	def display_guide(self):
		q = Label(frame2, text="Valitse aihe:",
		width=71, fg="black", font=("ariel", 14, "bold"))
		q.place(x=0, y=50)

		amount = Label(frame2, text="Määrä:",
		font=("ariel", 14, "bold"))
		amount.place(x=200, y=150)

	# Funktiot osa-alueen valintaa varten sekä kysymykset tietyltä välilä
	def math(self):
		Menu.startpos = 0
		Menu.range = 30
		Quiz()
	def geography(self):
		Menu.startpos = 30
		Menu.range = 60
		Quiz()
	def history(self):
		Menu.startpos = 60
		Menu.range = 90
		Quiz()
	def mixed(self):
		Menu.startpos = 0
		Menu.range = 90
		Quiz()

	# Muuttaa sliderin lukua reaaliajassa
	def on_scale_changed(val):
		Menu.amount = int(val)

	# Tulostaa osa-alueen valintaa varten painikkeet
	def display_buttons(self):
		Menu.amount = 1

		# Matikka
		math = Button(frame2, text="Matikka",command=self.math,
		width=10, bg="red", fg="white",font=("ariel",16,"bold"))
		math.place(x=355,y=100)

		# Biologia
		geo = Button(frame2, text="Maantieto",command=self.geography,
		width=10, bg="red", fg="white",font=("ariel",16,"bold"))
		geo.place(x=355,y=150)

		# Historia
		history = Button(frame2, text="Historia",command=self.history,
		width=10, bg="red", fg="white",font=("ariel",16,"bold"))
		history.place(x=355,y=200)

		# Sekoitus
		mixed = Button(frame2, text="Sekoitus",command=self.mixed,
		width=10, bg="red", fg="white",font=("ariel",16,"bold"))
		mixed.place(x=355,y=250)
		
		# Sammutuspainike
		quit_button = Button(frame2, text="Sammuta", command=gui.destroy,
		width=8,bg="black", fg="white",font=("ariel",16," bold"))
		quit_button.place(x=725,y=50)




# Luo ikkunan
gui = Tk()

# Määritetään ikkunan koko ja että voi muokata
gui.geometry("850x450")
gui.resizable(0, 0)

# Määritetään kanvas ikkunalle
frame2 = Frame(gui)

# Ikkunan nimi
gui.title("Tietovisa")

# Tulosten tiedosto
file_path = "results.txt"

# Kun ikkuna luodaan, tarkistetaan onko jo tulostiedostoa luotu, jos ei luo tiedoston ja lisää yksitoista riviä
try:
    with open(file_path, "r") as file:
        content = file.read()

except FileNotFoundError:
    with open(file_path, "w") as file:
        for i in range(1, 11):
            file.write(f"\n")


# Hakee kysymys tiedot json tiedostosta
with open('data.json', encoding='utf-8') as f:
	data = json.load(f)

# Laitetaan taulukoiden sisällöt kolmeen eri muuttujaan
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

# Aloitetaan ohjelma käynnistämällä valikkoluokka/ikkuna
menu = Menu()

# Aloittaa ohjelman
gui.mainloop()
