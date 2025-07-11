# HandsFreeMeet

**HandsFreeMeet** is an automation tool that launches Facebook Messenger in the default browser and automatically handles group video calls with no user interaction required.

This program is built for older generation who doesn't know how to operate a computer.  It starts automatically when the computer boots up and runs only if the specific external microphone is connected, ensuring it's used only when intended.  

## Features

- Automatically connects to Wi-Fi
- Launches Messenger and joins/answers video calls
- Goes full screen and ends the call automatically
- Shuts down after the call ends
- Works only when an external microphone is connected

## Installation

Clone the Repository:

```bash
git clone https://github.com/Deeshan-Liyanage27/HandsFreeMeet.git
cd HandsFreeMeet
```

### Install Python Dependencies (Required):

```bash
pip install pyautogui
```

### Install Audio Device Cmdlets (Required):

```bash
#Run the following command as Administrator in Powershell 
Install-Module -Name AudioDeviceCmdlets
```

## How to run?
Open PowerShell and run **Get-AudioDevice -List**
Get the name and ID of the external device.
Replace them with the current.
Right click on the .ps1 file and select **Run with PowerShell**.

## Autorun (Optional)

To make the script run automatically on startup, follow this guide:

[ Automate PowerShell scripts using Task Scheduler](https://blog.netwrix.com/how-to-automate-powershell-scripts-with-task-scheduler)
