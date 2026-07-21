from  ImportEngine import Importer          
print(Importer.parse("data/cats.csv"))

"""from typing import 

from .ImportInterface import ImportInterface
from .Cat import Cat
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter


class Importer(ImportInterface):
    importers = [DocxImporter, CSVImporter]

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
            
"""