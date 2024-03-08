Migrated to `atelier-epita/documentation`
# fiches-tuto

Markdown sources files for genereation of "fiches tutos" at l'Atelier

## Contributing

Everyone can contribute by creating or updating the files according to the reference.
([template.md](src/template.md))

Feel free to open issues for suggestions and to facilitate the workflow of remaining work.

## Locale

local variations must start with prs_, lyn_, tls_...

## Generate

```bash
python3 generator/generate.py --dir src --out docs
```

Note: if you added a static image, once you generate locally, the pdf will not feature the image you added locally. static images are fetched from "github.com/Atelier-Epita/fiches-tuto/raw/main/static/". Once pushed to main, the pdf will feature the image.
