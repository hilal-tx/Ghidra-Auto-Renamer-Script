# @author hilal-tx
# @category Analysis

from ghidra.program.model.data import StringDataType
from ghidra.program.model.symbol import SourceType
import re

def get_defined_strings(program):
    dataManager = program.getListing()
    return dataManager.getDefinedData(True)

def main():
    pass

if __name__ == "__main__":
    main()
