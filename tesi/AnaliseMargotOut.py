import xml.etree.ElementTree as ET
import os.path


class AnaliseMargotOut:

    def __init__(self):
        os.chdir("../predictor/output")
        self.tree = ET.parse("OUTPUT.xml")
        print("Xml read")

    def get_all_evidence(self):
        return [el.text for el in self.tree.findall("*/evidence")]

    def get_all_claim(self):
        return [el.text for el in self.tree.findall("*/claim")]

    def get_all_claim_evidence(self):
        return [el.text for el in self.tree.findall("*/claim_evidence")]

"""
amo = AnaliseMargotOut()
ev = amo.get_all_evidence()
cl = amo.get_all_claim()
cl_ev = amo.get_all_claim_evidence()
print(ev)
print(cl)
print(cl_ev)
"""
