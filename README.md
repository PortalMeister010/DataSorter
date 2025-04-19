# 📁 Portal File Manager

**Portal File Manager** is a lightweight desktop application that helps you organize files by sorting them into folders based on their extensions.  
Built with Python and Tkinter, it's designed to be simple, flexible, and easy to use.

## ✨ Features

- 📂 Multi-file upload with automatic sorting  
- ⚙️ Custom file type settings (e.g., `.jpg` → `Pictures`, `.pdf` → `Documents`)  
- ➕ Add new file types via the GUI  
- ❌ Delete file types one by one or with checkboxes  
- 💾 Settings saved persistently in a local `settings.json` file  
- 🖥️ Clean graphical interface built with Tkinter  
- 📜 Scrollable support for managing many file types  

## 🚀 Getting Started

### Requirements

- Python 3.x  
- Tkinter (usually included with Python)

### Run the app

```bash
git clone https://github.com/your-username/portal-file-manager.git
cd portal-file-manager
python portal_file_manager.py
```

## 🛠️ How It Works

1. Add file type rules (e.g., `.png` → `D:\Images`)  
2. Click "Choose Data" and select files to upload  
3. Files will be copied to the matching folders based on their extensions  
4. Modify or delete file type rules at any time  

## 💼 Configuration

Settings are stored in a local file called `settings.json`.  
This allows the app to remember your file type assignments between sessions.

### Example

```json
{
  ".pdf": "D:\\Documents\\PDFs\\",
  ".jpg": "D:\\Pictures\\"
}
```

## 💡 Planned Features

- Drag & Drop support  
- File preview thumbnails  
- Export/import of settings  
- Predefined templates for common file types  
- Better cross-platform support (Windows/Linux/macOS)

## 📦 Packaging (Optional)

To build a standalone `.exe` using PyInstaller:

```bash
pyinstaller --noconfirm --onefile --windowed portal_file_manager.py --icon=icon.ico
```

## 📄 License

This project is licensed under the MIT License.  
Feel free to use, modify, and distribute it.

## 🙌 Contributions

Contributions are welcome!  
If you have ideas, improvements, or bug fixes, feel free to open an issue or a pull request.
