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

Reopen project in WSL Ubuntu using `code .`

Open Devcontainer in VScode using 'Reopen in container'

### Can't run on rootless Podman on Linux

You need to make some changes to the `devcontainer.json` file.
Uncomment:

```json
    // "--userns=keep-id:uid=1000,gid=1000", // Keep the user id and group id the same as the host in Podman rootless setup
```

Comment:

```json
"source=/var/run/docker.sock,target=/var/run/docker.sock,type=bind,readonly" // You can't use this on Linux with Podman rootless setup
```

### Can't launch a new window through the container on Linux.

Use the command `xhost +`. Though be aware of the [risks](https://stackoverflow.com/questions/63884968/why-is-xhost-considered-dangerous)
