Start-Sleep -Seconds 30

# CHANGE NAME FOR YOUR DEVICE BY CHECKING IT THROUGH "Get-AudioDevice -List"
$webcam = Get-PnpDevice -PresentOnly | Where-Object { $_.FriendlyName -match '^USB2.0_Camera'}

if ($webcam) {
    Write-Host "External Microphone found: $($webcam.FriendlyName)"

    Write-Host "Setting up audio devices"
    # CHANGE ID FOR YOUR AUDIO DEVICE BY CHECKING IT THROUGH "Get-AudioDevice -List"
    Set-AudioDevice -ID "{0.0.1.00000000}.{15a29f24-c2b6-4fac-b710-f2e287ce485d}" # Make it default device  .

    Set-AudioDevice -PlaybackMute $false
    Set-AudioDevice -RecordingMute $false
    
    # CHANGE THE WIFI NETWORK NAME TO YOUR DESIRED 
    netsh wlan set autoconnect enabled=yes name="RNDS" 
    netsh wlan connect name="RNDS"
    $wifi = netsh wlan show interfaces | Select-String -Pattern "State" | ForEach-Object { $_.ToString().Split(':')[1].Trim() }
    while ($wifi -ne "connected") {
        Write-Host "Connecting to Wi-Fi..."
        netsh wlan connect name="RNDS"
        Start-Sleep -Seconds 10
        $wifi = netsh wlan show interfaces | Select-String -Pattern "State" | ForEach-Object { $_.ToString().Split(':')[1].Trim() }
    }       

    Write-Host "Starting Messenger"
    Start-Process "https://www.messenger.com/"
    
    python .\CallManager.py
    Write-Host "Automation complete."

    Start-Sleep -Seconds 60
    Stop-Computer -Force # To shut down the computer after the call

} else {
    Write-Host "No External Microphone found."
}

