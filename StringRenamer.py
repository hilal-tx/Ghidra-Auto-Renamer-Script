# @author hilal-tx
# @category Analysis

from ghidra.program.model.data import StringDataType
from ghidra.program.model.symbol import SourceType
import re

def get_defined_strings(program):
    dataManager = program.getListing()
    return dataManager.getDefinedData(True)

def sanitize_string(s):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '_', s).strip('_')
    return cleaned[:20]

def main():
    dataIterator = get_defined_strings(currentProgram)
    for data in dataIterator:
        try:
            if data.hasStringValue():
                string_val = data.getValue()
                if not isinstance(string_val, str) and not isinstance(string_val, unicode):
                    continue
                clean_str = sanitize_string(string_val)
                if len(clean_str) < 3:
                    continue
                new_func_name = "func_" + clean_str
                
                string_address = data.getAddress()
                try:
                    references = getReferencesTo(string_address)
                except Exception as e:
                    print("XREF referanslari alinirken hata: " + str(e))
                    continue

                for ref in references:
                    from_addr = ref.getFromAddress()
                    func = getFunctionContaining(from_addr)
                    if func is not None:
                        current_name = func.getName()
                        if not current_name.startswith("FUN_"):
                            continue
                        try:
                            func.setName(new_func_name, SourceType.USER_DEFINED)
                            print("{} adresindeki string, {} fonksiyonuna atandi (Eski ad: {})".format(string_address, new_func_name, current_name))
                        except Exception as e:
                            print("Fonksiyon isimlendirme sirasinda hata: " + str(e))
        except Exception as e:
            print("String degeri okunurken hata olustu: " + str(e))

if __name__ == "__main__":
    main()
