# Pocket CFD — legal pages

The public pages Google Play and Apple require. Publishing this folder with GitHub Pages
gives you the three URLs the stores ask for.

## Publish

1. Create a **new public repository** on GitHub, e.g. `pocket-cfd-legal`.
   Public matters: GitHub Pages on a private repo needs a paid plan, and these pages have
   to be readable without a login anyway.
2. Upload every file in this folder to the repository root.
3. Repo → **Settings → Pages** → Source: **Deploy from a branch**, Branch: **main**,
   folder: **/ (root)** → Save.
4. Wait a minute or two. Your URLs are:

```
https://<username>.github.io/pocket-cfd-legal/
https://<username>.github.io/pocket-cfd-legal/privacy.html
https://<username>.github.io/pocket-cfd-legal/terms.html
```

## Fill in the placeholders first

Anything still reading `[LIKE THIS]` is highlighted in red on the page, so it is obvious
if you miss one. Edit `../privacy-policy.md` and `../terms-and-conditions.md`, then:

```
python3 build.py
```

That regenerates `privacy.html` and `terms.html`. Also edit `index.html` by hand — the
support email, the copyright line and the Play link.

## Where the URLs go

| Where | Which URL |
|---|---|
| `src/config.js` → `PRIVACY_URL`, `TERMS_URL` | privacy.html, terms.html |
| Play Console → Store listing → Privacy policy | privacy.html |
| Play Console → Store listing → Support (website) | the root URL |
| App Store Connect → App Privacy → Privacy Policy URL | privacy.html |
| App Store Connect → Support URL / Marketing URL | the root URL |

## Keep it alive

Both stores expect these to work for as long as the app is listed. Don't delete the repo,
and if you rename it, update the URLs in Play Console, App Store Connect and
`src/config.js` — a dead privacy policy link is grounds for removal.
