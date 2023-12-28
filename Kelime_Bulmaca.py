from random import choice

while True:
    print("Hoş geldiniz")

    Kelime_listesi = choice(["system", "data", "algorithm", "such", "base", "node", "model", "case",
                      "program", "information", "set", "code", "function", "process", "application", "software",
                      "class", "point", "type", "network", "tree", "object", "element", "input", "operation", "level",
                      "memory", "table", "order", "file", "variable", "language", "write", "list", "structure",
                      "compute", "sequence", "computer", "bit", "probability", "machine", "array", "page", "error",
                      "step", "search", "most", "path", "graph", "web", "length", "several", "security", "proof",
                      "access", "obtain", "matrix", "task", "image", "form", "return", "interface", "resource",
                      "address", "implementation", "loop", "first", "read", "location", "hardware", "behavior",
                      "programming", "field", "key", "parameter", "distribution", "definition", "instance",
                      "interaction", "internet", "representation", "edge", "stack", "return", "procedure",
                      "link", "output", "block", "domain", "store", "call", "device", "server", "static", "dataset",
                      "detection", "write", "execute", "least", "key"])

    harfler = ["a","e","i","u","o"]
    harfler1=["b","m","s"]

    Kelime_listesi = Kelime_listesi.lower() #küçük harfe çevirme
    harfsayisi = len(Kelime_listesi)

    if harfsayisi%2 == 1:
        hak = (harfsayisi//2) + 1

    else:
        hak = (harfsayisi//2)

    tahminler = []
    hata = []
    toplam=0

    while hak > 0:
        bosluk =""

        for harf in Kelime_listesi :
            if harf in tahminler:
                bosluk = bosluk + harf

            else:
                bosluk = bosluk + "_"

        if bosluk == Kelime_listesi :
            print("Kelimeyi doğru bildiniz. Tebrikler")
            break
        print("-"*40)
        Tahmin = input("Harf Giriniz:")
        katsayi = Kelime_listesi.count(Tahmin)
        for i in harfler:
            if Tahmin == i:
                puan = katsayi * 2
            else:
                puan = katsayi * 3

        toplam=toplam+puan
        print("Kalan hak:",hak,"      Puan:",toplam)
        print('Kelimeniz:"',bosluk,'"')

        Tahmin = Tahmin.lower()

        if Tahmin == Kelime_listesi:
            print("Tebrikler Kelimeyi Tahmin Ettiniz")
            break
        elif Tahmin in tahminler or Tahmin in hata:
            print("{} daha önce söylendi lütfen başka bir harf giriniz".format(Tahmin))

        elif Tahmin in Kelime_listesi:

            print("Doğru.{0} harfi kelimemiz içerisinde {1} kere geçiyor".format(Tahmin,katsayi))
            tahminler.append(Tahmin)

        else:
            print("Kelimede böyle bir harf yok")
            hata.append(Tahmin)
            toplam=toplam-4
            hak = hak - 1

        if hak == 0:
            print("Geriye hakkınız kalmadı. Maalesef bilemediniz")
            print("Kelimemiz {}".format(Kelime_listesi))

    print("Oyundan çıkmak istiyorsanız:\n1-Çıkış\n2-Devam etmek istiyorsanız 2'ye tıklayın")
    secim = input(">>>>")

    if secim == 1:
        break

    elif secim == 2:
        continue