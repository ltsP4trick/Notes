## apps:
```
sudo dnf remove fedora-chromium-config totem -y && sudo dnf update --refresh -y && sudo dnf install -y snapd gnome-tweaks xclip dkms kernel-devel kernel-headers gimp nano zsh flatpak libreoffice libreoffice-langpack-pl python3-virtualenv     google-noto-sans-fonts google-noto-serif-fonts google-noto-sans-mono-fonts    python3-black python-numpy python-matplotlib python-pandas python-scipy      zsh-syntax-highlighting zsh-autosuggestions
```
## rpm fusion:
- [rpm fusion](https://rpmfusion.org/Configuration)
- [multimedia](https://rpmfusion.org/Howto/Multimedia)
- [nvidia](https://rpmfusion.org/Howto/NVIDIA)
- [cuda](https://rpmfusion.org/Howto/CUDA)
```
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y && sudo dnf update --refresh -y && sudo dnf install -y vlc steam && sudo dnf groupupdate Multimedia core -y
```

## Snap and VS code
```
sudo ln -s /var/lib/snapd/snap /snap && sudo snap install discord signal-desktop teams && sudo snap install code --classic

```

## Brave
```
sudo dnf install dnf-plugins-core -y && sudo dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/x86_64/ && sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc && sudo dnf install brave-browser -y
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

### Laptop:

```
yum install tuned-utils

powertop2tuned -n -e laptop
```


### hostname:
```sudo hostnamectl set-hostname``` *name*

### gnome:

```
gsettings set org.gnome.desktop.wm.preferences resize-with-right-button true

```

2. ext:
- [clipboard indicator](https://extensions.gnome.org/extension/779/clipboard-indicator/)
- [caffeine](https://extensions.gnome.org/extension/517/caffeine/)
- [top icon](https://extensions.gnome.org/extension/615/appindicator-support/)  [optional on ubuntu]


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
