$webcam = Get-PnpDevice -PresentOnly | Where-Object { $_.FriendlyName -match '^USB2.0_Camera'}

if ($webcam) {
    Write-Host "Webcam found: $($webcam.FriendlyName)"

} else {
    Write-Host "No webcam found."
}