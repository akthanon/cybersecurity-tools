#!/usr/bin/env python3
"""
ps_encode.py — Encode a PowerShell command to the Base64 string used by:
  powershell -NoP -NonI -EncodedCommand <base64>

Usage examples:
  python ps_encode.py -c "Write-Output 'hola'"
  echo "Write-Output 'hola'" | python ps_encode.py
  python ps_encode.py -f archivo.ps1
"""

import argparse
import base64
import sys
from pathlib import Path

def encode_command(cmd: str) -> str:
    # PowerShell expects UTF-16LE for -EncodedCommand
    return base64.b64encode(cmd.encode('utf-16le')).decode('ascii')

def parse_args():
    p = argparse.ArgumentParser(description="Encode PowerShell command to -EncodedCommand Base64")
    group = p.add_mutually_exclusive_group()
    group.add_argument('-c', '--command', help='PowerShell command as a string')
    group.add_argument('-f', '--file', type=Path, help='Path to a .ps1 file (or any text file) to encode')
    p.add_argument('--full', action='store_true',
                   help='Print the full invocation: powershell -NoP -NonI -EncodedCommand <BASE64>')
    return p.parse_args()

def main():
    args = parse_args()

    if args.command:
        cmd = args.command
    elif args.file:
        try:
            cmd = args.file.read_text(encoding='utf-8')
        except Exception:
            # Fallback to default system encoding if utf-8 fails
            cmd = args.file.read_text()
    else:
        # Read from stdin (useful for pipes)
        if sys.stdin.isatty():
            # No stdin piped and no args -> ask user (interactive)
            cmd = input("Ingresa el comando de PowerShell a codificar:\n> ")
        else:
            cmd = sys.stdin.read()

    cmd = cmd.rstrip('\n')  # remove trailing newline if present
    if not cmd:
        print("No se proporcionó ningún comando.", file=sys.stderr)
        sys.exit(1)

    encoded = encode_command(cmd)

    if args.full:
        print(f"powershell -NoP -NonI -EncodedCommand {encoded}")
    else:
        print(encoded)

if __name__ == "__main__":
    main()
