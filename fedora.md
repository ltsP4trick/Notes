## Delta rpm and mirror plugins
` sudo nano /etc/dnf/dnf.conf `

```
fastestmirror=true
deltarpm=true
```

## apps & [rpm fusion](https://rpmfusion.org/Configuration):
```
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y && sudo dnf remove fedora-chromium-config totem -y && sudo dnf update --refresh -y && sudo dnf install -y gnome-tweaks xclip dkms kernel-devel kernel-headers gimp nano zsh flatpak libreoffice libreoffice-langpack-pl python3-virtualenv     google-noto-sans-fonts google-noto-serif-fonts google-noto-sans-mono-fonts    python3-black python-numpy python-matplotlib python-pandas python-scipy      zsh-syntax-highlighting zsh-autosuggestions       vlc && sudo dnf groupupdate Multimedia core -y
```

## Brave && Fedora
```
sudo dnf install dnf-plugins-core -y && sudo dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/x86_64/ && sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc && sudo dnf install brave-browser -y

sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc && sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo' && sudo dnf update --refresh -y && sudo dnf install code -y
```

### now, reboot computer

## Flatpak apps
```
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo && flatpak install flathub com.discordapp.Discord org.signal.Signal org.gtk.Gtk3theme.Adwaita-dark -y

```

### Signal system Tray

[source](https://github.com/flathub/org.signal.Signal/issues/116#issuecomment-589998170)
```
nano /var/lib/flatpak/app/org.signal.Signal/current/active/export/share/applications/org.signal.Signal.desktop
```
`--use-tray-icon`


### in the meantime you can change shortcuts or configure stuff that is below

### git
```
git config --global user.name ''
git config --global user.email '52964049+itsP4trickn@users.noreply.github.com'
git config --global core.editor nano
ssh-keygen -t rsa -b 4096
xclip -sel clip < ~/.ssh/id_rsa.pub
```
[Git configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)

### zsh:
- [oh my zsh](https://github.com/ohmyzsh/ohmyzsh/#getting-started)
- [fav theme](https://github.com/denysdovhan/spaceship-prompt#oh-my-zsh)

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" 

git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" && ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme" && nano .zshrc
```

 ```spaceship"```

## Clamav

### Install
```
sudo apt install clamav clamav-daemon
```
### Run

` freshclam ` - update database

sudo clamscan -r / | grep FOUND >> /home/pnogas/report

### [Laptop](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/performance_tuning_guide/chap-red_hat_enterprise_linux-performance_tuning_guide-tuned#installation-and-usage):

```
yum install tuned-utils -y && powertop2tuned -n -e laptop && systemctl start tuned && systemctl enable tuned
```


### hostname:
```sudo hostnamectl set-hostname``` *name*

### gnome:

```
gsettings set org.gnome.desktop.wm.preferences resize-with-right-button true

```

2. ext:

- [fuzzy search](https://extensions.gnome.org/extension/3956/gnome-fuzzy-app-search/)

```
sudo dnf install -y gnome-shell-extension-emoji-selector gnome-shell-extension-appindicator gnome-shell-extension-caffeine gnome-shell-extension-dash-to-dock gnome-shell-extension-gpaste -y && dnf remove twitter-twemoji-fonts -y
```

## Last thing
Grub:
```
sudo nano /etc/default/grub

```
EFI:
```
sudo grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg
```
Bios:
```
grub2-mkconfig -o /boot/grub2/grub.cfg
```
Remove sudo:
``` 
sudo nano /etc/group
```
