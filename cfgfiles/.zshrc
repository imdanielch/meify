#imports
source ~/.zsh/keybind.zsh
source ~/.zsh/prompt.zsh
source ~/.zsh/alias.zsh

#enable cmd history
export HISTSIZE=100
export HISTFILE="$HOME/.zsh_history"
export SAVEHIST=$HISTSIZE
setopt hist_ignore_all_dups
setopt hist_ignore_space
setopt autocd

#load nvm
export NVM_DIR="/home/daniel/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm

