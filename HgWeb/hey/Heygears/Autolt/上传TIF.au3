;ControlFocus("titile","text","controID") controID = Edit instance
ControlFocus("打开","","Edit1")

;Wait 10 seconds for the Upload window to apper
WinWait("#32770","","10")

;Set the File name text on the Edit field
ControlSetText("打开","","Edit1","F:\Web\Heygears\Test_Img\448KB.tif")
Sleep(2000)

;Click on the Open button
ControlClick("打开","","Button1")