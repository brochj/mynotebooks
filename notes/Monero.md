---
pinned: true
title: Monero
created: '2021-11-12T20:19:42.341Z'
modified: '2022-01-20T19:01:55.605Z'
---

# Monero

1. Create a ubuntu container

```sh
apt update
apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y
```

2. Install XMRIG from Source

```git
git clone https://github.com/xmrig/xmrig.git
cd xmrig
mkdir build
cd build
cmake ..
make
```

3. Create a Digital wallet

go to [getmonero.org](https://www.getmonero.org/downloads/) and download Monero GUI Wallet

4. inside `xmrig/build` folder

run the command to start mining
```
./xmrig -o <miningpool>:<port> -u <wallet-address -p <(optional)-name-of-device>

```
Example
```
./xmrig -o gulf.moneroocean.stream:10128 -u 45fojehGdsw1TJ8Cj8W6XaNhHneGrvKUY86Eej2LVy7U1MmeEiV2D7Y5vh3xEbHhvTahMn1ECGCEcdAX74eJqCi6AJC8fhk -p container
```

## Choose a mining pool

[miningpoolstats.stream/monero](https://miningpoolstats.stream/monero)

```
gulf.moneroocean.stream:10128 
xmr.2miners.com:2222
```
