Title: Multiple ssh key quagmire
Tags: linux, ssh, git
Date: 2015-06-12T23:08

On my work computer, I use my [work GitHub account][github-work], and I use ssh agent forwarding like crazy. Being able to SSH into a machine and run `git fetch` from there with my local key, or `scp` some files to a second machine, is essential. And it works just fine with `ForwardAgent yes` in my `~/.ssh/config` file.

I recently setup a [git repo for my personal bash scripts][homedir]. It's just some scripts I use at home, and wanted to have them around on my work laptop. It's on my [personal account][github-personal] though, so I have to check it out using a different SSH key (because GitHub figures out which account you are by your SSH key, so a key can only be linked to a single account).

The normal solution for using multiple github accounts is to define a second profile in your ssh config like so:

    Host github-personal
      HostName github.com
      User git
      IdentityFile ~/.ssh/github-personal.pem

Then you can clone repos from your secondary account with:

    git clone github-personal:stevearm/homedir.git

and everything works. Atleast until you start using `ForwardAgent`. Now that `github-personal.pem` is sitting in my `.ssh` directory, git doesn't work properly on remote machines through forwarded agents:

    laptop$ ssh server
    server$ ssh git@github.com
    Hi stevearm!

## Behold SSH-agent

It seems that ssh (and by extension git) will use the private keys it has in its agent. Even if you use `ssh -i newkey.pem` that simply appends `newkey.pem` to the agent (and [it doesn't even put it first][ssh-key-order]). So once the ssh-agent has keys for one of the GitHub accounts, it will always use that key.

### IdentitiesOnly to the rescue?

Setting `IdentitiesOnly` will force ssh agent to not use any of its own keys, and instead only use the one specified:

    Host github-personal
      HostName github.com
      User git
      IdentityFile ~/.ssh/github-personal.pem
      IdentitiesOnly yes

Doing this works for dealing with GitHub from repos on my laptop (which already worked), but still breaks when using a forwarded agent on a remote machine. It seems that if I ssh to a server, then using ssh from there doesn't use my local laptop config.

One thing I didn't try was setting up a profile in `.ssh/config` for the server and use IdentitesOnly to restrict my server connection to a single key. That key may then be the only one used when talking to GitHub, which may work (as long as it's practical to create profiles for every work server).

### Brute force management of ssh-agent

My current working solution is to manually manage what keys are in `ssh-agent`. My requirements mean I only need this extra key once every month or two, so this solution might be too manual for your needs.

1. Move the public and private keys for my personal github from `.ssh` and remove the profile from `.ssh/config`. One (or both) of these steps keep the keys from being auto-added to `ssh-agent`. If you let the key get added automatically, the agent doesn't let you remove it (as [other people have found][ssh-key-delete]). My work keys are still in `.ssh` and auto-added to `ssh-agent` like normal.
2. Add my personal github key: `ssh-add ~/src/homedir/.ssh-key`
3. See that is has been added: `ssh-add -l`
4. Do the `git push` for whatever commits I wanted
5. Drop the personal github key from ssh-agent: `ssh-add -d ~/src/homedir/.ssh-key`
6. See that the keys are back to normal: `ssh-add -l`

[github-work]: https://github.com/stephenarmstrong
[github-personal]: https://github.com/stevearm
[homedir]: https://github.com/stevearm/homedir
[ssh-key-order]: http://sealedabstract.com/code/github-ssh-with-multiple-identities-the-slightly-more-definitive-guide/
[ssh-key-delete]: http://stackoverflow.com/questions/25464930/how-to-remove-a-ssh-key
