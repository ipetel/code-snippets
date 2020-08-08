# screen command in Linux

- Starting Named Session: `screen -S <session_name>`
- Session list: `screen -ls`

*output example from `screen -ls`: 10835.pts-0.linuxize-desktop   (Detached)*

- Restore specific screen: `screen -r 10835.pts-0.linuxize-desktop`
- Detach a screen session: `screen -d 10835.pts-0.linuxize-desktop`
- Detach and kill session: `screen -XS 10835.pts-0.linuxize-desktop quit`
