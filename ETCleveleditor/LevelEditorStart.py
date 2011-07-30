##############################################################################
##
##      DEBUGGING DATA
##
##      DATE - DEBUGGER - DEBUGGER TAG
##      **Method Affected
##      ***Brief description Changes Made
##
##      07/29/2011 - Zachary Cummings - ZJC
##      ** N/A
##      *** Code from last update deemed unnecessary
##
##      07/27/2011 - Zachary Cummings - ZJC
##      ** N/A
##      *** Added an array that will be accessed from MergeProject UI
##      *** and LevelEditorUIBase. It will store a list of any merges or
##      *** imports that occur so we can adjust the nameing conventions later.
##
##
##############################################################################

import LevelEditor
import sys, datetime
from Logger import *

sys.stdout = Logger('LevelEditor.log')
sys.stderr = sys.stdout

print '**************************************************'
print datetime.datetime.now()

base.le = LevelEditor.LevelEditor()
# You should define LevelEditor instance as
# base.le so it can be reached in global scope

## #ZJC - 07/29/2011: Code below determined not necessary
## base.le.prefixImportMerge = []# ZJC - 07/27/2011: When a library is imported, add prefix to the list 



run()
