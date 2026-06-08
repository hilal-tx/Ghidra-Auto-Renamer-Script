# @author hilal-tx
# @category Analysis

from ghidra.program.model.data import StringDataType
from ghidra.program.model.symbol import SourceType
import re

def get_defined_strings(program):
    dataManager = program.getListing()
    return dataManager.getDefinedData(True)

def sanitize_string(s):
    return re.sub(r'[^a-zA-Z0-9]', '_', s).strip('_')

def main():
    pass

if __name__ == "__main__":
    main()
