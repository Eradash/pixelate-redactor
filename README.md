# pixelate-redactor

Redact images with pixels

Works with Python >= 2.6, Python >= 3.2.

## Installation

```bash
pip install pixelate-redactor
```

## Example

```bash
pixelate-redactor \
  --input=img/example_img_original.png \
  --output=img/example_img_redacted.png \
  --pixel-size=10 \
  --start-x=90 \
  --start-y=180 \
  --size-x=150 \
  --size-y=150
```

From this:

![original](https://raw.githubusercontent.com/Eradash/pixelate-redactor/master/img/example_img_original.png)

To this:

![redacted](https://raw.githubusercontent.com/Eradash/pixelate-redactor/master/img/example_img_redacted.png)
