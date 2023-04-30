import streamlit as st

yas = int(st.number_input("Birikime Başlamak İstediğiniz Yaşı Giriniz: "))

emekli_yasi = int(st.number_input("Emekli Olmak İstediğiniz Yaşı Giriniz: "))
gerekli_ay = int((emekli_yasi - yas) * 12)

aylik_birikim = st.number_input("Aylık Yapacağınız Birikim Miktarı: ")
ev_kirası = st.number_input("Alacağınız Evin Kira Getirisi: ")
ev_fiyati = st.number_input("Alacağınız Evin Fiyatı: ")
pesinat_orani = st.number_input("Peşinat Oranınız ")
ev_pesinat = ev_fiyati * pesinat_orani
aylik_kredi = (ev_fiyati - ev_pesinat) / (15 * 12)
borc = 0
birikim = 0
ev_sayisi = 0
odenecek_ev_sayisi = 0
ay = 0
ilk_ay = 0

if st.button("Hesapla"):
    while ay < gerekli_ay:

        birikim += aylik_birikim + (ev_kirası * ev_sayisi) - (aylik_kredi * odenecek_ev_sayisi)

        if ev_sayisi == 0 and birikim >= ev_pesinat:
            ev = birikim // ev_pesinat
            birikim -= ev_pesinat * ev
            ev_sayisi += ev
            odenecek_ev_sayisi += ev
            ilk_ay = ay
            biten_ay = list(range(ilk_ay, gerekli_ay, 15))

        if ev_sayisi >= 1 and birikim >= ev_pesinat:
            ev = birikim // ev_pesinat
            birikim -= ev_pesinat * ev
            ev_sayisi += ev
            odenecek_ev_sayisi += ev
            if ay in biten_ay:
                odenecek_ev_sayisi -= 1

        ay += 1

    # Hakan'ın aylık kira geliri
    st.write("Hakan'ın Aylık Kira geliri:", ev_sayisi * ev_kirası)

    # Hakan'ın sahip olduğu ev sayısı
    st.write("Hakan'ın sahip olduğu ev sayısı:", ev_sayisi)
