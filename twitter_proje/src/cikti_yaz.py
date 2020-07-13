import sys
import json


dosya  =  open('veriler.txt', "a")
dosya2 =  open("veriler.html", "w+")



def Verileri_Yaz(veri):

    dosya.writelines(

        str(veri) + "\n"

    )



def Oranlari_yazdir(**kwargs):

    oranlar = kwargs

    try:

        text = '''
        <html>
        <head>
            <meta charset="utf-8">
            <title>Veriler</title>
        </head>
        
        <body>
        <center><h1> Veri Çıktıları </h1></center><hr><br>
        
            <center><h3> Kullanıcı ID:  {} </h3></center>
                
             <center><TABLE BORDER CELLPADDING=2>
    
                <TR>
    
                   <TH ALIGN=LEFT> Oran Adı</TH>
    
                   <TH ALIGN=LEFT> Oran Yüzdesi </TH>
    
                </TR>
    
                <TR>
    
                   <TD> {} </TD>
    
                   <TD> {} </TD>
    
                </TR>
    
                <TR>
    
                   <TD> {} </TD>
    
                   <TD> {} </TD>
    
                </TR>
    
                <TR>
    
                   <TD> {} </TD>
    
                   <TD> {} </TD>
    
                </TR>
    
                <TR>
    
                   <TD> {} </TD>
    
                   <TD> {} </TD>
    
                </TR>
    
                <TR>
    
                   <TD> {} </TD>
    
                   <TD> {} </TD>
    
                </TR>
    
                <TR>
    
                   <TD> {} </TD>
    
                   <TD> {} </TD>
    
                </TR>
        
             </TABLE></center>
             
             <br><br>

    
    
        </body>
    </html>
        
        '''.format(

            oranlar['kullanıcı_id'],
            "Pozitif Oran", oranlar['pozitif'],
            "Siyasi Oran", oranlar['siyasi'],
            "Argo Oran", oranlar['argo'],
            "Dini Oran", oranlar['dini'],
            "Futbol Oran", oranlar['futbol'],
            'Negatif Oran', oranlar['negatif'],

        )



        dosya2.writelines(text)

    except:

        print("HTML dosya yazımında bir hata oluştu.")