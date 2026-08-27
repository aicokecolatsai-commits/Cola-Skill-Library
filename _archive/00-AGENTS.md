# Workspace Safety Rules

These rules apply to work in this repository.

## Safe Delete

- Do not permanently delete files by default.
- Before deleting or moving files, explain the target path and confirm it is inside the intended workspace.
- Prefer moving unwanted files to a recoverable holding folder such as `.trash/` instead of deleting them.
- Never run recursive delete commands unless the user explicitly asks for that exact action and the absolute target path has been verified.

## Blocked High-Risk Commands

Do not run or suggest running these commands from automation:

- `rm -rf`, `rm -fr`, `rm -r`, `rm -R`, `rm -f`
- `Remove-Item -Recurse`, unless the user explicitly approves the exact absolute path
- `sudo`
- `dd`
- `mkfs`
- `diskutil erase`
- `chmod 777`, `chmod -R 777`
- `git reset --hard`
- `git push --force`, `git push -f`
- `git clean -f`
- `git branch -D`
- `shutdown`
- `reboot`
- `truncate`
- shell redirection patterns that empty files, such as `: > file`

## Permission Mode

- Use an "Accept Edits" working style in this workspace: file edits may proceed when they are scoped and reversible.
- Ask before running commands that install software, access the network, delete files, change system settings, or modify files outside this workspace.
- Keep backups before modifying configuration files.

## Windows Notes

- This workspace runs on Windows / PowerShell, so the macOS `trash` and zsh alias steps from the source guide are not applied directly.
- For local cleanup, use a recoverable `.trash/` folder inside the workspace unless the user asks for another destination.
