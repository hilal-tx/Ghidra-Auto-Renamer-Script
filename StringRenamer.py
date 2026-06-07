# Tersine Mühendislik Final Projesi - Ghidra Otomatik Fonksiyon Yeniden Adlandırma Scripti
# Bu script, programda tanımlı olan string (metin) referanslarını bulur ve
# bu stringleri kullanan/çağıran fonksiyonların isimlerini string içeriğine göre otomatik olarak günceller.
# @author hilal-tx
# @category Analysis

from ghidra.program.model.data import StringDataType
from ghidra.program.model.symbol import SourceType
import re

# Konsola bilgi mesajı yazdırıyoruz
print("Otomatik fonksiyon yeniden adlandırma scripti başlatıldı...")

# Mevcut programın Data (Veri) yöneticisini alıyoruz
dataManager = currentProgram.getListing()

# Programdaki tüm verileri (data) dolaşmak için iterator alıyoruz
dataIterator = dataManager.getDefinedData(True)

# Kaç fonksiyonun yeniden adlandırıldığını takip etmek için sayaç
rename_count = 0

for data in dataIterator:
    # Verinin bir string (metin) olup olmadığını kontrol ediyoruz
    if data.hasStringValue():
        # Stringin içeriğini alıyoruz
        string_val = data.getValue()
        
        # Sadece yeterince uzun ve anlamlı stringleri dikkate almak için bir filtreleme yapıyoruz
        if isinstance(string_val, str) or isinstance(string_val, unicode):
            # String çok kısaysa veya boşsa atla
            if len(string_val) < 4:
                continue
                
            # String içeriğini temizliyoruz (Sadece harf ve rakamları bırakıyoruz)
            clean_str = re.sub(r'[^a-zA-Z0-9]', '_', string_val).strip('_')
            
            # Temizlenmiş string çok kısaysa atla
            if len(clean_str) < 3:
                continue
                
            # Yeni fonksiyon adı için bir format belirliyoruz (Örn: func_string_icerigi)
            # Eğer string çok uzunsa ilk 20 karakterini alıyoruz
            new_func_name = "func_" + clean_str[:20]
            
            # Bu stringin bellek adresini alıyoruz
            string_address = data.getAddress()
            
            # Bu string adresine yapılan referansları (nereden çağrıldığını) buluyoruz
            references = getReferencesTo(string_address)
            
            for ref in references:
                # Referansın yapıldığı (stringin çağrıldığı) adresi alıyoruz
                from_addr = ref.getFromAddress()
                
                # Bu adresin hangi fonksiyona ait olduğunu buluyoruz
                func = getFunctionContaining(from_addr)
                
                if func is not None:
                    # Mevcut fonksiyonun ismini alıyoruz
                    current_name = func.getName()
                    
                    # Sadece varsayılan Ghidra isimlerini (FUN_ ile başlayanlar) değiştiriyoruz
                    # Eğer kullanıcı veya başka bir script zaten isimlendirdiyse dokunmuyoruz
                    if current_name.startswith("FUN_"):
                        try:
                            # Fonksiyonun ismini değiştiriyoruz (SourceType.USER_DEFINED kullanarak)
                            func.setName(new_func_name, SourceType.USER_DEFINED)
                            print("Fonksiyon yeniden adlandırıldı: {} -> {}".format(current_name, new_func_name))
                            rename_count += 1
                        except Exception as e:
                            # Eğer yeniden adlandırma sırasında bir hata oluşursa konsola yazdırıyoruz
                            print("Hata: {} fonksiyonu {} olarak adlandırılamadı. Sebep: {}".format(current_name, new_func_name, str(e)))

# Script tamamlandığında ekrana özet bilgi yazdırıyoruz
print("Script tamamlandı. Toplam {} fonksiyon yeniden adlandırıldı.".format(rename_count))
