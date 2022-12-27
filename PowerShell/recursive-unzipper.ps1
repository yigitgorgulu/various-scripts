Write-Output "Starting to process items..."

Get-ChildItem -Path "*.zip" | ForEach-Object {
	Write-Output ("Processing {0}..." -f ($_.Name))
	Expand-Archive $_
	Set-Location $_.BaseName
	
	while ( Get-ChildItem -Directory ) {
		$dir = Get-ChildItem -Directory
		Set-Location -Path $dir.Name
	}
	
	$loc = Get-Location
	while ( ($_.DirectoryName + "\" + $_.BaseName) -ne $loc.Path.ToString() ) {
		Move-Item * ..
		Set-Location ..
		Get-ChildItem | ForEach-Object {
			if ( $_.PSIsContainer ) {
				Remove-Item $_
			}
		}
		$loc = Get-Location
	}
	
	Set-Location ..
}

Write-Output "Done."