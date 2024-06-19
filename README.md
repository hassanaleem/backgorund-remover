# Background Remover

## Setup
Install the required packages by running the following command:
```bash
pip3.10 install -r requirements.txt
```

## Usage 
```bash
python3.10 background_remover.py [filepath] [rgba] [(width, height)]
```

color and size are optional arguments. default background color will be white and defalt size will be (800, 600)

### Example: 
```bash
python3.10 background_remover.py input.jpeg (0, 0, 0) (600, 480)
```

## Supported Formats

The background remover script supports the following file formats:

    Image: jpg, jpeg, png
    Video: mp4, avi, mov
