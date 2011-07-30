import sys
from direct.showbase.DirectObject import DirectObject
from GameEntity import *;

class GameStateManager(DirectObject):
    def __init__(self, world):
        self.world = world;
        self.states = [];
        taskMgr.add(self.updateStates);
        
    def initialize(self):
        copy = self.states[:]; # copies the stack of game states
        for state in copy:
            state.initialize();
            
    def updateStates(self, task):
        # update top state if it is enabled
        if len(self.states) > 0 and self.states[0].enabled:
            self.states[0].update(self);
        
        return task.cont;
    
    def pushState(self, gameState):
        if not gameState.initialized:
            gameState.initialize();
        self.states.append(gameState);
        
    def popState(self, gameState):
        # check whether there is a state to remove
        if len(self.states) > 0:
            # copy starting after the first state
            if len(self.states) > 1:
                self.states = self.states[1:]
            else:
                self.states = [];
            
        
class GameState(DirectObject):
    def __init__(self, stateManager):
        self.stateManager = stateManager;
        self.initialized = False;
        self.enabled = True;
        self.entityManager = GameEntityManager();
        
    def getWorld(self):
        return self.stateManager.world;
    property(fget = getWorld);
        
    def initialize(self):
        self.stateManager.initialize();
        self.initialized = True;
    
    def update(self):
        if self.entityManager.enabled:
            self.entityManager.update();
            
    def destroy(self):
        self.initialized = False;
        self.enabled = False;
        del self.entityManager;
        self.stateManager = None;