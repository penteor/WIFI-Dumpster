@echo off

:MENU
ECHO.
ECHO ...............................................
ECHO PRESS 1, 2 , etc. to select your task, or 9 to EXIT.
ECHO ...............................................
ECHO.
ECHO 1 - List Available SSIDs
ECHO 2 - List Wireless Profiles
ECHO 3 - List Blocked Wireless Access Points
ECHO 4 - Details about current Interface
ECHO 5 - Generate Full Report
ECHO 6 - Show Clear Text Passwords
ECHO 7 - Dump Encrypted Profiles
ECHO 8 - EXIT
ECHO.

SET /P M=Type one number then press ENTER:
IF %M%==1 GOTO ListAll
IF %M%==2 GOTO Profiles
IF %M%==3 GOTO BlockedAP
IF %M%==4 GOTO Interface
IF %M%==5 GOTO FullReport
IF %M%==6 GOTO ClearText
IF %M%==7 GOTO ExportProfiles
IF %M%==8 GOTO EOF

:ListAll
netsh wlan show networks
GOTO MENU

:Profiles
netsh wlan show profiles
GOTO MENU

:BlockedAP
netsh wlan show filters
GOTO MENU

:Interface
netsh wlan show interfaces
GOTO MENU

:FullReport
netsh wlan show all
GOTO MENU

:ClearText
netsh wlan show profiles | findstr "All User Profile"
set /p Profile=Type Profile name:
netsh wlan show profiles name=%Profile% key=clear

:ExportProfiles
netsh wlan export profile folder=.
