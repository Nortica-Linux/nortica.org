# Nortica documentation

Source for **<https://docs.nortica.org>**, built with MkDocs Material. Nortica was formerly known as DebianZFS; this is the new, independent site.

## Project repositories

- [Nortica-Linux/nortica](https://github.com/Nortica-Linux/nortica): live image, installer and system setup.
- [Nortica-Linux/config](https://github.com/Nortica-Linux/config): dotfiles and user desktop setup.
- [Nortica-Linux/nortica.org](https://github.com/Nortica-Linux/nortica.org): this website, documentation and media.

## Editing

Markdown lives under `docs/`, navigation in `mkdocs.yml`, and styles in `docs/assets/extra.css`. Gruvbox light/dark palettes follow the OS preference and can be switched from the header. System fonts avoid third-party font requests.

Original artwork lives in `media/`. `docs/media` is a relative symlink so MkDocs publishes those exact files without maintaining duplicate assets. Keep the horizontal logo as the home-page banner, the symbol as the header mark and the supplied favicon as the browser icon.

The home page optionally loads public documentation issues directly from GitHub's API. No token is required; if the API is unavailable or rate-limited, ordinary tracker links remain available.

## Preview and build

With Docker installed:

```sh
docker run --rm -it -p 127.0.0.1:8000:8000 -v "$PWD:/docs" squidfunk/mkdocs-material:9.7.7
```

Then open <http://127.0.0.1:8000>. To build and check the generated site:

```sh
docker run --rm -v "$PWD:/docs" squidfunk/mkdocs-material:9.7.7 build --strict
python3 tests/check_site.py site
```

GitHub Actions runs the same strict build and static-site checks on pushes and pull requests. It does not deploy and needs no production credentials.

## Publish (authorized production maintainers only)

On the hosting node, with the configured Kubernetes context:

```sh
./publish.sh
```

This builds the mounted repository strictly in the `nortica-docs` builder, checks the generated site, and atomically switches nginx to the successful output. A failed build leaves the published site in place. Concurrent publishes are serialized; the previous successful build is retained until the next publish. No restart is needed for routine content changes.

The production infrastructure is managed separately; do not add kubeconfigs, DNS tokens, SSH keys, credentials, cluster Secret manifests or private user data here. The web server receives only generated static files, not the source repository or its `.git` directory.

## Contributing

Use this repository's issues for documentation changes, the main repository for installer/system problems and the config repository for dotfile issues. Remove all private data from logs before posting them publicly.
