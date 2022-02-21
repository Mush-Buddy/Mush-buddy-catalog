# class for mushroom with all the desired traits

from curses import use_default_colors
from logging import NullHandler
from typing import _get_type_hints_obj_allowed_types


class Mushroom:

    # iinit method
    def __init__(self, nameScientific, nameCommon, description, veilType, capShape, gillType, bruising, dateCreated, use, licenses, wikiPage):
        self.image_links = []
        self.nameScientific = nameScientific
        self.nameCommon = nameCommon
        self.description = description
        self.foundInStates = []
        self.seasons = []
        self.hasVeil = False
        self.veilType = veilType;
        self.stemColors = []
        self.capShape = capShape
        self.capColors = []
        self.hasGills = False
        self.gillType = gillType
        self.sporePrint = []
        self.bruising = bruising
        self.use = use 
        self.dateCreated = dateCreated
        self.license = licenses
        self.wikiPage = wikiPage
        self.citationList = []

    def addImageLink(self, link):
        self.image_links.append(link);

    def addState(self, state):
        self.foundInStates.append(state);

    def addSeason(self, season):
        self.seasons.append(season)

    def setHasVeil(self, VeilBool):
        self.hasVeil=VeilBool
    
    def addStemColor(self, color):
        self.stemColors.append(color)

    def addCapColor(self, color):
        self.capColors.append(color)

    def setGills(self, gillBool):
        self.hasVeil=gillBool


    


    
    






