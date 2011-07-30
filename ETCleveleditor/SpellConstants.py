##############################################################################
##
##      DEBUGGING DATA
##
##      DATE - DEBUGGER - DEBUGGER TAG
##      **Method Affected
##      ***Brief description Changes Made
##
##
##      07/26/2011 - Zachary Cummings - ZJC
##      ** SPELL_PANDACANNON, SPELL_NEEDLES, SPELL_SPOREBLAST, SPELL_GUASSBOOM
##      *** Same changes made to all four functions:
##      *** Changed the "chargeSequence" dictionary values to fit naming convention
##      *** for the new characters loaded into the game.
##
##
##############################################################################


#
# Template for Spells
# Remember to place commas after each line!
#

SPELL_PANDACANNON =     {
                            'name':             'PandaCannon',
                            'modelPath':        'panda', 
                            'anims':            {},
                            'damage':           10,
                            'hitThreshold':     30,
                            'cooldown':         1.0, # in seconds, after chargeSequence is complete
                            'attackRange':      250, # to launch a projectile
                            'mass':             0.004,
                            'chargeSequence':   {
                                                    'firstAnimation':       '_ani_charge',      #ZJC - 07/26/2011: animation value to match naming convention
                                                    'firstAnimationTime':   1.0,
                                                    'secondAnimation':      '_ani_attack3',     #ZJC - 07/26/2011: animation value to match naming convention
                                                    'secondAnimationTime':  1.0,
                                                    'idleAnimation':        '_ani_idle'         #ZJC - 07/26/2011: animation value to match naming convention
                                                }
                                                
                            ## ZJC - 07/26/2011: Here is the previous version of the code and the previous naming conventions
                            ##                  Left here for reference, not much use otherwise.
                            ## 'chargeSequence':   {
                                                    ## 'firstAnimation':       'anim_chargeFemale',
                                                    ## 'firstAnimationTime':   1.0,
                                                    ## 'secondAnimation':      'anim_attackFemale',
                                                    ## 'secondAnimationTime':  1.0,
                                                    ## 'idleAnimation':        'anim_idleFemale'
                                                ## }
                        }

SPELL_NEEDLES =         {
                            'name':             'Needles',
                            'modelPath':        './LEGameAssets/Models/attack_light.egg', 
                            'anims':            {},  # key and egg file
                            'damage':           10,
                            'hitThreshold':     30,
                            'cooldown':         1.0, # in seconds, after chargeSequence is complete
                            'attackRange':      250, # to launch a projectile
                            'mass':             0.004,  # lower mass travels faster
                            'chargeSequence':   {
                                                    'firstAnimation':       '_ani_charge',      #ZJC - 07/26/2011: animation value to match naming convention
                                                    'firstAnimationTime':   1.0,
                                                    'secondAnimation':      '_ani_attack3',     #ZJC - 07/26/2011: animation value to match naming convention
                                                    'secondAnimationTime':  1.0,
                                                    'idleAnimation':        '_ani_idle'         #ZJC - 07/26/2011: animation value to match naming convention
                                                }
                        }

SPELL_SPOREBLAST =      {
                            'name':             'SporeBlast',
                            'modelPath':        './LEGameAssets/Models/attack_medium.egg',      
                            'anims':            {},
                            'damage':           15,
                            'hitThreshold':     30,
                            'cooldown':         1.0, # in seconds, after chargeSequence is complete
                            'attackRange':      250, # to launch a projectile
                            'mass':             0.004,
                            'chargeSequence':   {
                                                    'firstAnimation':       '_ani_charge',      #ZJC - 07/26/2011: animation value to match naming convention
                                                    'firstAnimationTime':   1.0,
                                                    'secondAnimation':      '_ani_attack2',     #ZJC - 07/26/2011: animation value to match naming convention
                                                    'secondAnimationTime':  1.0,
                                                    'idleAnimation':        '_ani_idle'         #ZJC - 07/26/2011: animation value to match naming convention
                                                }
                        }

SPELL_GUASSBOOM =       {
                            'name':             'GuassBoom',
                            'modelPath':        './LEGameAssets/Models/attack_heavy.egg', 
                            'anims':            {},
                            'damage':           20,
                            'hitThreshold':     30,
                            'cooldown':         1.0, # in seconds, after chargeSequence is complete
                            'attackRange':      250, # to launch a projectile
                            'mass':             0.004,
                            'chargeSequence':   {
                                                    'firstAnimation':       '_ani_charge',      #ZJC - 07/26/2011: animation value to match naming convention
                                                    'firstAnimationTime':   1.0,
                                                    'secondAnimation':      '_ani_attack1',     #ZJC - 07/26/2011: animation value to match naming convention
                                                    'secondAnimationTime':  1.0,
                                                    'idleAnimation':        '_ani_idle'         #ZJC - 07/26/2011: animation value to match naming convention
                                                }
                        }

SPELL_ENEMYBLAST =      {
                            'name':             'SporeBlast',
                            'modelPath':        './LEGameAssets/Models/attack_enemy.egg', 
                            'anims':            {},
                            'damage':           10,
                            'hitThreshold':     30,
                            'cooldown':         1.0, # in seconds, after chargeSequence is complete
                            'attackRange':      100, # to launch a projectile; note that enemies will by default stop getting closer to their target at 70
                            'mass':             0.004,
                            'chargeSequence':   {
                                                    'firstAnimation':       'anim_chargeMale',
                                                    'firstAnimationTime':   1.0,
                                                    'secondAnimation':      'anim_attackMale',
                                                    'secondAnimationTime':  1.0,
                                                    'idleAnimation':        'anim_idleMale'
                                                }
                        }

ATTACK_LIGHT = SPELL_NEEDLES
ATTACK_MEDIUM = SPELL_SPOREBLAST
ATTACK_HEAVY = SPELL_GUASSBOOM
ATTACK_ENEMY = SPELL_ENEMYBLAST