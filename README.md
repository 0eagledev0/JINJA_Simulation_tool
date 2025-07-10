# JINJA_Simulation_tool

![](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white) ![](https://camo.githubusercontent.com/050fc4e602f25dd4fc337b873fbc62b7d393673a9f4b1e7529a9a61ea35485a5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d4646443433423f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d626c7565) ![](https://img.shields.io/badge/Python-3.11-<>.svg) ![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black) ![YAML](https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515)

---

[Lire en français](README_FR.md)

---

## Description
This project provides a graphical user interface (GUI) for rendering templates using Jinja2. The application allows users to select and combine variable files (in JSON, YAML, or Jinja format) with Jinja templates to generate rendered content. The interface is built using Python's Tkinter library.

## Features
- **File Selection:** Allows users to select variable files in JSON, YAML, or Jinja formats and template files in Jinja format.
- **Dynamic Content Rendering:** Renders content based on the selected variable and template files using Jinja2 templating engine.
- **Clipboard Copying:** Provides functionality to copy the rendered content to the clipboard.
- **Error Handling:** Displays error messages if files are not selected or if an error occurs during rendering.

## Prerequisites
- Python version > 3.6 
- Tkinter (usually included with Python)
- `jinja2` library
- `pyyaml` library

## Installation
1. Clone the repository or download the project files.
2. Install the required Python libraries:
   ```bash
   pip install jinja2 pyyaml 
   ```

## Usage
1. Run the `Main.py` script to start the GUI application:
   ```bash
   python Main.py
   ```
2. In the application window, select the type of variables and templates you wish to use from the dropdown menu.
3. Click the "Browse" buttons to select the variable and template files.
4. Click the "Submit" button to render the content based on the selected files.
5. The rendered content will be displayed in a new window with an option to copy it to the clipboard.

## Project Structure
- `Main.py`: Contains the main application code, including the GUI and logic for file selection and content rendering.
- `tools_jinja.py`: Contains utility functions for reading files, merging templates, and rendering content using Jinja2.

## Contributions
Contributions are welcome! If you have suggestions for improvements or bug fixes, please open an issue or submit a pull request on the project's repository.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for more details.

## Warnings
- Ensure that the selected files are in the correct format to avoid errors during rendering.
