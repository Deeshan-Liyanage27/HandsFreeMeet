$webcam = Get-PnpDevice -PresentOnly | Where-Object { $_.FriendlyName -match '^USB2.0_Camera'}

if ($webcam) {
    Write-Host "Webcam found: $($webcam.FriendlyName)"

    Write-Host "Setting up audio devices"
    Set-AudioDevice -ID "{0.0.1.00000000}.{cc36137c-e592-49ef-8316-c219798507fb}" # Make it default device 
    Set-AudioDevice -PlaybackMute $false
    Set-AudioDevice -RecordingMute $false

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

    # Stop-Computer -Force # To shut down the computer after the call

} else {
    Write-Host "No webcam found."
}

