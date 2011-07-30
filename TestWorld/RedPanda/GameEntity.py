import sys
from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject

class GameComponent(DirectObject):
    def __init__(self):
        self.owner = None;
        self.intialized = False;
        self.enabled = True;
        self.name = "GameComponent";

    def initialize(self):
        self.initialized = True;

    def update(self):
        pass;
        
    def destroy(self):
        self.initialized = False;
        self.enabled = False;
        if not self.owner == None:
            self.owner.removeComponent(self);
        self.owner = None;

class GameEntity(GameComponent):
    def __init__(self, nodePath):
        GameComponent.__init__(self);
        self.components = {};
        self.name = "GameEntity";
        self.nodePath = nodePath;
    
    def initialize(self):
        copy = self.components.values()[:];
        for component in copy:
            component.initialize();
        base.initialize(self);
    
    def update(self):
        copy = self.components.values()[:];
        for component in copy:
            if component.enabled:
                component.update();

    def addComponent(self, component):
        if not component.owner == None:
            component.owner.removeComponent(component);
        component.owner = self;
        if not component.initialized:
            component.initialize();
        self.components[component.name] = component;

    def removeComponent(self, component):
        del self.components[component.name];

class GameEntityManager(DirectObject):
    def __init__(self):
        self.enabled = True;
        self.initialized = False;
        self.gameEntitys = {};
    
    def initialize(self):
        copy = self.gameEntitys.values()[:];
        for entity in copy:
            entity.initialize();
        self.initialized = True;
    
    def update(self):
        copy = self.gameEntitys.values()[:];
        for gameEntity in copy:
            if gameEntity.enabled:
                gameEntity.update();
      
    def addEntity(self, gameEntity):
        if not gameEntity.initialized:
            gameEntity.initialize();
        self.gameEntitys[gameEntity.name] = gameEntity;
    
    def removeEntity(self, gameEntity):
        del self.gameEntitys[gameEntity.name];