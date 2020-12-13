## apps:
```
sudo add-apt-repository multiverse && sudo add-apt-repository restricted && sudo apt update && sudo apt upgrade -y && sudo apt-get install -y gnome-tweaks xclip dkms  pavucontrol gimp nano zsh flatpak libreoffice libreoffice-langpack-pl python3-virtualenv     python3-black python3-numpy python3-matplotlib python3-pandas python3-scipy      zsh-syntax-highlighting zsh-autosuggestions   ubuntu-restricted-extras vlc
```
## Steam
```
sudo dpkg --add-architecture i386 && sudo apt install steam

```
## Flatpak and VS code
```
sudo snap install discord signal-desktop teams

wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg && sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/ && sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list' && sudo apt install apt-transport-https -y && sudo apt update && sudo apt install code -y

```
## Brave
```
sudo apt install apt-transport-https curl gnupg -y && curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add - && echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list && sudo apt update && sudo apt install brave-browser -y
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

### Laptop:
```
yum install tuned-utils

powertop2tuned -n -e laptop
```


### hostname:
```sudo hostnamectl set-hostname``` *name*

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


## Last thing
Grub
```
sudo nano /etc/default/grub

Remove sudo:
``` 
sudo nano /etc/group
```
