# Ghidra Auto-Renamer: String-Based Function Renaming Script

Bu proje, İstinye Üniversitesi Tersine Mühendislik (Reverse Engineering) dersi final projesi kapsamında, statik analiz süreçlerini otomatize etmek amacıyla geliştirilmiştir.

**Geliştirici:** [Hilal Şengül]  

---

## 📖 Proje Özeti ve Amacı
Zararlı yazılım (malware) analizi veya "CrackMe" çözümleri gibi tersine mühendislik süreçlerinde, sembolleri temizlenmiş (stripped) derlenmiş dosyalar incelenirken en büyük zaman kaybı isimsiz fonksiyonların (örn: `FUN_00401020`) ne işe yaradığını tespit etmektir.

Bu proje, Ghidra'nın dahili Python (Jython) motoru ve `FlatProgramAPI` mimarisi kullanılarak yazılmış bir otomasyon betiğidir. Temel amacı, program belleğinde tanımlı olan karakter dizilerini (string referanslarını) taramak, bu dizilere referans veren (XREF) isimsiz fonksiyonları tespit etmek ve fonksiyon isimlerini, içerdikleri string verisine göre dinamik ve anlamlı bir şekilde (örn: `FUN_00401020` -> `sub_Access_Granted`) yeniden adlandırmaktır.

---

## ⚙️ Teknik Altyapı ve Çalışma Mantığı
Script, karmaşıklığı en aza indirmek ve güvenli bir yeniden adlandırma yapmak için aşağıdaki algoritmik adımları izler:

1. **Bellek Taraması (Memory Scanning):** Ghidra'nın `Memory` ve `Listing` arayüzleri kullanılarak, programın veri (data) bölümlerindeki tanımlı tüm stringler (ASCII/Unicode) tespit edilir.
2. **Çapraz Referans Analizi (XREF Resolution):** Bulunan her bir string adresi için `ReferenceManager` kullanılarak, bu stringin hangi kod blokları (fonksiyonlar) tarafından çağrıldığı bulunur.
3. **Veri Temizleme (Sanitization):** String içerikleri, geçerli bir fonksiyon ismi olabilmesi için özel karakterlerden, boşluklardan ve geçersiz sembollerden arındırılır (Regex veya karakter filtresi uygulanır).
4. **Sembol Tablosu Güncellemesi (Symbol Table Update):** Ghidra'nın `SymbolTable` API'si çağrılarak, varsayılan isme sahip olan fonksiyonların sembolleri yeni üretilen anlamlı isimlerle değiştirilir. İşlem sırasında mevcut anlamlı isimlerin üzerine yazılmasını önlemek için güvenlik kontrolleri yapılır.

---

## 🚀 Öne Çıkan Özellikler
* **Hedefli İsimlendirme:** Sadece varsayılan Ghidra isimlendirmesine sahip (`FUN_` veya `DAT_` ile başlayan) fonksiyonları hedef alır, analistin daha önce manuel olarak verdiği isimleri bozmaz.
* **Karakter Sınırlandırması:** Çok uzun stringlerin (örn: uzun hata logları) fonksiyon isimlerini bozmaması için maksimum karakter limiti uygular.
* **Detaylı Konsol Çıktısı (Logging):** Hangi adresteki stringin, hangi fonksiyona atandığını Ghidra Python konsolunda adım adım raporlayarak analiz sürecini şeffaflaştırır.

---

## 🛠️ Sistem Gereksinimleri
* **Ghidra:** v10.x veya v11.x+ (FlatProgramAPI destekli tüm sürümler)
* **Dil:** Python 2.7 (Ghidra'nın entegre Jython yorumlayıcısı)
* **İşletim Sistemi:** Windows, Linux (Kali/AlmaLinux vb.) veya macOS (Ghidra'nın çalıştığı tüm platformlar desteklenir).

---

## 💻 Kurulum ve Kullanım Kılavuzu

Scripti analiz ortamınıza entegre etmek ve çalıştırmak için aşağıdaki adımları sırasıyla uygulayınız:

1. Bu repoda bulunan `StringRenamer.py` dosyasını yerel diskinize indirin veya repoyu klonlayın (`git clone`).
2. Ghidra uygulamasını başlatın, analiz edilecek ikili dosyayı (binary) yükleyin ve **CodeBrowser** arayüzüne geçiş yapın.
3. Üst menü çubuğundan **Window -> Script Manager** seçeneğine tıklayarak script yöneticisini açın.
4. Script Manager penceresinin sağ üst kısmında yer alan **"Script Directories"** (klasör ve liste ikonu) butonuna tıklayın. Açılan listeden `StringRenamer.py` dosyasının bulunduğu yerel dizini ekleyin.
5. Arama çubuğuna script adını yazarak veya listeden bularak seçin.
6. Seçili durumdayken yeşil **"Run Script"** (Oynat) butonuna tıklayarak işlemi başlatın.
7. Yeniden adlandırma işleminin loglarını alt kısımdaki `Console: Python` penceresinden anlık olarak takip edebilirsiniz.

