# social.anchoestack

Bangladesh (BDT) price page for Anchorstack's Facebook reels and page management.
Live at **https://social.anchorstacklabs.com**

## Files

| File | What it is |
|---|---|
| `index.html` | The finished page. Upload this. |
| `og-image.jpg` | Link-preview image (1200×630) for WhatsApp/Facebook. Upload next to `index.html`. |
| `src/template.html` | Editable source of the page. |
| `src/og-image.html` | Source of the preview image. |
| `src/assets/` | Logo and favicon used by the build. |
| `build.py` | Rebuilds `index.html` from the template. |

## Editing

1. Change text or prices in `src/template.html`.
2. Run `python3 build.py`.
3. Commit and push. Both `index.html` and `og-image.jpg` must sit in the site's root folder.

Placeholders in the template:
- `{{LOGO}}`, `{{FAV}}`: filled with the logo and favicon.
- `{{wa:message}}`: becomes a WhatsApp link that opens with that message.

## After changing the preview image

Open Facebook's Sharing Debugger, paste the URL and click **Scrape Again**, so Facebook and WhatsApp show the new image.
