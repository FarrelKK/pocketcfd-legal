# Legal pages

The public pages Google Play and Apple require, kept next to the code that they describe.

```
docs/
├── privacy-policy.md        ← edit this
├── terms-and-conditions.md  ← and this
├── build.py                 ← then run this
├── privacy.html             ← generated
├── terms.html               ← generated
├── index.html               ← landing / support page, edit by hand
└── .nojekyll                ← stops GitHub trying to run Jekyll
```

## 1. Fill in the placeholders

Anything reading `[LIKE THIS]` renders **highlighted in red** on the published page, so an
unfilled one is impossible to miss. Edit the two `.md` files — your name, email, city, the
date and the privacy policy URL — then:

```bash
cd docs
python3 build.py
```

Edit `index.html` by hand too: support email, copyright line, and the Play link once you
have one.

## 2. Publish

**This only works if the repository is public.** GitHub Pages will not serve a private
repository on the free plan.

### If this repo is public

Settings → **Pages** → Source: **Deploy from a branch** → Branch **main**, folder
**/docs** → Save.

```
https://<username>.github.io/<repo>/
https://<username>.github.io/<repo>/privacy.html
https://<username>.github.io/<repo>/terms.html
```

### If this repo is private (likely, for a paid app)

Keep editing the markdown here — this stays the source of truth — but publish from a
separate public repo:

1. Create a public repo, e.g. `pocket-cfd-legal`
2. Copy the contents of this `docs/` folder into its root
3. Settings → Pages → branch **main**, folder **/ (root)**

Re-copy the two generated `.html` files whenever you change the text. Two files, thirty
seconds, and your source stays closed.

## 3. Where the URLs go

| Where | Which URL |
|---|---|
| `src/config.js` → `PRIVACY_URL` / `TERMS_URL` | privacy.html / terms.html — the About screen opens these |
| Play Console → Store listing → Privacy policy | privacy.html |
| Play Console → Store settings → Support → Website | the root URL |
| App Store Connect → App Privacy → Privacy Policy URL | privacy.html |
| App Store Connect → Support URL and Marketing URL | the root URL |

## 4. Keep them alive

Both stores expect these URLs to work for as long as the app is listed. Don't delete or
rename the repo without updating Play Console, App Store Connect and `src/config.js` — a
dead privacy policy link is grounds for removal.
