# Ghidra Otomatik Fonksiyon Yeniden AdlandÄ±rma (Auto-Renamer) Scripti
Ä°stinye Ãœniversitesi, Tersine MÃ¼hendislik Final Projesi - GeliÅŸtirici: Hilal ÅengÃ¼l
## Projenin AmacÄ±
Bu proje, analiz edilen yazÄ±lÄ±mlarda bulunan tanÄ±mlÄ± string (metin) referanslarÄ±nÄ± kullanarak, bu stringleri Ã§aÄŸÄ±ran fonksiyonlarÄ± otomatik olarak yeniden isimlendiren bir araÃ§ geliÅŸtirmeyi hedefler. Temel amaÃ§, analiz sÃ¼recini hÄ±zlandÄ±rmak ve karmaÅŸÄ±k kod bloklarÄ±nÄ± daha anlaÅŸÄ±lÄ±r hale getirmektir.
## Tersine MÃ¼hendislik SÃ¼reÃ§lerine FaydalarÄ±
- Ä°simsiz (Ã¶rn: FUN_00401000) fonksiyonlarÄ±n amacÄ±nÄ± hÄ±zlÄ±ca belirleme imkanÄ± sunar.
- Ã‡ok sayÄ±da string ve fonksiyon iÃ§eren bÃ¼yÃ¼k yazÄ±lÄ±mlarda zaman tasarrufu saÄŸlar.
- Statik analizin verimliliÄŸini artÄ±rarak manuel inceleme yÃ¼kÃ¼nÃ¼ azaltÄ±r.
## KullanÄ±lan Teknik AltyapÄ±
- Ghidra FlatProgramAPI
- Jython (Python)
## Kurulum
1. `StringRenamer.py` dosyasÄ±nÄ± bilgisayarÄ±nÄ±za indirin.
2. Ghidra dizininde yer alan `ghidra_scripts` klasÃ¶rÃ¼nÃ¼n iÃ§erisine kopyalayÄ±n. (Alternatif olarak Ghidra Script Manager Ã¼zerinden yeni bir dizin yolu gÃ¶sterebilirsiniz.)
