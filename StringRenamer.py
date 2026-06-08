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
        if data.hasStringValue():
            string_val = data.getValue()
            if not isinstance(string_val, str) and not isinstance(string_val, unicode):
                continue
            clean_str = sanitize_string(string_val)
            if len(clean_str) < 3:
                continue
            new_func_name = "func_" + clean_str
            
            string_address = data.getAddress()
            references = getReferencesTo(string_address)
            for ref in references:
                from_addr = ref.getFromAddress()
                func = getFunctionContaining(from_addr)
                if func is not None:
                    current_name = func.getName()
                    if not current_name.startswith("FUN_"):
                        continue
                    func.setName(new_func_name, SourceType.USER_DEFINED)

if __name__ == "__main__":
    main()
