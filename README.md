
##Ⅰ Prepare Enviroment
1. code Editor : Visual Studio Code (or other you like)
2. Install Python 3.10+
3. pip install selenium (version:  4.4.3)
4. Extract "HTMLTestRunner.rar"  file on ./toos/, add to  python install path:  .\Python\Lib
5. Download webDriver for different browser with version , add to python install path .\Python
   Chrome -> Chromedriver :  http://chromedriver.storage.googleapis.com/index.html
   Edge -> Edgedriver : https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

## Ⅱ get start
1. Get code: 
   git clone https://github.com/EheJie/PrudentailAssignment.git
2. User Guide:  UesrGuide.xls
3. About Code:
   ./Run.py      --- This is ther portal of This framework, we run all cases from this portal
   ./Engine.py  --- This file use to define browser and get url
   ./conf/      ---Folder: This folder ues to save comfigures   
   ./testcase/    ---Folder: This folder use to save all test cases for auto
   ./Scripts/     ---Folder: This folder use to save all auto-cases script
   ./po/          ---Folder: This folder use to save pages object, include page element , handle function, page-business
   ./lib/ShareModules.py   This file is user save frameWork command functions
   ./lib/ShareBusiness.py   This file is user save product command business functions or workflows
   ./logs/        ---Folder: this folder user to save log 
   ./result/img/  ---Folder: When cases was fail or error, save screenshot to here
   ./result/report/   ---Folder : This Folder user to save history reports

   
