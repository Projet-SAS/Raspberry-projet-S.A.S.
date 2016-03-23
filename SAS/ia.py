# -*- coding: utf-8 -*
#!/usr/bin/env python

userRequest = {"temp": 23, "lumZ1": 500, "lumZ2": 500, "forceLight": False}

class tortIA:
    """docstring for tortIA

		prends en entrée:
			la température [intérieure] + [extérieure]
			la luminosité de la zone 1 (Gauche face au tableau)
			la luminosité de la zone 2 (Droite face au tableau)
			Si une personne est détectée.

			+ les conditions définites par l'utilisateur (userRequest)
    """
    def __init__(self, temp, lumZon1, lumZon2, is_somebody, userRequest):
        self.temp = temp
        self.lumZon1 = lumZon1
        self.lumZon2 = lumZon2
        self.is_somebody = is_somebody
        self.userRequest = userRequest

    """diffData
    
    retourn une donnée indiquant si l'arduino doit monter ou baisser les réglages sous le format suivant :
    	donnée1:action_donnée2:action_donnée3:action [...]
   
    """
    def diffData(self):
            diffTemp = str("temp:" + str("up" if self.temp < self.userRequest["temp"] else "down" if self.temp > self.userRequest["temp"] else "none"))
            difflumZon1 = str("lumZon1:" + str("up" if self.lumZon1 < self.userRequest["lumZ1"] else "down" if self.lumZon1 > self.userRequest["lumZ1"] else "none"))
            difflumZon2 = str("lumZon2:" + str("up" if self.lumZon2 < self.userRequest["lumZ2"] else "down" if self.lumZon2 > self.userRequest["lumZ2"] else "none"))
            result = str(diffTemp + "_" + difflumZon1 + "_" + difflumZon2)
            return(result)

ia = tortIA(22, 500, 480, False, userRequest)
print ia.diffData()