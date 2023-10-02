(First posted at https://github.com/bit-team/backintime/issues/1338#issuecomment-1454740118)

There might be a better way to add a new key, but this is how I have added it and was able to install backintime from launchpad on an ubuntu 22.04 server I had to manage for a while.
One worthy modification would be adding the new keys in the user keyring instead of the system's.
I followed and adapted the steps detailed at https://itsfoss.com/apt-key-deprecated/.

**Before following the steps below, please prepare all the needed and required backups of the current keyring!!**

We will use backintime as an example in the following: 

1)Get the link from https://launchpad.net/~bit-team/+archive/ubuntu/stable under Technical details about this PPA > get the link to the Signing Key 
![image](https://user-images.githubusercontent.com/769635/222902963-103b1c94-0e77-4939-be25-4fb36a9c2574.png)

And download to the trusted keyring

```
curl -sS "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x589eedcd16567b0e6d23c3144b6071b7d6fdc9d0" |  \ 
gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/bit_team_pub.gpg
```

2)Check that the fingerprint is the same with: `gpg --show-keys /etc/apt/trusted.gpg.d/bit_team_pub.gpg`

![image](https://user-images.githubusercontent.com/769635/222903322-d78e3410-e5ed-4e0a-a722-6b2c4a5bf7e4.png)

3)Add the repo to your sources.list

```
echo  "deb [signed-by=/etc/apt/trusted.gpg.d/bit_team_pub.gpg] https://ppa.launchpadcontent.net/bit-team/stable/ubuntu jammy main" | sudo tee /etc/apt/sources.list.d/bitteam.list
```

4)Finally, install / update backintime:

```
sudo apt update
sudo apt install backintime-qt
```
