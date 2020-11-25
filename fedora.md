## apps:
```
sudo dnf remove fedora-chromium-config totem -y && sudo dnf install -y gnome-tweaks xclip dkms kernel-devel kernel-headers pavucontrol gimp nano zsh flatpak google-noto-sans-fonts google-noto-serif-fonts google-noto-sans-mono-fonts google-noto-emoji-color-fonts libreoffice libreoffice-langpack-pl python3-virtualenv     python3-black python-numpy python-matplotlib python-pandas python-scipy      zsh-syntax-highlighting zsh-autosuggestions && git clone https://github.com/aircrack-ng/rtl8812au.git && systemctl reboot
```
### Wifi
https://github.com/aircrack-ng/rtl8812au/tree/07c704c0a7131208a909c3fc36e7daa122b98b16


## rpm fusion:
- [rpm fusion](https://rpmfusion.org/Configuration)
- [multimedia](https://rpmfusion.org/Howto/Multimedia)
- [nvidia](https://rpmfusion.org/Howto/NVIDIA)
- [cuda](https://rpmfusion.org/Howto/CUDA)
```
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y
sudo dnf remove firefox && sudo dnf install -y vlc steam telegram-desktop && sudo dnf groupupdate Multimedia core -y
sudo dnf install akmod-nvidia -y ###After this please reboot your system
sudo dnf install xorg-x11-drv-nvidia-cuda -y ###After this please reboot your system
```

## Flatpak and VS code
```
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo && sudo flatpak install flathub -y com.discordapp.Discord org.signal.Signal org.gtk.Gtk3theme.Adwaita-dark

sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc && sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo' && sudo dnf check-update -y && sudo dnf install code -y
```
## Delta rpm and mirror plugins
` sudo nano /etc/dnf/dnf.conf `

```
fastestmirror=true
deltarpm=true
```

### git
```
git config --global user.name **name**
git config --global user.email 'nogaspat+git@gmail.com'
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
sudo dnf install clamav clamav-update
```
### Run

` freshclam ` - update database

sudo clamscan -r / | grep FOUND >> /home/pnogas/report



### hostname:
```sudo hostnamectl set-hostname``` *name*

### [block websites](https://bytenbit.com/how-to-block-websites-on-windows-ubuntu-macintosh/)

```sudo nano /etc/hosts```

```
127.0.0.1 www.facebook.com
127.0.0.1 www.youtube.com
```
write it at the end of file

### if gnome:

```
sudo dnf install -y gnome-shell-extension-pomodoro && gsettings set org.gnome.desktop.wm.preferences resize-with-right-button true   
```

2. ext:
- [bluetooth](https://extensions.gnome.org/extension/1401/bluetooth-quick-connect/)
- [audio switcher](https://extensions.gnome.org/extension/1028/gnome-shell-audio-output-switcher/)
- [clipboard indicator](https://extensions.gnome.org/extension/779/clipboard-indicator/)
- [caffeine](https://extensions.gnome.org/extension/517/caffeine/)
- [top icon](https://extensions.gnome.org/extension/615/appindicator-support/)


### if plasma
```
sudo dnf install -y gnome-themes-extra
```
windows managment -> windows behavior -> Advanced -> windwos placment == center
left click on panel -> configure -> behavior -> Cycle through windows when scrolling
System Settings > Input Devices > Keyboard > Hardware > NumLock on KDE Startup

## Last thing
Grub
```
sudo nano /etc/default/grub

```
EFI:
```
sudo grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg
```

Remove sudo:
``` 
sudo nano /etc/group
```
