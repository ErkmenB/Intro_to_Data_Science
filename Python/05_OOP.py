class veri_bilimci():
    print("bu bir sınıftır.")
    bolum = ""
    deneyim_yili = 0
    sql = "Evet"
    bildigi_diller = []
    
    #Orneklendirme
    
veri_bilimci.sql = "Hayır"

veri_bilimci.sql

ali = veri_bilimci()

ali.sql = "Evet"

ali.sql

ali.bildigi_diller.append("python")

ali.bildigi_diller

# =============================================================================
# # örnek özellikleri 
# =============================================================================

class veri_bilimci():
    def __init__(self):
        self.bildigi_diller = []
            

ali = veri_bilimci()

veli = veri_bilimci()

ali.bildigi_diller.append("R")

ali.bildigi_diller

veli.bildigi_diller.append("python")

veli.bildigi_diller

# Ornek metodları


class veri_bilimci():
    def __init__(self):
        self.bildigi_diller = []
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        

dir(veri_bilimci)

ali = veri_bilimci()

ali.bildigi_diller
veli = veri_bilimci()

veli.bildigi_diller

veri_bilimci.dil_ekle

ali.dil_ekle("R")

ali.bildigi_diller
veli.dil_ekle("Python")

veli.bildigi_diller
