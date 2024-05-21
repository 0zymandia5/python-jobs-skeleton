from dotenv import load_dotenv
import json
import sys

#loading env vars
load_dotenv()

with open('behaviors/menu.json') as json_file:
    menu = json.load(json_file);
print("************TOPICS MENU************")
for key in menu:
    print(key +".- "+ menu[key]["name"]);
print("***********************************")
option = sys.argv[1] if(len(sys.argv)>1) else input('Select a Topic to display its jobs: ');
#importation of the file and instansciation of the main class dynamically
dynModule = __import__(menu[option]["module"], fromlist=[menu[option]["className"]])
dynaClass = getattr(dynModule, menu[option]["className"])
dynaInst =  dynaClass()
#SubMenu Setup to display & run functions
subMenu=menu[option]["menu"];
print("*************JOBS MENU*************")
for keySubMenu in subMenu:
    print(keySubMenu +".- "+ subMenu[keySubMenu]["name"]); 
print("***********************************")
optionSubMenu = sys.argv[2] if(len(sys.argv)>2) else input('Select a Job to be Executed: ');
if subMenu[str(optionSubMenu)]["fileDir"] != "":
    with open(subMenu[str(optionSubMenu)]["fileDir"]) as query_file:
        queryJson = json.load(query_file);
        class_function = getattr(dynaInst, subMenu[str(optionSubMenu)]["function"])
        class_function(queryJson)
else:
        class_function = getattr(dynaInst, subMenu[str(optionSubMenu)]["function"])
        class_function()

                