# assuming you have your gh-pages branch checked out in a sibling folder
# or you can copy the output locally into .\site-output\
mkdir content\recovered

Get-ChildItem .\site-output\ -Recurse -Filter *.html | ForEach-Object {
  $out = $_.FullName.Replace('\site-output\','\content\recovered\').Replace('.html','.md')
  New-Item -ItemType Directory -Path (Split-Path $out) -Force | Out-Null
  pandoc $_.FullName -f html -t gfm -o $out
}
