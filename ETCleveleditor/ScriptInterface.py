##############################################################################
##
##      DEBUGGING DATA
##
##      DATE - DEBUGGER - DEBUGGER TAG
##      **Method Affected
##      ***Brief description Changes Made
##
##      07/29/2011 - Peter Kinney - PBK
##      ** triggerCondition
##      *** Added code responsible for handling the conditional trigger
##
##
##      07/20/2011 - Zachary Cummings - ZJC
##      ** playSound
##      *** Commented out redundant call of loadSfx
##      *** Added new line to play sound object
##
##
##############################################################################


from Rope import *
from pandac.libpandaModules import *

class ScriptInterface:
    
    def __init__(self, world):
        self.world = world


    
    # IMPORTANT NOTE: Currently, all parameters passed to these functions are strings.  If they should be another type,
    # they must be cast or looked up

    # Controls
    
    def DisableControls(self):
        pass
    
    def EnableControls(self):
        pass
    
    # Cameras and Cutscenes
    
    def SetCamera(self, cameraNP):
        pass

    # Journal and Quests
    
    def OpenJournalEntry(self, entryTag):
        self.world.journalMgr.openJournalEntry(entryTag)
    
    def SetJournalEntryValue(self, entryTag, valueString):
        self.world.journalMgr.setEntryValue(entryTag, int(valueString))

    # Conversations
    
    def OpenConversation(self, convoTag):
        self.world.conversationMgr.openConversation(convoTag)
    
    def CloseConversation(self):
        self.world.conversationMgr.closeConversation()
    
    # GameObject Property Manipulation
    
    # TODO: test
    def DestroyGameObject(self, gameObjString):
        gameObj = self.GetGameObject(gameObjString)
        if gameObj != None:
            self.world.combatMgr.destroyObject(gameObj)
            if gameObjString in self.world.gameObjects:
                del self.world.gameObjects[gameObjString]
            if gameObjString in self.world.objects:
                del self.world.objects[gameObjString]
            gameObj.removeNode()
    
    def AddMainCharHP(self, hpString):
        self.AddHP(self.world.hero, int(hpString))
        
    def FillMainCharHP(self):
        self.FillHP(self.world.hero)
        
    def SubtractMainCharHP(self, hpString):
        self.SubtractHP(self.world.hero, int(hpString))
        
    def KillMainChar(self):
        self.Kill(self.world.hero)
        
    def AddHP(self, gameObjString, hpString):
        gameObj = self.GetGameObject(gameObjString)
        gameObj.increaseHealth(int(hpString))
    
    def FillHP(self, gameObjString):
        gameObj = self.GetGameObject(gameObjString)
        gameObj.fillHealth()
    
    def SubtractHP(self, gameObjString, hpString):
        gameObj = self.GetGameObject(gameObjString)
        gameObj.decreaseHealth(int(hpString))
    
    def Kill(self, gameObj):
        gameObj = self.GetGameObject(gameObjString)
        gameObj.die()
        
    def SetStrategy(self, gameObjString, strategyKey):
        gameObj = self.GetGameObject(gameObjString)
        pass
    
    def SetPassable(self, gameObjString, flag):
        gameObj = self.GetGameObject(gameObjString)
        pass
        # TODO: need to alter collision thingys here as well as GameObject variable
    
    # CONSIDER: knockback    
    # TODO: revive
    # TODO: respawn/relocate to the position of a placeholder object or start location
    
    # Changing Scenes
    
    def ChangeScene(self, sceneName):
        self.world.openScene(sceneName)
    
    def ChangeSceneTo(self, sceneName, startObjectName):
        self.world.openScene(sceneName)
        startObject = self.GetGameObject(startObjectName)
        if startObject != None:
            self.world.moveHeroTo(startObject)
        
    # Utility and Debugging
    
    def PrintToConsole(self, message):
        print 'SCRIPT MESSAGE: %s' %(message)
    
    def GetGameObject(self, gameObjString):
        if gameObjString in self.world.gameObjects:
            gameObj = self.world.gameObjects[gameObjString]
            return gameObj
        else:
            self.PrintToConsole('==ERROR== no GameObject named \'%s\' in scene' %(gameObjString))
            return None
    def RunCamera(self, cameraName):
        self.world.runCamera(cameraName)
        
    def AddItem(self,itemType, count):
        self.world.inventoryMgr.addItem(itemType,int(count))
        
        
        
    # Check Conditions
    
    def HasJournalEntry(self, entryTag):
        return self.world.journalMgr.isJournalEntryOpen(entryTag)
    
    def HasJournalEntryAndValue(self, entryTag, valueString):
        return self.world.journalMgr.isJournalEntryOnValue(entryTag, int(valueString))
    
    def HasManyItems(self, itemTag, count):
        return (self.world.inventoryMgr.getItemCount(itemTag) == count)
    
    def HasItem(self, itemTag):
        return self.world.inventoryMgr.hasItem(itemTag)
    
    def RunObjectOnRope(self, gameObjString, 
                        ropeString, 
                        sequenceTime,
                        isLoop=False,
                        followPath = False,
                        lookAtObject = None):
        gameObj = self.GetGameObject(gameObjString)

        if(gameObj == None):
            return
        if ropeString in self.world.objects:
            rope = self.world.objects[ropeString]
        else:
            self.PrintToConsole('==ERROR== no GameObject named \'%s\' in scene' %(ropeString))
            return
        if(lookAtObject):
            lookAtObject = self.GetGameObject(lookAtObject)
            if(lookAtObject==None):
                return
            #print "type: ", type(gameObj.getNP().node())
        sequence = UniformRopeMotionInterval(rope,
                                             gameObj.getNP(),
                                             duration= float(sequenceTime),
                                             followPath = followPath,
                                             lookAt = lookAtObject)
        
        if(isinstance(gameObj.getNP().node(), Camera)):
            self.world.runCamera(gameObjString, sequence, isLoop)
            return
                
        self.world.addSequence(sequence)

        if(isLoop):
            sequence.loop()
        else:
            sequence.start()
            
    def playSound(self, soundName):
        if soundName in self.world.sounds:
            soundObj = self.world.sounds[soundName]
        else:
            self.PrintToConsole('==ERROR== no GameObject named \'%s\' in scene' %(soundName))
            return
        ## print soundObj                               # ZJC - 07/20/2011: Not Necessary
        ## mySound = base.loader.loadSfx(soundObj)      # ZJC - 07/20/2011: Not Necessary, redundant
        ## print mySound                                # ZJC - 07/20/2011: Not Necessary
        ## mySound.play()                               # ZJC - 07/20/2011: Not Necessary, redundant
        soundObj.play() #ZJC - 07/20/2011: soundObj is already loaded, so can be played without reloading
        
    def triggerCondition(self, gameObjString):                  #PBK - 07/29/2011: Added the conditional trigger function
        gameObj = self.GetGameObject(gameObjString)
        if gameObj != None:
            gameObj.callTrigger(self.world, "LE-trigger-onCondition")   #PBK - 07/29/2011: Triggers the onCondition event of gameObj
        
#    def RunObjectOnRopeFollow(self, gameObjString, ropeString, sequenceTime, isLoop = False):
#        gameObj = self.GetGameObject(gameObjString)
#        if(gameObj == None):
#            return
#        rope = self.GetGameObject(ropeString)
#        if ropeString in self.world.objects:
#            rope = self.world.objects[ropeString]
#        else:
#            self.PrintToConsole('==ERROR== no GameObject named \'%s\' in scene' %(ropeString))
#            return
#        
#        sequence = UniformRopeMotionInterval(rope,
#                                             gameObj.getNP(),
#                                             duration= float(sequenceTime),
#                                             followPath = True)
#         
#        self.world.addSequence(sequence)
#        if(isLoop):
#            sequence.loop()
#        else:
#            sequence.start()
            
        
    
    