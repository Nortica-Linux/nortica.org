# Website scope

- Work only in this website repository unless the user explicitly approves changes to other Nortica repositories.
- Use Nortica branding and the Gruvbox palette, with `#d79921` as the dark-theme main yellow; preserve the original warm brown/red/green accents in the light theme. Keep artwork in `media/`, but display only the small top-left logo; do not add a large banner.
- Never rewrite, expand, polish or otherwise change the user's documentation content unless explicitly asked. Rebranding permits only the requested name/link substitutions, not prose, command or structural rewrites.
- Documentation, issue, source and download links belong to the Nortica-Linux organization. Debian upstream links are still appropriate for Debian itself.
- Verify commands, release asset names and config paths against the upstream Nortica repositories; do not invent release details.
- Never commit credentials, kubeconfigs, tokens, private keys, private logs or Kubernetes Secret manifests. This repository is public.
- Run a strict MkDocs build and `python3 tests/check_site.py <site-dir>` before publishing. On the authorized production node, run `./publish.sh` after changes and report failures. Do not attempt production deployment from CI or a contributor machine.
- Keep the old DebianZFS deployment untouched until explicitly instructed otherwise.
