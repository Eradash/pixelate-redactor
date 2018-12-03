# pixelate-redactor

Redact images with pixels

Works with Python >= 2.6, Python >= 3.2.

## Installation

```bash
pip install pixelate-redactor
```

## Example

### `pixelate-redactor`

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


### `pixelate-redactor-boxes`

```bash
pixelate-redactor \
  --input=img/example_img_original.png \
  --output=img/example_img_redacted.png \
  --pixel-size=10 \
  --boxes=img/boxes.json
```


with `img/boxes.json`:

```json
{
  "__box_name_1__": {
    "px": 90,
    "py": 180,
    "sx": 150,
    "sy": 150
  },
  "__box_name_2__": {
    "px": 90,
    "py": 180,
    "sx": 150,
    "sy": 150
  }
}
```

(the values are the same, to keep the same result from the single box example)

* `px` -> Position X
* `py` -> Position Y
* `sx` -> Size X
* `sy` -> Size Y


### Results

From this:

![original](https://raw.githubusercontent.com/Eradash/pixelate-redactor/master/img/example_img_original.png)

To this:

![redacted](https://raw.githubusercontent.com/Eradash/pixelate-redactor/master/img/example_img_redacted.png)
