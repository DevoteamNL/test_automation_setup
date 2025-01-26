# test-automation-toolset

## Last tested versions

### Windows version

- Edition Windows 11 Pro
- Version 24H2
- OS build 26100.2894

### VScode version

- VScode version: 1.96.4
- Decontainer plugin version: 0.394.0

### WSL version

- WSL version: 2.3.26.0
- Verify with: `wsl -v`

### Linux distribution:

- Ubuntu 24.04.1 LTS
- Verify with: `cat /etc/os-release | grep PRETTY_NAME`

## Common problems

Before trying anything, always remember that a restart can do wonders..

If problems persist or continue to happen, proceed with checking the common problems and solutions below.

### Failure to pull image

ERROR: failed to solve: ghcr.io/test-automation-toolset:0.0.4: failed to resolve source metadata for ... error getting credentials

Clear the cache using `rm ~/.docker/config.json` in WSL terminal.

Otherwise, use `docker pull ghcr.io/test-automation-toolset:0.0.4` to pull the image manually.

### Failure to mount or connect remote environment

Often recognised by empty Explorer in VScode or terminal message: `chdir(2) failed.: Permission denied`

Remove cache and vscode config from WSL using `rm -r .cache .vscode-server vscode-remote-containers`

### Problems regarding Rancher-Desktop

Exit Rancher-Desktop completely. Make sure the App is not available in the icon tray.

```pwsh
wsl --unregister rancher-desktop

wsl --unregister rancher-desktop-data

wsl --set-default Ubuntu
```

Open Rancher-Desktop. Wait for startup.

Check Rancher Desktop WSL integrations with Ubuntu in:

- Preferences -> WSL -> Integrations -> [x] Ubuntu

Click on Apply and wait for startup.

Check functionality in WSL Ubuntu using `docker ps`

Reopen in project in WSL Ubuntu using `code .`

Open Devcontainer in VScode using 'Reopen in container'
