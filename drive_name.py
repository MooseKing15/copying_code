import win32com.client
strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")

def DVD_Name():
    # 4. Win32_LogicalDisk
    LogicalDisk_DeviceID = "E:"
    colItems = objSWbemServices.ExecQuery("SELECT * from Win32_LogicalDisk WHERE DeviceID=\"" + LogicalDisk_DeviceID + "\"")
    print('Copying Disk:', colItems[0].VolumeName)


    # putting it together
    return(colItems[0].VolumeName)