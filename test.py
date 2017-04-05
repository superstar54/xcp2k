
import xml.etree.cElementTree as cElementTree


xml_path = "cp2k_input.xml"

tree = cElementTree.parse(xml_path)
root = tree.getroot()

# Extract the cp2k version and revision
version = root.find("CP2K_VERSION").text
revision = root.find("COMPILE_REVISION").text
print(version)
print(revision)
