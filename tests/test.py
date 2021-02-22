# Librairie permettant de manipuler des fichiers
import glob
# Librairie permettant d'interagir avec n'importe quel OS
import os
from os.path import dirname, abspath
#Librairie XML

from lxml import etree
from lxml.etree import XMLSyntaxError


# FAIRE LA DOCUMENTATION DES FONCTIONS
def test_well_formed(doc):
    """ Test XM# doc_a_tester = os.path.abspath(os.path.join(chemin_actuel, os.pardir, "*.xml"), key=os.path.getctime)L bien formé (par rapport à la syntaxe XML)
            
            :param doc: doc à tester
            :type doc: TextIOWrapper
            :returns: rien
    """
    with open(doc) as doc:
        try:
            doc = etree.parse(doc)
            print("Votre XML est bien formé")
        except XMLSyntaxError:
            print("Attention ! Votre XML n'est pas bien formé")

        # Test présence du name space TEI (les atributs fonctionnent comme des dict)
def test_ns(doc):
    """ Test si l'élément racine est bien TEI avec le ns TEI
            
            :param doc: doc à tester
            :type doc: TextIOWrapper
            :returns: rien
    """
    with open(doc) as doc:
        doc = etree.parse(doc)
        # récupère tous les enfants de la root
        root = doc.getroot()
        # récupère l'élément racine
        root = root.tag
        assert root == "{http://www.tei-c.org/ns/1.0}TEI", "La racine doit être TEI (avec l'espace de nom TEI"



        # Test XML valide (par rapport au schéma du projet)
def test_schema(doc):
    """ Test si le document est conforme au schéma du projet 
            
            :param doc: doc à tester
            :type doc: TextIOWrapper
            :returns: rien
    """
    with open(doc) as doc:
        relaxng_doc = etree.parse(schema)
        relaxng = etree.RelaxNG(relaxng_doc)
        doc = etree.parse(doc)
        if relaxng.validate(doc) == True:
            print("Votre document est conforme au schéma!")
        else:
            raise Exception("Votre document n'est pas valide par rapport au schéma!")

chemin_actuel = os.path.dirname(os.path.abspath(__file__))

# Import du document XML du dossier d'au-dessus modifié le plus récemment
# doc_a_tester = max(glob.iglob('../*.xml'), key=os.path.getctime)

dossier = dirname(dirname(abspath(__file__)))

for filename in dossier:
    if filename.endswith(".xml"):
        doc_a_tester = filename
        print("Fichier en cours de test : {fichier}".format(fichier = doc_a_tester))

        # Import du schéma indépendant de l'OS
        schema = os.path.abspath(os.path.join(chemin_actuel, os.pardir, "tei_all.rng"))

        # print(schema)

        # print(doc_a_tester)
        # print(schema)

        # On appelle les fonctions de test sur le document à tester
        test_well_formed(doc_a_tester)
        test_ns(doc_a_tester)
        test_schema(doc_a_tester)
    else:
        pass