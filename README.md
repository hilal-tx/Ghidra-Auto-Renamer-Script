
# Ghidra Otomatik Fonksiyon Yeniden Adlandırma (Auto-Renamer) Scripti
**İstinye Üniversitesi**, Tersine Mühendislik Final Projesi - **Geliştirici:** Hilal Şengül

---

## Projenin Amacı
Bu proje, analiz edilen yazılımlarda bulunan tanımlı string (metin) referanslarını kullanarak, bu stringleri çağıran fonksiyonları otomatik olarak yeniden isimlendiren bir araç geliştirmeyi hedefler. Temel amaç, analiz sürecini hızlandırmak ve karmaşık kod bloklarını daha anlaşılır hale getirmektir.

---

## Tersine Mühendislik Süreçlerine Faydaları
- **Hızlı Tespit:** İsimsiz (örn: `FUN_00401000`) fonksiyonların amacını hızlıca belirleme imkanı sunar.
- **Zaman Tasarrufu:** Çok sayıda string ve fonksiyon içeren büyük yazılımlarda zaman tasarrufu sağlar.
- **Verimlilik Artışı:** Statik analizin verimliliğini artırarak manuel inceleme yükünü azaltır.

---

## Kullanılan Teknik Altyapı
- `Ghidra FlatProgramAPI`
- `Jython` (`Python`)

---

## Kurulum
1. `StringRenamer.py` dosyasını bilgisayarınıza indirin.
2. Ghidra dizininde yer alan `ghidra_scripts` klasörünün içerisine kopyalayın. *(Alternatif olarak Ghidra Script Manager üzerinden yeni bir dizin yolu gösterebilirsiniz.)*

---

## Kullanım Adımları
1. Ghidra üzerinde analiz etmek istediğiniz projeyi açın.
2. `CodeBrowser` penceresinde üst menüden `Window` -> `Script Manager` seçeneğine tıklayın.
3. Arama kutusuna `StringRenamer.py` yazarak scripti bulun.
4. Scriptin üzerine çift tıklayarak veya `Run` butonuna basarak çalıştırın.
5. İşlem tamamlandığında alt kısımdaki konsoldan kaç adet fonksiyonun yeniden adlandırıldığını kontrol edebilirsiniz.
