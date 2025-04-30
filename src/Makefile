.PHONY: help run-pascal run-python run-cpp run-go build-pascal clean

help:
\t@echo "Available commands:"
\t@echo "  make run-pascal FILE=path/to/file.pas     # Compile and run Pascal file"
\t@echo "  make run-python FILE=path/to/file.py      # Run Python file"
\t@echo "  make run-cpp FILE=path/to/file.cpp        # Compile and run C++ file"
\t@echo "  make run-go FILE=path/to/file.go          # Run Go file"
\t@echo "  make build-pascal FILE=path/to/file.pas   # Compile Pascal file only"
\t@echo "  make clean                                # Remove compiled files"

run-pascal:
\tfpc $(FILE) && ./$(basename $(notdir $(FILE)))

build-pascal:
\tfpc $(FILE)

run-python:
\tpython3 $(FILE)

run-cpp:
\tg++ -o temp.out $(FILE) && ./temp.out

run-go:
\tgo run $(FILE)

clean:
\trm -f *.o *.out *.ppu *.exe temp.out
