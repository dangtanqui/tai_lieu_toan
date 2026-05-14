#!/usr/bin/env bash
# Script kiem ke phan mem thuong mai tren Ubuntu/Debian
# Tuong duong check_software.ps1 nhung danh cho Linux
# CHI DOC, KHONG thay doi he thong

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
OUT="$SCRIPT_DIR/software_result.txt"

# Danh sach phan mem can check (phien ban co tren Linux hoac dang web/portable)
SW_LIST=(
    "1Password"
    "Adobe Acrobat"
    "Adobe Creative Cloud"
    "AnyDesk"
    "ApowerMirror"
    "Apowersoft"
    "Araxis Merge"
    "Axure"
    "Balsamiq"
    "Beyond Compare"
    "Burp Suite"
    "Charles"
    "Cisco AnyConnect"
    "Cisco Secure Client"
    "Citrix Workspace"
    "Citrix Receiver"
    "DataGrip"
    "Datadog Agent"
    "DBeaver"
    "DbVisualizer"
    "Docker Desktop"
    "EaseUS"
    "EndNote"
    "Fiddler"
    "Foxit"
    "GitHub Copilot"
    "Grammarly"
    "IntelliJ IDEA"
    "JetBrains CLion"
    "CLion"
    "JetBrains GoLand"
    "GoLand"
    "JetBrains Rider"
    "Rider"
    "JetBrains Toolbox"
    "PhpStorm"
    "PyCharm"
    "RubyMine"
    "WebStorm"
    "DataSpell"
    "ReSharper"
    "Kaspersky"
    "LanguageTool"
    "LastPass"
    "MATLAB"
    "Simulink"
    "MindManager"
    "XMind"
    "MobaXterm"
    "Movavi"
    "Navicat"
    "Nessus"
    "Nitro"
    "Oracle Database"
    "Oracle Client"
    "Java SE"
    "Parallels"
    "Postman"
    "Insomnia"
    "Power BI"
    "Qlik"
    "Quartus"
    "Radmin"
    "Ranorex"
    "ReadyAPI"
    "SoapUI"
    "RealVNC"
    "VNC Server"
    "VNC Viewer"
    "Remote Desktop Manager"
    "SAP GUI"
    "SAP BusinessObjects"
    "Crystal Reports"
    "SecureCRT"
    "SimpleMind"
    "SketchUp"
    "Slack"
    "Sublime Text"
    "Sublime Merge"
    "Tableau"
    "TeamViewer"
    "Trend Micro"
    "UiPath"
    "Veeam"
    "Visual Studio Code"
    "VMware Workstation"
    "VMware Horizon"
    "WinRAR"
    "Zoom"
    "Microsoft Teams"
    "Microsoft Edge"
    "WPS Office"
    "OnlyOffice"
    "Foxit PDF"
    "Telegram"
    "MongoDB Compass"
)

# Mau in (chi cho terminal)
if [ -t 1 ]; then
    GREEN="\033[1;32m"
    GRAY="\033[1;30m"
    CYAN="\033[1;36m"
    YELLOW="\033[1;33m"
    NC="\033[0m"
else
    GREEN=""; GRAY=""; CYAN=""; YELLOW=""; NC=""
fi

echo "Dang quet phan mem da cai..."

# Thu thap moi nguon -> file tam (de match nhieu lan)
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

# 1. APT packages - chi lay ten package (tranh false positive tu description)
{
    if command -v dpkg-query >/dev/null 2>&1; then
        dpkg-query -W -f='APT: ${Package}\n' 2>/dev/null
    fi
} >> "$TMP"

# 2. Snap packages
if command -v snap >/dev/null 2>&1; then
    snap list 2>/dev/null | awk 'NR>1 {print "SNAP: " $1 " " $0}' >> "$TMP"
fi

# 3. Flatpak
if command -v flatpak >/dev/null 2>&1; then
    flatpak list --columns=application,name 2>/dev/null \
        | awk 'NR>0 {print "FLATPAK: " $0}' >> "$TMP"
fi

# 4. .desktop files (lay Name=)
find /usr/share/applications \
     /var/lib/snapd/desktop/applications \
     /var/lib/flatpak/exports/share/applications \
     ~/.local/share/applications \
     2>/dev/null -name "*.desktop" -print0 \
    | xargs -0 -I{} sh -c '
        name=$(grep -m1 "^Name=" "$1" 2>/dev/null | sed "s/^Name=//")
        [ -n "$name" ] && echo "DESKTOP: $name | $1"
    ' _ {} >> "$TMP" 2>/dev/null

# 5. /opt subdirs (phan mem cai thu cong)
ls -1 /opt 2>/dev/null | awk '{print "OPT: " $0}' >> "$TMP"

# 6. JetBrains Toolbox apps
for p in \
    ~/.local/share/JetBrains/Toolbox/apps \
    ~/.local/share/JetBrains \
    /opt/JetBrains \
    ~/.config/JetBrains
do
    if [ -d "$p" ]; then
        ls -1 "$p" 2>/dev/null | awk -v base="$p" '{print "JETBRAINS: " $0 " (" base ")"}'
    fi
done >> "$TMP"

# 7. Cac binary trong /usr/local/bin va /usr/bin
ls -1 /usr/local/bin 2>/dev/null | awk '{print "LOCALBIN: " $0}' >> "$TMP"

# Khoi tao output
{
    echo "===== SOFTWARE CHECK RESULT (Linux) ====="
    echo "Date:   $(date)"
    echo "Host:   $(hostname)"
    echo "User:   $USER"
    echo "OS:     $(lsb_release -ds 2>/dev/null || uname -a)"
    echo ""
} > "$OUT"

found=0
notfound=0

for sw in "${SW_LIST[@]}"; do
    # Tim trong file tam: case-insensitive, word-boundary (giam false positive)
    pattern="\b$(printf '%s' "$sw" | sed 's/[][().+*?^$|\\]/\\&/g')\b"
    hit="$(grep -iE -m1 -- "$pattern" "$TMP" 2>/dev/null || true)"
    if [ -n "$hit" ]; then
        line="[FOUND]     $sw  ->  $hit"
        printf "${GREEN}%s${NC}\n" "$line"
        found=$((found+1))
    else
        line="[NOT FOUND] $sw"
        printf "${GRAY}%s${NC}\n" "$line"
        notfound=$((notfound+1))
    fi
    echo "$line" >> "$OUT"
done

{
    echo ""
    echo "===== TONG KET ====="
    echo "Da cai (FOUND):    $found"
    echo "Khong co (NOT):    $notfound"
    echo ""
    echo "Luu y: [FOUND] CHI co nghia phan mem co tren may, KHONG dong nghia voi"
    echo "'khong ban quyen'. Day chi la buoc kiem ke ban dau."
} | tee -a "$OUT"

printf "${CYAN}Ket qua da luu: %s${NC}\n" "$OUT"
