# repeart

repeart is a Python tool that generates images of repeating strings. It provides a convenient way to create visually appealing patterns with customizable parameters.

## Usage

To use repeart, execute the following command:
```
python3 main.py [arguments]
```

## Arguments

The following arguments can be supplied to the script:

- `--alg=`: Specifies the algorithm for generating the string pattern. (Optional, default: hello-world)
- `--width=`: Sets the width of the generated image in pixels. (Optional, default: 500)
- `--height=`: Sets the height of the generated image in pixels. (Optional, default: 500)
- `--variance=`: Adjusts the variation in the string pattern. (Optional, default: 0.0)
- `--fontColor=`: Sets the color of the string characters. (Optional, default: white)
- `--backgroundColor=`: Sets the background color of the image. (Optional, default: black)

Note: All arguments are optional, and default values will be used if not provided.

## Algorithms

repeart supports various algorithms for generating the string pattern. Each algorithm produces a different string output based on specific rules or data sources. The following algorithms are available:

- `one`: Returns the string "1" as the output.
- `hello-world`: Returns the string "Hello world!" as the output.
- `pi`: Returns the numerical value of pi (π) as a string.
- `bible`: Downloads the King James Version (KJV) of the Bible from "https://www.o-bible.com/download/kjv.txt" and replaces newline characters with spaces. The resulting text is used as the output string.
- `url`: Allows you to specify a custom URL using the `url=` prefix. The tool sends a GET request to the specified URL and replaces newline characters with spaces. The response text is used as the output string.
- `selenium`: Generates a string in the format of a Selenium web element.



If the provided algorithm (`--alg`) does not match any of the predefined algorithms, the generator will repeat the string specified in `--alg` as the output.

## Examples

Here are some examples of how to use repeart:

- Generate a string image with default parameters:
```
python3 main.py
```

- Generate a string image with a specific width and height:
```
python3 main.py --width=800 --height=600
```

- Generate a string image using the `one` algorithm:
```
python3 main.py --alg=one
```

- Generate a string image using the `url` algorithm:
```
python3 main.py --alg=url=https://example.com/api/data
```

Please note that some algorithms may require additional dependencies or external resources.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per the terms of the license.
