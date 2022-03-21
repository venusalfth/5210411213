class computerpart:
    def __init__(self,pabrikan,nama,jenis,harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

class processor(computerpart):
    def __init__(self,pabrikan,nama,harga,jumlah_core,speed):
        super().__init__(pabrikan,nama,"processor",harga)
        
        self.jumlah_core = jumlah_core
        self.speed = speed

class randomaccesmemomry(computerpart):
    def __init__(self, pabrikan, nama,harga,kapasitas):
        super().__init__(pabrikan, nama,"RAM",harga)
        self.kapasitas = kapasitas

class harddisksata(computerpart):
    def __init__(self, pabrikan, nama,harga,kapasitas,rpm):
        super().__init__(pabrikan, nama,"SATA",harga)
        self.kapasitas =kapasitas
        self.rpm = rpm

p = processor("intel","core i7",43500000,4,"4,3 Ghz")
m = randomaccesmemomry("V-Gen","DDR4 500 im PC19200/2400Ghz",3200000,"4GB")
hdd = harddisksata("Segate","HDD 2,5 inch",295000,"500GB",7200)

parts = [p,m,hdd]
for part in parts:
    print("{} {} produksi {}".format(part.jenis,part.nama,part.pabrikan))
