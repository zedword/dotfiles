#
# ~/.bashrc
#

eval "$(starship init bash)"

# If not running interactively, don't do anything
#[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grupdate='sudo grub-mkconfig -o /boot/grub/grub.cfg'
alias shutoff='sudo shutdown -h now'
alias logoff='sudo systemctl restart display-manager'
#PS1='[\u@\h \W]\$ '


# BEGIN_KITTY_SHELL_INTEGRATION
if test -n "$KITTY_INSTALLATION_DIR" -a -e "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; then source "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; fi
# END_KITTY_SHELL_INTEGRATION
