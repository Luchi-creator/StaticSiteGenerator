from enum import Enum

class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"

class Textnode:
    def __init__(self,text,text_type,url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(textnode_one,textnode_two):
        if textnode_one.text == textnode_two.text and textnode_one.text_type == textnode_two.text_type and textnode_one.url == textnode_two.url:
            return True
        else:
            return False

    def __repr__(textnode):
        return f"Textnode({textnode.text},{textnode.text_type},{textnode.url})"
    
    