# SearchSite

The utility is designed to search for sites.

## Install
```
$pip3 install -r requirements.txt
```

## Running

```
$python3 search_site.py [OPTIONS]

OPTIONS:
    -h, --help         show this help message and exit
    -m, --max          maximum length website domain generation
    -b, --bigchar      add bigchar in alphabet
    -c, --smallchar    add smallchar in alphabet
    -n, --number       add number in alphabet
    -s, --symbols      add symbols in alphabet
    -u, --url          open url in webbrowser
    -o, --out          out file
```

## Stoping
Ctrl+C - stopping and showing statistics

## Saving
All named sites are saved in the `site.txt` file or you can specify in which file the generated sites will be saved.

