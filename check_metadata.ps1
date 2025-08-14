# Scan all Markdown files for bad metadata format
$ContentDir = "content"
Write-Host "Scanning $ContentDir for malformed Pelican metadata..." -ForegroundColor Cyan

Get-ChildItem -Path $ContentDir -Recurse -Filter *.md | ForEach-Object {
    $FilePath = $_.FullName
    $BadLines = @()
    $InsideMeta = $true

    Get-Content $FilePath | ForEach-Object {
        $line = $_.Trim()

        # Stop checking metadata when content starts
        if ($InsideMeta -and $line -eq "") {
            $InsideMeta = $false
        }

        # Only check lines before first empty line
        if ($InsideMeta) {
            # Pelican metadata should be like "Key: Value"
            if ($line -match "^\S.*$") {
                $parts = $line.Split(":")
                if ($parts.Count -ne 2) {
                    $BadLines += $line
                }
            }
        }
    }

    if ($BadLines.Count -gt 0) {
        # --- THIS IS THE CORRECTED LINE ---
        Write-Host "`nPossible bad metadata in ${FilePath}:" -ForegroundColor Yellow
        $BadLines | ForEach-Object { Write-Host "   $_" -ForegroundColor Red }
    }
}

Write-Host "`nScan complete." -ForegroundColor Green