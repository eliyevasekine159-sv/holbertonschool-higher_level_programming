#!/usr/bin/python3
"""Module for serializing and deserializing with XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML file to create.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize an XML file to a dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        # XML elementlərini yenidən lüğətə çeviririk
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        return None
