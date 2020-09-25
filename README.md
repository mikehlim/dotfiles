# dotfiles

i3 Theme Arc-Dark, Papirus, Terminus TTF and etc

#Package installations

sudo apt-get install i3 i3blocks arc-theme lxappearance fonts-terminus blueman light copyq nemo ranger compton caffeine redshift-gtk trash-cli flameshot rofi xss-lock lxpolkit feh autorandr udiskie rxvt-unicode gnome-terminal gnome-keyring network-manager-vpnc-gnome network-manager-openvpn-gnome remmina filezilla virtualbox smplayer vlc audacious gimp openssh-server git uim uim-byeoru


#papirus icon theme installation

git clone "https://github.com/PapirusDevelopmentTeam/papirus-icon-theme.git"
./papirus-icon-theme/install.sh

#tap to click

sudo mkdir -p /etc/X11/xorg.conf.d && sudo tee <<'EOF' /etc/X11/xorg.conf.d/90-touchpad.conf 1> /dev/null
Section "InputClass"
        Identifier "touchpad"
        MatchIsTouchpad "on"
        Driver "libinput"
        Option "Tapping" "on"
EndSection

EOF
