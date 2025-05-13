# 6LACKL1ST

A custom GUI application designed for specific security and system administration tasks, featuring a modern dark theme and drag-and-drop functionality.

## Description

6LACKL1ST is a multi-functional application built with Python and Tkinter, offering a variety of tools and features. The application includes:

- A reverse-shell generator for PowerShell
- An account generator
- A drag-and-drop interface for file operations
- A modern, customizable GUI with a dark theme
- Additional pages for future expansion or customization

The application is designed with a clean and intuitive interface, making it easy to navigate and use.

## Installation

To run this application, you'll need to install the required dependencies. Here's how you can set it up:

1. Clone the repository:

   ```bash
   git clone [your-repository-url]
   cd 6LACKL1ST
   ```
2. Install the required Python packages:

   ```bash
   pip install customtkinter tkinterdnd2 pillow pyglet
   ```
3. Run the application:

   ```bash
   python main.py
   ```

## Usage

### Running the Application

- Launch the application by running `main.py`.
- The application will start with a dashboard that allows you to navigate between different tools.

### Key Features

1. **Reverse-Shell Generator**

   - Drag and drop files or select files manually to process.
   - Generate reverse shells for PowerShell.
2. **Account Generator**

   - Create custom accounts with specific configurations.
3. **Drag-and-Drop Functionality**

   - Easily drag and drop files into the application for processing.
4. **Customizable GUI**

   - The application features a modern dark theme with customizable elements.
5. **Multiple Pages**

   - Navigate between different pages using the navigation panel on the left.

### Navigation

- Use the navigation panel on the left side to switch between different tools and pages.
- The "Launch" button in the center of the screen triggers the main functionality of the application.

## Customization

The application allows for customization of the GUI. You can modify the appearance by changing the following:

- **Theme**: The application uses a dark theme by default, but you can switch to a light theme if desired.
- **Colors**: Modify the color scheme by adjusting the `customtkinter` settings.
- **Fonts**: The application uses custom fonts (`HackGlitch` and `Hackout`) for a unique look.

## Dependencies

The application relies on the following libraries:

- `customtkinter`: For the custom GUI elements and themes.
- `tkinterdnd2`: For drag-and-drop functionality.
- `pillow`: For image processing.
- `pyglet`: For font handling.

## Known Issues

- Some features are currently under development (e.g., Pages 3-7).
- The application is optimized for Windows but may require additional configuration for Linux or macOS.

## Contributing

Contributions are welcome! If you'd like to add new features, fix bugs, or improve the application, please fork the repository and submit a pull request.

