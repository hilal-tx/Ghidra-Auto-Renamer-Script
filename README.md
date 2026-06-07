# Ghidra Auto-Renamer

Bu proje, İstinye Üniversitesi Tersine Mühendislik (Reverse Engineering) dersi final projesi kapsamında geliştirilmiştir.

**Geliştirici:** [Hilal Şengül]  

---

## 📖 Proje Hakkında (Overview)
Ghidra ile derlenmiş (stripped) ikili dosyalar analiz edilirken, fonksiyonlar varsayılan olarak `FUN_00401020` gibi jenerik isimler alır. Bu durum statik analizi zorlaştırır. 

Bu Python (Jython) scripti, program içerisindeki string (metin) referanslarını otomatik olarak tarar ve bu stringleri çağıran isimsiz fonksiyonları, string içeriğine uygun anlamlı isimlerle (Örn: `FUN_00401020` -> `print_Access_Granted`) dinamik olarak yeniden adlandırır. Analistlerin iş yükünü hafifleterek tersine mühendislik sürecini hızlandırmayı hedefler.

### 🚀 Özellikler (Features)
* Bellek üzerindeki tüm tanımlı string referanslarının otomatik analizi.
* Fonksiyon isimlerinin, içerdiği stringe göre temizlenerek (geçersiz karakterlerden arındırılarak) yeniden adlandırılması.
* Ghidra konsolunda detaylı adım adım loglama.

---

## 🛠️ Gereksinimler (Requirements)
* Ghidra v10.x veya v11.x+
* Python 2.7 (Ghidra'nın dahili Jython motoru ile çalışır)

---

## 💻 Kullanım (Usage)

Scripti kendi Ghidra ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Analiz etmek istediğiniz ikili (binary) dosyayı Ghidra'ya yükleyin ve `CodeBrowser` aracında açın.
2. Üst menüden **Window -> Script Manager** sekmesini açın.
3. Sağ üst köşedeki **Script Directories** (Klasör ikonu) butonuna tıklayın ve bu repoyu indirdiğiniz dizini listeye ekleyin.
4. Script listesinden `StringRenamer.py` dosyasını bulun.
5. Üzerine çift tıklayarak veya yeşil **Run Script** butonuna basarak scripti çalıştırın.
6. İşlem sonuçlarını ve adlandırılan fonksiyonları Ghidra'nın alt kısmındaki `Console: Python` penceresinden takip edebilirsiniz.

---
