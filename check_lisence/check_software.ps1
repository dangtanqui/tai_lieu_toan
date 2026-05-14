$sw = @(
"1Password","ABBYY FineReader","Ablebits","Adobe Acrobat",
"Adobe Creative Cloud","Advanced Uninstaller PRO","Aiseesoft",
"AnyDesk","ApowerMirror","ApowerREC","Apowersoft","Araxis Merge",
"Audio Voice Recorder","AutoCAD","Autodesk Revit","Avaya IP Office",
"Axure RP","Balsamiq","BB FlashBack","Beyond Compare","BookmarkSync",
"Burp Suite","Charles Proxy","Cisco AnyConnect","Cisco Secure Client",
"Citrix Workspace","Citrix Receiver","Cool Edit Pro","Datadog Agent",
"DBeaver","DbVisualizer","Docker Desktop","DWGSee","EaseUS","EndNote",
"Esna iLink","Fiddler","Telerik","FMEA-Pro","Foxit PDF Editor",
"PhantomPDF","FTA-Pro","GitHub Copilot","Grammarly","HD Tune",
"Internet Download Manager","IDM","JetBrains CLion",
"JetBrains DataGrip","JetBrains GoLand","IntelliJ IDEA",
"PhpStorm","PyCharm","ReSharper","JetBrains Rider","WebStorm",
"JSON Formatter","JSON Viewer","Kaspersky","LanguageTool",
"LastPass","MapInfo","MATLAB","Simulink","Microsoft Project",
"Microsoft Visio","MindManager","XMind","MiniTool Partition",
"MobaXterm","Monica AI","Movavi","Navicat","Nessus","Tenable",
"NetScanTools","Nitro Pro","Oracle Database","Oracle Client",
"Java SE","Parallels Remote","pdfFactory","PHA-Pro","Postman",
"Power BI","Qlik Sense","QlikView","Quartus Prime","Radmin",
"Ranorex","ReadyAPI","SoapUI","RealVNC","VNC Server",
"VNC Viewer","Remote Desktop Manager","SAP GUI",
"SAP BusinessObjects","Crystal Reports","Screenpresso",
"SecureCRT","SimpleMind","SketchUp","Slack","Snagit",
"Sublime Text","SVA-Pro","Tableau","TeamViewer","Tera Term",
"Trend Micro","UiPath","Veeam Backup",
"Visual Studio Professional","Visual Studio Enterprise",
"VMware Horizon","vCenter","WinRAR","WinZip","Zip Extractor"
)

$paths = @(
"HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall",
"HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",
"HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall"
)

$installed = $paths |
ForEach-Object {
    Get-ChildItem $_ -ErrorAction SilentlyContinue
} |
ForEach-Object {
    try {
        $n = $_.GetValue("DisplayName")
        if ($n) { $n }
    }
    catch {}
}

$resultFile = "$PSScriptRoot\software_result.txt"

"===== SOFTWARE CHECK RESULT =====" | Out-File $resultFile

$sw | ForEach-Object {

    $k = $_

    $hit = $installed | Where-Object {
        $_ -like "*$k*"
    }

    if ($hit) {
        $line = "[FOUND]    $k  ->  $($hit[0])"
        Write-Host $line -ForegroundColor Green
    }
    else {
        $line = "[NOT FOUND] $k"
        Write-Host $line -ForegroundColor DarkGray
    }

    Add-Content -Path $resultFile -Value $line
}

Write-Host ""
Write-Host "Result saved to: $resultFile" -ForegroundColor Cyan

pause