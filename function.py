def savat(mahsulot, mahsulotlar):
    if mahsulot.lower() in mahsulotlar:
        print(f'Siz tanlagan {mahsulot} mahsulot bor')
    else:
        print(f'Siz tanlagan {mahsulot} mavjud emas ')
mahsulotlar = [mahsulotlar.lower() for mahsulotlar in input('Mahsulotni kiriting:').split(',')]       
mahsulot = input('qidirgan mahsulotingizni kiriting: ').lower()
savat(mahsulot, mahsulotlar)
