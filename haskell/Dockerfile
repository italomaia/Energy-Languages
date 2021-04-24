FROM energy/base:1

ENV COMPILER=/usr/bin/go

COPY . .

RUN apk add --no-cache cabal ghc

RUN curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh
