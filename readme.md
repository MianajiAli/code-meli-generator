# Iranian National Code Generator

This Python script generates valid Iranian national codes (code meli) based on user input. You can modify the prefix codes to generate codes for different cities by changing the `prefixes` list in the first line of the Python script.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/iranian_code_generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd iranian_code_generator
    ```

3. Open the Python script (`code_generator.py`) in a text editor.

4. Modify the `prefixes` list in the first line of the script to include the desired prefix codes for cities.

5. Save the changes and close the editor.

6. Run the script:

    ```bash
    python code_generator.py
    ```

7. Follow the instructions provided by the script.

## Functionality

The script allows the user to specify the number of codes to generate or generate all possible valid codes. Valid codes are generated for the specified prefixes.

Generated codes are written to a text file named `all_valid_codes.txt`.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Code Documentation

For detailed code documentation, please refer to the [codes.md](codes.md) file.
