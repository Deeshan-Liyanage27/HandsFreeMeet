$webcam = Get-PnpDevice -PresentOnly | Where-Object { $_.FriendlyName -match '^USB2.0_Camera'}

if ($webcam) {
    Write-Host "Webcam found: $($webcam.FriendlyName)"

    Write-Host "Setting up audio devices"
    Set-AudioDevice -ID "{0.0.1.00000000}.{cc36137c-e592-49ef-8316-c219798507fb}" # Make it default device 
    Set-AudioDevice -PlaybackMute $false
    Set-AudioDevice -RecordingMute $false

    Write-Host "Starting Messenger"
    Start-Process "https://www.messenger.com/"
    
    python .\move.py
    Write-Host "Automation complete."

    # Stop-Computer -Force # To shut down the computer after the call

} else {
    Write-Host "No webcam found."
}