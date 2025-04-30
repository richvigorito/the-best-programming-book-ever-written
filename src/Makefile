.PHONY: help run-pascal run-python run-cpp run-go build-pascal clean

help:
	@echo "Available commands:"
	@echo "  make run-pascal FILE=path/to/file.pas     # Compile and run Pascal file"
	@echo "  make run-python FILE=path/to/file.py      # Run Python file"
	@echo "  make run-cpp FILE=path/to/file.cpp        # Compile and run C++ file"
	@echo "  make run-go FILE=path/to/file.go          # Run Go file"
	@echo "  make build-pascal FILE=path/to/file.pas   # Compile Pascal file only"
	@echo "  make clean                                # Remove compiled files"

run-pascal:
	fpc $(FILE) && ./$(basename $(FILE))

build-pascal:
	fpc $(FILE)

run-python:
	python3 $(FILE)

run-cpp:
	g++ -o temp.out $(FILE) && ./temp.out

run-go:
	go run $(FILE)

clean:
	rm -f *.o *.out *.ppu *.exe temp.out

