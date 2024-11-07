# We Just Sad
## Installation
### 1. Download from Google Drive
   link: https://drive.google.com/file/d/1nL-UkcrsD_6IHww6uBbFkYs-rp31z8SJ/view?usp=drive_link
### 2. Download from Repository
Download ```{V}JustSadInstaller.exe``` from ```dist``` folder or from <b>release</b> section

## Development

### Clone this repository
```
git clone https://github.com/Wissanupong-Chanliem/WejustSad.git
```

### Run game
```
python watcher.py
```

### Project Structure
```
│
├── achievement
│   └── achievement_k.py
├── src
│   ├── components
│   │   └── **/*.py
│   ├───function
│   │   └── **/*.py
│   ├── main.py
│   └── classes.py
├── static
│   ├── images
│   │   └── *.webp
│   └── font
│       └── *.ttf
└── .gitignore
```
- **main.py** : contain main game loop and pages
- **classes.py** : contain base class for inheritance
- **static** : contain static resources like fonts and images
- **src** : contain source code for the game
- **src/components** : contain reusable ui components
- **src/function** : contain function for creating features
