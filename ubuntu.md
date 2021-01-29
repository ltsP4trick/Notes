## apps:
```
sudo add-apt-repository multiverse && sudo add-apt-repository restricted && sudo apt-get update && sudo apt-get upgrade -y && apt-get dist-upgrade -y && sudo apt-get install -y linux-headers-$(uname -r) gnome-tweaks ttf-mscorefonts-installer gnome-shell-extension-prefs gnome-weather laptop-mode-tools xclip dkms gnome-shell-extensions git gimp nano zsh flatpak libreoffice libreoffice-l10n-pl python3-virtualenv     black python3-numpy python3-matplotlib python3-pandas python3-scipy      zsh-syntax-highlighting zsh-autosuggestions   ubuntu-restricted-extras vlc steam
```
`
apt remove yelp
`

## Snap and VS code
```
sudo snap install discord signal-desktop teams && sudo snap install code --classic

```

## Brave
```
sudo apt install apt-transport-https curl gnupg -y && curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add - && echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list && sudo apt update && sudo apt install brave-browser -y
```


### git
```
git config --global user.name ''
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
sudo apt install clamav clamav-daemon
```
### Run

` freshclam ` - update database

sudo clamscan -r / | grep FOUND >> /home/pnogas/report


### hostname:
```sudo hostnamectl set-hostname``` *name*

### gnome:

```
gsettings set org.gnome.desktop.wm.preferences resize-with-right-button true && gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'

```

2. ext:
- [user themes](https://extensions.gnome.org/extension/19/user-themes/)
- [clipboard indicator](https://extensions.gnome.org/extension/779/clipboard-indicator/)
- [caffeine](https://extensions.gnome.org/extension/517/caffeine/)
- [fuzzy search](https://extensions.gnome.org/extension/3956/gnome-fuzzy-app-search/)


## Last thing
Grub

```
sudo nano /etc/default/grub && sudo update-grub

```