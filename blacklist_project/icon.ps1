Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;
using System.Drawing;
using System.Drawing.Imaging;

public class IconExtractor {
    [DllImport("Shell32.dll")]
    public static extern int ExtractIconEx(string lpszFile, int nIconIndex, IntPtr[] phIconLarge, IntPtr[] phIconSmall, int nIcons);

    public static Icon GetIcon(string fileName) {
        IntPtr[] largeIcon = new IntPtr[1];
        IntPtr[] smallIcon = new IntPtr[1];
        ExtractIconEx(fileName, 0, largeIcon, smallIcon, 1);
        if (largeIcon[0] != IntPtr.Zero)
            return Icon.FromHandle(largeIcon[0]);
        return null;
    }
}
"@

$filePath = "./hack.ico"
$icon = [IconExtractor]::GetIcon($filePath)

if ($null -ne $icon) {
    $icon.ToBitmap().Save("./icon.png", [System.Drawing.Imaging.ImageFormat]::Png)
    Write-Host "Icon extracted successfully."
} else {
    Write-Host "No icon found in the file."
}
