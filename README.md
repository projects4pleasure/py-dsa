
### Install UV
```
brew install uv
```

### For cli command completion
```
eval "$(uv generate-shell-completion zsh)"
```

### Initialize project
```
uv init
```

### Run Python code
#### From root
```
uv run <filename.py>
```
#### From sub-projects like data_structures and sorting

From project root
```
cd data_structures
uv run linked_list.py
```

```
cd sorting
uv run main.py
```


### UV tools
#### UV update shell first
```

```

#### UV install tools
```
uv tool run ruff

```
#### UV use tools
```
uv tool run ruff check
```
