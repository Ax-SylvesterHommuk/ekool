class Kool:
    def __init__(self):
        self.nimi = ""
        self.hinded = []
        self.teema = []
        self.õpetaja = []
        self.õpilased = []
        self.järjestatud_õpilased = []
        
        
    def adding_nimi(self):
        self.nimi = input("Sisesta kooli nimi:")
        
        
    def adding_hindeds(self, hinded):
        self.hinded.append(hinded)
        
        
    def adding_teema(self, teema):
        self.teema.append(teema)
        
        
    def adding_õpetaja(self, õpetaja):
        self.õpetaja.append(õpetaja)
        õpetaja.õpetamine_kool(self)
        
        
    def registering_õpilane_2kool(self, õpilane):
        if õpilane.õpilane_kool == "":
            self.õpilased.append(õpilane)
            õpilane.õpilane_kool = self
            
            
    def show_hinded(self):
        print("--- Kooli hinnete nimekiri ---")
        for i in self.hinded:
            print(i.nimi)
            
            
    def show_õpilased(self):
        print("--- Kooli õpilaste nimekiri ---")
        for i in self.õpilased:
            print(i.õpilane_nimi)
            
            
    def show_õpetaja(self):
        print("--- Kooli õpetajate nimekiri ---")
        for i in self.õpetaja:
            print(i.nimi)
            
            
    def show_teema(self):
        print("--- Kooli teema nimekiri ---")
        for i in self.teema:
            print(i.nimi)
            
            
    def getmark(self, õpilane):
        return õpilane.return_avg_mark()
    
    
    def getranked(self, õpilased, kool):
        for i in õpilased:
            i.getting_avg_mark(i)
        self.järjestatud_õpilased = sorted(õpilased, key=kool.getmark, reverse=True)
        
        
    def show_kool_ranking(self, kool, õpilased):
        print("--- Kooli õpilaste järjestus ---")
        self.getranked(õpilased, kool)
        g = 1
        for i in self.järjestatud_õpilased:
            print(str(g) + ".", i.õpilane_nimi,"Keskmine hinne on ", str(i.õpilane_avg_mark))
            g += 1
            
           
           
            
class Hinded:
    def __init__(self):
        self.nimi = ""
        self.õpilased = []
        self.hinded_kohustuslik_õppimine = []
        
        
        
    def naming_hinded(self, nimi):
        self.nimi = nimi
        
        
    def õpilased_learning_the_hinded(self, õpilane):
        self.õpilased.append(õpilane)
        
        
    def add_teema_to_hinded(self, teema):
        self.hinded_kohustuslik_õppimine.append(teema)
        
        
        
        
class Teema:
    def __init__(self):
        self.nimi = ""
        self.kohustuslik_õppimine = []
        self.õpetaja = []
        self.õpilased = []
        
        
        
    def naming_teema(self, nimi):
        self.nimi = nimi
        
        
    def add_hinded_to_teema(self, hinded):
        self.kohustuslik_õppimine.append(hinded)
        hinded.add_teema_to_hinded(self)
        
        
    def adding_õpetaja(self, õpetaja):
        self.õpetaja.append(õpetaja)
        õpetaja.teaching_teemas(self)
        
        
    def registering_õpilane_2teema(self, õpilane, teema):
        for i in teema.kohustuslik_õppimine:
            if i == õpilane.õpilane_hinded:
                teema.õpilased.append(õpilane)
                õpilane.adding_teema(õpilane)
            else:
                print("!!! Sa ei saa seda uurida! !!!")
                
                
                
                
class õpetaja:
    def __init__(self):
        self.nimi = ""
        self.kools = []
        self.teemas = []
        
        
        
    def naming_õpetajas(self):
        self.nimi = input(str("Sisesta õpetaja nimi:"))
        
        
    def teaching_teemas(self, teema):
        self.teemas.append(teema)
        
        
    def õpetamine_kool(self, kool):
        self.kools.append(kool)
        
        
    def show_teemas(self):
        print("--- " + self.nimi, "Õpetab selliseid teemasid ---")
        for i in self.teemas:
            print(i.nimi)
            
            
            
            
class õpilane:
    def __init__(self):
        self.õpilane_kool = ""
        self.õpilane_avg_mark = 0
        self.õpilane_nimi = ""
        self.õpilane_hinded = ""
        self.õpilane_marks = []
        self.õpilane_mark_total = 0
        self.õpilane_teemas = []
        self.failed_teemas = []
        self.passed_teemas = []
        self.õpilane_kohustuslik_õppimine = []
        
        
    def return_avg_mark(self):
        return self.õpilane_avg_mark
    
    
    def getting_avg_mark(self, õpilane):
        for i in õpilane.õpilane_marks:
            self.õpilane_mark_total += i
        self.õpilane_avg_mark = round(self.õpilane_mark_total/len(self.õpilane_marks),2)
        return õpilane.õpilane_avg_mark
    
    
    def naming_õpilane(self):
        self.õpilane_nimi = input(str("Sisesta õpilase nimi:"))
        
        
    def  registering_to_teema(self, teema):
        for i in self.õpilane_kohustuslik_õppimine:
            if i == teema:
                self.õpilane_teemas.append(teema)
                
                
    def adding_hinded(self, hinded):
        self.õpilane_hinded = hinded
        self.õpilane_kohustuslik_õppimine = hinded.hinded_kohustuslik_õppimine
        hinded.õpilased_learning_the_hinded(self)
        
        
    def passed_the_teema(self, teema):
        self.passed_teemas.append(teema)
        
        
    def failed_the_teema(self, teema):
        self.failed_teemas.append(teema)
        
        
    def add_a_mark(self, mark, teema):
        if mark == 1 or mark == 2 or mark == 3 or mark == 4 or mark == 5:
            self.õpilane_marks.append(mark)
            if mark == 1 or mark == 2:
                self.failed_the_teema(teema)
            if mark == 3 or mark == 4 or mark == 5:
                self.passed_the_teema(teema)
                
                
    def show_teema_stats(self):
        print("---" + self.õpilane_nimi, f"Teema olek on:")
        if self.failed_teemas.__len__() == 0:
            print(f"--- Ei ühtegi ebaõnnestunud teemat ---")
        else:
            print(f"Ebaõnnestunud teemad:")
            for i in self.failed_teemas:
                print(i.nimi)
        if self.passed_teemas.__len__() == 0:
            print(f"--- Läbitud teemasid pole ---")
        else:
            print(f"Läbitud teemad:")
            for i in self.passed_teemas:
                print(i.nimi)