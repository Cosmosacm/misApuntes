Write-Host 'Primera linea de escritura'
Write-Host 'Aprendiendo Power shell'

$nombre1 = 'Ardanys Canchila M'
New-Variable nombre2
New-Variable -Name nombre3
New-Variable -Name nombre4 -Value 'cosmosacm'

New-Variable -Name constante -Value 'acm' -Option ReadOnly

Get-Variable

$nombre5 = Read-Host 'Digite su nombre'

Write-Host $nombre5.GetType().Name