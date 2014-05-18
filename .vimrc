set runtimepath+=~/.vim_runtime

source ~/.vim_runtime/vimrcs/basic.vim
source ~/.vim_runtime/vimrcs/filetypes.vim
source ~/.vim_runtime/vimrcs/plugins_config.vim
source ~/.vim_runtime/vimrcs/extended.vim

try
source ~/.vim_runtime/my_configs.vim
catch
endtry

let NERDTreeIgnore = ['\.pyc$']
let g:NERDTreeWinSize = 40

"   Function quits NERDTree buffer when last file is closed
function! NERDTreeQuit()
    redir => buffersoutput
    silent buffers
    redir END
"   1BufNo  2Mods.     3File           4LineNo
    let pattern = '^\s*\(\d\+\)\(.....\) "\(.*\)"\s\+line \(\d\+\)$'
    let windowfound = 0
          
    for bline in split(buffersoutput, "\n")
        let m = matchlist(bline, pattern)
              
        if (len(m) > 0)
            if (m[2] =~ '..a..')
                let windowfound = 1
            endif
        endif
    endfor
          
    if (!windowfound)
        quitall
    endif
endfunction
autocmd WinEnter * call NERDTreeQuit()

autocmd VimEnter * NERDTree
autocmd BufEnter * NERDTreeMirror
autocmd VimEnter * wincmd w

execute pathogen#infect()

syntax on
set clipboard=unnamed
set number
set tabstop=4 shiftwidth=4 expandtab

set nocompatible
filetype off

set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

Bundle 'gmarik/vundle'
Bundle 'Valloric/YouCompleteMe'

filetype plugin indent on
