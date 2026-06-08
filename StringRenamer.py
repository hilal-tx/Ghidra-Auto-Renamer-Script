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
            string_address = data.getAddress()
            references = getReferencesTo(string_address)

if __name__ == "__main__":
    main()
