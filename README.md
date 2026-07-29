<h1 align="center">Pixel Art Generator</h1>

<p align="center">
<img src="https://raw.githubusercontent.com/amirsamgoharpey/pixel-art-generator/main/pixel_art_generator.png">

<br>

<img src="https://img.shields.io/github/directory-file-count/amirsamgoharpey/pixel-art-generator">
<img src="https://img.shields.io/github/languages/code-size/amirsamgoharpey/pixel-art-generator">
<img src="https://img.shields.io/github/followers/amirsamgoharpey">

</p>

---

## About

A small procedural pixel art generator written in Python.

The program creates random symmetric pixel patterns and exports them as SVG files.

The idea behind this project was to experiment with:
- random generation
- geometric patterns
- symmetry
- SVG creation

---

## How it works

The generator creates 4 random rectangles on one side of the canvas, then mirrors them to the other side to create a symmetric design.

Each generated image contains:
- Random color selection
- Random rectangle positions
- Horizontal symmetry
- SVG output

---

## Example

Generated with this code:

<p align="center">
<a href="https://github.com/amirsamgoharpey/pixel-art-generator/blob/main/happy.svg">
happy.svg
</a>
</p>

---

## Usage

Clone the repository:

```bash
git clone https://github.com/amirsamgoharpey/pixel-art-generator
```

Install the required package:

```bash
pip install pycairo
```

Generate your own pixel art:

```python
from artgen import creator

creator("filename")
```

This will create:

```
filename.svg
```

---

## Using it in other projects

You can also import the generator and use it inside your own Python projects:

```python
from artgen import creator

creator("profile_picture")
```

For example, it can be used for generating random default images or simple procedural graphics.

---

## License

This project is open source and free to use.

Feel free to modify, improve, or use the code in your own projects.

---

## Last words

I originally made this project just for fun and to explore procedural generation.

Have a nice day :)
