Write-Output "Starting to process items..."

Get-ChildItem -Directory | ForEach-Object {
	Write-Output ("Processing {0}..." -f ($_.Name))
	$parts = $_.Name -Split " "
	$new_name = ""
	foreach ( $part in $parts ) {
		$new_part = "{0}{1}" -f ($part.Substring(0, 1).toupper(), $part.Substring(1))
		$new_name += $new_part + " "
	}
	$new_name = $new_name.Substring(0, $new_name.Length - 1)
	
	Rename-Item $_ temp
	Rename-Item temp $new_name
}

Write-Output "Done."