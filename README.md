# Ghidra Auto Renamer Script

Bu proje, Tersine Mühendislik final projesi kapsamında geliştirilmiş bir Ghidra scriptidir.

## Özellikler

- Python (Jython) ve Ghidra FlatProgramAPI kullanılarak yazılmıştır.
- Program içerisinde tanımlı string referanslarını bulur.
- Bu stringleri çağıran ve ismi varsayılan (`FUN_` ile başlayan) olarak kalmış fonksiyonları tespit eder.
- Fonksiyonları, kullandıkları string içeriğine göre otomatik olarak yeniden adlandırır (örn: `func_stringIcerigi`).
- Hoca değerlendirmesi için kod üzerinde detaylı Türkçe yorum satırları bulunmaktadır.

## Kurulum ve Kullanım

1. `StringRenamer.py` dosyasını Ghidra'nın `ghidra_scripts` klasörüne kopyalayın (veya Ghidra Script Manager üzerinden bu dizini ekleyin).
2. Ghidra'da analiz etmek istediğiniz dosyayı açın ve CodeBrowser ekranına geçin.
3. `Window -> Script Manager` menüsünü açın.
4. Listeden `StringRenamer.py` scriptini bulup çalıştırın.
5. Değiştirilen fonksiyonların detayları Ghidra konsolunda görüntülenecektir.
